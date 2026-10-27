"""Direct integer checks for ternary quotients of consecutive four generators.
Only finite checks are performed; the unbounded proof is in RESULT.md.
"""

def data(x,r):
    q0=x-1 if x%3==1 else x
    A=(r*q0)//3
    B=x-1-A
    def q(t):
        return (3*(-t)+r-1)//r if t<0 else (3*t+(3-r)-1)//(3-r)
    W={t:q(t)*x+t for t in range(-A,B+1)}
    G=[x,2*x+1,3*x-1,3*x+2] if r==1 else [x,2*x-1,3*x-2,3*x+1]
    if r==1:
        predicted=({-A,B} if x%3==0 else {-A,B-1,B} if x%3==1 else {B})
    else:
        predicted=({-A,-A+1}|({B} if B>0 else set()) if x%3==0 else
                   {-A,-A+1,B} if x%3==1 else {-A,B})
    return W,G,predicted

def is_quotient(n,x,r):
    a=3*x-r
    return (3*n+a+2)//(a+3) <= (3*n)//a

def verify_apery_and_formulas(maxx=800):
    count=0
    for x in range(3,maxx+1):
        for r in [1,2]:
            W,G,predicted=data(x,r)
            assert len(W)==x and len({w%x for w in W.values()})==x
            assert min(W.values())==0
            pf_offsets={t for t,w in W.items() if all(w+g not in W.values() for g in G[1:])}
            assert pf_offsets==predicted,(x,r,pf_offsets,predicted)
            pf=sorted(W[t]-x for t in predicted)
            genus_num=(2*sum(W.values())-x*(x-1))//(2*x)
            expect_genus=x*(x-1)//2+(x+1)//3 if r==1 else x*(x-1)//2
            assert genus_num==expect_genus,(x,r,genus_num,expect_genus)
            expected_type= (2 if x%3==0 else 3 if x%3==1 else 1) if r==1 else (2 if x==3 or x%3==2 else 3)
            assert len(pf)==expected_type,(x,r,pf)
            F=max(pf)
            if r==1:
                expected_F=x*x-(4*x)//3 if x%3==0 else (x-2)*x+2*(x-1)//3 if x%3==1 else x*x-x+2*x//3
            else:
                expected_F=x*x-x-2*x//3 if x%3==0 else (x-2)*x+(x-1)//3 if x%3==1 else x*x-x-(2*x)//3
            assert F==expected_F,(x,r,F,expected_F)
            count+=1
    print(f'APERY/PF/GENUS/FROBENIUS: PASS: {count} parameter pairs, x=3..{maxx}')

def verify_direct(maxx=90):
    count=0
    for x in range(3,maxx+1):
        for r in [1,2]:
            W,G,predicted=data(x,r)
            F=max(W.values())-x
            for t,w in W.items():
                assert is_quotient(w,x,r),('not-member',x,r,t,w)
                if w>=x:assert not is_quotient(w-x,x,r),('non-minimal',x,r,t,w)
            for n in range(F+1):
                predicted_member=n>=W[next(t for t,w in W.items() if w%x==n%x)]
                assert is_quotient(n,x,r)==predicted_member,('membership',x,r,n)
            gaps=[n for n in range(F+1) if not is_quotient(n,x,r)]
            actual_pf=[n for n in gaps if all(is_quotient(n+g,x,r) for g in G)]
            assert actual_pf==sorted(W[t]-x for t in predicted),(x,r,actual_pf)
            count+=1
    print(f'DIRECT MEMBERSHIP AND GAP TESTS: PASS: {count} parameter pairs, x=3..{maxx}')

if __name__=='__main__':
    verify_apery_and_formulas()
    verify_direct()
