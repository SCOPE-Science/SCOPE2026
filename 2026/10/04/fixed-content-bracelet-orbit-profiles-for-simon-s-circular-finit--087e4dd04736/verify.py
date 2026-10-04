from math import factorial, gcd
from itertools import permutations


def phi(n):
    r=n
    p=2
    x=n
    while p*p<=x:
        if x%p==0:
            while x%p==0:
                x//=p
            r-=r//p
        p+=1
    if x>1:
        r-=r//x
    return r


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def orbit_formula(d,k):
    N=d*k
    S=sum(phi(ell)*factorial(N//ell)//(factorial(d//ell)**k) for ell in divisors(d))
    if d%2==0:
        R=N*factorial(N//2)//(factorial(d//2)**k)
    elif k==1:
        R=d
    elif k==2:
        R=2*d*factorial(d-1)//(factorial((d-1)//2)**2)
    else:
        R=0
    num=S+R
    assert num%(2*N)==0
    return num//(2*N)


def canonical(word):
    word=tuple(word)
    n=len(word)
    rev=word[::-1]
    reps=[]
    for s in range(n):
        reps.append(word[s:]+word[:s])
        reps.append(rev[s:]+rev[:s])
    return min(reps)


def multiset_words(d,k):
    N=d*k
    counts=[d]*k
    w=[None]*N
    out=[]
    def rec(i):
        if i==N:
            out.append(tuple(w)); return
        for c in range(k):
            if counts[c]:
                counts[c]-=1; w[i]=c; rec(i+1); counts[c]+=1
    rec(0)
    return out


def brute(d,k):
    return len({canonical(w) for w in multiset_words(d,k)})

for d in range(1,5):
    for k in range(1,5):
        if d*k<=10:
            f=orbit_formula(d,k)
            b=brute(d,k)
            assert f==b,(d,k,f,b)

expected={
1:[1,1,1,3,12,60,360],
2:[1,2,11,171,5736,312240,24327000],
3:[1,3,94,15402,5605608,3811808040,4345461120240],
}
for d,row in expected.items():
    assert [orbit_formula(d,k) for k in range(1,8)]==row

for k in range(3,12):
    assert orbit_formula(1,k)==factorial(k-1)//2
assert orbit_formula(1,1)==orbit_formula(1,2)==1
print('VERIFY_OK')
