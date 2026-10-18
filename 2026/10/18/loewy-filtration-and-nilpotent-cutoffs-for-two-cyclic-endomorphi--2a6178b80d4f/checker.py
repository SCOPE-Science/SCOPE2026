"""Exact finite verification for two-cyclic-summand endomorphism radical filtrations."""
from itertools import product

def mult(x,y,p,a,b):
    ma=p**a; mb=p**b
    A,B,C,D=x; E,F,G,H=y
    return ((A*E+B*G)%ma, (A*F+B*H)%ma,
            (C*E+D*G)%mb, (C*F+D*H)%mb)

def add(x,y,p,a,b):
    ma=p**a; mb=p**b
    return ((x[0]+y[0])%ma,(x[1]+y[1])%ma,
            (x[2]+y[2])%mb,(x[3]+y[3])%mb)

def all_end(p,a,b):
    d=b-a
    for A,B,C,D in product(range(p**a),range(p**a),range(p**a),range(p**b)):
        yield (A,B,p**d*C,D)

def radical_gen(p,a,b):
    d=b-a
    return ((p,0,0,0),(0,1,0,0),(0,0,p**d,0),(0,0,0,p))

def predicted_exp(p,a,b,k):
    d=b-a
    if d==1:
        u=(k+1)//2;v=k//2
        return max(a-u,0)+2*max(a-v,0)+max(b-u,0)
    return max(a-k,0)+2*max(a-k+1,0)+max(b-k,0)

def closure(gens,p,a,b):
    z=(0,0,0,0); S={z}
    for g in gens:
        new=set(); h=z
        for _ in range(p**b):
            new.update(add(x,h,p,a,b) for x in S)
            h=add(h,g,p,a,b)
            if h==z:break
        S=new
    return S

def run(p,a,b):
    assert a<b
    J={x for x in all_end(p,a,b) if x[0]%p==x[3]%p==0}
    assert len(J)==p**(3*a+b-2)
    generators=radical_gen(p,a,b)
    assert closure(generators,p,a,b)==J
    gens=list(generators)
    cutoff=2*b-1 if b==a+1 else b
    for k in range(1,cutoff+1):
        S=closure(gens,p,a,b)
        pred=p**predicted_exp(p,a,b,k)
        assert len(S)==pred, (p,a,b,k,len(S),pred)
        if k<cutoff: gens=[mult(x,y,p,a,b) for x in gens for y in generators]
        else: assert len(S)==1
    for f in J:
        x=f
        for k in range(1,cutoff+1):
            if x==(0,0,0,0):break
            x=mult(x,f,p,a,b)
        else:assert False,(p,a,b,f)
    print('PASS',p,a,b,'radical_order',len(J),'cutoff',cutoff)

def run_equal(p,b):
    M=p**b; Z=(0,0,0,0)
    w=(0,1,p%M,0)
    v=w
    for k in range(1,2*b+1):
        assert (v!=Z)==(k<2*b),(p,b,k,v)
        v=mult(v,w,p,b,b)
    for k in range(b+1):
        assert p**(4*max(b-k,0))>=1
    print('PASS_EQUAL',p,b,'max_nilpotent_index',2*b)

if __name__=='__main__':
    for triple in ((2,1,2),(3,1,2),(2,1,3),(2,2,3),(2,2,4),(2,3,4),(2,3,5)):
        run(*triple)
    for pair in ((2,1),(2,2),(3,2),(2,4)):
        run_equal(*pair)
    print('ALL_CHECKS_PASSED')
