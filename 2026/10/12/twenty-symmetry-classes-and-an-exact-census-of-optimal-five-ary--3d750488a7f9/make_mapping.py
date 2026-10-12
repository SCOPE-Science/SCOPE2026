import json
v=[]
for a in range(3):
 for b in range(3):
  for c in range(3):
   x=(a,b,c)
   if any(x) and x[next(i for i,u in enumerate(x)if u)]==1:v.append(x)
A=[[p for p,x in enumerate(v) if sum(v[l][k]*x[k]for k in range(3))%3==0]for l in range(13)]
gens=json.load(open('generators.json'))
with open('gmap.txt','w')as f:
 for pm,lm in gens:
  vals=[]
  for l in range(13):
   for j in range(4):
    ll=lm[l];jj=A[ll].index(pm[A[l][j]])
    vals.append(4*ll+jj)
  f.write(' '.join(map(str,vals))+'\n')
print('adj',A)
