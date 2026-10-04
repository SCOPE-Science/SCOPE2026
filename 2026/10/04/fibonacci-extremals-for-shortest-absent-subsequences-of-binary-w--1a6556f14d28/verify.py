from itertools import product

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def iota_binary(s):
    if len(set(s))<2:
        return len(s)  # relative to alph(s), unary special case
    seen=set(); k=0
    for ch in s:
        seen.add(ch)
        if len(seen)==2:
            k+=1; seen.clear()
    return k

def distinct_subseq_count_len(s,L):
    # DP: dp[l] number of distinct subsequences of length l;
    # last[ch][l] contribution last added when reading ch.
    dp=[0]*(L+1); dp[0]=1
    last={'0':[0]*(L+1),'1':[0]*(L+1)}
    for ch in s:
        old=dp[:]
        for l in range(1,L+1):
            add=old[l-1]
            dp[l]=old[l]+add-last[ch][l]
            last[ch][l]=add
    return dp[L]

def sas_count(s):
    alph=set(s)
    if len(alph)==1:
        return 1
    k=iota_binary(s)
    L=k+1
    return 2**L-distinct_subseq_count_len(s,L)

def formula(n):
    if n==1: return 1
    if n%2==0:
        m=n//2; return fib(m+3)
    m=(n-1)//2; return 2*fib(m+1)

def exhaustive(N=14):
    rows=[]
    for n in range(1,N+1):
        best=-1; words=[]
        for bits in product('01', repeat=n):
            s=''.join(bits); c=sas_count(s)
            if c>best: best=c; words=[s]
            elif c==best: words.append(s)
        assert best==formula(n),(n,best,formula(n))
        rows.append((n,best,len(words),words[:8]))
    return rows

def matrices():
    # row-vector action for H(01), H(10)
    def A(x,y): return x+y,y
    def B(x,y): return x,x+y
    for k in range(0,13):
        states={(1,1)}
        for _ in range(k):
            states={A(*v) for v in states}|{B(*v) for v in states}
        mx=max(x+y for x,y in states)
        assert mx==fib(k+3),(k,mx,fib(k+3))
    # Interior exceptional-block Fibonacci product inequality.
    for m in range(2,60):
        for j in range(1,m):
            assert fib(j+1)*fib(m-j+3) <= 2*fib(m+1)

def witnesses(N=31):
    for n in range(2,N+1):
        if n%2==0:
            m=n//2
            blocks=['01' if i%2==1 else '10' for i in range(1,m+1)]
            s=''.join(blocks)
        else:
            m=(n-1)//2
            blocks=['01' if i%2==1 else '10' for i in range(1,m)]
            last='001' if m%2==1 else '110'
            s=''.join(blocks)+last
        assert len(s)==n
        assert sas_count(s)==formula(n),(n,s,sas_count(s),formula(n))

if __name__=='__main__':
    matrices(); witnesses(); rows=exhaustive()
    for row in rows: print(*row)
    print('VERIFY_OK')
