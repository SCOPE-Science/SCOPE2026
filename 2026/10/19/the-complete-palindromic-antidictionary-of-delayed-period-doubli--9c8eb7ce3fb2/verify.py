"""Independent finite checks for the q-uniform delayed period-doubling antidictionary."""
from collections import defaultdict

def substitution_prefix(q, threshold):
    w='0'
    while len(w)<threshold:
        w=''.join('0'*(q-1)+('1' if c=='0' else '0') for c in w)
    return w[:threshold]

def arithmetic_word(q, N):
    out=[]
    for i in range(N):
        x=i; t=0
        while x%q==q-1:
            t+=1
            x//=q
        out.append('1' if t%2 else '0')
    return ''.join(out)

def T(q,u):
    return ''.join('0'*(q-1)+('1' if c=='0' else '0') for c in u)+'0'*(q-1)

def proposed(q, nmax):
    r={'11'}
    for j in range(1,2*q-1):
        u='0'*j
        for t in range(10):
            if len(u)+2>nmax:break
            if j!=q-1:
                b=('1' if (t%2==0) else '0')
                r.add(b+u+b)
                if j==2*q-2:
                    r.add(('0' if b=='1' else '1')+u+('0' if b=='1' else '1'))
            u=T(q,u)
    return r

def check(q,N=25000,nmax=75):
    s=substitution_prefix(q,N)
    a=arithmetic_word(q,N)
    assert a==s,(q,'generator disagreement')
    observed=set()
    prev={''}
    for n in range(1,nmax+1):
        f={s[i:i+n] for i in range(N-n+1)}
        for x in prev:
            for b in '01':
                w=x+b
                if w not in f and (n==1 or (w[1:] in prev and w[:-1] in prev)):
                    observed.add(w)
        prev=f
    assert observed==proposed(q,nmax), (q,'unexpected',sorted(observed-proposed(q,nmax),key=lambda u:(len(u),u))[:10],'missing',sorted(proposed(q,nmax)-observed,key=lambda u:(len(u),u))[:10])
    print(f'q={q}: generators agree N={N}, exact MAW collection through n={nmax}: {len(observed)}')
for q in range(2,10):check(q)
print('VERIFY_OK q=2..9 independent_generators_N25000 full_absent_factor_enumeration_lengths_1..75')
