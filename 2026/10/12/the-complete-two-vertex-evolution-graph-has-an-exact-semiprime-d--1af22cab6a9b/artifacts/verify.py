from itertools import product

def scale(s,x,q): return (s*x[0]%q,s*x[1]%q)

def mul(x,y,params,q):
    a,b,c,d=params
    z1=x[0]*y[0]%q
    z2=x[1]*y[1]%q
    return ((z1*a+z2*b)%q,(z1*c+z2*d)%q)

def lines(q):
    return [(1,t) for t in range(q)] + [(0,1)]

def in_line(x,v,q):
    if x==(0,0): return True
    if v[0]:
        s=x[0]*pow(v[0],-1,q)%q
        return scale(s,v,q)==x
    return x[0]==0

def is_ideal_line(v,params,q):
    e1=(1,0); e2=(0,1)
    return in_line(mul(v,e1,params,q),v,q) and in_line(mul(v,e2,params,q),v,q)

def ideal_lines(params,q):
    return [v for v in lines(q) if is_ideal_line(v,params,q)]

def line_square_zero(v,params,q):
    return mul(v,v,params,q)==(0,0)

def product_zero(I,J,params,q):
    e=[(1,0),(0,1)]
    Bi=e if I is None else [I]
    Bj=e if J is None else [J]
    return all(mul(x,y,params,q)==(0,0) for x in Bi for y in Bj)

def direct_semiprime(params,q):
    return all(not line_square_zero(v,params,q) for v in ideal_lines(params,q))

def direct_prime(params,q):
    ideals=[None]+ideal_lines(params,q)
    return all(not product_zero(I,J,params,q) for I in ideals for J in ideals)

for q in (2,3,5,7):
    total=perfect=semiprime_nonperfect=nonsemiprime=prime_count=0
    for a,b,c,d in product(range(1,q),repeat=4):
        params=(a,b,c,d)
        total+=1
        det=(a*d-b*c)%q
        defect=(pow(a,3,q)+b*c*c)%q
        predicted_nonsemiprime=(det==0 and defect==0)

        sp=direct_semiprime(params,q)
        pr=direct_prime(params,q)
        assert sp==pr
        assert (not sp)==predicted_nonsemiprime

        if det:
            perfect+=1
            assert sp
        elif sp:
            semiprime_nonperfect+=1
        else:
            nonsemiprime+=1
        prime_count+=pr

    assert total==(q-1)**4
    assert nonsemiprime==(q-1)**2
    assert perfect==(q-1)**3*(q-2)
    assert semiprime_nonperfect==(q-1)**2*(q-2)
    assert prime_count==q*(q-2)*(q-1)**2
    print({"q":q,"total":total,"perfect":perfect,
           "semiprime_nonperfect":semiprime_nonperfect,
           "nonsemiprime":nonsemiprime,
           "prime_semiprime_total":prime_count})
print("VERIFY_OK")
