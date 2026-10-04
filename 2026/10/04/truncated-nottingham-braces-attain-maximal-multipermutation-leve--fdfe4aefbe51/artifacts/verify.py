from itertools import product

def add(a,b,p): return tuple((x+y)%p for x,y in zip(a,b))

def compose_tangent(f,g,p,N):
    # f,g store coefficients of x^2,...,x^N. Return f(x+g) modulo x^(N+1).
    h=[0]*(N+1); h[1]=1
    for j,c in enumerate(g,2): h[j]=c%p
    out=[0]*(N+1)
    power=[0]*(N+1); power[0]=1
    for d in range(1,N+1):
        new=[0]*(N+1)
        for i,a in enumerate(power):
            if not a: continue
            for j,b in enumerate(h):
                if b and i+j<=N: new[i+j]=(new[i+j]+a*b)%p
        power=new
        if d>=2:
            c=f[d-2]%p
            if c:
                for k,a in enumerate(power): out[k]=(out[k]+c*a)%p
    return tuple(out[2:])

def star(f,g,p,N):
    return add(g,compose_tangent(f,g,p,N),p)

def socle(p,N):
    els=list(product(range(p), repeat=N-1))
    zero=(0,)*(N-1)
    S=[]
    for g in els:
        ok=True
        for f in els:
            # lambda_g(f)=f(x+g), for the associated left brace with reversed multiplication.
            if compose_tangent(f,g,p,N)!=f:
                ok=False; break
        if ok:S.append(g)
    pred=[tuple(([0]*(N-2))+[c]) for c in range(p)] if N>=2 else [zero]
    return els,S,pred

def quotient_sanity(p,N):
    # dropping the top coefficient intertwines the right-brace multiplication B_N -> B_(N-1)
    if N<=2:return True
    els=list(product(range(p), repeat=N-1))
    for f in els:
        for g in els:
            lhs=star(f,g,p,N)[:-1]
            rhs=star(f[:-1],g[:-1],p,N-1)
            if lhs!=rhs:return False
    return True

def run():
    cases=[(3,2),(3,3),(5,4)]
    for p,N in cases:
        els,S,pred=socle(p,N)
        assert set(S)==set(pred)
        assert quotient_sanity(p,N)
        print(f'p={p} N={N} order={len(els)} socle_size={len(S)} quotient_ok=True')
    print('CHECK_OK')
if __name__=='__main__': run()
