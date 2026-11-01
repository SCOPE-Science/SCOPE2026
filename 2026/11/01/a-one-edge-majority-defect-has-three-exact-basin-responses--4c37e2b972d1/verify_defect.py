"""Exact finite-state algebra and independent bit-level tests for majority on a biclique with one missing edge.

Requires Python 3.10+ and sympy. The mathematical justification for the finite class reduction is given in RESULT.md.
"""
from itertools import product
from math import comb
from sympy import symbols, expand

X_a,C_a,X_b,C_b=symbols('X_a C_a X_b C_b')


def vote(s,d,old):
    return 1 if 2*s>d else (0 if 2*s<d else old)


def quotient_step(a,b,state):
    p,q,u,v=state
    A,B=a-1,b-1
    pp=A if 2*(q+v)>b else (0 if 2*(q+v)<b else p)
    qq=B if 2*(p+u)>a else (0 if 2*(p+u)<a else q)
    return (pp,qq,vote(q,B,u),vote(p,A,v))


def tags(n):
    A=n-1
    if n==2: return {'Z':0,'O':1}
    k=A//2
    if n%2:
        ans={'Z':0,'M':k,'O':A}
        if k>=2:ans.update({'L':1,'H':A-1})
    else:
        ans={'Z':0,'m':k,'p':k+1,'O':A}
        if k>=2:ans.update({'L':1,'H':A-1})
    return ans


def tag_for(n,p):
    if p==0:return 'Z'
    if p==n-1:return 'O'
    A=n-1;k=A//2
    if n%2:
        if p<k:return 'L'
        if p==k:return 'M'
        return 'H'
    if p<k:return 'L'
    if p==k:return 'm'
    if p==k+1:return 'p'
    return 'H'


def tag_weight(n,X,C):
    if n==2:return {'Z':1,'O':1}
    if n%2: return {'Z':1,'O':1,'M':C,'L':(X-C)/2-1,'H':(X-C)/2-1}
    return {'Z':1,'O':1,'m':C,'p':C,'L':X/2-C-1,'H':X/2-C-1}


def orbit_info(a,b,state):
    seen={};x=state
    while x not in seen:
        seen[x]=len(seen)
        x=quotient_step(a,b,x)
    return seen[x],len(seen)-seen[x]


def category_census(a,b):
    TA,TB=tags(a),tags(b)
    WA,WB=tag_weight(a,X_a,C_a),tag_weight(b,X_b,C_b)
    E=0;R=0;B=0;T=0
    for ca,p in TA.items():
        for cb,q in TB.items():
            for u,v in product((0,1),repeat=2):
                t,r=orbit_info(a,b,(p,q,u,v))
                assert r in (1,2)
                w=WA[ca]*WB[cb]
                if t==0 and r==1:E+=w
                if t==0 and r==2:R+=w
                if r==2:B+=w
                T=max(T,t)
    return expand(E),expand(R),expand(B),T


def formula(a,b):
    if a==2 and b==2:
        E=4
    elif a==2:
        E=2+2*C_b
    elif b==2:
        E=2+2*C_a
    elif a%2==0 and b%2==0:
        E=2+2*C_a*C_b
    else:E=2
    if a==2 and b==2:
        B=2
    elif a==2:
        B=2*(X_b-C_b)
    elif b==2:
        B=2*(X_a-C_a)
    elif a%2 and b%2:
        B=2*X_a*X_b
    elif a%2==0 and b%2==0:
        B=2*(X_a-C_a)*(X_b-C_b)
    elif a%2==0:
        B=2*(X_a*X_b-C_a*(X_b-C_b))
    else:
        B=2*(X_a*X_b-C_b*(X_a-C_a))
    T=4 if (a==2 and b%2 or b==2 and a%2) else (3 if (a%2)!=(b%2) else 2)
    return expand(E),expand(B),T


def actual_graph_step(a,b,state):
    # State is a bit tuple: left vertices 0..a-1 and right a..a+b-1; missing edge (0,a).
    left=state[:a];right=state[a:]
    return tuple(vote(sum(right)-right[0] if i==0 else sum(right), b-1 if i==0 else b,left[i]) for i in range(a))+tuple(vote(sum(left)-left[0] if j==0 else sum(left),a-1 if j==0 else a,right[j]) for j in range(b))


