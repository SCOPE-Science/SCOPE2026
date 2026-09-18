from decimal import Decimal, localcontext

PREC = 90
EPS = Decimal('1e-80')
GAMMA = Decimal('0.5772156649015328606065120900824024310421593359399235988057672348848677267777')


def prod(xs):
    z=1
    for x in xs: z*=x
    return z

def sieve(n):
    a=bytearray(b'\x01')*(n+1); a[:2]=b'\x00\x00'
    for p in range(2,int(n**0.5)+1):
        if a[p]: a[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if a[i]]
PR=sieve(600)

def phi_sq(ps): return prod([p-1 for p in ps])

with localcontext() as ctx:
    ctx.prec=PREC
    def log_bounds(n):
        z=Decimal(n).ln(); return z-EPS,z+EPS
    def DU_y(y):
        return y-1-Decimal(1)/y-Decimal('3.15')/y**2-Decimal('12.85')/y**3-Decimal('71.3')/y**4-Decimal('463.2275')/y**5-Decimal('4585')/y**6
    def DL_y(y):
        return y-1-Decimal(1)/y-Decimal('2.85')/y**2-Decimal('13.15')/y**3-Decimal('70.7')/y**4-Decimal('458.7275')/y**5-Decimal('3428.7225')/y**6
    def DU(n): return DU_y(log_bounds(n)[0])
    def pi_upper(n): return Decimal(n)/DU(n)
    def pi_lower(n): return Decimal(n)/DL_y(log_bounds(n)[1])
    def rs_axler_q(n):
        ylo,yhi=log_bounds(n)
        ulo=(ylo.ln()-EPS); uhi=(yhi.ln()+EPS)
        eg_hi=(GAMMA+EPS).exp()+EPS
        H_hi=eg_hi*uhi+Decimal('2.50637')/uhi
        return DU_y(ylo)/H_hi

    def rad_divides(m, support_set):
        t=m; p=2
        while p*p<=t:
            if t%p==0:
                if p not in support_set: return False
                while t%p==0: t//=p
            p+=1
        return t==1 or t in support_set

    def verify_level(k, r, L, C, boundary_support, boundary_m):
        # k is the coefficient in phi(n)>k*pi(n); r is the only support size requiring enumeration.
        P_r=prod(PR[:r]); PHI_r=phi_sq(PR[:r]); P_prev=prod(PR[:r-1]); PHI_prev=phi_sq(PR[:r-1]); P_next=P_r*PR[r]
        phiL=boundary_m*phi_sq(boundary_support)
        assert prod(boundary_support)*boundary_m==L
        assert len(boundary_support)==r and len(set(boundary_support))==r
        # L fails both phi>k*pi and B>(k-1)A.
        lb=pi_lower(L)
        assert Decimal(phiL) <= Decimal(k)*(lb-Decimal(r))
        # Any later n with <=r-1 prime divisors succeeds.
        margin_prev=Decimal(PHI_prev)/Decimal(P_prev)*DU(L)-Decimal(k)
        assert margin_prev>0
        # Enumerate r-prime radicals in (L,C). Since d>=P_r, m<C/P_r is small.
        mmax=(C-1)//P_r
        qmax=(C-1)//P_prev
        primes=[p for p in PR if p<=qmax]
        checked=0; min_margin=None; min_n=None
        def rec(start, chosen, d, phid):
            nonlocal checked,min_margin,min_n
            need=r-len(chosen)
            if need==0:
                if not (P_r<=d<C): return
                ss=set(chosen)
                for m in range(1,mmax+1):
                    if not rad_divides(m,ss): continue
                    n=m*d
                    if not (L<n<C): continue
                    phin=m*phid
                    margin=Decimal(phin)-Decimal(k)*pi_upper(n)
                    assert margin>0,(k,n,margin,chosen,m)
                    checked+=1
                    if min_margin is None or margin<min_margin:
                        min_margin=margin; min_n=n
                return
            max_i=len(primes)-need
            for i in range(start,max_i+1):
                p=primes[i]; nd=d*p
                if need>1:
                    mc=1
                    for j in range(i+1,i+need): mc*=primes[j]
                    if nd*mc>=C: break
                elif nd>=C: break
                rec(i+1,chosen+[p],nd,phid*(p-1))
        rec(0,[],1,1)
        # Tail until next primorial.
        margin_tail=Decimal(PHI_r)/Decimal(P_r)*DU(C)-Decimal(k)
        assert margin_tail>0
        # Global analytic tail from P_{r+1}.
        q=rs_axler_q(P_next)
        assert q>Decimal(k)
        return {
            'k':k,'P_r':P_r,'P_next':P_next,'L':L,'phiL':phiL,'omegaL':r,
            'lower_pi_gap':lb-Decimal(phiL)/Decimal(k),
            'previous_stratum_margin':margin_prev,'checked':checked,
            'min_finite_margin':min_margin,'min_finite_n':min_n,
            'tail_margin':margin_tail,'global_q':q,'qmax':qmax,'mmax':mmax
        }

    P18=prod(PR[:18]); P20=prod(PR[:20])
    L7=2*P18*73//59
    support7=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,73]
    out7=verify_level(7,18,L7,4*P18,support7,2)

    L8=7*P20*73//71
    support8=list(PR[:19])+[73]
    out8=verify_level(8,20,L8,8*P20,support8,7)

    for out in (out7,out8):
        print('LEVEL',out['k'])
        for key in ['L','phiL','omegaL','lower_pi_gap','previous_stratum_margin','checked','min_finite_margin','min_finite_n','tail_margin','global_q','qmax','mmax']:
            print(key,'=',out[key])
    print('PASS')
