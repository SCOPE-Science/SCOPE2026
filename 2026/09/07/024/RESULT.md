# A sharp volume threshold for h2* <= 3h1* on reduced reflexive weighted-projective 4-simplices

## Context

Ehrhart positivity and unimodality for reflexive (Gorenstein) polytopes connects
toric Fano geometry, Hibi-type coefficient inequalities, and the
Braun-Davis-Solus program on the integer decomposition property (IDP) implying
unimodality. Sharp linear bounds between h*-coefficients and the volume range
over which they hold were unknown even for 4-dimensional simplices. This record
certifies a finite, exactly checkable extremal fragment: a sharp normalized-volume
threshold at which the clean inequality h2* <= 3h1* first fails.

## Definitions

- Let q = (q0,...,q4) be positive integers with gcd(q) = 1 and Q = sum qi.
- Let N = Z^5 / Z q and ui the image of the i-th standard basis vector.
  The **reduced weighted-projective 4-simplex** is
  Delta(q) = conv(u0,...,u4) in N_R ~= R^4. Its normalized volume is Q.
- **Reflexivity criterion (F1):** Delta(q) is reflexive iff qi | Q for all i
  (Conrads, Prop. 3.5; cf. Batyrev; Braun-Kreuzer-Skarke). Scope is restricted
  to this class only, not all reflexive 4-polytopes.
- **Age formula (F2):** h*_j = #{k in [0,Q-1] : age(k) = j}, where
  age(k) = (1/Q) sum_i ((k qi) mod Q). When (F1) holds every age is an integer
  and in dimension 4 h* = (1, h1, h2, h1, 1).
- Excess means h2* - 3h1*.

## Result (machine-checked classification fragment)

Among reduced reflexive weighted-projective 4-simplices:

1. There are exactly **136** with normalized volume Q <= 377.
2. All 136 satisfy **h2* <= 3h1***.
3. Equality holds for exactly two weights (up to permutation),
   **(1,1,3,3,4)** and **(1,2,2,3,4)**, both with Q = 12 and
   h* = (1,2,6,2,1).
4. The bound Q <= 377 is best possible in this class: Q = 378 admits the
   reflexive weight **(2,7,54,126,189)** with h* = (1,75,226,75,1),
   so excess = 1 > 0, and no smaller-volume reflexive weight in this class
   violates the inequality.
5. The next violator in the sweep Q <= 430 is **(3,7,60,140,210)**,
   Q = 420, h* = (1,83,252,83,1), excess 3. (The sweep Q <= 430 contains
   139 rows total, including one further reflexive row
   (1,20,84,105,210) at Q = 420 with h* = (1,93,232,93,1), excess -47,
   which is not a violator.)
6. The breakdown is explained by the finite 14-member **(6,14,21)-core family**
   q = (u,v,6m,14m,21m) with m = u+v, u | 42, v | 42, gcd(u,v) = 1
   (u <= v), Q = 42m, for which
   age(k) = {ku/42m} + {kv/42m} + {k/7} + {k/3} + {k/2}.
   All 14 give reflexive weights. Exact table:

| Q | (u,v,m) | q | h* | excess |
|---|---|---|---|---|
| 84 | (1,1,2) | (1,1,12,28,42) | (1,21,40,21,1) | -23 |
| 126 | (1,2,3) | (1,2,18,42,63) | (1,28,68,28,1) | -16 |
| 168 | (1,3,4) | (1,3,24,56,84) | (1,36,94,36,1) | -14 |
| 210 | (2,3,5) | (2,3,30,70,105) | (1,43,122,43,1) | -7 |
| 294 | (1,6,7) | (1,6,42,98,147) | (1,61,170,61,1) | -13 |
| 336 | (1,7,8) | (1,7,48,112,168) | (1,68,198,68,1) | -6 |
| 378 | (2,7,9) | (2,7,54,126,189) | (1,75,226,75,1) | +1 |
| 420 | (3,7,10) | (3,7,60,140,210) | (1,83,252,83,1) | +3 |
| 546 | (6,7,13) | (6,7,78,182,273) | (1,108,328,108,1) | +4 |
| 630 | (1,14,15) | (1,14,90,210,315) | (1,125,378,125,1) | +3 |
| 714 | (3,14,17) | (3,14,102,238,357) | (1,140,432,140,1) | +12 |
| 924 | (1,21,22) | (1,21,132,308,462) | (1,181,560,181,1) | +17 |
| 966 | (2,21,23) | (2,21,138,322,483) | (1,188,588,188,1) | +24 |
| 1806 | (1,42,43) | (1,42,258,602,903) | (1,348,1108,348,1) | +64 |

