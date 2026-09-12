"""Final independent verifier for the transposition-type witness.

Rebuilds rotation system from scratch (no shared code with the search),
checks: K(4,10) structure, symmetry g=(phi,+1) with b0=[0,2,1,3],
g has order 10 and acts as a 10-cycle on B, rotation system well-formed,
face trace gives F=20 all length-4 (=> genus 4), Euler check.
"""
import json

A = [0,1,2,3]; B = list(range(10))
phi = [1,0,2,3]
rotA = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],[0,9,8,7,6,5,4,3,2,1]]
rotB0 = [0,2,1,3]
rotB = [None]*10; rotB[0]=list(rotB0)
for i in range(1,10):
    rotB[i]=[phi[a] for a in rotB[i-1]]

res = {}
# 1. well-formed rotations
assert all(sorted(r)==B for r in rotA), 'rotA malformed'
assert all(sorted(r)==A for r in rotB), 'rotB malformed'
res['rotations_wellformed'] = True
# 2. symmetry (cyclic-order sense)
def same_cyc(X,Y):
    n=len(X)
    return any(all(X[(r+t)%n]==Y[t] for t in range(n)) for r in range(n))
for i in range(10):
    assert same_cyc([phi[a] for a in rotB[i]], rotB[(i+1)%10]), f'rotB symm fails at {i}'
for j in range(4):
    assert same_cyc([(x+1)%10 for x in rotA[j]], rotA[phi[j]]), f'rotA symm fails at {j}'
res['symmetric'] = True
# 3. g order + B action
seen=set(); cur=0; cyc=[]
while cur not in seen:
    seen.add(cur); cyc.append(cur); cur=(cur+1)%10
assert len(cyc)==10, 'B action not a 10-cycle'
res['B_action_is_10cycle'] = True
# dart order of g
vis=set(); order=1
from math import gcd
def lcm(a,b): return a*b//gcd(a,b)
for s in (0,1):
    for x in (range(4) if s==0 else range(10)):
        for y in (range(10) if s==0 else range(4)):
            if (s,x,y) in vis: continue
            cur=(s,x,y); L=0
            while cur not in vis:
                vis.add(cur); L+=1
                a,b2,c=cur
                cur=(0,phi[b2],(c+1)%10) if a==0 else (1,(b2+1)%10,phi[c])
            order=lcm(order,L)
res['g_order']=order
assert order==10
# 4. face trace (independent implementation)
succA=[{b:r[(t+1)%len(r)] for t,b in enumerate(r)} for r in rotA]
succB=[{a:r[(t+1)%len(r)] for t,a in enumerate(r)} for r in rotB]
seen=set(); faces=[]
for j in range(4):
    for b in range(10):
        if (0,j,b) in seen: continue
        cur=(0,j,b); f=[]
        while cur not in seen:
            seen.add(cur); f.append(cur)
            _,x,y=cur
            cur=(1,y,succB[y][x]) if cur[0]==0 else (0,succA[x][y],y) if False else None
            # careful: unpack properly
            break
        break
    break
# (redo cleanly below to avoid the muddled line above)
seen=set(); faces=[]
for j in range(4):
    for b in range(10):
        if (0,j,b) in seen: continue
        cur=(0,j,b); f=[]
        while cur not in seen:
            seen.add(cur); f.append(cur)
            if cur[0]==0:
                _,jj,bb=cur
                cur=(1,bb,succB[bb][jj])
            else:
                _,bb,jj=cur
                cur=(0,succA[jj][bb] if False else jj,succA[jj][bb])
                # state (0, j_next=A-vertex, b_next): A-vertex stays jj? No:
                # from B-side dart (bb,jj) we go to A-side (jj, b_next)
                cur=(0,jj,succA[jj][bb])
        faces.append(f)
V=14; E=40; F=len(faces)
lens=sorted(len(f) for f in faces)
res.update({'F':F,'face_lengths':lens,'euler_genus':(2-(V-E+F))//2})
assert F==20 and all(L==4 for L in lens), f'not all quads: F={F} {lens}'
assert V-E+F==2-2*4
res['min_genus_quad']=True
print(json.dumps(res,indent=1))
with open('output/artifacts/verification.json','w') as f:
    json.dump({'rotA':rotA,'rotB':[list(r) for r in rotB],'phi':phi,'result':res},f,indent=1)