def small_direct(a,b):
    E=R=B=0;T=0
    for st in product((0,1),repeat=a+b):
        seen={};x=st
        while x not in seen:
            seen[x]=len(seen)
            x=actual_graph_step(a,b,x)
        t=seen[x];r=len(seen)-t
        assert r in (1,2)
        T=max(T,t)
        if t==0 and r==1:E+=1
        if t==0 and r==2:R+=1
        if r==2:B+=1
    return E,R,B,T


def complete_census(a,b):
    E=R=B=0
    for p,q in product(range(a+1),range(b+1)):
        weight=comb(a,p)*comb(b,q)
        x=(p,q);seen={}
        def step(state):
            p,q=state
            return (a if 2*q>b else (0 if 2*q<b else p),
                    b if 2*p>a else (0 if 2*p<a else q))
        while x not in seen:
            seen[x]=len(seen)
            x=step(x)
        t=seen[x];r=len(seen)-t
        assert r in (1,2)
        if t==0 and r==1:E+=weight
        if t==0 and r==2:R+=weight
        if r==2:B+=weight
    return E,R,B


def main():
    # Mathematical class signatures: a=2, a odd >=3, a even >=4.
    # Class families absent at a=3 or a=4 have zero binomial weight.
    reps=(2,5,6)
    count=0
    for a,b in product(reps,repeat=2):
        E,R,B,T=category_census(a,b)
        e,predb,predt=formula(a,b)
        assert expand(E-e)==0,(a,b,'fixed',E,e)
        assert expand(R-2)==0,(a,b,'periodic two states',R)
        assert expand(B-predb)==0,(a,b,'basin',B,predb)
        assert T==predt,(a,b,T,predt)
        print(f'symbolic classes {a} x {b}: E={E}, R={R}, B={B}, T={T}')
        count+=1
    # Validate the class-equivariance for many actual dimensions and the endpoint strata.
    checks=0
    for a,b in product(range(2,31),repeat=2):
        A,B=a-1,b-1
        for p,q,u,v in product(range(a),range(b),(0,1),(0,1)):
            old=(tag_for(a,p),tag_for(b,q),u,v)
            new=quotient_step(a,b,(p,q,u,v))
            other=quotient_step(a,b,(tags(a)[old[0]],tags(b)[old[1]],u,v))
            assert (tag_for(a,new[0]),tag_for(b,new[1]),new[2],new[3]) == (tag_for(a,other[0]),tag_for(b,other[1]),other[2],other[3])
            checks+=1
        if a>2 and b>2:
            e,r,bsc,t=category_census(5 if a%2 else 6,5 if b%2 else 6)
        else:
            e,r,bsc,t=category_census(2 if a==2 else (5 if a%2 else 6),2 if b==2 else (5 if b%2 else 6))
        substitutions={X_a:2**(a-1),X_b:2**(b-1),C_a:comb(a-1,(a-1)//2),C_b:comb(b-1,(b-1)//2)}
        e0,b0,t0=formula(a,b)
        assert int(e.subs(substitutions))==int(e0.subs(substitutions))
        assert int(bsc.subs(substitutions))==int(b0.subs(substitutions))
        assert t==t0
    print('quotient compatibility checks:',checks)
    nstates=0
    for a,b in product(range(2,8),repeat=2):
        E,R,B,T=small_direct(a,b)
        e,bsc,t=formula(a,b)
        vals={X_a:2**(a-1),X_b:2**(b-1),C_a:comb(a-1,(a-1)//2),C_b:comb(b-1,(b-1)//2)}
        assert (E,R,B,T)==(int(e.subs(vals)),2,int(bsc.subs(vals)),t),(a,b,E,R,B,T)
        nstates+=2**(a+b)
    print('independent bit-level initial states checked:',nstates)
    baseline=0
    for a,b in product(range(2,31),repeat=2):
        E,R,B=complete_census(a,b)
        Ca=comb(a-1,(a-1)//2) if a%2==0 else 0
        Cb=comb(b-1,(b-1)//2) if b%2==0 else 0
        assert E==(2+4*Ca*Cb if a%2==0 and b%2==0 else 2)
        assert R==2
        assert B==2*(2**(a-1)-Ca)*(2**(b-1)-Cb)
        baseline+=1
    print('complete-biclique comparison cases:',baseline)
    print('nine symbolic class cases, formulas, period counts, sharp times: PASS')

if __name__=='__main__':main()