The first two global violators are the 7th and 8th members; excess grows to 64.

## Proof / evidence

Two independent counting routes, both rerun by the auditor:

(a) **Exhaustive divisor-tuple sweep (age route).** For each 5 <= Q <= 430:
list all nondecreasing 5-tuples of divisors of Q summing to Q; keep gcd = 1;
compute the age histogram; keep palindromic rows. By (F1) this enumerates every
candidate reduced reflexive weight. Result: 136 rows Q <= 377, 139 rows
Q <= 430, no violator below 378, violators exactly at 378 and 420 (in range),
equality exactly at the two Q = 12 weights. Independent recount confirmed
136 reduced divisor tuples exist at Q <= 377 and all 136 are age-palindromic,
so the filter excludes nothing in range. Script <60 lines, stdlib only,
deterministic, ~1 minute.

(b) **Independent gauge-fixed Ehrhart recount (no age formula).** Fix q; each
class of N has a unique representative x in Z^5 with 0 <= x4 < q4; [x] lies in
t Delta(q) iff x_i + mu qi >= 0 for all i with mu = (t-S)/Q, S = sum x.
Counting per (S,x4) via exact stars-and-bars C(T-B+3,3) with
b_i = ceil((S-t)qi/Q), B = sum b_i, uses only integer arithmetic (no roots of
unity, no modular inverses). From L(t) = |tP cap N|, t = 0..4, solve
L(t) = sum_j h_j C(t+4-j,4). Confirmed:
- (1,1,3,3,4), Q=12: L = (1,7,31,97,241), h* = (1,2,6,2,1), match;
- (1,2,2,3,4), Q=12: L = (1,7,31,97,241), h* = (1,2,6,2,1), match;
- (2,7,54,126,189), Q=378: L = (1,80,616,2365,6461), h* = (1,75,226,75,1), match;
- (3,7,60,140,210), Q=420: L = (1,88,682,2623,7171), h* = (1,83,252,83,1), match;
plus 10 random Q <= 377 rows and summation-window widening checks.

(c) **Core-family closed form.** The identities 6m/Q = 1/7, 14m/Q = 1/3,
21m/Q = 1/2 give the fractional-part age decomposition above; all 14
(u,v) pairs (coprime divisors of 42) verified to satisfy Q = 42m, qi | Q,
gcd = 1, with raw age loop agreeing with the fractional-part formula on all 14.

**What is not claimed:** no human-readable analytic proof of item 2 covering
all 136 cases by hand; the proof of item 2 is the reproducible exhaustive
computation. No statement beyond weighted-projective simplices.

## Limitations

- Inequality for Q <= 377 proved by exhaustive computation, not a conceptual
  analytic argument.
- Completeness depends on the classical criterion qi | Q (Conrads/Batyrev/
  Braun et al.), cited not re-proved.
- No claim for non-weighted-projective reflexive 4-polytopes.
- Sweep covers Q <= 430; family table extends to Q = 1806 for that subfamily only.

## Reproducibility

```
python3 output/artifacts/scan_weights.py      # full table (~1 min)
python3 output/artifacts/audit_ehrhart.py     # witness recount (seconds)
python3 output/artifacts/family_table.py      # 14-member table (seconds)
python3 output/artifacts/supplement_checks.py # frac-formula + samples
python3 output/artifacts/reflexivity_audit.py # completeness audit
```

## References

- Conrads, Weighted projective spaces and reflexive simplices, Prop. 3.5
  (reflexivity criterion qi | Q).
- Batyrev, Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces.
- Braun-Kreuzer-Skarke and Braun-Davis-Solus literature on reflexive
  weighted-projective simplices.
- Braun, Davis, Hanley, Lane, Solus, The Integer Decomposition Property and
  Weighted Projective Space Simplices, arXiv:2103.17156.
- Braun, Davis, Solus, Detecting the Integer Decomposition Property and
  Ehrhart Unimodality in Reflexive Simplices, arXiv:1608.01614.
- Ghirlanda, A classification algorithm for reflexive simplices,
  arXiv:2510.09131.
