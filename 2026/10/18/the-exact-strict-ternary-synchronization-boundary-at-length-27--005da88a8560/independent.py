"""Independent finite check using square-free candidates and a full 2D LCS table."""

def lcs(x, y):
    M = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                M[i + 1][j + 1] = M[i][j] + 1
            else:
                M[i + 1][j + 1] = max(M[i][j + 1], M[i + 1][j])
    return M[-1][-1]

def pass_sync(s):
    n = len(s)
    for width in range(2, n + 1):
        for i in range(n - width + 1):
            for cut in range(i + 1, i + width):
                if 16 * lcs(s[i:cut], s[cut:i + width]) >= 7 * width:
                    return False
    return True

def squarefree_suffix(s):
    return all(s[-2 * length:-length] != s[-length:]
               for length in range(1, len(s) // 2 + 1))

def main():
    level = ['0']
    for n in range(2, 29):
        later = [w + c for w in level for c in '012' if squarefree_suffix(w + c)]
        level = later
        if n in (27, 28):
            good = [w for w in level if pass_sync(w)]
            expected = ['012010212021012102010212012',
                        '021020121012021201020121021'] if n == 27 else []
            assert sorted(good) == sorted(expected), (n, good)
            assert len(level) == (5162 if n == 27 else 6740), (n, len(level))
            print('length:', n, 'squarefree_candidates_with_first_symbol_0:', len(level),
                  'valid:', len(good), 'examples:', good)
    print('INDEPENDENT_ENUMERATION_OK')

if __name__ == '__main__':
    main()
