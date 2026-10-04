import itertools, math


def chord(n, i, j, R=1.0):
    k = abs(i-j)
    k = min(k, n-k)
    return 2.0*R*math.sin(math.pi*k/n)


def quartet_delta(n, q, R=1.0):
    a,b,c,d = q
    sums = [
        chord(n,a,b,R)+chord(n,c,d,R),
        chord(n,a,c,R)+chord(n,b,d,R),
        chord(n,a,d,R)+chord(n,b,c,R),
    ]
    sums.sort()
    return (sums[2]-sums[1])/2.0


def exact_formula(n, R=1.0):
    h = math.pi/(2*n)
    if n % 4 == 0:
        return R*(2.0-math.sqrt(2.0))
    if n % 4 == 1:
        k=(n-1)//4
        return 4.0*R*math.cos(h)*math.sin(k*h)**2
    if n % 4 == 2:
        k=(n-2)//4
        return 4.0*R*math.cos(h)*math.sin(k*h)*math.sin((k+1)*h)
    k=(n-3)//4
    return 4.0*R*math.sin(k*h)*math.sin((k+1)*h)


def balanced_witness(n):
    p=n//2
    q=n-p
    a=p//2
    c=p-a
    b=q//2
    d=q-b
    return (0, a, a+b, a+b+c)


def brute(n):
    best=-1.0
    witness=None
    for q in itertools.combinations(range(n),4):
        x=quartet_delta(n,q)
        if x>best:
            best=x; witness=q
    return best,witness

for n in range(4,61):
    best,w=brute(n)
    expected=exact_formula(n)
    bw=quartet_delta(n,balanced_witness(n))
    if abs(best-expected)>2e-12 or abs(bw-expected)>2e-12:
        raise SystemExit(f'FAIL n={n} best={best} expected={expected} balanced={bw} witness={w}')
print('VERIFY_OK n=4..60')
