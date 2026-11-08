"""Exact finite-state certificate for a four-versus-three reset response.

Python >=3.9, standard library only. The target is 0 in the five-vertex path;
all walkers start at vertex 2, jump at total rate one, and are killed upon
first target arrival. No external data are required.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product

EXPECTED = {
    1: (F(12), F(-10)),
    2: (F(1555,272), F(-169263,73984)),
    3: (F(629176456,168587283), F(-4963736468372212,9473890663107363)),
    4: (F(98335794451053,35264790234112), F(52393068681552240430947689,1243605430255921087768428544)),
}

def solve(a, b):
    # Exact Gauss-Jordan elimination with pivoting.
    n=len(a)
    aug=[list(map(F,row))+[F(b[i])] for i,row in enumerate(a)]
    for j in range(n):
        k=next((i for i in range(j,n) if aug[i][j]),None)
        assert k is not None, 'singular transient generator'
        aug[j],aug[k]=aug[k],aug[j]
        inv=1/aug[j][j]
        aug[j]=[z*inv for z in aug[j]]
        for i in range(n):
            if i==j or not aug[i][j]: continue
            r=aug[i][j]
            aug[i]=[x-r*y for x,y in zip(aug[i],aug[j])]
    return [row[-1] for row in aug]

def transition(v):
    # Individual jump rates. Jump to zero kills the whole joint process.
    if v==4: return [(3,F(1))]
    return [(v-1,F(1,2)),(v+1,F(1,2))]

def matrix_counts(n):
    states=sorted({tuple(t.count(i) for i in range(1,5)) for t in combinations_with_replacement(range(1,5),n)})
    ids={x:i for i,x in enumerate(states)}
    a=[[F(n if i==j else 0) for j in range(len(states))] for i in range(len(states))]
    for i,counts in enumerate(states):
        for v in range(1,5):
            for w,rate in transition(v):
                if w==0:continue
                nxt=list(counts)
                if not nxt[v-1]: continue
                nxt[v-1]-=1; nxt[w-1]+=1
                a[i][ids[tuple(nxt)]]-=counts[v-1]*rate
    return a, ids[(0,n,0,0)]

def moment_response(a, start):
    one=[F(1)]*len(a)
    u=solve(a,one)
    v=solve(a,u)
    mu=u[start]
    # E[T^2]/2 = v[start]; derivative of Poisson-restart MFPT at r=0.
    return mu,mu**2-v[start]

def matrix_labelled(n):
    states=list(product((1,2,3,4),repeat=n))
    ids={x:i for i,x in enumerate(states)}
    a=[[F(n if i==j else 0) for j in range(len(states))] for i in range(len(states))]
    for i,x in enumerate(states):
        for p,v in enumerate(x):
            for w,rate in transition(v):
                if w==0:continue
                nxt=x[:p]+(w,)+x[p+1:]
                a[i][ids[nxt]]-=rate
    return a, ids[(2,)*n]

def main():
    for n in range(1,5):
        a,start=matrix_counts(n)
        mu,d=moment_response(a,start)
        assert (mu,d)==EXPECTED[n],(n,mu,d)
        print('N=',n,'transient_states=',len(a),'E[T]=',mu,'d/dr E[T_r]|0=',d)
    # Independent unsymmetrized calculation for small cases.
    for n in (1,2,3):
        a,start=matrix_labelled(n)
        assert moment_response(a,start)==EXPECTED[n]
        print('independent labelled check passed:',n,'states',len(a))
    # Independent direct resetting-generator check at a positive rate.
    for n in (3,4):
        a,start=matrix_counts(n)
        r=F(1,1000)
        b=[row[:] for row in a]
        for i in range(len(b)):
            b[i][i]+=r
            b[i][start]-=r
        actual=solve(b,[F(1)]*len(b))[start]
        assert (actual-EXPECTED[n][0])*EXPECTED[n][1]>0
        print('positive reset check passed:',n,'r=1/1000')
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':main()
