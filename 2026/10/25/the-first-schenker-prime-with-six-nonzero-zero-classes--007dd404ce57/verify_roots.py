"""Independent p=2339 modular check using the truncated exponential basis."""
from math import factorial
P = 2339
assert all(P % d for d in range(2, int(P**0.5) + 1))
fact = [1] * P
for j in range(1, P): fact[j] = fact[j-1] * j % P
invfact = [pow(fact[j], -1, P) for j in range(P)]
roots = []
for r in range(1, P):
    s, power = 1, 1
    for j in range(1, r+1):
        power = power * r % P
        s = (s + power * invfact[j]) % P
    if s == 0: roots.append(r)
assert roots == [156,470,520,589,1092,2170], roots
print("lambda_2339:", len(roots))
print("roots:", *roots)
print("VERIFY_OK")
