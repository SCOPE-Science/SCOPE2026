from collections import Counter

def pd(k):
    s='0'
    for _ in range(k):
        s=''.join('01' if ch=='0' else '00' for ch in s)
    return s

def circular_palindromes(s):
    n=len(s)
    double=s+s
    return {double[i:i+m] for m in range(1,n+1) for i in range(n) if double[i:i+m]==double[i:i+m][::-1]}

def phi(v):
    comp=v.translate(str.maketrans('01','10'))
    return '0'.join(comp)

def lifted(H):
    return {'00','101','01010'} | {f(v) for v in H if len(v)%2 for f in (phi, lambda x:'0'+phi(x)+'0')}

base={'0','1','00','000','010'}
for k in range(2,10):
    s=pd(k)
    direct=circular_palindromes(s)
    if k==2: predicted=base
    else: predicted=lifted(prev)
    assert direct==predicted,(k,len(direct),len(predicted),direct-predicted,predicted-direct)
    assert len(direct)==3*2**(k-1)-1,(k,len(direct))
    total=len(direct)
    even=[v for v in direct if len(v)%2==0]
    assert even==['00']
    assert Counter(map(len,direct)) == Counter(map(len,predicted))
    print('rank',k,'palindromes',total)
    prev=direct
