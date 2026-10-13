from math import gcd, lcm
from itertools import combinations

LETTERS = ('l','r','p','q','L','R','P','Q')
PI = {'l':'BACD','r':'ABDC','p':'BADC','q':'ABCD','L':'DCAB','R':'CDBA','P':'CDAB','Q':'DCBA'}
CHI = {'l':'AC','r':'BD','p':'AD','q':'BC','L':'CA','R':'DB','P':'DA','Q':'CB'}
PARAMS = {'A':(0,40),'B':(18,28),'C':(4,42),'D':(5,15)}
NEXT = {a:tuple(b for b in LETTERS if PI[a][-2:]==PI[b][:2]) for a in LETTERS}

def ct(x,r1,m1,r2,m2):
    if (x-r1)%m1==0:
        k=(x-r1)//m1
        return r2+m2*k
    if (x-r2)%m2==0:
        k=(x-r2)//m2
        return r1+m1*k
    return x

def a(x): return ct(x,0,40,18,28)
def b(x): return ct(x,4,42,5,15)
def T(x): return a(b(x))

def has_exact_period(x,n):
    y=x
    for d in range(1,n+1):
        y=T(y)
        if y==x:
            return d==n
    return False

def words(n):
    out=[]
    def rec(pref):
        if len(pref)==n:
            out.append(''.join(pref)); return
        if not pref:
            for z in LETTERS: rec([z])
        else:
            for z in NEXT[pref[-1]]: rec(pref+[z])
    rec([])
    return out

def chain_status(w):
    # After processing a prefix, every integer solution is represented as
    # u_j=A_j*k+B_j for one arbitrary integer parameter k.
    pairs=[(1,0)]
    for letter in w:
        X,Y=CHI[letter]
        rX,mX=PARAMS[X]; rY,mY=PARAMS[Y]
        c=rY-rX
        A,B=pairs[-1]
        aa=mX*A
        dd=c-mX*B
        g=gcd(aa,mY)
        if dd%g:
            return False,False
        mod=mY//g
        if mod==1:
            k0=0
        else:
            k0=(pow((aa//g)%mod,-1,mod)*((dd//g)%mod))%mod
        pairs=[(Aj*mod,Aj*k0+Bj) for Aj,Bj in pairs]
        Acur,Bcur=pairs[-1]
        numA=mX*Acur
        numB=mX*Bcur-c
        assert numA%mY==0 and numB%mY==0
        pairs.append((numA//mY,numB//mY))
    # Exactness asks u_i != u_j for equal-parity indices. If two such
    # affine functions are identical, exactness is impossible; otherwise
    # only finitely many k are excluded, so some exact integer solution exists.
    for i in range(len(pairs)):
        for j in range(i+1,len(pairs)):
            if (i-j)%2==0 and pairs[i]==pairs[j]:
                return True,False
    return True,True

assert gcd(40,28)==4 and 18%4!=0
assert gcd(42,15)==3 and (5-4)%3!=0
profile=[]
for n in range(1,8):
    ws=words(n)
    integer=sum(chain_status(w)[0] for w in ws)
    exact=sum(chain_status(w)[1] for w in ws)
    profile.append((n,len(ws),integer,exact))
assert profile == [(1,8,8,8),(2,16,8,8),(3,32,8,8),(4,64,6,6),(5,128,4,4),(6,256,2,2),(7,512,0,0)]
assert [w for w in words(6) if chain_status(w)[0]] == ['LqRpQl','LqPrQl']

cycles={
3:(20,40,46),
5:(158,200,760,275,550),
7:(410,1600,575,1138,560,2200,1558),
8:(2510,10000,3575,7018,3560,14200,5075,9958),
}
for n,C in cycles.items():
    assert len(C)==n and len(set(C))==n
    for i,x in enumerate(C): assert T(x)==C[(i+1)%n]
    assert has_exact_period(C[0],n)
    for x in range(C[0]): assert not has_exact_period(x,n)
assert lcm(*cycles)==840
best=None
for k in range(1,9):
    for S in combinations(range(1,9),k):
        if lcm(*S)==840: best=S; break
    if best is not None: break
assert len(best)==4 and best==(3,5,7,8)
print('interpretability_profile(n,total,integer,exact):', profile)
print('interpretable_length_6_words:', ['LqRpQl','LqPrQl'])
print('cycles:', cycles)
print('least_nonnegative_points:', {n:C[0] for n,C in cycles.items()})
print('cycle_lcm:', lcm(*cycles))
print('minimal_length_set_size:', len(best), 'example:', best)
print('VERIFY_OK')
