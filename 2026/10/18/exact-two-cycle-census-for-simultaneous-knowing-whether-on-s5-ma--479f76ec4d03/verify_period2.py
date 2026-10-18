"""Exact integer checks for cyclic simultaneous knowing-whether 2-cycles.

Run: python3 verify_period2.py (Python 3 standard library only).
"""

def unanimity(x, n):
    out = 0
    for i in range(n):
        a = (x >> ((i-1) % n)) & 1
        b = (x >> i) & 1
        c = (x >> ((i+1) % n)) & 1
        if a == b == c:
            out |= 1 << i
    return out


def matching_conjunction(x, m):
    n = 2*m
    def knows_pair(a, b):
        return ((x >> a) & 1) == ((x >> b) & 1)
    result = 0
    for i in range(m):
        a, b = 2*i, 2*i+1
        left_f = (2*((i-1) % m)+1, a)
        right_f = (b, 2*((i+1) % m))
        if knows_pair(a, b) and knows_pair(*left_f): result |= 1 << a
        if knows_pair(a, b) and knows_pair(*right_f): result |= 1 << b
    return result


def adjacency():
    n = 16
    m = [[0]*n for _ in range(n)]
    allowed = []
    for word in range(32):
        a = [(word >> j) & 1 for j in range(5)]
        mid = [int(a[j] == a[j+1] == a[j+2]) for j in range(3)]
        if int(mid[0] == mid[1] == mid[2]) == a[2]:
            start = sum(a[j] << j for j in range(4))
            end = sum(a[j+1] << j for j in range(4))
            m[start][end] += 1
            allowed.append(word)
    assert len(allowed) == 16
    return m


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def charpoly_by_traces(a):
    n = len(a)
    powers = [[int(i==j) for j in range(n)] for i in range(n)]
    traces = [0]
    coeff = [1]
    for k in range(1, n+1):
        powers = multiply(powers, a)
        traces.append(sum(powers[i][i] for i in range(n)))
        num = -sum(coeff[k-j]*traces[j] for j in range(1, k+1))
        assert num % k == 0
        coeff.append(num//k)
    return coeff


def polynomial_mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return out


def run():
    matrix = adjacency()
    expected = [0]*9 + polynomial_mul(polynomial_mul([-1,1],[-1,-1,0,1]),[1,1,0,1])
    assert charpoly_by_traces(matrix) == list(reversed(expected)), (charpoly_by_traces(matrix), expected)
    prod = [[int(i==j) for j in range(16)] for i in range(16)]
    counts = {}
    checks = 0
    for n in range(1, 17):
        prod = multiply(prod, matrix)
        if n % 2: continue
        trace = sum(prod[i][i] for i in range(16))
        brute = 0
        for x in range(1 << n):
            assert matching_conjunction(x, n//2) == unanimity(x,n)
            if unanimity(unanimity(x,n), n) == x:
                brute += 1
            checks += 1
        assert trace == brute, (n,trace,brute)
        # All-ones is the unique fixed configuration on a connected cycle.
        assert sum(unanimity(x,n)==x for x in range(1<<n)) == 1
        counts[n] = trace
    assert counts == {2:1,4:5,6:7,8:5,10:31,12:11,14:71,16:85}
    print('VERIFY_OK: 16-state transfer polynomial,', checks,
          'exhaustive valuations; two-cycle counts', counts)

if __name__ == '__main__':
    run()
