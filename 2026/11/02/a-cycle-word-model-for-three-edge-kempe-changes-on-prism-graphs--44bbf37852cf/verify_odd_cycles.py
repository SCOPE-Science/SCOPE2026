"""Independent finite spot checks of the all-size five-cycle certificate."""
from verify_reduction import cycle_word_moves, words
A=['12132','12312','13212','13232','13132']
B=['121212','121232','123232','123132','121312']
def witness(n):
    base=A if n%2 else B
    prefix='12'*((n-len(base[0]))//2)
    return [tuple(map(int,prefix+s)) for s in base]
for n in range(5,61):
    v=witness(n)
    assert len(set(v))==5
    for i in range(5):
        x,y=v[i],v[(i+1)%5]
        assert x[0]==1 and x[-1]==2
        assert all(x[j]!=x[(j+1)%n] for j in range(n))
        assert y in cycle_word_moves(x),(n,i)
print('FIVE_CYCLE_ALL_TESTED_5_TO_60_PASS')
