from collections import Counter,defaultdict
import csv,json
z=json.load(open('quartic_orbits.json'))
mons=z['mons'];idx={tuple(m):i for i,m in enumerate(mons)}
basis=[(1,0,0),(0,1,0),(0,0,1)]
def mmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)] for i in range(3)]
def rank(A):
 A=[list(row) for row in A];r=0
 for c in range(3):
  piv=next((i for i in range(r,3) if A[i][c]),None)
  if piv is None:continue
  A[r],A[piv]=A[piv],A[r]
  for i in range(3):
   if i!=r and A[i][c]:A[i]=[a^b for a,b in zip(A[i],A[r])]
  r+=1
 return r
rows=[];groups=defaultdict(lambda:dict(equations=0,orbits=0));byrank=defaultdict(lambda:Counter())
for l in open('splittings.tsv'):
 data=list(map(int,l.split()));mask,w=data[:2];fixed=data[2:9];m=data[9:16];total=data[16]
 H=[[int(mask>>idx[(2*basis[i][0]-basis[j][0]+1,2*basis[i][1]-basis[j][1]+1,2*basis[i][2]-basis[j][2]+1)]&1) if all(2*basis[i][k]-basis[j][k]+1>=0 for k in range(3)) else 0 for j in range(3)] for i in range(3)]
 f=rank(mmul(mmul(H,H),H))
 prediction=[1,2,4,7][f]
 assert prediction==total,(mask,w,f,total)
 cycle=','.join(str(d) for d,a in enumerate(m,1) for _ in range(a))
 assert sum((d*a for d,a in enumerate(m,1)))==total
 groups[cycle]['equations']+=w;groups[cycle]['orbits']+=1
 byrank[f][cycle]+=w
 r=0
 for a,b,c in [(1,y,z) for y in (0,1) for z in (0,1)]+[(0,1,z) for z in (0,1)]+[(0,0,1)]:
  value=0
  for i,(X,Y,Z) in enumerate(mons):
   if mask>>i&1:
    value ^= (a if X else 1) * (b if Y else 1) * (c if Z else 1)
  r+=1-value
 rows.append(dict(mask=mask,orbit_size=w,p_rank=f,rational_points=r,geometric_bitangents=total,cycles=cycle,fixed_counts=','.join(map(str,fixed))))
print('Groups')
for k,v in sorted(groups.items(),key=lambda x:(sum(map(int,x[0].split(','))),x[0])):print(k,v)
print('By rank',dict(byrank))
print('weighted smooth',sum(x['orbit_size'] for x in rows))
with open('splitting_orbits.csv','w') as fd:
 w=csv.DictWriter(fd,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
with open('splitting_distribution.csv','w') as fd:
 w=csv.writer(fd);w.writerow(['cycle_lengths','smooth_equations','projective_orbits'])
 for k,v in sorted(groups.items(),key=lambda x:(sum(map(int,x[0].split(','))),x[0])):w.writerow([k,v['equations'],v['orbits']])

# Independent bitangent-line computation uses different finite-field models.
A={};B={}
for line in open('splittings.tsv'):
 v=[int(t) for t in line.split()]
 A[v[0]]=(v[1],tuple(v[2:9]))
for line in open('independent_fixed_counts.txt'):
 v=[int(t) for t in line.split()]
 B[v[0]]=(v[1],tuple(v[2:9]))
assert A==B and len(A)==78
assert sum(v['equations'] for v in groups.values())==10920
assert sum(v['orbits'] for v in groups.values())==78
assert groups['7']['equations']==3072
assert groups['7']['orbits']==20
assert len(groups)==10
print('All independent arithmetic, orbit and distribution checks passed.')
