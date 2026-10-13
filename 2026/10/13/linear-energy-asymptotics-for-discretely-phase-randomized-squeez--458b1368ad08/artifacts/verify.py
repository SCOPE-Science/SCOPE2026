import math

def p_sv(j, M, c):
    if j % 2:
        return 0.0
    k = j // 2
    nbar = c * M
    q = nbar / (1.0 + nbar)
    logp = (-0.5 * math.log1p(nbar)
            + math.lgamma(2*k + 1) - 2*math.lgamma(k + 1)
            - k*math.log(4.0) + k*math.log(q))
    return math.exp(logp)

def visibility(M, c):
    total = 0.0
    for j in range(0, M, 2):
        a = p_sv(j, M, c)
        b = p_sv(j + M, M, c)
        total += a*b/(a+b)
    return 4.0*total

def h(x, c):
    pref = math.sqrt(2.0/(math.pi*c))
    return pref/(math.sqrt(x)*math.exp(x/(2*c)) + math.sqrt(x+1)*math.exp((x+1)/(2*c)))

def simpson(f, a, b, n):
    if n % 2: n += 1
    step=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        s += (4 if i%2 else 2)*f(a+i*step)
    return s*step/3

def limit_visibility(c):
    return 2.0*simpson(lambda x:h(x,c),0.0,1.0,20000)

def rate(c):
    return c - 1.0 - math.log(c)

def classical_logfactor(M,c):
    # log of e^(cM) M! / (cM)^M
    return c*M + math.lgamma(M+1) - M*math.log(c*M)

for c in (0.2, 0.5, 0.8):
    target=limit_visibility(c)
    vals=[visibility(M,c) for M in (200,500,1000,2000)]
    assert target > 0
    assert abs(vals[-1]-target) < 0.01
    I=rate(c)
    assert I > 0
    M=4000
    normalized=(classical_logfactor(M,c)-0.5*math.log(M))/M
    assert abs(normalized-I) < 0.01
    assert c*(M+1)/M < 1.0
print('VERIFY_OK')
