"""Convert side-preserving bipartite canonical codes to unrooted isomorphism counts."""
from itertools import permutations
from pathlib import Path

def canonical_rows(rows):
    a=len(rows); b=5
    best=None
    for p in permutations(range(a)):
        columns=sorted(sum(1<<r for r,i in enumerate(p) if rows[i]>>j&1) for j in range(b))
        code=sum(col<<(a*k) for k,col in enumerate(columns))
        if best is None or code<best:best=code
    return best

if __name__=='__main__':
    home=Path(__file__).resolve().parent
    lines=[tuple(map(int,line.split())) for line in (home/'all_graphs10.txt').read_text().splitlines()]
    squares={code for a,b,code in lines if a==b==5}
    orbits={min(code,canonical_rows([(code>>(5*j))&31 for j in range(5)])) for code in squares}
    print('side-preserving connected classes n=10',len(lines))
    print('balanced-side classes',len(squares),'after side exchange',len(orbits))
    count=len(lines)-len(squares)+len(orbits)
    print('unlabelled connected bipartite graphs n=10',count)
    assert count==4032
    lines9=[line for line in (home/'all_graphs9.txt').read_text().splitlines()]
    assert len(lines9)==730
    print('unlabelled connected bipartite graphs n=9',len(lines9))
    print('PASS')
