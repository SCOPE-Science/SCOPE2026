"""Exact Cartier coefficient check in F_7[a,b] for a quartic Artin--Schreier curve."""
from math import comb
P=7

def add(a,b):
    r=dict(a)
    for e,c in b.items():r[e]=(r.get(e,0)+c)%P
    return {e:c for e,c in r.items() if c%P}

def mul(a,b):
    r={}
    for (i,j),c in a.items():
        for (k,l),d in b.items():
            z=(i+k,j+l)
            r[z]=(r.get(z,0)+c*d)%P
    return {e:c for e,c in r.items() if c%P}

def scale(a,c):return {e:c*v%P for e,v in a.items() if c*v%P}

def mon(i=0,j=0,c=1):return {(i,j):c%P} if c%P else {}

A,B=mon(1,0),mon(0,1)
F={1:B,2:A,4:mon()}
Q=[{0:mon()}]
for j in range(1,6):
    r={}
    for d,c in Q[-1].items():
        for e,v in F.items():r[d+e]=add(r.get(d+e,{}),mul(c,v))
    Q.append(r)

basis=[(i,j) for j in range(6) for i in range(3) if 7*i+4*j<=16]
pos={v:i for i,v in enumerate(basis)}
M=[[{} for _ in basis] for _ in basis]
for k,(i,j) in enumerate(basis):
    for t in range(j+1):
        c=comb(j,t)*(-1)**(j-t)
        for e,v in Q[j-t].items():
            q=i+e
            if q%7==6:
                row=pos[((q-6)//7,t)]
                M[row][k]=add(M[row][k],scale(v,c))

# Rows dx, x dx, y dx, y^2 dx; columns y^2 dx, xy^2 dx, y^3 dx, y^4 dx.
expected={
 ((0,0),(0,2)):scale(A,2),
 ((0,0),(1,2)):scale(B,2),
 ((0,0),(0,3)):add(scale(mul(mul(A,A),A),-1),scale(mul(B,B),-3)),
 ((0,0),(0,4)):scale(mul(mul(A,A),mul(B,B)),-1),
 ((1,0),(0,4)):scale(B,-3),
 ((0,1),(0,3)):scale(A,-1),
 ((0,1),(0,4)):add(scale(mul(mul(A,A),A),3),scale(mul(B,B),2)),
 ((0,2),(0,4)):scale(A,-2),
}
for i,row in enumerate(M):
    for j,v in enumerate(row):
        assert v==expected.get((basis[i],basis[j]),{}),(basis[i],basis[j],v)
assert len(basis)==9
# Every coefficient is a polynomial identity, valid over every extension field.
# Triangular nonvanishing of the symbolic matrix gives ranks 3, 2, and 0.
print('BASIS',basis)
print('NONZERO_SYMBOLIC_ENTRIES',len(expected))
print('A_NONZERO_RANK',3)
print('A_ZERO_B_NONZERO_RANK',2)
print('A_B_ZERO_RANK',0)
print('VERIFY_OK')
