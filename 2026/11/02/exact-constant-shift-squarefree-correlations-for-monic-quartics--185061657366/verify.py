"""Exact finite-field test of simultaneous squarefreeness for shifted monic quartics.
No external dependencies. The gcd test does not use the proof's repeated-root count.
"""
from itertools import product

FIELD_SPECS = [
    (2, (0, 1)),
    (3, (0, 1)),
    (2, (1, 1, 1)),
    (5, (0, 1)),
    (7, (0, 1)),
    (2, (1, 1, 0, 1)),
    (3, (1, 0, 1)),
    (11, (0, 1)),
    (13, (0, 1)),
    (2, (1, 1, 0, 0, 1)),
    (17, (0, 1)),
    (5, (2, 0, 1)),
]


def field(p, mod):
    m = len(mod)-1
    q = p**m
    digits=[]
    for x in range(q):
        a=[]; v=x
        for _ in range(m): a.append(v%p);v//=p
        digits.append(a)
    def encode(a):return sum((v%p)*p**i for i,v in enumerate(a))
    add=[[encode([digits[x][i]+digits[y][i] for i in range(m)]) for y in range(q)] for x in range(q)]
    neg=[encode([-z for z in digits[x]]) for x in range(q)]
    mul=[]
    for x in range(q):
        row=[]
        for y in range(q):
            d=[0]*(2*m-1)
            for i,a in enumerate(digits[x]):
                for j,b in enumerate(digits[y]):d[i+j]=(d[i+j]+a*b)%p
            for k in range(2*m-2,m-1,-1):
                coeff=d[k]
                if coeff:
                    for j in range(m):d[k-m+j]=(d[k-m+j]-coeff*mod[j])%p
            row.append(encode(d[:m]))
        mul.append(row)
    inv=[None]*q
    for a in range(1,q):
        for b in range(1,q):
            if mul[a][b]==1:inv[a]=b;break
        if inv[a] is None: raise AssertionError('not a field')
    return q,add,neg,mul,inv


def is_bad(coef, add,neg,mul,inv, ints):
    f=coef
    der=[mul[ints[j]][f[j]] for j in range(1,len(f))]
    while der and der[-1]==0:der.pop()
    if not der:return True
    a=list(f);b=der
    while b:
        lead=inv[b[-1]]
        while len(a)>=len(b):
            k=mul[a[-1]][lead];shift=len(a)-len(b)
            for j in range(len(b)):
                a[shift+j]=add[a[shift+j]][neg[mul[k][b[j]]]]
            while a and a[-1]==0:a.pop()
        a,b=b,a
    return len(a)>1


def expected(q,c,mul):
    if q%2==0:return q*q
    if q%8!=1:return q*(q-1)
    squares={mul[x][x] for x in range(1,q)}
    fourth={mul[x][mul[x][mul[x][x]]] for x in range(1,q)}
    if c in fourth:return q*(q-5)
    if c in squares:return q*(q+3)
    return q*(q-1)


def main():
    cases=0;polytests=0;fieldorders=[]
    for p,mod in FIELD_SPECS:
        q,add,neg,mul,inv=field(p,mod)
        fieldorders.append(q)
        intrep=[n%p for n in range(5)]
        # Exhaust all nonzero shifts through q=17, and inspect a complete
        # representative set of multiplicative classes for q=25.
        cs=list(range(1,q)) if q<=17 else [1,2,3,4]
        observed={c:0 for c in cs}
        for a,b,d,e in product(range(q),repeat=4):
            f=[e,d,b,a,1]
            polytests+=1
            if not is_bad(f,add,neg,mul,inv,intrep):continue
            for c in cs:
                shifted=[add[e][c],d,b,a,1]
                if is_bad(shifted,add,neg,mul,inv,intrep): observed[c]+=1
        for c in cs:
            v=expected(q,c,mul)
            assert observed[c]==v,(q,c,observed[c],v)
            cases+=1
        print('FIELD_OK',q,'shifts',len(cs),'both-nonsquarefree-range',min(observed.values()),max(observed.values()),flush=True)
    print('VERIFY_OK','fields',len(fieldorders),'shift_cases',cases,'quartics',polytests,flush=True)

if __name__=='__main__':main()
