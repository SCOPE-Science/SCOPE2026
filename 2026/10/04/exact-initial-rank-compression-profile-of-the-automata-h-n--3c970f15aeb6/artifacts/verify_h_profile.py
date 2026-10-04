from collections import deque

def trans(n):
    a=[]; b=[]
    for i in range(1,n+1):
        a.append(n if i==1 else 1 if i==n else i)
        b.append(i+1 if i<n-1 else 1 if i==n-1 else 3)
    return {'a':a,'b':b}

def image(mask, arr):
    out=0; i=0
    while mask:
        if mask&1: out |= 1 << (arr[i]-1)
        mask >>= 1; i += 1
    return out

def bfs(n):
    T=trans(n); full=(1<<n)-1
    q=deque([full]); d={full:0}; count={full:1}; word={full:''}
    while q:
        m=q.popleft()
        for ch in 'ab':
            u=image(m,T[ch])
            if u not in d:
                d[u]=d[m]+1; count[u]=count[m]; word[u]=word[m]+ch; q.append(u)
            elif d[u]==d[m]+1:
                count[u]+=count[m]
    h=n//2+1
    for s in range(1,h+1):
        target=n-s
        md=min(v for m,v in d.items() if m.bit_count()<=target)
        states=[m for m,v in d.items() if v==md and m.bit_count()<=target]
        c=sum(count[m] for m in states)
        expected=1 if s==1 else 3*s-3
        ew='b' if s==1 else 'bab'*(s-1)
        if md!=expected or c!=1 or len(states)!=1 or word[states[0]]!=ew:
            raise AssertionError((n,s,md,c,word[states[0]],expected,ew))
    if h+1 <= n-1:
        target=n-(h+1)
        md=min(v for m,v in d.items() if m.bit_count()<=target)
        if not (md>3*h): raise AssertionError(('boundary',n,h,md))
    return max(d.values())

def apply_word(n,w):
    T=trans(n); S=set(range(1,n+1))
    for ch in w:
        S={T[ch][i-1] for i in S}
    return S

for n in range(4,15):
    bfs(n)
for n in range(4,301):
    h=n//2+1
    T=trans(n)
    S=set(range(1,n+1))
    S={T['b'][i-1] for i in S}
    if len(S)!=n-1: raise AssertionError(('replay',n,1,len(S),n-1))
    for s in range(2,h+1):
        for ch in 'ab':
            S={T[ch][i-1] for i in S}
        S={T['b'][i-1] for i in S}
        if len(S)!=n-s: raise AssertionError(('replay',n,s,len(S),n-s))
    if h+1 <= n-1:
        for ch in 'ab':
            S={T[ch][i-1] for i in S}
        S={T['b'][i-1] for i in S}
        if len(S) != n-h: raise AssertionError(('boundary-replay',n,len(S),n-h))
print('VERIFY_OK')
