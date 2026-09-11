# Certified random two-generation probability interval for HN

## Context

Random (2-)generation probability is the core Liebeck–Shalev benchmark for
finite simple groups. For the Harada–Norton sporadic simple group HN, no
rigorous published interval for the uniform random-pair generation
probability was available — only heuristics and general asymptotic
machinery.

## Definitions

Let G = HN, |G| = 273030912000000 = 2^14 · 3^6 · 5^6 · 7 · 11 · 19.
Let P2(HN) be the probability that a uniformly random ordered pair
(x, y) in G × G generates G. Write Q = 1 − P2(HN).

## Result

With exact rational endpoints

- L = 4266101020747/4266108000000 ≈ 0.999998364023,
- U = 1299599999999/1299600000000 ≈ 0.999999999999,

P2(HN) ∈ [L, U].

In outward-rounded decimals, P2(HN) ∈ [0.999998364, 1.000000000],
of width ≈ 1.64e−06 < 0.05, with lower endpoint > 0.85.

## Proof / evidence

Maximal ledger (ATLAS v3, HN page; Wilson et al.): 14 conjugacy classes
of maximal subgroups with (order, index m = [G:H]):

A12 (239500800, 1140000); 2.HS.2 (177408000, 1539000);
U3(8):3 (16547328, 16500000); 2^1+8.(A5×A5).2 (3686400, 74064375);
(D10×U3(5)).2 (2520000, 108345600); 5^1+4.2^1+4.5.4 (2000000, 136515456);
2^6.U4(2) (1658880, 164587500); (A6×A6).D8 (1036800, 263340000);
2^3+2+6.(3×L3(2)) (1032192, 264515625); 5^2+1+2.4.A5 (750000, 364041216);
M12:2 (190080, 1436400000) twice (two distinct G-classes);
3^4:2.(A4×A4).4 (93312, 2926000000); 3^1+4:4.A5 (58320, 4681600000).

Every non-generating pair lies in some maximal subgroup. For class i
with index m_i and n_i conjugates, n_i = [G : N_G(H_i)] ≤ [G : H_i] = m_i,
and a fixed conjugate contains a random pair with probability 1/m_i^2.
Union bound: Q ≤ Σ_i n_i/m_i^2 ≤ Σ_i 1/m_i =: S, where exactly
S = 6979253/4266108000000 ≈ 1.6359766e−06. Hence P2(HN) ≥ 1 − S = L.

Fixing one A12 conjugate (m_1 = 1140000), pairs inside it never generate,
so Q ≥ 1/m_1^2 and P2(HN) ≤ 1 − 1/m_1^2 = U. Width U − L = S − 1/m_1^2
≈ 1.6360e−06 < 0.05; L > 0.85. Decimals round outward (floor L, ceil U
at 1e−9).

## Limitations

The bound is deliberately crude (union over maximal conjugates, no
per-class character-theoretic refinement), so the interval is not sharp.
The decimal upper certificate 1.000000000 is the ceiling of exact
U ≈ 0.999999999999. Completeness of the 14-class maximal list is taken
from the published classification as represented by ATLAS.

## Reproducibility

Stdlib-only script checks the |HN| factorisation, every order × index =
|G|, the exact sum S, containment, width/threshold gates, and rounding
direction:

    python3 artifacts/compute_interval.py   # prints VERIFY_OK

## References

- ATLAS v3: Harada–Norton group HN. https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/HN
- T. C. Burness, M. W. Liebeck, A. Shalev, Generation and random
  generation: from simple groups to maximal subgroups, Adv. Math. 248
  (2013), 59–95. https://www.ma.imperial.ac.uk/~mwl/maxgenfinal.pdf
- M. W. Liebeck, A. Shalev, The probability of generating a finite
  simple group, Geom. Dedicata 56 (1995), 103–113.
- T. C. Burness, Simple groups, generation and probabilistic methods
  (survey).
  https://research-information.bris.ac.uk/files/167260457/2019_Simple_groups_generation_and_probabilistic_methods.pdf
