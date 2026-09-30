from itertools import combinations, permutations

def hdist(a,b): return (a^b).bit_count()

def path_internal_masks(n,a,b):
    diff=[i for i in range(n) if (a^b)>>i & 1]
    if len(diff)<=1: return [0]
    out=[]
    for perm in permutations(diff):
        x=a; m=0
        for i in perm[:-1]:
            x ^= 1<<i; m |= 1<<x
        out.append(m)
    return tuple(set(out))

def is_dmv_vertices(n,k,verts):
    Sbits=0
    for v in verts: Sbits |= 1<<v
    for a,b in combinations(verts,2):
        d=hdist(a,b)
        if d>k: return False
        if not any((pm&Sbits)==0 for pm in path_internal_masks(n,a,b)):
            return False
    return True

def exact_mu(n,k):
    V=list(range(1<<n)); pairs={}
    for a,b in combinations(V,2):
        d=hdist(a,b)
        pairs[(a,b)]=None if d>k else path_internal_masks(n,a,b)
    best=0; witness=None
    for S in range(1<<(1<<n)):
        s=S.bit_count()
        if s<=best: continue
        verts=[v for v in V if (S>>v)&1]
        ok=True
        for a,b in combinations(verts,2):
            ps=pairs[(a,b)]
            if ps is None or not any((pm&S)==0 for pm in ps):
                ok=False; break
        if ok: best=s; witness=verts
    return best,witness

def ball1(n): return [0]+[1<<i for i in range(n)]
def std_S3(n): return [1<<i for i in range(n)] + [1|(1<<i) for i in range(1,n)]
def parity_Q4(): return [v for v in range(16) if sum((v>>i)&1 for i in range(3))%2==0]

def main():
    expected={(2,2):3,(2,3):3,(3,2):4,(3,3):5,(4,2):5,(4,3):8}
    for nk,want in expected.items():
        got,wit=exact_mu(*nk)
        assert got==want,(nk,got,want)
        print(f'exact Q_{nk[0]} mu_{nk[1]}={got}; witness={wit}')
    for n in range(2,13):
        B=ball1(n); assert len(B)==n+1 and is_dmv_vertices(n,2,B)
    print('k=2 Hamming-ball constructions checked for n=2..12')
    P=parity_Q4(); assert len(P)==8 and is_dmv_vertices(4,3,P)
    print('Q_4 parity construction checked')
    for n in range(5,13):
        S=std_S3(n); assert len(S)==2*n-1 and is_dmv_vertices(n,3,S)
    print('k=3 size-(2n-1) constructions checked for n=5..12')
    for n in range(5,13):
        y=0; i=1
        K=[0,1<<y,1<<i,(1<<y)|(1<<i)]
        Sbits=sum(1<<v for v in K)
        assert all(pm&Sbits for pm in path_internal_masks(n,0,(1<<y)|(1<<i)))
    print('Frankl-extremal obstruction checked for n=5..12')
    print('VERIFY_OK')
if __name__=='__main__': main()
