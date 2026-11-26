# Independent mathematical audit

## correctness

PASS

For a=2pq+r in lowest terms, the first iterate is q(2p+r)/(2p), so its reduced denominator is d=2p/gcd(q,2p) and its floor is Q=q+floor(qr/(2p)). Applying the same reduction to a number of denominator d gives the necessary and sufficient conditions d>1 and d divides Q. For q<q0=2 ceil((p+1)/4) one has q<p; for even q, Q<=2q-1<p=d, and for odd q, Q<2p=d. At q0 the denominator is p and the only feasible positive multiple is Q=p, so the problem reduces to the half-open remainder interval in the proof. For p=3 mod 4 it starts at 2p-4+4/(p+1) and ends at 2p; the smallest odd r is 2p-3, except when it equals p at p=3 and r=5 is needed. For p=1 mod 4 the endpoints are 2p-12+36/(p+3) and 2p-8+24/(p+3). At p>=37 the first odd r is 2p-11, below the upper endpoint and coprime to p. The only smaller primes of that class are 5,13,17,29; their intervals yield r=3,17,25,49, respectively. Thus in every branch the first possible quotient is feasible, and the least remainder there gives global minimality. Independent bounded replay: python3 /workspace/reproductions/frozen_checks.py entrance checked all smaller reduced numerators and the first exact-two numerator for 33 odd primes below 142 by unreduced integer two-step arithmetic. Frozen verification code and notes were inspected, not executed, and the finite check is not the proof.

## originality

PASS

The map, entrance-order problem, general residue recurrence and divisibility criterion are prior. The supported distinct claim is the exact minimum for the mixed denominator family 2p, including the first feasible quotient and every rounding and coprimality exception. The finite-class description allows a search for a fixed p, but does not identify the minimum uniformly in p.

## value

PASS

This resolves a concrete case of an explicitly posed minimum problem, for the natural smallest-even-factor mixed family beyond prime powers. A quotient obstruction plus finite coprime rounding yields a complete classification across an infinite family, with exceptional primes proved exhaustive. It is more than checking that some orbit works or counting admissible classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
