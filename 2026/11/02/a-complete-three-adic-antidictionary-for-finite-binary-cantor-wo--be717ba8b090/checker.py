from collections import defaultdict

def cantor(k):
    w='1'
    for _ in range(k):w=''.join('101' if b=='1' else '000' for b in w)
    return w

def candidate(k):
    G=3**(k-1)
    W={'11','0'*(G+1),'0'+cantor(k-1)+'0'}
    W.update('1'+'0'*t+'1' for t in range(1,G) if t not in {3**i for i in range(k-1)})
    for j in range(1,k):
        H=3**(j-1); V=cantor(j-1)
        W.add('0'*(H+1)+V+'0'*(H+1))
        W.add('1'+'0'*H+V+'0'*H+'1')
    return W

def brute(k):
    s=cantor(k);N=len(s)
    F={''}
    for i in range(N):
        for j in range(i+1,N+1):F.add(s[i:j])
    M=set()
    for core in F:
        for a in '01':
            if a+core not in F:continue
            for b in '01':
                w=a+core+b
                if core+b in F and w not in F:M.add(w)
    return M,F

def main():
    for k in range(1,7):
        M,F=brute(k)
        C=candidate(k)
        assert M==C, (k,sorted(M-C),sorted(C-M))
        assert len(M)==3**(k-1)+k+1,(k,len(M))
        print(f'k={k}, length={len(cantor(k))}, factor_count={len(F)-1}, minimal_absent={len(M)}, PASS')
if __name__=='__main__':main()
