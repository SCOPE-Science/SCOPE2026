# Certified refutation of the conjoined S1={2,3,5,7,50021} census claim

## Context

Let S1 = {2,3,5,7,50021}. The admitted target claimed that the S-unit
equation x + y = 1 with x, y in Z[{2,3,5,7,50021}^{-1}]^times has exactly
212 solutions up to symmetry (1269 ordered via N = 6N' - 3), that every
solution satisfies logarithmic Weil height h <= 14, and that the full
ledger containing (1/2,1/2), (2,-1), (9,-8), (25,-24), (49,-48) up to S3
symmetry with no others is enumerated by a certified sieve replay. The
set S1 is the four small primes plus the large prime 50021, the canonical
just-above-tableau frontier set: its radical 2*3*5*7*50021 = 10504410
exceeds the published von Kanel-Matschke radical tableau limit of 1e7,
and no solution file for S1 exists in that database.

## Definitions

An S1-unit is a nonzero rational whose numerator and denominator in lowest
terms have all prime factors in S1. For a reduced fraction p/q the
logarithmic Weil height is h(p/q) = log max(|p|,|q|). Ordered solutions are
pairs (x,y) of S1-units with x + y = 1. Up-to-symmetry solutions biject
with primitive triples 0 < a <= b < c with a + b = c, all of a, b, c
S1-smooth and gcd(a,b) = 1 (a, b, c are the cleared-denominator numerators;
primitivity is coprimality). If T is the number of such triples and exactly
one is symmetric (a = b), the ordered count is 6T - 3.

## Result

The conjoined claim is FALSE. Under the claim's own height cap h <= 14,
the complete solution set is exactly 66 primitive triples (393 ordered via
6*66 - 3 = 393), not 212 triples (1269 ordered). The named witnesses are
present, the S3 conversion is exact, and the ledger is machine-certified.
Hence no census can simultaneously have 212 triples and fit under height
14: either the 212/1269 count or the h <= 14 cap (or both) is wrong. This
is a rigorous TARGET disproof; it does not certify the global unbounded
solution count.

## Proof / evidence

1. Height cap made rigorous. With h(p/q) = log max(|p|,|q|), h <= 14 forces
max(|p|,|q|) <= e^14. Writing e = sum_{k<=N} 1/k! + R with 0 < R < 1/(N*N!)
for N = 22 and D = N!, exact big-integer arithmetic certifies
e < (N*s+1)/(N*D) where s = sum_{k<=N} D/k!, and pow(e_num,14) <
1202605*pow(e_den,14). Hence e^14 < 1202605, so every solution with h <= 14
has numerator and denominator at most B := 1202604. The script asserts this
with exact integers; no floating point is used. Independently,
e^14 ~= 1202604.284, confirming tightness.
2. Complete smooth list. Trial division of every integer 1..B by
{2,3,5,7,50021} yields exactly 1349 S1-smooth integers; each entry is
re-factored to confirm no outside prime divides it.
3. Exhaustive triple census. The double loop over the sorted 1349-list finds
exactly 66 triples with c <= B; the unique symmetric one is (1,1,2), so
ordered solutions = 6*66 - 3 = 393.
4. Independent recount. Looping directly over coprime unit pairs x = +-u/v
(u, v S1-smooth, max <= B) with 1 - x an S1-unit also gives 393.
5. Sanity checks. The claim's named solutions correspond to triples
(1,1,2), (1,2,3), (1,8,9), (1,24,25), (1,48,49), all present in the ledger.
Exactly three triples involve the large prime: (1,300125,300126) with
300125 = 5^3*7^4 and 300126 = 2*3*50021, (21,50000,50021) with
50000 = 2^4*5^5, and (400,50021,50421) with 400 = 2^4*5^2 and
50421 = 3*7^5. The remaining 63 triples exactly reproduce the known closed
{2,3,5,7} census of 63. Since 393 != 1269, the conjunction is refuted.

## Limitations

This disproves the conjunction of the 212/1269 count with the h <= 14 cap.
It does not certify the global solution count without a height cap, since
solutions of Weil height above 14 would lie outside the exhaustively
searched box B = 1202604. A spot-check to c <= 2e8 found no further
7-smooth triple, but the unbounded census remains open.

## Reproducibility

Stdlib-only script output/artifacts/verify_census.py prints VERIFY_OK in
about one minute: it re-derives the height certificate, re-sieves the 1349
smooth integers, re-enumerates the 66 triples, re-counts 393 ordered pairs
by an independent loop, checks all named witnesses and the three
50021-triples, and regenerates output/artifacts/ledger_66.txt.

## References

- Data for elliptic curves and classical Diophantine equations
(von Kanel-Matschke data page), S-unit Tables 1-3 and N = 6N' - 3 rule:
https://bmatschke.github.io/solving-classical-diophantine-equations/
- Solver for the S-unit equation x + y = 1 (SageMath docs, Baker-Wustholz
plus Yu plus LLL method):
https://doc.sagemath.org/html/en/reference/number_fields/sage/rings/number_field/S_unit_solver.html
- S-unit (unit equation u + v = 1; S-integral points on P1 minus three
points): https://en.wikipedia.org/wiki/S-unit
