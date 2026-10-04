from collections import deque

WITNESSES = {
    7: (0,1,2,3),
    8: (0,1,2,8),
    9: (0,1,7,10),
    10:(0,1,9,12),
    11:(0,1,13,10),
    12:(0,6,14,16),
    13:(0,8,16,18),
    14:(0,12,14,20),
    15:(0,14,16,22),
}

def graph(n):
    k=5
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(N):
        j=(i+1)%N
        adj[i].add(j); adj[j].add(i)
    for i in range(n):
        a=2*i; b=(2*i+k)%N
        adj[a].add(b); adj[b].add(a)
    assert all(len(a)==3 for a in adj)
    return [tuple(sorted(a)) for a in adj]

def distances(adj):
    N=len(adj); out=[]
    for s in range(N):
        d=[-1]*N; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0:
                    d[v]=d[u]+1; q.append(v)
        assert min(d)>=0
        out.append(d)
    return out

def balls(D,r):
    N=len(D)
    return [sum(1<<v for v in range(N) if D[c][v]<=r) for c in range(N)]

def valid_burning_sequence(D, seq):
    b=len(seq); N=len(D); allmask=(1<<N)-1; cover=0
    for i,c in enumerate(seq):
        r=b-1-i
        cover |= sum(1<<v for v in range(N) if D[c][v]<=r)
        for j in range(i):
            # source i+1 must still be unburned from source j+1
            assert D[seq[j]][c] >= i-j
    return cover==allmask

def max_uncovered_after_prefix(n, radii):
    adj=graph(n); D=distances(adj); N=2*n; allmask=(1<<N)-1
    Bs=[balls(D,r) for r in radii]
    best=N; arg=None
    if len(radii)==2:
        for a in range(N):
            A=Bs[0][a]
            for b in range(N):
                missing=(allmask ^ ((A|Bs[1][b]) & allmask)).bit_count()
                if missing<best: best=missing; arg=(a,b)
    elif len(radii)==3:
        for a in range(N):
            A=Bs[0][a]
            for b in range(N):
                AB=A|Bs[1][b]
                for c in range(N):
                    missing=(allmask ^ ((AB|Bs[2][c]) & allmask)).bit_count()
                    if missing<best: best=missing; arg=(a,b,c)
    else:
        raise ValueError
    return best,arg

def main():
    # Positive side and validity of the displayed sequences.
    for n,seq in WITNESSES.items():
        adj=graph(n); D=distances(adj)
        assert valid_burning_sequence(D,seq), (n,seq)

    # n=7 is not 3-burnable. Even ignoring source-validity constraints,
    # balls of radii 2 and 1 always leave at least two vertices, so one
    # final radius-0 source cannot finish.
    miss,arg=max_uncovered_after_prefix(7,(2,1))
    assert miss>=2, (miss,arg)

    # n=16,17,18 are not 4-burnable. Again we prove the stronger covering
    # obstruction: any three balls of radii 3,2,1 leave at least two vertices.
    obstructions={}
    for n in (16,17,18):
        miss,arg=max_uncovered_after_prefix(n,(3,2,1))
        assert miss>=2, (n,miss,arg)
        obstructions[n]=(miss,arg)

    # For n>=19, maximum degree 3 gives |B_r| <= 1+3(1+2+...+2^(r-1)).
    ball_caps={0:1,1:4,2:10,3:22}
    assert sum(ball_caps[r] for r in (3,2,1,0))==37
    assert 2*19==38

    # For n>=8, the analogous 3-round cap is 10+4+1=15 < 2n.
    assert ball_caps[2]+ball_caps[1]+ball_caps[0]==15
    assert 2*8==16

    print('witnesses', WITNESSES)
    print('n7_min_uncovered_after_r2_r1', miss if False else max_uncovered_after_prefix(7,(2,1)))
    print('n16_18_min_uncovered_after_r3_r2_r1', obstructions)
    print('four_round_degree3_capacity',37)
    print('three_round_degree3_capacity',15)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
