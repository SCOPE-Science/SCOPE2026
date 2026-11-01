"""Independent bit-parallel exact LCS exhaustive check for ternary adjacent pairs."""
import json


def lcs_bit(a, b):
    masks = [0, 0, 0]
    for k, x in enumerate(b):
        masks[int(x)] |= 1 << k
    state = 0
    for x in a:
        union = masks[int(x)] | state
        shifted = (state << 1) | 1
        state = union & (union ^ (union - shifted))
    return state.bit_count()


def admissible(w):
    n = len(w)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if 20 * lcs_bit(w[i:j], w[j:n]) > 9 * (n - i):
                return False
    return True


def run():
    words = ['0']
    sizes = {'1': 1}
    for n in range(2, 34):
        next_words = []
        for word in words:
            alphabet_bound = min(2, max(int(c) for c in word) + 1)
            for x in range(alphabet_bound + 1):
                new = word + str(x)
                if admissible(new):
                    next_words.append(new)
        words = next_words
        sizes[str(n)] = len(words)
    return sizes


if __name__ == '__main__':
    result = run()
    assert result['33'] == 0
    witness = '01020120212012101201020120212012'
    assert len(witness) == 32
    assert all(20 * lcs_bit(witness[i:j], witness[j:k]) < 9 * (k-i)
               for k in range(2, 33) for j in range(1, k) for i in range(j))
    print(json.dumps({'canonical_counts': result, 'strict_32_witness': witness,
                      'strict_32_passed': True}, sort_keys=True, indent=2))
