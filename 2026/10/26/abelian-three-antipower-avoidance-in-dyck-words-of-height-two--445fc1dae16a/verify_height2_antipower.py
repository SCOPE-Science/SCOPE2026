"""Independent finite regression for height-two Dyck words avoiding abelian 3-antipowers.

Run: python3 verify_height2_antipower.py
Only finite computations are tested; the general theorem requires the mathematical proof.
"""
from itertools import product


def words_height_two(n):
    # Independent balance-based generation, without using the height-code theorem.
    def recurse(prefix, up, down, height):
        if up == down == n:
            yield prefix
            return
        if up < n and height < 2:
            yield from recurse(prefix + '0', up + 1, down, height + 1)
        if down < up:
            yield from recurse(prefix + '1', up, down + 1, height - 1)
    yield from recurse('', 0, 0, 0)


def has_abelian_three_antipower(w):
    L = len(w)
    for p in range(1, L // 3 + 1):
        for i in range(0, L - 3*p + 1):
            # Counts computed afresh in each of three literal substrings.
            b = [w[i+j*p:i+(j+1)*p].count('0') for j in range(3)]
            if len(set(b)) == 3:
                return True
    return False


def predicted(n):
    ans = {'01' * n}
    if n % 2 == 0:
        ans.add('0011' * (n // 2))
    if n >= 4 and n % 3 != 0:
        ans.add('00' + '10' * (n-2) + '11')
    if n >= 5 and n % 3 == 2:
        ans.add('01' + '00' + '10' * (n-3) + '11')
        ans.add('00' + '10' * (n-3) + '11' + '01')
    return ans


def height_code(w):
    h = 0
    code = [0]
    for i, c in enumerate(w, start=1):
        h += 1 if c == '0' else -1
        if i % 2 == 0:
            assert h in (0, 2)
            code.append(h // 2)
    return code


def arithmetic_obstruction(code):
    n = len(code)-1
    for s in range(1, n//3 + 1):
        for j in range(n-3*s+1):
            x = [code[j+t*s] for t in range(4)]
            if x[0] == x[3] and len(set(x)) > 1:
                return True
    return False


def check():
    total = 0
    for n in range(1, 16):
        actual = set()
        for w in words_height_two(n):
            direct = has_abelian_three_antipower(w)
            code = height_code(w)
            encoded = arithmetic_obstruction(code)
            assert direct == encoded, (n, w, code, direct, encoded)
            if not direct:
                actual.add(w)
            total += 1
        wanted = predicted(n)
        assert actual == wanted, (n, actual-wanted, wanted-actual)
        expected_count = (1 + int(n%2 == 0) +
            int(n >= 4 and n%3 != 0) + 2*int(n >= 5 and n%3 == 2))
        assert len(actual) == expected_count
    for n in range(16, 151):
        wanted = predicted(n)
        assert len(wanted) == (1 + int(n%2==0) +
            int(n>=4 and n%3!=0) + 2*int(n>=5 and n%3==2))
        for w in wanted:
            assert not has_abelian_three_antipower(w), (n, w)
    print('HEIGHT_TWO_ABELIAN_ANTIPOWER_PASS lengths=1..15 total=', total,
          'constructive_lengths=16..150')


if __name__ == '__main__':
    check()
