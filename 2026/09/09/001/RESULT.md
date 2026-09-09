# Exact mod-4 classification of singular overpartitions with parts prime to 3

## Context
Andrews singular overpartitions at k=3, i=1 count overpartitions whose parts
are not divisible by 3. Per Sang–Shi (arXiv:1712.08930 §1), this equals the
Rogers–Ramanujan–Gordon number Abar_{3,3,1}(n). Andrews noted mod-3
congruences; Chen–Hirschhorn–Sellers proved an infinite mod-3 family;
Sang–Shi proved analytic mod-4 dissections including S(4n+2) ≡ 0 (mod 4).
No source records an exact odd-mod-4 dichotomy or a combinatorial witness
for this object (arXiv search "singular overpartition crank": zero results).

## Definitions
- S(n) = number of overpartitions of n with all parts prime to 3; S(0)=1.
- G(q) = prod_{3∤m} (1+q^m)/(1−q^m) = Σ S(n) q^n.
- R(q) = G(q)/G(q²) = prod_{m odd, 3∤m} (1+q^m)/(1−q^m).
- t(n) = #{odd divisors d of n with 3∤d}; t(0)=0.
- v_3(m) = 3-adic valuation; stripped part u = m/3^{v_3(m)}.
- Overpartition encoded by distinct values (descending) with
  (multiplicity, overline-bit). φ₁ flips the bit of the largest value;
  ψ flips all bits.

## Result
Lemma (mod-4 two-dissection): R(q) ≡ 1 + 2T(q) (mod 4), i.e.
  G(q) ≡ G(q²)(1 + 2T(q)) (mod 4), where T(q)=Σ t(n)q^n.
Theorem 4: S(n) is even for all n ≥ 1.
Theorem 1 (odd dichotomy): for odd m ≥ 1, S(m) ≡ 2·t(m) (mod 4).
Theorem 2 (square criterion): for odd m, S(m) ≡ 2 (mod 4) iff
  m/3^{v_3(m)} is a perfect square, else S(m) ≡ 0 (mod 4).
Corollary 3: (a) S(p) ≡ 0 (mod 4) for every prime p ≠ 3
  (odd primes via t(p)=2; S(2)=4); (b) S(3^a) ≡ 2 (mod 4) for all a ≥ 0;
  (c) S(2m) ≡ 0 (mod 4) for every odd m (i.e. S(4n+2) ≡ 0).
  Non-closure: S(4)=10 ≡ 2, S(12)=198 ≡ 2 (mod 4); no 2^k induction.
Witness: φ₁ is a fixed-point-free involution giving exact 2-split
  (S(m)/2, S(m)/2) for every m (proof of Theorem 4). On non-rectangular
  overpartitions (≥2 distinct values) every V₄=⟨φ₁,ψ⟩ orbit has size
  exactly 4 (proved). For odd m, rectangles (single value) number exactly
  2·t(m), so S(m) = 4k + 2t(m) bijectively (independent proof of Theorem 1).
  E.g. m=9: (37,37) rect 2; m=25: (2973,2973) rect 6.
First values: S=1,2,4,6,10,16,24,36,52,74,104,… (n=0,…).

## Proof / evidence
Lemma: (1+x)/(1−x)=1+2x/(1−x); expanding prod(1+a_m) with
  a_m=2q^m/(1−q^m), every ≥2-factor product carries 4; valid as formal
  series (degree N uses only m ≤ N). Theorem 1: for odd m,
  S(m) ≡ R(m)+Σ_{k≥1}S(k)R(m−2k); each summand is even·even ≡ 0 mod 4
  (m−2k odd ≥1 in range gives R=2t even; S(k) even for k≥1). Theorem 2:
  for odd m, t(m) is the divisor count of the 3-free odd part, odd iff
  square. Corollary: S(2n) ≡ S(n)+2t(2n) from G=G(q²)R (k=n term plus
  even·even rest); S(2m) ≡ 0 for odd m by 0+0/2+2 cases; t(2n)=t(n).
  Machine corroboration (exact integer arithmetic, N=120): all identities
  coefficient-by-coefficient; witness assertion-checked for odd m ≤ 25.

## Limitations
- The subcase S(4n+2) ≡ 0 coincides with Sang–Shi (4.33) for S_{6,3};
  acknowledged overlap. Novelty is the unified lemma, full odd square
  criterion, prime family, and V₄ witness.
- No equal 3- or 4-way crank split is claimed (abandoned plan dropped).
- N=120 computation corroborates; proofs are all-n formal series.
- Object identification Qbar_{3,1}=Abar_{3,3,1} cited from Sang–Shi.

## Reproducibility
stdlib-only: `python3 output/artifacts/series.py`,
  `python3 output/artifacts/crank.py`. Replays: mod-2, R=1+2T mod 4,
  G=G(q²)R mod 4, odd dichotomy, even lift, square criterion, prime and
  doubling checks to N=120; witness 2-splits and V₄ size-4 assertions.

## References
- Sang–Shi arXiv:1712.08930 (mod-4 RRG dissections; object identification).
- Chen–Hirschhorn–Sellers arXiv:1405.3626 (infinite mod-3 family).
- Hirschhorn–Sellers overpartition 2/3/4-dissections (via Sang–Shi).
- Andrews singular overpartitions; Bringmann–Lovejoy–Osburn / Garvan
  rank/crank/spt programs (distinct objects, no k=3 singular witness).
