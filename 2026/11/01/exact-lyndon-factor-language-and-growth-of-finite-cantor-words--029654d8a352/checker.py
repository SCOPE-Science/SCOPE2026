"""Independent finite-rank check of the Cantor Lyndon-factor decomposition."""

def cantor(rank):
    word = '1'
    for j in range(rank):
        word = word + '0' * (3 ** j) + word
    return word


def is_lyndon(word):
    return len(word) == 1 or all(word < word[i:] for i in range(1, len(word)))


def brute_lyndon_factors(word):
    distinct = {word[i:j] for i in range(len(word))
                for j in range(i + 1, len(word) + 1)}
    return {factor for factor in distinct if is_lyndon(factor)}


def predicted(rank):
    lyndon = {'0', '1', '01'}
    if rank == 0:
        return {'1'}
    for k in range(2, rank + 1):
        previous = cantor(k - 1)
        prefixes = [previous[:j+1] for j, ch in enumerate(previous) if ch == '1']
        additions = {'0' * t + prefix
                     for t in range(3 ** (k - 2) + 1, 3 ** (k - 1) + 1)
                     for prefix in prefixes}
        assert len(additions) == 4 * (6 ** (k - 2))
        assert not (lyndon & additions)
        lyndon |= additions
    return lyndon


def run():
    for rank in range(0, 6):
        word = cantor(rank)
        direct = brute_lyndon_factors(word)
        structural = predicted(rank)
        assert direct == structural, (rank, direct - structural, structural - direct)
        expected = 1 if rank == 0 else (4 * 6 ** (rank - 1) + 11) // 5
        assert len(direct) == expected
        print(f'rank={rank} length={len(word)} lyndon_factors={len(direct)} exact_sets_agree')
    print('All independent direct-set comparisons passed.')


if __name__ == '__main__':
    run()
