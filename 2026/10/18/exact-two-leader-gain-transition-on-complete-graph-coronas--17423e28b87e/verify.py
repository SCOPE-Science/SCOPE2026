"""Reproduce the exact two-leader classification on complete-graph one-leaf coronas.
Requires sympy. Run: python verify.py
"""
import itertools
import sympy as sp

m,k,t=sp.symbols('m k t',positive=True)
# Graph Laplacian resolvent: eliminate the pendant variables.
U=(t+1)/(t*(t+2))
V=(t+1)/(t*(t+2)+m*(t+1))
core_diag=(U+(m-1)*V)/m
core_off=(U-V)/m
leaf_diag=1/(1+t)+core_diag/(1+t)**2
leaf_off=core_off/(1+t)**2
own=core_diag/(1+t)
other=core_off/(1+t)
base=sp.Rational(1,2)+(m-1)*(m+2)/m
c=1/(2*m)

def finite_coeff(f,n):
    return sp.factor(sp.diff(f-c/t,t,n).limit(t,0)/sp.factorial(n))

def trace_formula(g1,g2,h):
    a,b,z=(finite_coeff(v,0) for v in (g1,g2,h))
    a1,b1,z1=(finite_coeff(v,1) for v in (g1,g2,h))
    A=(k/m)*(1+k*(a+b-2*z)/2)
    B=1+k*(a+b)+k**2*(a*b-z**2+c*(a1+b1-2*z1))
    return sp.factor(base+B/A)

f={
    'CC':trace_formula(core_diag,core_diag,core_off),
    'LL':trace_formula(leaf_diag,leaf_diag,leaf_off),
    'CO':trace_formula(core_diag,leaf_diag,own),
    'CX':trace_formula(core_diag,leaf_diag,other),
}
expected={
 'CC':(k**2*(m*m+3*m-6)+k*(m**3+4*m*m-4*m)+m**3)/(k*m*(k+m)),
 'CX':(k**2*(m**3+5*m*m-2*m-12)+k*(4*m**3+6*m*m-8*m)+2*m**3)/(k*m*(k*(m+2)+2*m)),
}
for name,v in expected.items():
    assert sp.cancel(f[name]-v)==0,(name,'formula')
print('General rational resolvent identities: OK (CC, CX)')

positive_polynomial=(k**2*(m*m-2*m-2)+k*m*(m-3)*(m+2)+m*m*(m-2))
assert sp.factor(f['CC']-f['LL']) == sp.factor(-positive_polynomial/((k+m)*(k*(m+1)+m)))
assert sp.factor(f['CC']-f['CO']) == sp.factor(-(2*k*k+k*(m*m+4)+m**3)/(m*(k+2)*(k+m)))
phase=2*k*k+m*(6-m)*k-m*m*(m-2)
assert sp.cancel((f['CC']-f['CX'])-phase/((k+m)*(k*(m+2)+2*m))) == 0
print('Three global orbit-comparison identities: OK')

# Independent direct matrix builds; all unordered pairs checked exactly.
for M in range(3,8):
    N=2*M
    L=sp.zeros(N)
    def add(u,v):
        L[u,u]+=1; L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    for u in range(M):
        for v in range(u+1,M):add(u,v)
        add(u,M+u)
    for K in (sp.Rational(1,5),sp.Rational(1,1),sp.Rational(5,1),sp.Rational(100,1)):
        vals={}
        for u,v in itertools.combinations(range(N),2):
            A=L.copy()
            A[u,u]+=K;A[v,v]+=K
            direct=sp.trace(A.inv())
            typ= ('CC' if u<M and v<M else
                  'LL' if u>=M and v>=M else
                  'CO' if (u%M)==(v%M) else 'CX')
            predicted=sp.factor(f[typ].subs({m:M,k:K}))
            assert direct==predicted,(M,K,u,v,typ,direct,predicted)
            vals[(u,v)]=direct
        minv=min(vals.values())
        critical=sp.Rational(M,4)*(M-6+sp.sqrt((M-2)**2+16))
        winning={'CC'} if K<critical else {'CX'} if K>critical else {'CC','CX'}
        good=[a for a,v in vals.items() if v==minv]
        assert all(('CC' if a[0]<M and a[1]<M else
                    'LL' if a[0]>=M else
                    'CO' if a[0]%M==a[1]%M else 'CX') in winning for a in good)
    print(f'Exact exhaustive node-pair checks: m={M}, 4 gains, {N*(N-1)//2} pairs each: OK')
print('All checks PASS')
