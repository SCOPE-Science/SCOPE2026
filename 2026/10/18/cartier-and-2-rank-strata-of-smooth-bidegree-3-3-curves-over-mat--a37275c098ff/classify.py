from collections import Counter
from pathlib import Path

def rank(M):
    q=M[:];r=0
    for c in range(4):
        z=next((i for i in range(r,4) if q[i]&(1<<c)),None)
        if z is None:continue
        q[z],q[r]=q[r],q[z]
        for i in range(4):
            if i!=r and q[i]&(1<<c):q[i]^=q[r]
        r+=1
    return r

def hasse(mask):
    I=((1,1),(1,2),(2,1),(2,2))
    return [sum(((mask >> ((2*ic-ir)*4+(2*jc-jr)))&1)<<c for c,(ic,jc) in enumerate(I)) for ir,jr in I]

def mul(A,B):return [sum([0]) if False else __import__('functools').reduce(int.__xor__, (B[j] for j in range(4) if (A[i]>>j)&1),0) for i in range(4)]

def points(mask):
    P=0
    for X in (0,1,2):
        for Y in (0,1,2):
            bit=0
            for i in range(4):
                for j in range(4):
                    t=(int(i==3) if X==2 else (int(i==0) if X==0 else 1))*(int(j==3) if Y==2 else (int(j==0) if Y==0 else 1))
                    bit^=((mask>>(4*i+j))&1)&t
            P+=int(bit==0)
    return P

equations=Counter();classes=Counter();point_joint=Counter();stab=Counter()
for line in Path('orbit_reps.txt').read_text().splitlines():
    m,size=map(int,line.split())
    H=hasse(m);a=4-rank(H);P=H
    for _ in range(3):P=mul(P,H)
    f=rank(P);z=points(m)
    equations[(f,a)]+=size;classes[(f,a)]+=1;point_joint[(f,a,z)]+=size;stab[size]+=1
print('EQUATIONS_CLASSES')
for k in sorted(equations):print(*k,equations[k],classes[k])
print('POINT_TOTALS',sorted(Counter({z:sum(n for (f,a,n1),n in point_joint.items() if n1==z) for z in range(9)}).items()))
print('ORBIT_SIZE_COUNTS',sorted(stab.items()))
assert sum(equations.values())==16020 and sum(classes.values())==252
Path('statistics.txt').write_text(''.join(f'f={f} a={a} equations={equations[f,a]} classes={classes[f,a]}\n' for f,a in sorted(equations)))
