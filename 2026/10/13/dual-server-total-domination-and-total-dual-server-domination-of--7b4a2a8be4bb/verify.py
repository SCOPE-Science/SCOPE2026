from itertools import product


def profiles_of_order(n, minimum=1):
    def rec(rem, lo, acc):
        if rem == 0:
            if len(acc) >= 2:
                yield tuple(acc)
            return
        for x in range(lo, rem + 1):
            yield from rec(rem - x, x, acc + [x])
    yield from rec(n, minimum, [])


def adjacency(parts):
    owner=[]
    for i,s in enumerate(parts):
        owner += [i]*s
    n=len(owner)
    return [[u!=v and owner[u]!=owner[v] for v in range(n)] for u in range(n)]


def valid_ds(adj, lab):
    R=[i for i,x in enumerate(lab) if x==1]
    B=[i for i,x in enumerate(lab) if x==2]
    if not R or not B:
        return False
    for v,x in enumerate(lab):
        if x==0:
            if not any(adj[v][u] for u in R): return False
            if not any(adj[v][u] for u in B): return False
    return True


def valid_dst(adj, lab):
    if not valid_ds(adj,lab): return False
    S=[i for i,x in enumerate(lab) if x]
    return all(any(adj[v][u] for u in S) for v in S)


def valid_tds(adj, lab):
    if not valid_ds(adj,lab): return False
    R=[i for i,x in enumerate(lab) if x==1]
    B=[i for i,x in enumerate(lab) if x==2]
    return all(any(adj[v][u] for u in R) for v in R) and all(any(adj[v][u] for u in B) for v in B)


def brute(parts, pred):
    adj=adjacency(parts)
    n=sum(parts)
    best=None
    tests=0
    for lab in product((0,1,2), repeat=n):
        tests += 1
        w=sum(x!=0 for x in lab)
        if best is not None and w>=best:
            continue
        if pred(adj,lab): best=w
    return best,tests


def dst_formula(parts):
    n=sum(parts); r=len(parts); s=min(parts); t=sum(x==1 for x in parts)
    star=(r==2 and s==1)
    if star: return n
    if t>=2: return 2
    if s<=2: return 3
    return 4


def tds_formula(parts):
    n=sum(parts); r=len(parts); s=min(parts)
    star=(r==2 and s==1)
    return None if star or n==3 else 4


def main():
    profiles=0; dst_tests=0; tds_tests=0
    for n in range(2,9):
        for parts in profiles_of_order(n):
            profiles += 1
            got,tests=brute(parts,valid_dst); dst_tests += tests
            exp=dst_formula(parts)
            assert got==exp,(parts,'dst',got,exp)
            got,tests=brute(parts,valid_tds); tds_tests += tests
            exp=tds_formula(parts)
            assert got==exp,(parts,'tds',got,exp)
    print('ALL CHECKS PASSED')
    print(f'profiles={profiles}')
    print(f'dst_assignments_enumerated={dst_tests}')
    print(f'tds_assignments_enumerated={tds_tests}')
    print('orders=2..8')

if __name__=='__main__': main()
