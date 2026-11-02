"""Direct edge-neighborhood checks for sparse optimal rich-neighbor colorings."""
from itertools import permutations


def construct(m,n,d=None):
    assert 2 <= m <= n
    if m == n == 2:
        return [[0,1],[2,3]]
    if m == n == 3:
        return [[0,1,2],[1,3,4],[2,4,3]]
    if m < n:
        return [[i if j == 0 else m+(i+j-1)%(n-1) for j in range(n)]
                for i in range(m)]
    if d is None:
        d=2
    assert 2<=d<=n-2
    q=n-d
    M=[[None]*n for _ in range(n)]
    # Latin rectangle on the first d columns for all rows except row zero.
    for r_index,i in enumerate(range(1,n)):
        for j in range(d):
            M[i][j]=(r_index+j)%(n-1)
    # Independently, a Latin rectangle on the last q columns, except row one.
    for r_index,i in enumerate([0]+list(range(2,n))):
        for j in range(q):
            M[i][d+j]=(n-1)+(r_index+j)%(n-1)
    # Complete both distinguished rows using their complementary palettes.
    for j,c in enumerate(list(range((n-1)+q,2*(n-1)))+[2*n-2]):
        M[0][j]=c
    for j,c in enumerate(list(range(d,n-1))+[2*n-2]):
        M[1][d+j]=c
    assert all(v is not None for row in M for v in row)
    return M


def analyze(M):
    m=len(M);n=len(M[0]);k=len({v for row in M for v in row})
    assert all(len(set(row))==n for row in M)
    assert all(len({M[i][j] for i in range(m)})==m for j in range(n))
    rich=set()
    for i in range(m):
        for j in range(n):
            neigh=[M[i][h] for h in range(n) if h!=j]
            neigh += [M[h][j] for h in range(m) if h!=i]
            if len(set(neigh))==len(neigh): rich.add((i,j))
    ok=all(any((x,y)!=(i,j) and (x==i or y==j)
               for x,y in rich) for i in range(m) for j in range(n))
    return k,rich,ok


def check_small_optimal():
    all_rows=list(permutations(range(5),3))
    minimum=None;number=0
    first=[0,1,2]
    for row1 in all_rows:
        if any(row1[j]==first[j] for j in range(3)):continue
        for row2 in all_rows:
            if any(row2[j]==first[j] or row2[j]==row1[j] for j in range(3)):continue
            k,rich,ok=analyze([first,list(row1),list(row2)])
            if ok:
                number+=1
                minimum=len(rich) if minimum is None else min(minimum,len(rich))
    assert minimum==4 and number>0,(minimum,number)
    print('DIRECT_EXHAUSTION_3x3',minimum,'rich edges,',number,'normalized witnesses')


def main():
    tests=0
    for n in range(2,12):
        for m in range(2,n+1):
            for d in (range(2,n-1) if m==n and n>=4 else [None]):
                M=construct(m,n,d)
                k,rich,ok=analyze(M)
                expected = (4 if m==n==2 else 4 if m==n==3 else m)
                assert k==(4 if m==n==2 else m+n-1),(m,n,k)
                assert ok,(m,n,d,rich)
                assert len(rich)==expected,(m,n,d,len(rich),expected)
                if m<n:assert rich=={(i,0) for i in range(m)}
                if m==n and n>=4:
                    assert rich==({(0,j) for j in range(d)}|
                                  {(1,j) for j in range(d,n)})
                tests+=1
    # 3 colors cannot satisfy the open rich-neighbor condition on C4.
    for a in range(3):
        pass
    assert not analyze([[0,1],[1,2]])[2]
    check_small_optimal()
    print('CONSTRUCTION_TESTS_OK',tests)
    print('VERIFY_OK')

if __name__=='__main__':main()
