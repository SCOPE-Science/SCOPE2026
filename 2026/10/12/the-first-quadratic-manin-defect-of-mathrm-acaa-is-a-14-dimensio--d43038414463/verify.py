from fractions import Fraction
from itertools import permutations
from collections import Counter

# Multilinear arity-4 monomials in one nonsymmetric binary operation.
# Leaves are 0,1,2,3 and a product is a tuple (left,right).
def trees(leaves):
    if len(leaves)==1:
        return [leaves[0]]
    out=[]
    for k in range(1,len(leaves)):
        for a in trees(leaves[:k]):
            for b in trees(leaves[k:]):
                out.append((a,b))
    return out

B=[]
for p in permutations(range(4)):
    B.extend(trees(p))
# The construction above can repeat no labelled planar tree.
assert len(B)==120 and len(set(B))==120
idx={m:i for i,m in enumerate(B)}

def mul(a,b): return (a,b)

def r1(x,y,z):
    # (x*y)*z + (x*z)*y
    return Counter({mul(mul(x,y),z):1, mul(mul(x,z),y):1})

def r2(x,y,z):
    # (x*y)*z + x*(y*z) + (y*x)*z + y*(x*z)
    return Counter({mul(mul(x,y),z):1, mul(x,mul(y,z)):1,
                    mul(mul(y,x),z):1, mul(y,mul(x,z)):1})

def subst(poly, old, new):
    def rec(t):
        if isinstance(t,int): return new if t==old else t
        return (rec(t[0]),rec(t[1]))
    return Counter({rec(m):c for m,c in poly.items()})

def rel_consequences(rel):
    # Five partial compositions generating the arity-4 part of the operadic ideal:
    # R o_i mu (i=1,2,3) and mu o_j R (j=1,2).
    base=[]
    # Use temporary leaves 0,1,2 for x,y,z, then insert a binary product of
    # one chosen leaf with the new leaf 3.
    q=rel(0,1,2)
    base.append(subst(q,0,mul(0,3)))
    base.append(subst(q,1,mul(1,3)))
    base.append(subst(q,2,mul(2,3)))
    base.append(Counter({mul(m,3):c for m,c in q.items()}))
    base.append(Counter({mul(3,m):c for m,c in q.items()}))
    return base

def perm_tree(t,p):
    if isinstance(t,int): return p[t]
    return (perm_tree(t[0],p),perm_tree(t[1],p))

rows=[]
for rel in (r1,r2):
    for q in rel_consequences(rel):
        for p in permutations(range(4)):
            v=[Fraction(0) for _ in B]
            for m,c in q.items():
                v[idx[perm_tree(m,p)]] += Fraction(c)
            rows.append(v)
assert len(rows)==240

# Exact RREF over Q.
def rref(mat):
    a=[row[:] for row in mat]
    m=len(a); n=len(a[0]); piv=[]; r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        z=a[r][c]
        a[r]=[x/z for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                z=a[i][c]
                a[i]=[a[i][j]-z*a[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    return a,piv

rr,piv=rref(rows)
rank=len(piv)
free=[j for j in range(120) if j not in set(piv)]
assert rank==106
assert len(free)==14
# Retain only nonzero RREF rows in pivot order.
rr=rr[:rank]
piv_to_row={c:i for i,c in enumerate(piv)}

# Reduce a basis vector e_j modulo the relation row space into the free-column quotient basis.
def reduce_basis(j):
    out=[Fraction(0) for _ in free]
    if j in piv_to_row:
        row=rr[piv_to_row[j]]
        for k,f in enumerate(free):
            out[k] = -row[f]
    else:
        out[free.index(j)] = Fraction(1)
    return out

# Character of S4 action on the 14-dimensional quotient.  A permutation relabels leaves.
def action_trace(p):
    tr=Fraction(0)
    for col,f in enumerate(free):
        image=perm_tree(B[f],p)
        coords=reduce_basis(idx[image])
        tr += coords[col]
    assert tr.denominator==1
    return int(tr)

reps={
    '1^4':(0,1,2,3),
    '2,1,1':(1,0,2,3),
    '2,2':(1,0,3,2),
    '3,1':(1,2,0,3),
    '4':(1,2,3,0),
}
chi={name:action_trace(p) for name,p in reps.items()}
assert chi=={'1^4':14,'2,1,1':-6,'2,2':2,'3,1':2,'4':0}

# S4 irreducible character table in the same class order.
classes=['1^4','2,1,1','2,2','3,1','4']
sizes=[1,6,3,8,6]
irr={
    '(4)':       [1, 1, 1, 1, 1],
    '(3,1)':     [3, 1,-1, 0,-1],
    '(2,2)':     [2, 0, 2,-1, 0],
    '(2,1,1)':   [3,-1,-1, 0, 1],
    '(1,1,1,1)': [1,-1, 1, 1,-1],
}
mult={}
for lam,ch in irr.items():
    num=sum(sz*chi[cl]*v for sz,cl,v in zip(sizes,classes,ch))
    assert num%24==0
    mult[lam]=num//24
assert mult=={'(4)':0,'(3,1)':0,'(2,2)':1,'(2,1,1)':3,'(1,1,1,1)':3}
assert sum(mult[k]*irr[k][0] for k in irr)==14

print('free_dimension=120')
print('arity4_relation_rows=240')
print('relation_rank_Q=106')
print('quotient_dimension=14')
print('character=' + repr(tuple(chi[c] for c in classes)))
print('specht_multiplicities=' + repr(mult))
print('CHECK_OK')
