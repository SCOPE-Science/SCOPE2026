"""Finite checks for binary neighbour-parity on line graphs of augmented cubes."""

def rank_gf2(rows):
    pivots = {}
    for row in rows:
        x = row
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def matmul_gf2(a, b):
    out = []
    for row in a:
        acc = 0
        while row:
            bit = row & -row
            acc ^= b[bit.bit_length()-1]
            row ^= bit
        out.append(acc)
    return out


def folded_line_adjacency(d):
    vertex_count = 1 << d
    mask = vertex_count - 1
    edges = sorted(set((min(v, v^jump), max(v, v^jump))
                       for v in range(vertex_count)
                       for jump in [1 << i for i in range(d)] + [mask]))
    a = []
    for i, (u, v) in enumerate(edges):
        row = 0
        for j, (s, t) in enumerate(edges):
            if i != j and (u == s or u == t or v == s or v == t):
                row |= 1 << j
        a.append(row)
    return a


def image_count(d):
    vertex_count = 1 << d
    m = (d + 1) * (vertex_count // 2)
    z = 1 << ((d-1)//2)
    r1 = vertex_count-2
    r2 = vertex_count//2-z-2
    return (m,r1,r2)


def check():
    for d in range(3,8):
        a = folded_line_adjacency(d)
        a2 = matmul_gf2(a, a)
        a3 = matmul_gf2(a2, a)
        m,r1,r2 = image_count(d)
        ranks = (rank_gf2(a), rank_gf2(a2), rank_gf2(a3))
        assert len(a) == m
        assert ranks == (r1,r2,0), (d, ranks, (r1,r2,0))
        assert not any(a3)
        print('dimension',d,'edge_sites',m,'ranks',list(ranks),
              'Jordan_blocks',{'size3':r2,'size2':r1-2*r2,'size1':m-2*r1+r2})
        if d == 3:
            counts = [0,0,0,0]
            for state in range(1<<m):
                v=state;t=0
                while v:
                    nxt = 0
                    for i,row in enumerate(a):
                        if (row&v).bit_count()%2:
                            nxt |= 1<<i
                    v=nxt;t+=1
                    assert t<=2
                counts[t]+=1
            assert counts == [1,1023,64512,0], counts
            print('dimension_3_exhaustive_extinction_times',counts)
    print('FOLDED_LINE_VERIFY_OK')

if __name__ == '__main__':
    check()
