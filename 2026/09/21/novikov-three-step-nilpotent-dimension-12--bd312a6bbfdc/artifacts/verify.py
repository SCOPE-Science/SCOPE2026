"""Exact verification for the 12-dimensional 3-step nilpotent Lie algebra in RESULT.md.

The calculation uses only Python's standard-library Fraction arithmetic.
It reconstructs the linear consequences of the Novikov identities used in
Burde--Dekimpe--Vercammen (2008), then reduces one right-multiplication
commutator entry to the nonzero constant -1/4.
"""
from fractions import Fraction
from itertools import combinations

n = 12
G1 = set(range(4))
G2 = set(range(4, 8))
G3 = set(range(8, 12))
G23 = G2 | G3

# Nonzero brackets [x_i,x_j] for i<j, with 0-based indices.
br = {
    (0,1): {4:1}, (2,3): {4:-1}, (0,3): {5:1},
    (2,4): {10:-1}, (0,5): {9:1}, (2,7): {8:1},
    (0,6): {10:1}, (3,4): {11:-1}, (0,7): {11:1},
    (3,5): {8:1}, (1,2): {6:1},
    (3,6): {8:-1, 9:-2, 10:2},
    (1,3): {7:1},
    (1,4): {8:-2, 9:-2, 10:2},
    (1,6): {8:-2, 9:-2, 10:2},
}

def B(i,j):
    if i < j: return br.get((i,j), {})
    if i > j: return {r:-c for r,c in br.get((j,i), {}).items()}
    return {}

def vid(i,r,c):
    return (i*n+r)*n+c

def add(row, v, a):
    if not a: return
    z = row.get(v, Fraction(0)) + Fraction(a)
    if z: row[v] = z
    elif v in row: del row[v]

class Echelon:
    def __init__(self): self.rows = {}
    def put(self, row, rhs=0):
        row = {k:Fraction(v) for k,v in row.items() if v}
        rhs = Fraction(rhs)
        while row:
            p = min(row)
            if p not in self.rows:
                a = row[p]
                self.rows[p] = ({k:v/a for k,v in row.items()}, rhs/a)
                return
            prow, prhs = self.rows[p]
            a = row[p]
            for k,v in prow.items():
                z = row.get(k, Fraction(0)) - a*v
                if z: row[k] = z
                elif k in row: del row[k]
            rhs -= a*prhs
        assert rhs == 0, ("linear contradiction", rhs)
    def expressions(self):
        out = {}
        for p in sorted(self.rows, reverse=True):
            row, rhs = self.rows[p]
            c, d = rhs, {}
            for q,a in row.items():
                if q == p: continue
                f = -a
                if q in out:
                    cq,dq = out[q]
                    c += f*cq
                    for u,z in dq.items():
                        d[u] = d.get(u,Fraction(0)) + f*z
                        if not d[u]: del d[u]
                else:
                    d[q] = d.get(q,Fraction(0)) + f
                    if not d[q]: del d[q]
            out[p] = (c,d)
        return out

E = Echelon()

def zero(i,r,c): E.put({vid(i,r,c):1})

# Lower-central-series ideal restrictions, exactly as in the 2008 argument.
for i in range(n):
    for r in G1:
        for c in G23: zero(i,r,c)
    for r in G2:
        for c in G3: zero(i,r,c)
for i in G23:
    for r in G1:
        for c in G1: zero(i,r,c)
    for r in G2:
        for c in G2: zero(i,r,c)
    for r in G3:
        for c in G3: zero(i,r,c)
for i in G3:
    for r in G2:
        for c in G1: zero(i,r,c)
    for r in G3:
        for c in G2: zero(i,r,c)
assert len(E.rows) == 1088

# ad(x)=L(x)-R(x), equivalently L_i e_j-L_j e_i=[x_i,x_j].
for i,j in combinations(range(n),2):
    b = B(i,j)
    for r in range(n):
        E.put({vid(i,r,j):1, vid(j,r,i):-1}, b.get(r,0))
assert len(E.rows) == 1376

# Novikov cyclic identity: x_i.[x_j,x_k]+x_j.[x_k,x_i]+x_k.[x_i,x_j]=0.
for i,j,k in combinations(range(n),3):
    b1,b2,b3 = B(j,k),B(k,i),B(i,j)
    if not (b1 or b2 or b3): continue
    for r in range(n):
        row = {}
        for s,a in b1.items(): add(row,vid(i,r,s),a)
        for s,a in b2.items(): add(row,vid(j,r,s),a)
        for s,a in b3.items(): add(row,vid(k,r,s),a)
        if row: E.put(row)
assert len(E.rows) == 1504

# Sparse adjoint matrices, columns are images of basis vectors.
ad = []
for i in range(n):
    M = {}
    for c in range(n):
        for r,a in B(i,c).items(): M[(r,c)] = Fraction(a)
    ad.append(M)

# Operator identity
# L([x,y])+ad([x,y])-[ad(x),L(y)]-[L(x),ad(y)]=0.
for i,j in combinations(range(n),2):
    bij = B(i,j)
    for r in range(n):
        for c in range(n):
            row, rhs = {}, Fraction(0)
            for s,a in bij.items(): add(row,vid(s,r,c),a)
            rhs -= sum(Fraction(a)*ad[s].get((r,c),0) for s,a in bij.items())
            for t in range(n):
                a = ad[i].get((r,t),0)
                if a: add(row,vid(j,t,c),-a)
                a = ad[i].get((t,c),0)
                if a: add(row,vid(j,r,t),a)
                a = ad[j].get((t,c),0)
                if a: add(row,vid(i,r,t),-a)
                a = ad[j].get((r,t),0)
                if a: add(row,vid(i,t,c),a)
            if row or rhs: E.put(row,rhs)
assert len(E.rows) == 1678
assert n**3-len(E.rows) == 50

expr = E.expressions()
def affine(v): return expr.get(v,(Fraction(0),{v:Fraction(1)}))

def mul(A,B):
    ca,da=A; cb,db=B
    c=ca*cb; l={}; q={}
    for u,z in da.items(): l[u]=l.get(u,Fraction(0))+z*cb
    for u,z in db.items(): l[u]=l.get(u,Fraction(0))+z*ca
    for u,z in da.items():
        for v,w in db.items():
            key=(u,v) if u<=v else (v,u)
            q[key]=q.get(key,Fraction(0))+z*w
    return c,{u:z for u,z in l.items() if z},{u:z for u,z in q.items() if z}

def plus(P,Q,sign=1):
    c,l,q=P; c2,l2,q2=Q
    l=dict(l); q=dict(q); c += sign*c2
    for u,z in l2.items():
        l[u]=l.get(u,Fraction(0))+sign*z
        if not l[u]: del l[u]
    for u,z in q2.items():
        q[u]=q.get(u,Fraction(0))+sign*z
        if not q[u]: del q[u]
    return c,l,q

# R_i(r,c)=L_c(r,i).  Evaluate [R_2,R_3] at row 11, column 2.
i,j,r,c = 1,2,10,1
P=(Fraction(0),{}, {})
for t in range(n):
    P=plus(P,mul(affine(vid(t,r,i)), affine(vid(c,t,j))),1)
    P=plus(P,mul(affine(vid(t,r,j)), affine(vid(c,t,i))),-1)
assert P == (Fraction(-1,4),{}, {})

print("linear ranks: 1088, 1376, 1504, 1678; free variables: 50")
print("[R_2,R_3]_(11,2) = -1/4")
