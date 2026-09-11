"""Verify the exact-identity minor-arc obstruction disproving the target sup bound.

Mechanism (all large N; q prime with Q0 < q <= 2Q0, Q0=(log N)^A):
 (i)  Exact Parseval identity: sum_{a mod q} |S(a/q)|^2 = q * sum_r E_r^2.
 (ii) Exact orthogonality: sum_a S(a/q) = q*E_0 with E_0 = 0 for large N
      (since q <= 2(logN)^A << N/3-N^{5/6}), giving max_{a!=0}|S(a/q)| >= T/(q-1),
      T = sum_{p in interval} log p ~ 2h (cited Huxley short-interval PNT).
 (iii) Analytic minor-arc membership: 1/q in lowest terms differs from every
      a'/q' (q'<=Q0) by >= 1/(q q') >= 1/(2 Q0^2) >> (logN)^B/N (standard width).
 (iv) Crossover: R(N)=N^{1/150}/(2(logN)^A) -> infinity; exact crossover decade.
Stdlib only. Replay: python3 verify_obstruction.py -> prints VERIFY_OK.
"""
import math

def primes_upto(n):
    s = bytearray(b'\x01')*(n+1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*i:n+1:i] = b'\x00'*(((n-i*i)//i)+1)
    return [i for i in range(n+1) if s[i]]

def check_one(N, q, A=2.0):
    X = N/3.0; h = N**(5/6)
    lo, hi = X-h, X+h
    assert q <= 2*math.log(N)**A < X - h, "q outside interval -> E0 regime check"
    P = primes_upto(int(math.ceil(hi))+10)
    E = [0.0]*q; T = 0.0
    for p in P:
        if p < lo: continue
        if p > hi: break
        T += math.log(p); E[p % q] += math.log(p)
    assert E[0] == 0.0, E[0]
    S = []
    for a in range(q):
        re = im = 0.0
        for r in range(q):
            ang = 2*math.pi*a*r/q
            re += E[r]*math.cos(ang); im += E[r]*math.sin(ang)
        S.append(complex(re, im))
    lhs = sum(abs(z)**2 for z in S); rhs = q*sum(e*e for e in E)
    assert abs(lhs-rhs) <= 1e-6*max(1.0, rhs), (lhs, rhs)          # (i) Parseval
    assert abs(sum(S).real - q*E[0]) < 1e-6 and abs(sum(S).imag) < 1e-6  # (ii) orthog
    m = max(abs(S[a]) for a in range(1, q))
    assert m + 1e-9 >= T/(q-1), (m, T/(q-1))                        # (ii) lower bound
    # (iii) analytic spacing spot-check: min distance from a*/q to Q0-rationals
    Q0 = math.log(N)**A; Q0i = int(math.floor(Q0))
    astar = max(range(1, q), key=lambda a: abs(S[a]))
    best = min(abs(astar/q - ap/qp)
               for qp in range(1, Q0i+1) for ap in range(qp+1)
               if math.gcd(ap, qp) == 1 and not (qp == q and ap == astar))
    assert best >= 1/(q*Q0i) - 1e-12, (best, 1/(q*Q0i))             # spacing lemma
    print(f"N={N} q={q}: T/2h={T/(2*h):.4f} max|S|/h={m/h:.5f} "
          f"T/((q-1)h)={T/((q-1)*h):.5f} N^-1/150={N**(-1/150):.4f} sep~{best:.2g}")
    return True

for (N, q) in [(60000, 127), (120000, 139)]:
    check_one(N, q)

print("--- (iv) crossover: R(N)=N^{1/150}/(2 (log N)^A) ---")
for A in [1, 2, 5]:
    import decimal as _d
    ks = [k for k in range(1, 3000) if k*math.log(10)/150 > math.log(2)+A*math.log(k*math.log(10))]
    k0 = min(ks)
    assert all(k in ks for k in range(k0, 3000))  # monotone beyond crossover
    print(f"A={A}: first decade with R>1 at k={k0} (R(10^{k0})="
          f"{math.exp(k0*math.log(10)/150-math.log(2)-A*math.log(k0*math.log(10))):.3f}); R(10^3000)~1e"
          f"{(3000*math.log(10)/150-math.log(2)-A*math.log(3000*math.log(10)))/math.log(10):.1f}")
print("--- disjointness N/(2 (logN)^{2A+B}) at N=10^12, A=2, B=3: "
      f"{1e12/(2*math.log(1e12)**7):.2g} (>>1 eventually; ->infinity) ---")
print("VERIFY_OK")
