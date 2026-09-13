# Verify combinatorial facts about w3 = a B a b c c in F(a,b,c).
mp = {'a': 1, 'b': 2, 'c': 3}
w3 = [1, -2, 1, 2, 3, 3]
print("word:", w3, "length:", len(w3))

def red(w):
    return all(w[i] + w[i + 1] != 0 for i in range(len(w) - 1))

print("linearly reduced:", red(w3),
      "| cyclically reduced:", red(w3) and (w3[0] + w3[-1] != 0))
print("uses a:", any(abs(x) == 1 for x in w3),
      "uses b:", any(abs(x) == 2 for x in w3),
      "uses c:", any(abs(x) == 3 for x in w3))

ab = {g: sum(1 if x == g else (-1 if x == -g else 0) for x in w3)
      for g in (1, 2, 3)}
print("abelianization (a,b,c):", (ab[1], ab[2], ab[3]))
import math
g = math.gcd(math.gcd(ab[1], ab[2]), ab[3])
print("gcd:", g, "=> non-primitive" if g > 1 else "primitive?")

def is_power(w, k):
    n = len(w)
    if n % k != 0:
        return False
    d = n // k
    u = w[:d]
    return all(w[i] == u[i % d] for i in range(n)) and red(u)

print("proper power check (k=2,3,6):", {k: is_power(w3, k) for k in (2, 3, 6)})

phi = {1: 1, 2: 1, 3: -1}
print("phi(w3) =", sum(phi[abs(x)] * (1 if x > 0 else -1) for x in w3))
print("C6 elements order 2:", [k for k in range(6) if (2 * k) % 6 == 0 and (k % 6) != 0])
