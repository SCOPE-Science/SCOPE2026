"""Standalone verification of a five-run closed-factor classification.

Python 3 standard library only. Finite tests supplement the symbolic proof.
"""
from itertools import product


def closed(t):
    if len(t) == 1:
        return True
    for k in range(1, len(t)):
        p = t[:k]
        if p == t[-k:]:
            occ = sum(t[j:j+k] == p for j in range(len(t)-k+1))
            if occ == 2:
                return True
    return False


def observed(a,b,c,d,e):
    w = '0'*a + '1'*b + '0'*c + '1'*d + '0'*e
    return {f for i in range(len(w)) for j in range(i+1,len(w)+1)
            if closed(f := w[i:j])}


def classified(a,b,c,d,e):
    ans = { '0'*i for i in range(1,max(a,c,e)+1)}
    ans.update('1'*i for i in range(1,max(b,d)+1))
    for r,L,R in ((b,a,c),(d,c,e)):
        ans.update('0'*i+'1'*r+'0'*i for i in range(1,min(L,R)+1))
    ans.update('1'*i+'0'*c+'1'*i for i in range(1,min(b,d)+1))
    for i in range(1,min(a,c)+1):
        for j in range(1,min(b,d)+1):
            ans.add('0'*i+'1'*b+'0'*c+'1'*j)
    for i in range(1,min(b,d)+1):
        for j in range(1,min(c,e)+1):
            ans.add('1'*i+'0'*c+'1'*d+'0'*j)
    if b==d:
        for i in range(1,min(a,c)+1):
            for j in range(1,min(e,c)+1):
                ans.add('0'*i+'1'*b+'0'*c+'1'*d+'0'*j)
    for i in range(c+1,min(a,e)+1):
        ans.add('0'*i+'1'*b+'0'*c+'1'*d+'0'*i)
    return ans


def formula(a,b,c,d,e):
    I = int(b==d)
    x,y,t = min(a,c),min(c,e),min(b,d)
    return (max(a,c,e)+max(b,d)+x+y-I*min(a,c,e)+t
            +t*(x+y)+I*x*y+max(0,min(a,e)-c))


def main():
    count = 0
    for p in product(range(1,6), repeat=5):
        got = observed(*p)
        cls = classified(*p)
        assert got == cls, ('set mismatch',p,sorted(got-cls), sorted(cls-got))
        assert len(cls)==formula(*p), ('count mismatch',p,len(cls),formula(*p))
        a,b,c,d,e=p
        x,y,t=min(a,c),min(c,e),min(b,d)
        u=x+y; n=sum(p)
        if b==d:
            Q=t*u+x*y
            assert n*n-8*Q == ((2*u-n)**2+2*(x-y)**2
                                  +(4*n-6*u-8*t)*u), ('defect identity',p)
            assert Q*8 <= n*n, ('upper bound',p)
        else:
            Q=t*u
            assert Q*12 <= n*n, ('unequal run bound',p)
        count += 1
    for k in range(1,501):
        p=(2*k,k,2*k,k,2*k)
        n=sum(p)
        assert formula(*p) == n*n//8+3*n//4
    # Exploratory exact maxima, independent closed-set computation on small hosts.
    maxima=[]
    for n in range(5,15):
        best=-1
        for a in range(1,n-3):
            for b in range(1,n-a-2):
                for c in range(1,n-a-b-1):
                    for d in range(1,n-a-b-c):
                        e=n-a-b-c-d
                        best=max(best,formula(a,b,c,d,e))
        maxima.append(best)
    print('VERIFY_OK', 'parameter_tuples=',count,
          'scaled_witnesses=',500, 'M5_n5_to_n14=',maxima)

if __name__ == '__main__':main()
