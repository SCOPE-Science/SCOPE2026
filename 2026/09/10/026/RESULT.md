# Corrected census floor for C: y^2 = x^5 - 5x^3 + 4x + 1

## Context

The admitted target claimed that the smooth projective genus-2 curve
C: y^2 = f(x), f(x) = x^5 - 5x^3 + 4x + 1, has Jacobian of Mordell-Weil
rank exactly 1 and exactly 6 affine rational points
{(0,+-1),(1,+-1),(-1,+-1)} plus infinity, via a rank-1 Chabauty-Coleman
annihilator at p = 7 plus a Mordell-Weil sieve. The preset fallback
claimed a Strassman certificate of at most 6 affine points at p = 7.
Both are false: 10 further affine rational points exist, forcing at
least 17 total points and (via the Coleman rank-1 ceiling) rank >= 2.

## Definitions

- C/Q: smooth projective model of y^2 = f(x),
  f(x) = x^5 - 5x^3 + 4x + 1 = (x-2)(x-1)x(x+1)(x+2) + 1.
- J = Jac(C), genus g = 2. Discriminant disc(f) = 38569, prime; C has
  good reduction away from 38569 (in particular at p = 3, 5, 7, 11).
- The affine model is smooth; the plane projective closure has a unique
  point at infinity [0:1:0], with a single smooth place above it
  (odd-degree hyperelliptic model), so #C(F_q) = #affine + 1 at good p.
- Naive height H(a/b) = max(|a|, b) for x = a/b in lowest terms, b > 0.

## Result

For C: y^2 = x^5 - 5x^3 + 4x + 1:

1. **Point exhibition (census floor).** C(Q) contains at least 16 affine
   points plus infinity (17 total), at
   x in {-2, -7/4, -1, 0, 4/9, 1, 2, 3}:
   (-2,+-1), (-7/4,+-67/32), (-1,+-1), (0,+-1), (4/9,+-373/243),
   (1,+-1), (2,+-1), (3,+-11), plus infinity.
   In particular "exactly (0,+-1),(1,+-1),(-1,+-1) plus infinity" is
   false, and any "<= 6 affine" ceiling is false.
2. **Rank.** rank J(Q) >= 1 unconditionally (D = [(0,1)] - [inf] has
   infinite order); rank J(Q) >= 2 via the Coleman bound at good p = 7
   (#C(F_7) = 14 total, rank-1 ceiling 14 + 2 = 16 < 17 exhibited).
   Hence "rank exactly 1" is false.
3. **Torsion.** J(Q)_tors = 0.
4. **Galois.** Gal(f/Q) ~= S_5.
5. **Jacobian orders.** #J(F_p) = 27, 71, 120, 136 for p = 3, 5, 7, 11,
   by two independent exact enumerations (point-count formula and
   direct Mumford-divisor enumeration).
6. **Search windows.** No affine rational point with H(x) <= 2000
   outside the 8 listed x-values; no integral point with |x| <= 200000
   outside x in {-2,-1,0,1,2,3}.

## Proof / Evidence

All steps are exact (integer / Fraction / F_p[x] arithmetic); each
script prints an *_OK line. Key identities:
f(+-2) = 1, f(3) = 121 = 11^2,
f(-7/4) = 4489/1024 = (67/32)^2,
f(4/9) = 139129/59049 = (373/243)^2.

- Model: disc(f) = 38569 exactly (Bareiss on 9x9 Sylvester), prime by
  trial division; smooth/Q; good at 7 (38569 mod 7 = 6); f irreducible
  (mod-2 irreducible of degree 5); DDF patterns mod 2/7/11/19 =
  [5], [1,4], [1,1,3], [2,3] (`verify_model.py`, VERIFY_MODEL_OK).
- Points: 16 exact on-curve checks over Q (`verify_points.py`).
- Counts: #C(F_p) affine 6,10,13,12,19 (p = 3,5,7,11,13);
  #J(F_p) via (N1^2+N2)/2 - p with explicit F_{p^2} enumeration
  (`counts.py`); identical orders by Mumford enumeration
  (`jac_count.py`, JAC_COUNT_OK).
- Rank >= 1: reduction of D = [(0,1)] - [inf] is nontrivial mod 5
  (order 71 = #J(F_5), prime) and mod 11 (order dividing 136);
  a torsion order n = 5^a * 71 would have prime-to-11 part 5^a*71
  dividing 136, impossible (`rank_search.py`, R1_OK).
- Rank >= 2: #C(F_7) = 14 total recomputed; Coleman 1985 (r < g,
  p > 2g) gives rank-1 ceiling 14 + 2g - 2 = 16 < 17 exhibited
  (`coleman_floor.py`, COLEMAN_FLOOR_OK). Conditional only on the
  cited Coleman bound.
- Torsion: #J(F_5) = 71, #J(F_11) = 136, gcd = 1; pro-p kernel lemma
  eliminates all prime divisors and 5/11 powers
  (`torsion_trivial.py`, TORSION_TRIVIAL_OK).
- Galois: transitive (mod-2 irreducible) + 4-cycle (mod-7 [1,4]) +
  3-cycle (mod-11 [1,1,3]); only transitive S_5-subgroup with elements
  of order 4 and 3 is S_5 (`galois_s5.py`, GALOIS_S5_OK;
  mod-19 [2,3] recorded additionally).
- Infinity: affine chart smooth (disc != 0); unique plane point at
  infinity, one place above (`infinity.py`, INFINITY_OK).
- Windows: exhaustive coprime (a,b) search to H <= 2000 finds exactly
  the 8 x-values (auditor-extended from the H <= 200 artifact scan);
  isqrt scan to |x| <= 200000 finds exactly the 6 integral x-values
  (`rank_search.py`, `int_sweep.py` INT_SWEEP_OK).

## Limitations

Full census completeness (exactly these 17 points), the exact rank
value, second-generator height data, and any rank >= 2 Chabauty
analysis (e.g. quadratic Chabauty) are not claimed. The rank >= 2
upgrade depends on the cited Coleman 1985 bound at good p = 7;
everything else is self-contained exact computation. No Sage/Magma
and no Coleman integration / Strassman / sieve were performed (their
rank-1 premises are refuted).

## Reproducibility

Run `python3 <script>` for each artifact in output/artifacts/; each
prints its *_OK line (stdlib only except counts.py factorization
display, which uses sympy only for printing):
verify_model.py, counts.py, jac_count.py, rank_search.py,
verify_points.py, coleman_floor.py, torsion_trivial.py, galois_s5.py,
infinity.py, int_sweep.py.

## References

- R. Coleman, Effective Chabauty, Duke Math. J. 52 (1985).
- M. Stoll, Determining the rational points on a curve of genus 2 and
  Mordell-Weil rank 1 (2025).
- N. Bruin / M. Stoll, The Mordell-Weil sieve (LMS J. Comput. Math.).
- A. Booker et al., A database of genus 2 curves over Q (2016) / LMFDB.
- Math.SE 4205705 (Galois group of x^5-5x^3+4x+1 thread).
