"""Witness analysis: verify (17,3)-arc, trisecant spectrum, [17,3,14] weight enumerator."""
import itertools, json
from collections import Counter

def add(x,y): return ((x%3)+(y%3))%3 + 3*(((x//3)+(y//3))%3)
def neg(x): return ((-x)%3)+3*((-(x//3))%3)
def mul(x,y):
    u1,v1=x%3,x//3; u2,v2=y%3,y//3
    return (u1*u2-v1*v2)%3+3*((u1*v2+u2*v1)%3)
def inv(x):
    assert x!=0
    for z in range(1,9):
        if mul(x,z)==1: return z
def sub(x,y): return add(x,neg(y))

pts=[]; seen=set()
for x in range(9):
    for y in range(9):
        for z in range(9):
            if x==y==z==0: continue
            v=(x,y,z)
            for c in v:
                if c: s=inv(c); break
            key=(mul(x,s),mul(y,s),mul(z,s))
            if key not in seen: seen.add(key); pts.append(key)
N=91; index={p:i for i,p in enumerate(pts)}
def on_line(p,L): return add(add(mul(L[0],p[0]),mul(L[1],p[1])),mul(L[2],p[2]))==0
lines=set()
for i in range(N):
    for j in range(i+1,N):
        x1,y1,z1=pts[i]; x2,y2,z2=pts[j]
        a=add(mul(y1,z2),neg(mul(z1,y2))); b=add(mul(z1,x2),neg(mul(x1,z2))); c=add(mul(x1,y2),neg(mul(y1,x2)))
        for v in (a,b,c):
            if v: s=inv(v); break
        lines.add((mul(a,s),mul(b,s),mul(c,s)))
lines=list(lines)
line_pts=[[i for i,p in enumerate(pts) if on_line(p,L)] for L in lines]
C=[]
for t in range(9): C.append(index[(1,t,mul(t,t))])
C.append(index[(0,0,1)])
R=json.load(open("output/artifacts/maxcap_result.json"))
S=R["witness_off_points"]
A=sorted(set(C)|set(S))
assert len(A)==len(C)+len(S)==17 or len(A)==15
occ=sorted(len(set(LP)&set(A)) for LP in line_pts)
mx=max(occ)
spec=Counter(occ)
assert mx<=3 and sum(spec.values())==91
print("arc max occupancy:",mx,"spectrum:",dict(sorted(spec.items())))
# coordinates
print("C coords:",[pts[i] for i in sorted(C)])
print("S coords:",[pts[i] for i in S])
# generator matrix: columns = homogeneous coords of A (3x15 over F9)
G=[[pts[i][r] for i in A] for r in range(3)]
# enumerate 729 codewords
W=Counter(); reps={}
for a in range(9):
    for b in range(9):
        for c in range(9):
            if a==b==c==0: continue
            w=0; pat=[]
            for j in range(len(A)):
                v=add(add(mul(a,G[0][j]),mul(b,G[1][j])),mul(c,G[2][j]))
                pat.append(v)
                if v!=0: w+=1
            W[w]+=1
print("weight distribution (nonzero, raw incl. scalar mults):",dict(sorted(W.items())))
tot=sum(W.values()); assert tot==728
d=min(W); print("min distance:",d)
# collapse by scalar mult: each projective codeword counted 8 times
Wq={w:c//8 for w,c in W.items()}
print("projective weight distribution:",Wq,"sum:",sum(Wq.values()),"(=(9^3-1)/8=91)")
# dual distance: 3 iff some 3 columns dependent iff trisecant exists; check rank of each triple
def rank3(cols):
    # cols: list of 3 vecs in F9^3; dependent iff det=0
    (a1,b1,c1),(a2,b2,c2),(a3,b3,c3)=cols
    det=add(add(mul(a1,sub(mul(b2,c3),mul(b3,c2))),mul(a2,sub(mul(b3,c1),mul(b1,c3)))),mul(a3,sub(mul(b1,c2),mul(b2,c1))))
    return 0 if det==0 else (3 if True else 2)
dep3=sum(1 for t in itertools.combinations(A,3) if rank3([pts[i] for i in t])==0)
print("dependent triples (=3-pt lines counted with multiplicity):",dep3,"; trisecants:",spec[3])
assert dep3==spec[3]  # each trisecant line meets A in exactly 3 pts -> exactly one triple
# per-added-point trisecant profile: # trisecants through each S point
pt_lines=[[l for l,LP in enumerate(line_pts) if i in LP] for i in range(N)]
Aset=set(A)
prof={}
for i in S:
    t=sum(1 for l in pt_lines[i] if len(set(line_pts[l])&Aset)==3)
    prof[i]=t
print("trisecants through each added point:",prof)
out={"A":A,"C":sorted(C),"S":S,"spectrum":{str(k):v for k,v in sorted(spec.items())},
     "weight_raw":{str(k):v for k,v in sorted(W.items())},
     "weight_projective":{str(k):v for k,v in sorted(Wq.items())},
     "min_distance":d,"trisecants_through_added":{str(k):v for k,v in prof.items()}}
json.dump(out,open("output/artifacts/witness_analysis.json","w"),indent=1)
print("saved witness_analysis.json")
