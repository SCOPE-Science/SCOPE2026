# Scientific review: Eckardt-point wall crossing in Hesse-split cubic threefolds

## Correctness
**PASS.** The proof applies the polar-rank criterion for a smooth cubic threefold [1, Lemma 3.14], gives an exact identity for the ternary Hessian determinant, and exhausts the four mutually exclusive support cases for the last two coordinates. For a nonzero ternary triple the Hessian has rank at least one; rank one is restricted to three base points, occurring only when the Hesse parameter is zero or has cube 216. Each yields exactly six extra points. The smoothness boundary and classical Hesse formula identify precisely the equianharmonic modulus. Exact symbolic computations in `verify_hesse.py` independently check critical identities and representative configurations. No finite computation is used as proof of a universal quantifier.

## Originality
**PASS, with residual bibliographic risk.** The main related paper [1] supplies a rank criterion, counts 30 points for the Fermat threefold, and gives one 12-point non-Fermat Hesse example in Table 2. Those statements **do not imply** the count for every smooth plane-cubic parameter nor the precise modular jump. The full text of [2] gives the classical Hesse invariant of plane cubics, not Eckardt counts of the associated threefolds. The full text of [3] treats the Fermat endpoint and general finite-configuration results, not this complete non-Fermat family. No mathematically covering family theorem was identified in additional targeted searches; unlocated older or equivalent literature remains possible.

## Value
**PASS.** This is an exact, intrinsic classification for a natural full one-dimensional complex moduli family of split cubic threefolds. It identifies why a stable 12-point star locus acquires exactly 18 new points at the exceptional elliptic modulus and recovers the sharp 30-point case. The explanation distinguishes geometric flex lifts from the rank-one Hessian contribution, rather than merely reproducing the two known numerical examples.

## Scope and residual risks
The theorem concerns distinct geometric Eckardt points only. It does not classify arbitrary cubic threefolds, scheme multiplicities, or the singular limiting parameters. The derivation relies on the established polar-rank equivalence and Hesse modular-invariant formula, both cited at their exact locations. Comprehensive historical bibliographic completeness and independent validation are not claimed.

Self-review: passed. Independent audit: not yet performed.

## References
[1] Bockondas–Bossoto, *Eckardt points on a cubic threefold*, arXiv:2309.08124, Lemma 3.14, Example 4.1 and Table 2.
[2] Bonifant–Milnor, *On Real and Complex Cubic Curves*, arXiv:1603.09018, equation (14).
[3] Cools–Coppens, *Star points on smooth hypersurfaces*, arXiv:0903.2005, Example 2.13.
