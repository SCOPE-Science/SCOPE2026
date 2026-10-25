"""Independent exhaustive/linear-algebra checks of edge-neighbour XOR claims.

Python 3, standard library only. The transition matrix is constructed from
common endpoints of graph edges, independently of the incidence proof.
"""
from itertools import product


def rank_binary(rows):
    pivots = {}
    for value in rows:
        while value:
            p = value.bit_length()-1
            if p in pivots:
                value ^= pivots[p]
            else:
                pivots[p] = value
                break
    return len(pivots)


def apply(rows, vector):
    result=0
    for i,row in enumerate(rows):
        if (row&vector).bit_count()%2:
            result |= 1<<i
    return result


def matrix_multiply(left, right):
    ans=[]
    for row in left:
        combined=0
        while row:
            bit=row&-row
            combined ^= right[bit.bit_length()-1]
            row^=bit
        ans.append(combined)
    return ans


def adjacency(sizes):
    groups=[]
    for i,n in enumerate(sizes):
        groups += [i]*n
    edges=[(u,v) for u in range(len(groups))
                    for v in range(u+1,len(groups)) if groups[u]!=groups[v]]
    rows=[]
    for i,(u,v) in enumerate(edges):
        bits=0
        for j,(x,y) in enumerate(edges):
            if j!=i and (u==x or u==y or v==x or v==y):
                bits|=1<<j
        rows.append(bits)
    return rows


def expected_ranks(sizes):
    r=len(sizes);N=sum(sizes)
    b3=r-1-int(r%2==0)
    return N-2,b3,0


def run():
    tested=0
    rank_checks=0
    exhaustive_graphs=0
    exhaustive_states=0
    for r in range(2,7):
        for sizes in product((2,4,6),repeat=r):
            n=sum(sizes)
            if n>16:
                continue
            rows=adjacency(sizes);e=len(rows)
            second=matrix_multiply(rows,rows)
            third=matrix_multiply(second,rows)
            ranks=(rank_binary(rows),rank_binary(second),rank_binary(third))
            prediction=expected_ranks(sizes)
            assert ranks==prediction,(sizes,ranks,prediction)
            assert not any(third),sizes
            b3=prediction[1]
            b2=prediction[0]-2*b3
            b1=e-2*prediction[0]+b3
            assert b1>=0 and b2>=0 and b3>=0
            assert b1+2*b2+3*b3==e
            tested+=1
            rank_checks+=3
            if e<=12:
                counts=[0,0,0,0]
                for v in range(1<<e):
                    t=v
                    if t==0:
                        depth=0
                    else:
                        depth=None
                        for i in range(1,4):
                            t=apply(rows,t)
                            if t==0:
                                depth=i
                                break
                        assert depth is not None
                    counts[depth]+=1
                cum=[sum(counts[:t+1]) for t in range(4)]
                expect=[1,1<<(e-ranks[0]),1<<(e-ranks[1]),1<<e]
                assert cum==expect,(sizes,cum,expect)
                exhaustive_graphs+=1
                exhaustive_states+=1<<e
    print('LINE_GRAPH_EVEN_PARTS_VERIFY_OK',
          'graphs=',tested,'rank_checks=',rank_checks,
          'exhaustive_graphs=',exhaustive_graphs,
          'exhaustive_states=',exhaustive_states)


if __name__=='__main__':
    run()
