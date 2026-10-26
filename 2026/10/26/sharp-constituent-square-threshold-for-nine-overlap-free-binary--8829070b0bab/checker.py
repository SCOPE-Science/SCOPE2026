"""Complete integer verification for bounded-root binary overlap-free square products.

No external packages. Two independent enumerations are compared: (A) complete
binary-prefix search with dynamic factorization masks, and (B) direct square-block
search with whole-word overlap tests. The length cap is a proved consequence of
nine blocks with roots of length at most six: 9 * 2 * 6 = 108.
"""
from itertools import product

ROOT_CAP = 6
BLOCK_COUNT = 9
LENGTH_CAP = 2 * ROOT_CAP * BLOCK_COUNT


def append_is_safe(v):
    """True if a single-bit extension has not introduced an overlap at its end."""
    n = len(v)
    for p in range(1, (n - 1) // 2 + 1):
        if v[-2*p-1:-p] == v[-p-1:]:
            return False
    return True


def entirely_overlap_free(v):
    """Direct test of every possible start and period (independent of pruning)."""
    n = len(v)
    for i in range(n):
        for p in range(1, (n-i-1)//2 + 1):
            if v[i:i+p+1] == v[i+p:i+2*p+1]:
                return False
    return True


def prefix_method(root_cap):
    maximum = 2 * root_cap * BLOCK_COUNT
    cache = {'': 1}   # bit t means this prefix admits exactly t square blocks
    frontier = ['']
    final = []
    prefix_counts = [1]
    for n in range(1, maximum + 1):
        next_frontier = []
        for w in frontier:
            for bit in '01':
                v = w + bit
                if not append_is_safe(v):
                    continue
                next_frontier.append(v)
                mask = 0
                for r in range(1, min(root_cap, n//2) + 1):
                    if v[-2*r:-r] == v[-r:]:
                        mask |= cache[v[:-2*r]] << 1
                cache[v] = mask
                if mask & (1 << BLOCK_COUNT):
                    final.append(v)
        frontier = next_frontier
        prefix_counts.append(len(frontier))
    return sorted(final), prefix_counts


def block_method(root_cap):
    squares = []
    for r in range(1, root_cap+1):
        for letters in product('01', repeat=r):
            x = ''.join(letters)
            if entirely_overlap_free(x+x):
                squares.append(x+x)
    layers = [('', ())]
    layer_counts = [1]
    for depth in range(1, BLOCK_COUNT+1):
        next_layer = []
        for word, roots in layers:
            for square in squares:
                v = word + square
                if entirely_overlap_free(v):
                    next_layer.append((v, roots+(len(square)//2,)))
        layers = next_layer
        layer_counts.append(len(layers))
    return sorted(layers), layer_counts, len(squares)


def main():
    survivor_counts = {}
    for root_cap in range(1,ROOT_CAP+1):
        block, levels, num_blocks = block_method(root_cap)
        prefix, prefixes = prefix_method(root_cap)
        block_words = sorted({w for w, _ in block})
        assert prefix == block_words, (root_cap, prefix, block_words)
        survivor_counts[root_cap] = levels
        print('root_cap',root_cap,'available_square_blocks',num_blocks,
              'factorization_counts_at_blocks_0_through_9',levels,
              'distinct_nine_square_words',len(block_words))
        if root_cap < ROOT_CAP:
            assert block == []
        else:
            assert len(block) == 2
            assert len(block_words) == 2
            assert len(prefixes) == LENGTH_CAP + 1
            for w, lengths in block:
                assert len(w) == 48
                assert lengths == (3,2,2,2,6,2,2,2,3)
                assert entirely_overlap_free(w)
                assert len(w)==2*sum(lengths)
                print('extremizer',w,'root_lengths',lengths)
            assert block_words[0] == block_words[1][::-1]
            assert block_words[0] == ''.join('1' if x=='0' else '0' for x in block_words[1])
    assert survivor_counts[5][-1] == 0
    assert survivor_counts[6][-1] == 2
    print('two independent exhaustive procedures agree through all root caps 1..6')
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    main()
