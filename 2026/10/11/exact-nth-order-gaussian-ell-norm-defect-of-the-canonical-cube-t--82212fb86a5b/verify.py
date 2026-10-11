import math


def simpson(f, a, b, N=200000):
    if N % 2:
        N += 1
    h = (b-a)/N
    s = f(a) + f(b)
    for k in range(1, N):
        s += (4 if k % 2 else 2) * f(a+k*h)
    return s*h/3

for n in range(2, 9):
    f = lambda m: (m**n) * (math.sqrt(2/math.pi)*math.exp(-m*m/2))**n
    numeric = simpson(f, 0.0, 12.0, 40000)
    exact_moment = (2/math.pi)**(n/2) * 0.5 * (2/n)**((n+1)/2) * math.gamma((n+1)/2)
    assert abs(numeric-exact_moment) <= 2e-10 * max(1.0, exact_moment)
    c1 = (n**n/math.factorial(n))*exact_moment
    c2 = 2**(n-0.5)*n**((n-1)/2)*math.gamma((n+1)/2)/(math.factorial(n)*math.pi**(n/2))
    assert abs(c1-c2) <= 1e-13 * max(1.0, abs(c2))
print("VERIFY_OK")
