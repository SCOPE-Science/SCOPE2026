# Independent audit: exact Ehrhart recount via gauge-fixed lattice-point count.
# Lemma (gauge count). Let q=(q0..q4), Q=sum, N=Z^5/Zq, u_i=image(e_i),
# P=conv(u_i), t>=0. Every class in N has a UNIQUE representative x in Z^5
# with 0<=x_4<q_4. A class [x] lies in tP iff for S=sum(x), mu=(t-S)/Q,
#   x_i + mu*q_i >= 0 for all i.
# Proof sketch: tP = image of {y in R^5_{>=0} : sum y = t}; [x] in tP iff
# exists y>=0, sum t, y-x in R*q, i.e. y=x+mu*q for mu=(t-S)/Q. QED.
# Hence L(t)=#{x in Z^5: 0<=x4<q4, S=sum x, x_i >= ceil(-mu q_i) forall i}.
# With T=S-x4, b_i=ceil((S-t) q_i/Q), B=sum b_i (i=0..3):
#   count per (S,x4) = C(T-B+3,3) if T>=B else 0.  (stars and bars)
# All arithmetic exact integers. Independent of the age/roots-of-unity route.
from math import comb, gcd
from functools import reduce


def ehrhart_via_gauge(q, t):
    Q = sum(q)
    q4 = q[4]
    total = 0
    for S in range(t - (t * Q) // q4 - Q - 2, t + Q + 1):
        mu_num = t - S  # mu = mu_num / Q
        # b_i = ceil(-mu*q_i) = ceil((S-t)*q_i/Q) for i=0..3
        B = 0
        ok = True
        for i in range(4):
            a = (S - t) * q[i]
            b = -(-a // Q) if a > 0 else a // Q  # ceil(a/Q)
            # careful: ceil division for possibly negative a
            import math
            b = math.ceil(a / Q)
            B += b
        for x4 in range(q4):
            T = S - x4
            if T < B:
                continue
            # also need x4-condition: x_4 + mu q4 >= 0, i.e. x4 >= b_4
            import math
            b4 = math.ceil((S - t) * q4 / Q)
            if x4 < b4:
                continue
            total += comb(T - B + 3, 3)
    return total


def hstar_from_ehrhart(L):
    # L(t) for t=0..4, dim 4: L(t)=sum_j h_j C(t+4-j,4)
    h = [0] * 5
    h[0] = L[0]
    h[1] = L[1] - 5 * h[0]
    h[2] = L[2] - 15 * h[0] - 5 * h[1]
    h[3] = L[3] - 35 * h[0] - 15 * h[1] - 5 * h[2]
    h[4] = L[4] - 70 * h[0] - 35 * h[1] - 15 * h[2] - 5 * h[3]
    return tuple(h)


def age_hist(q):
    Q = sum(q)
    h = [0] * 5
    for k in range(Q):
        s = sum((k * qi) % Q for qi in q)
        h[s // Q] += 1
    return tuple(h)


if __name__ == "__main__":
    import math, time
    witnesses = [(1, 1, 3, 3, 4), (1, 2, 2, 3, 4),
                 (2, 7, 54, 126, 189), (3, 7, 60, 140, 210)]
    for q in witnesses:
        t0 = time.time()
        L = [ehrhart_via_gauge(q, t) for t in range(5)]
        h = hstar_from_ehrhart(L)
        ha = age_hist(q)
        print(q, "Q=", sum(q), "L=", L, "h(gauge)=", h, "h(age)=", ha,
              "MATCH" if h == ha else "MISMATCH", f"{time.time()-t0:.1f}s")
