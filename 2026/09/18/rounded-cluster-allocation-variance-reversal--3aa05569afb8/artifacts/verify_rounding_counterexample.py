from fractions import Fraction as Q

# Cluster 1: six small positive gradients and one large positive gradient.
c1 = [Q(1, 10)] * 6 + [Q(67, 5)]
c2 = [Q(-1)] * 3
n1, n2 = len(c1), len(c2)
N = n1 + n2
p1, p2 = Q(n1, N), Q(n2, N)

def mean(xs):
    return sum(xs, Q(0)) / len(xs)

def popvar(xs):
    mu = mean(xs)
    return sum((x - mu) ** 2 for x in xs) / len(xs)

mu1, mu2 = mean(c1), mean(c2)
v1, v2 = popvar(c1), popvar(c2)
G = p1 * mu1 + p2 * mu2
within = p1 * v1 + p2 * v2
between = p1 * (mu1 - G) ** 2 + p2 * (mu2 - G) ** 2
total = within + between

# Budget m=2. Nearest proportional counts are (1,1).
m = 2
m1 = m2 = 1
v_rand = total / m
v_cl = p1 * p1 * v1 / m1 + p2 * p2 * v2 / m2

assert mu1 == 2 and mu2 == -1
assert v1 == Q(1083, 50) and v2 == 0
assert G == Q(11, 10)
assert within == Q(7581, 500)
assert between == Q(189, 100)
assert total == Q(4263, 250)
assert v_rand == Q(4263, 500)
assert v_cl == Q(53067, 5000)
assert v_cl - v_rand == Q(10437, 5000)
assert v_cl / v_rand == Q(361, 290)

# Budget m=10 permits exact proportional counts (7,3).
m_exact = 10
v_cl_exact = p1 * p1 * v1 / 7 + p2 * p2 * v2 / 3
v_rand_exact = total / m_exact
assert v_cl_exact == Q(7581, 5000)
assert v_rand_exact == Q(4263, 2500)
assert v_rand_exact - v_cl_exact == between / m_exact == Q(189, 1000)

print('mu1 =', mu1)
print('sigma1^2 =', v1)
print('mu2 =', mu2)
print('sigma2^2 =', v2)
print('G =', G)
print('sigma_W^2 =', within)
print('sigma_B^2 =', between)
print('sigma^2 =', total)
print('rounded random variance =', v_rand)
print('rounded clustered variance =', v_cl)
print('clustered - random =', v_cl - v_rand)
print('clustered/random =', v_cl / v_rand)
print('exact-proportional random variance =', v_rand_exact)
print('exact-proportional clustered variance =', v_cl_exact)
print('exact-proportional reduction =', v_rand_exact - v_cl_exact)
