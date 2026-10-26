"""Exact finite divisibility Littlestone and VC certificate (Python 3, stdlib)."""
import json
from functools import lru_cache
from pathlib import Path

THRESHOLDS = (2, 4, 9, 27, 81, 320, 1280)

def can_shatter(n, depth):
    # Row y encodes h_y(x)=1 precisely when x divides y.
    # Query x=1 is constant, so x ranges from 2 to n.
    columns = [sum(1 << (y - 1) for y in range(x, n + 1, x))
               for x in range(2, n + 1)]
    @lru_cache(None)
    def win(version_space, remaining):
        if remaining == 0:
            return version_space != 0
        if version_space.bit_count() < (1 << remaining):
            return False
        for column in columns:
            yes = version_space & column
            no = version_space ^ yes
            if (yes.bit_count() < (1 << (remaining - 1)) or
                no.bit_count() < (1 << (remaining - 1))):
                continue
            if win(yes, remaining - 1) and win(no, remaining - 1):
                return True
        return False
    return win((1 << n) - 1, depth), win.cache_info().currsize


def check_witness(tree, n, depth):
    # A leaf carries one actual hypothesis that realizes its root-to-leaf bits.
    encountered = set()
    def visit(node, remaining, requirements):
        if remaining == 0:
            assert isinstance(node, dict) and set(node) == {'y'}
            y = node['y']
            assert isinstance(y, int) and 1 <= y <= n
            assert y not in encountered
            encountered.add(y)
            assert all((y % x == 0) == answer for x, answer in requirements)
            return
        assert isinstance(node, dict) and set(node) == {'x', 'yes', 'no'}
        x = node['x']
        assert isinstance(x, int) and 2 <= x <= n
        visit(node['yes'], remaining - 1, requirements + [(x, True)])
        visit(node['no'], remaining - 1, requirements + [(x, False)])
    visit(tree, depth, [])
    assert len(encountered) == (1 << depth)
    return len(encountered)


def prime_list(length):
    primes=[]
    value=2
    while len(primes) < length:
        if all(value % p for p in primes):primes.append(value)
        value += 1
    return primes

def vc_dimension(n):
    v, product=0,1
    for p in prime_list(20):
        if product * p > n: break
        product *= p; v+=1
    return v


def main():
    for depth, first_n in enumerate(THRESHOLDS, 1):
        previous, nodes1 = can_shatter(first_n - 1, depth)
        current, nodes2 = can_shatter(first_n, depth)
        assert not previous, (depth, first_n - 1, nodes1)
        assert current, (depth, first_n, nodes2)
        print('FIRST', depth, first_n, 'states', nodes1, nodes2)
    assert can_shatter(1280, 8)[0] is False
    assert vc_dimension(1280) == 4
    assert vc_dimension(1279) == 4
    data=json.loads((Path(__file__).parent/'witness.json').read_text(encoding='utf-8'))
    assert set(data) == {'n', 'depth', 'tree'}
    assert data['n']==1280 and data['depth']==7
    assert check_witness(data['tree'], 1280, 7)==128
    print('CERTIFIED: first online-batch gap >=3 at n=1280; Ldim=7, VCdim=4')

if __name__ == '__main__': main()
