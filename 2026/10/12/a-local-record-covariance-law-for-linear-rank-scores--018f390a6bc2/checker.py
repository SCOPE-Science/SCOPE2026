from fractions import Fraction
from itertools import permutations
from math import comb

def H(n, p=1):
    return sum((Fraction(1, j**p) for j in range(1, n+1)), Fraction(0))

def records(p):
    m = -1
    out=[]
    for x in p:
        out.append(int(x>m))
        m=max(m,x)
    return out

def run():
    perms=0
    local_checks=0
    global_checks=0
    weight_checks=0
    for n in range(2,10):
        rows=[]
        for p in permutations(range(1,n+1)):
            U=records(p)
            Q=sum(U)
            D=sum((p[j]-(j+1))**2 for j in range(n))
            R=Fraction(1)-Fraction(6*D,n*(n*n-1))
            rows.append((p,U,Q,D,R))
        N=len(rows); perms+=N
        ER=sum((R for *_,R in rows),Fraction(0))/N
        assert ER==0
        EQ=sum((Fraction(Q) for _,_,Q,_,_ in rows),Fraction(0))/N
        ED=sum((Fraction(D) for _,_,_,D,_ in rows),Fraction(0))/N
        for i in range(1,n+1):
            EU=sum((Fraction(U[i-1]) for _,U,_,_,_ in rows),Fraction(0))/N
            assert EU==Fraction(1,i); local_checks+=1
            EUD=sum((Fraction(U[i-1]*D) for _,U,_,D,_ in rows),Fraction(0))/N
            covD=EUD-EU*ED
            assert covD==-Fraction((n+1)*(i-1),2*(i+1)); local_checks+=1
            EUR=sum((Fraction(U[i-1])*R for _,U,_,_,R in rows),Fraction(0))/N
            covR=EUR-EU*ER
            assert covR==Fraction(3*(i-1),n*(n-1)*(i+1)); local_checks+=1
            rr=[R for _,U,_,_,R in rows if U[i-1]]
            assert sum(rr,Fraction(0))/len(rr)==Fraction(3*i*(i-1),n*(n-1)*(i+1)); local_checks+=1
            if i>1:
                nr=[R for _,U,_,_,R in rows if not U[i-1]]
                assert sum(nr,Fraction(0))/len(nr)==-Fraction(3*i,n*(n-1)*(i+1)); local_checks+=1
        EQR=sum((Fraction(Q)*R for _,_,Q,_,R in rows),Fraction(0))/N
        covQR=EQR-EQ*ER
        target=Fraction(3,n*(n-1))*(n+2-2*H(n+1))
        assert covQR==target; global_checks+=1
        EQ2=sum((Fraction(Q*Q) for _,_,Q,_,_ in rows),Fraction(0))/N
        varQ=EQ2-EQ*EQ
        assert varQ==H(n)-H(n,2); global_checks+=1
        ER2=sum((R*R for *_,R in rows),Fraction(0))/N
        varR=ER2-ER*ER
        assert varR==Fraction(1,n-1); global_checks+=1
        assert covQR*covQR/(varQ*varR)==target*target/(varQ*Fraction(1,n-1)); global_checks+=1

        if n<=8:
            weights=[
                [j for j in range(1,n+1)],
                [j*j-3*j+2 for j in range(1,n+1)],
                [(-1)**j*(j+1) for j in range(1,n+1)],
                [2*j+1 for j in range(1,n+1)],
            ]
            for w in weights:
                EL=sum((Fraction(sum(w[j]*p[j] for j in range(n))) for p,*_ in rows),Fraction(0))/N
                for i in range(1,n+1):
                    EUL=sum((Fraction(U[i-1]*sum(w[j]*p[j] for j in range(n))) for p,U,*_ in rows),Fraction(0))/N
                    cov=EUL-Fraction(1,i)*EL
                    rhs=Fraction(n+1,2*i*(i+1))*((i-1)*w[i-1]-sum(w[:i-1]))
                    assert cov==rhs
                    weight_checks+=1

    subset_checks=0
    for n in range(2,101):
        for i in range(1,n+1):
            den=comb(n,i)
            emax=sum(Fraction(m*comb(m-1,i-1),den) for m in range(i,n+1))
            assert emax==Fraction(i*(n+1),i+1); subset_checks+=1
            if i>1:
                esum=Fraction(i*(n+1),2)
                eearly=(esum-emax)/(i-1)
                assert eearly==Fraction(i*(n+1),2*(i+1)); subset_checks+=1
    print('VERIFY_OK')
    print(f'permutations_checked={perms}')
    print(f'local_formula_checks={local_checks}')
    print(f'global_formula_checks={global_checks}')
    print(f'general_weight_checks={weight_checks}')
    print(f'subset_moment_checks={subset_checks}')

if __name__=='__main__':
    run()
