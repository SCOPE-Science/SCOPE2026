# Scientific review

## Correctness — PASS

The quantified statement covers all positive real edge lengths and every graph point, including edge interiors and endpoints. The proof uses a standard degree-four principal-divisor criterion, justified by uniqueness of the real harmonic potential and integrality of all slopes, and eliminates each of the six edge types explicitly. The five unaffected unit-edge cases have unavoidable noninteger slopes \(1-t\), \(1+t\), or \(-t\). The variable-edge solution is controlled by a single necessary and sufficient integer \(k\in\{-1,0\}\); the endpoint tests are treated separately. An exact rational-Laplacian checker independently cross-checks rational instances but is not used to establish universal quantification. The definitions, range \(\lambda>0\), denominator \(\lambda+1\), and the distinction between \(K\sim4p\) and weaker Weierstrass conditions have been checked.

## Originality — PASS (best-knowledge primary-source comparison)

The closest 2023 paper, Amini–Gierczak–Richman, computes the equilateral \(K_4\) canonical Weierstrass locus (Example 3.5), not an asymmetric one-edge deformation. Amini–Kawaguchi (2026) supplies the general equivalence of the gap sequence \((1,2,5)\) with \(K\sim4p\) and component-level results, but not a location formula on this specific family. Chan–Jiradilok (2015) treats theta-characteristic **classes** on general \(K_4\) metric graphs, not the complete locus of individual points whose twice-double is canonical. Those results are compatible but none supplies the asymmetric threshold or exact interior-point positions as a stated or direct corollary. Semantic database searches covered metric tetrahedra, tropical hyperflex/subcanonical aliases, canonical divisors, and one-edge deformations; returned closest items concern different graphs, invariants or metrics, as detailed in `AUDIT.json`. Selected published mathematical claims were also compared by their implications.

**Residual risk:** Any literature search can miss an earlier specific classification or an unpublished calculation. No independence or comprehensive uniqueness guarantee is asserted. In particular, a general chip-firing algorithm can compute this example but does not by itself state its parameter phase diagram.

## Value — PASS

The equilateral tetrahedron is a canonical worked example in the tropical Weierstrass literature. Changing a single edge is the minimal metric deformation retaining most of its symmetry, and subcanonical points encode the exceptional genus-three gap sequence \((1,2,5)\). The result is a *complete continuum-parameter classification* with a sharp threshold and explicit migration of two points from vertices to edge interiors. It distinguishes shortening from lengthening and resolves a natural stability question not determined by the symmetric example or global weight counts. This exact boundary phenomenon is independently useful even without a downstream lifting theorem. The calculation is more than an arbitrary finite sample or a routine substitution into a known table.

## Limits and evidence

The claim does not classify all canonical Weierstrass points, algebraic lifts or six-parameter metric tetrahedra. Reproduction uses `verify.py` (Python standard library, exact fractions); the proof rather than the sampled checker is decisive for the all-real claim.

Self-review: passed. Independent audit: not yet performed.
