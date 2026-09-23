# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-011  
**Source path:** `2026/09/07/011`  
**Audited repository state:** `1182b71328a408a740c274616869ab885009b620`  
**RESULT.md blob:** `08709a426497fde409cd196564442cc362dcaf6f`  
**representatives.json blob:** `7a0a0551c1e40762ad63b07e8b9e2ca2238b3895`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent-audit pass; no Lean or expert attestation is claimed.

## Claim audited

The record claims at least five PGL3(F4)-conjugacy classes of degree-4 plane Cremona maps over F4: four symmetric maps of type `(4;2^3,1^3)` and one de Jonquieres map of type `(4;3,1^6)`, with explicit quartic inverses and certificates.

## Correctness — PASS

I independently reconstructed GF(4) arithmetic as `F2[t]/(t^2+t+1)` and parsed the five F/G coefficient triples from `artifacts/representatives.json`. A fresh sparse-polynomial composition check, not the record's replay code, verified for S1, S2, S3, S4 and DJ that both `G∘F` and `F∘G` satisfy the two projective identity cross-products identically over GF(4). The nonzero first composition coordinates had respectively 8, 7, 8, 4 and 32 monomials, matching the published cofactor-support counts on the G(F) side. Thus each displayed F has the displayed G as a rational inverse.

I also independently enumerated the 54-element monomial stabilizer of the three coordinate double points. Its action on the 84 three-subsets of the nine off-coordinate-line F4-points has exactly five orbits, of sizes 3, 9, 18, 27 and 27. The S1–S4 single-point triples fall in four different orbits; the fifth representative `{(1,1,1),(1,1,w),(1,1,w^2)}` is the collinear/fixed-line configuration identified in the record. The DJ representative has a unique triple base point, so it cannot be conjugate to the four symmetric representatives. These checks establish the stated lower bound of five distinct conjugacy classes. The record correctly limits itself to a lower bound, not a full quartic census.

## Originality — PASS, qualified

Searches used standard and equivalent terminology: `plane Cremona degree 4 F4`, `quartic birational transformations finite field`, `homaloidal type (4;2^3,1^3) finite field`, `de Jonquieres F4 quartic`, and the finite-field Cremona literature cited in the record. Closest sources located were general homaloidal/Cremona classifications over algebraically closed fields and finite-field generation/parity papers (including Schneider, arXiv:2008.07991, and Asgarli–Lai–Nakahara–Zimmermann, arXiv:1910.05302). I found no source giving these explicit F4 quartic representatives, their Galois-orbit base configurations, or composition-inverse certificates. This is a priority assessment relative to the searched literature, not a guarantee of absolute first publication.

## Scientific value — PASS

The surviving contribution is concrete rather than merely a restatement of a general theorem: explicit small-field birational maps with exact inverses, base-orbit data and conjugacy separation. These are reusable as finite-geometry examples and as exact regression instances for Cremona/birational software. The record does not overclaim a complete classification; the explicit lower-bound representatives retain value even if a later full census is produced.

## Repairs / limitations

No mathematical repair was required. The principal limitation remains the one already stated in RESULT.md: non-rational double orbits, F64 single orbits and infinitely-near configurations are not exhausted, so the evidence supports `at least five`, not a total count.

## Final disposition

**PASSED.** Correctness, originality relative to checked literature, and scientific value all survive independent scrutiny.