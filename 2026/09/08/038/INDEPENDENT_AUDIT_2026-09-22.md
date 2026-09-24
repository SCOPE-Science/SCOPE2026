# Independent audit — Hurwitz-space connectedness for PSL(2,7)

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/038`  
**Audited directory tree:** `cb92cf3b14275cd4bbd0bb5f6bb9fcad3072d4f0` (unchanged when checked at repository head `c40ff4843745efb8c2c7275f5cacbda243c36a25`)  
**Review type:** separate AI independent audit.

## Claim audited

For `G = PSL(2,7)` and the ordered product-one generating Nielsen class whose class multiset is `(2A,3A,7A,7A)`, the record claims 48,384 tuples (4,032 in each of 12 class-position patterns), a single full braid orbit, a free simultaneous-conjugation quotient of size 288 with one braid orbit, hence connectedness of the reduced Hurwitz space; it also gives cover genus 3 and reports that a canonical-section SL(2,7) lift sign is not braid-invariant.

## Correctness — PASS

I reconstructed the finite group from `SL(2,7)/{±I}`, obtaining 168 elements and conjugacy classes of sizes/orders `1/1, 21/2, 56/3, 42/4, 24/7, 24/7`. Selecting `7A` as the class of `[[1,1],[0,1]]`, independent product-one enumeration gives exactly 4,032 tuples in each of the 12 distinct class-position patterns, hence 48,384 total.

Generation is automatic: a proper maximal subgroup containing elements of order 7 is of type 7:3 and has no involutions, while the other maximal type S4 has no element of order 7. Since every tuple contains both an involution and an element of order 7, it cannot lie in a proper maximal subgroup.

An independently implemented Hurwitz-generator BFS, with inverse moves and closure checks, reaches all 48,384 tuples from one seed, so the full braid action is transitive. Because the tuples generate the centerless group PSL(2,7), their simultaneous-conjugation stabilizer is the center, hence trivial; therefore the inner quotient has `48384/168 = 288` elements, and transitivity descends to one reduced orbit. The degree-7 action has cycle types `2A: 2^2 1^3`, `3A: 3^2 1`, `7A: 7`; Riemann–Hurwitz gives ramification defect `2+4+6+6=18`, so `2g-2=-14+18=4` and `g=3`. The canonical-section lift-sign census independently reproduces 24,120 positive and 24,264 negative signs, and an explicit braid move changes the sign, confirming it is not an invariant.

## Originality — PASS, qualified to checked literature

Searches used both the record's terminology and standard equivalents: exact class tuple `(2A,3A,7A,7A)`, `PSL(2,7)`/`L3(2)`, Nielsen classes, braid orbits, four-point Hurwitz spaces, and degree-7 monodromy. I checked:
- M. D. Fried, arXiv:1803.10728, which develops Nielsen classes, braid actions and reduced Hurwitz spaces for general `(G,C)` and discusses the r=4 framework, but does not tabulate this class;
- B. Seguin, arXiv:2409.18246 / *Israel J. Math.* (published 2025), which concerns asymptotic growth of component counts as the number of branch points grows, not this finite four-point orbit census;
- H. M. Mohammed Salih, arXiv:2001.02295 / *J. Algebra* (2020), which treats affine primitive genus-one systems, a different group family;
- P. M. Khudhur, “Complete Classification of Degree 7 for Genus 1,” *Iraqi J. Sci.* 62(2) (2021), DOI `10.24996/ijs.2021.62.2.25`, whose L(3,2) tables cover genus-one degree-7 ramification types but not the present genus-3 `(2A,3A,7A,7A)` type.

To the best of my knowledge from these sources and targeted searches, I found no established equivalent or table giving this exact 48,384/288 one-orbit census. This is a priority assessment relative to inspected evidence, not a guarantee of exhaustive literature coverage.

## Scientific value — PASS

Connectedness is a genuine global braid-orbit invariant of a natural four-point Nielsen class and is not implied by the classical three-point `(2,3,7)` generation of PSL(2,7). The exact raw and reduced class sizes, one-orbit certificate, and genus calculation give reusable data for Hurwitz-space/component computations. The result therefore survives after subtracting the general framework and nearby classification literature.

## Disposition

**PASSED.** Correctness, originality relative to checked literature, and scientific value all pass. No repair is required.

## Access notes

All decisive comparison sources above were available through lawful open-access/arXiv routes. No Oxford institutional fallback was needed, and no inaccessible source was used to support a positive originality claim.
