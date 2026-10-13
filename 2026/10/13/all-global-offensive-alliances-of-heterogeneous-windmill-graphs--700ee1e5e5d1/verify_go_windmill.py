from itertools import product
from math import comb


def verts(ms):
    out=[('c',-1,-1)]
    for i,m in enumerate(ms):
        out += [('b',i,j) for j in range(m)]
    return out

def adjacent(u,v):
    if u==v: return False
    if u[0]=='c' or v[0]=='c': return True
    return u[1]==v[1]

def is_goa(ms,mask):
    V=verts(ms); S={V[k] for k in range(len(V)) if (mask>>k)&1}
    if not S: return False
    for v in V:
        if v in S: continue
        ins=sum(adjacent(v,u) for u in S)
        outs=sum(adjacent(v,u) for u in V if u not in S)
        if ins < outs+1:
            return False
    return True

def criterion(ms,mask):
    V=verts(ms)
    cin = bool(mask & 1)
    s=[]
    off=1
    for m in ms:
        si=sum((mask>>(off+j))&1 for j in range(m)); off+=m; s.append(si)
    if cin:
        return all(si >= m//2 for si,m in zip(s,ms))
    return all(si >= m//2+1 for si,m in zip(s,ms))

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def predicted_coeff(ms):
    A=[1]
    for m in ms:
        p=[0]*(m+1)
        for k in range(m//2,m+1): p[k]=comb(m,k)
        A=conv(A,p)
    A=[0]+A
    B=[1]
    for m in ms:
        p=[0]*(m+1)
        for k in range(m//2+1,m+1): p[k]=comb(m,k)
        B=conv(B,p)
    n=max(len(A),len(B)); A+= [0]*(n-len(A)); B += [0]*(n-len(B))
    return [A[i]+B[i] for i in range(n)]

subset_checks=criterion_checks=coef_checks=min_checks=0
cases=[]
for r in range(2,5):
    for ms in product(range(1,5), repeat=r):
        if 1+sum(ms)>12: continue
        V=verts(ms); N=len(V)
        coeff=[0]*(N+1)
        for mask in range(1<<N):
            a=is_goa(ms,mask); b=criterion(ms,mask)
            subset_checks+=1; criterion_checks+=1
            assert a==b,(ms,mask,a,b)
            if a: coeff[mask.bit_count()]+=1
        pred=predicted_coeff(ms)
        pred += [0]*(len(coeff)-len(pred))
        assert coeff==pred[:len(coeff)],(ms,coeff,pred)
        coef_checks += len(coeff)
        gamma=1+sum(m//2 for m in ms)
        mn=min(i for i,c in enumerate(coeff) if c)
        assert mn==gamma,(ms,mn,gamma)
        expected=1
        for m in ms: expected*=comb(m,m//2)
        assert coeff[gamma]==expected,(ms,coeff[gamma],expected)
        min_checks+=2
        cases.append(ms)
print(f'VERIFY_OK tuples={len(cases)} subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coef_checks} minimum_checks={min_checks} max_order={max(1+sum(ms) for ms in cases)}')
