"""Independent genus-two quotient computation using Fp and a quadratic extension.
Execute: python3 verify_quotients.py (stdlib only)."""
EXPECTED = {11:{0:0,1:6,3:10,4:-2,5:16,6:-16,7:2,8:-10,10:-6},
            13:{0:0,1:6,3:-10,4:-16,5:-10,6:14,7:-14,8:10,9:16,10:10,12:-6}}

def add(x,y,p):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def mul(x,y,p,d):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def scale(x,c,p):return (x[0]*c%p,x[1]*c%p)

def count_quotient(p,a,sgn,n):
    d= -1 if p==11 else -2
    elems=[(u,0) for u in range(p)] if n==1 else [(u,v) for v in range(p) for u in range(p)]
    zero=(0,0); one=(1,0)
    sq={mul(z,z,p,d) for z in elems if z!=zero}
    total=1
    for t in elems:
        t2=mul(t,t,p,d);t4=mul(t2,t2,p,d)
        factor=add(t,(2*sgn%p,0),p)
        second=add(add(t4,scale(t2,-4,p),p),((2+a)%p,0),p)
        rhs=mul(factor,second,p,d)
        total+=1+(0 if rhs==zero else (1 if rhs in sq else -1))
    return total

def run():
 for p, table in EXPECTED.items():
    # Check quadratic extension generator has no root in Fp.
    d=-1 if p==11 else -2
    assert all((u*u-d)%p for u in range(p))
    assert len(table)==p-2
    for a,b in table.items():
        ns=[[count_quotient(p,a,sign,n) for n in (1,2)] for sign in (1,-1)]
        assert ns[0][0]==p+1,(p,a,ns)
        assert ns[0][1]==p*p+1+2*b,(p,a,ns,b)
        # The two genus-two quotients have identical Frobenius numerators.
        assert ns[1]==ns[0],(p,a,ns)
        # Genus-two Weil numerator (1 + b*T^2 + p^2*T^4) follows
        # from N1,N2 plus the genus-two functional equation.
        assert abs(b)<=2*p
    assert len(set(table.values()))==(9 if p==11 else 9)
    if p==13:
        collision={z:sorted(a for a,b in table.items() if b==z) for z in set(table.values())}
        assert sorted(v for v in collision.values() if len(v)>1)==[[3,5],[8,10]]
        assert (3*3-5*5)%13!=0 and (8*8-10*10)%13!=0
 print('QUOTIENT_REPLAY_OK')
if __name__=='__main__':run()
