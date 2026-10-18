# Scientific review: the \(\mathbf F_4\) smooth-point theorem

## Correctness — PASS

The geometric hypothesis is a geometrically integral, normal degree-two del Pezzo surface with rational double point singularities. Uppal's residual cases over \(\mathbf F_4\) have one geometric singularity of type \(A_2\) or \(A_4\), and the cited separability criterion applies. Every rational zero of the quadratic coefficient lifts rationally. If that zero locus contains more than one point, at least one lift is smooth. Otherwise the quadratic is an anisotropic binary norm conic; the exact \(20\times30\) trace-evaluation calculation has binary rank \(19\). The explicitly described Artin--Schreier image has dimension \(11\), so it is the whole kernel. Absence of unramified rational points would force the global weighted equation to factor over an algebraic closure, contradicting geometric integrality. The finite rank is recomputed from `verify.py`, with both row and column elimination and concrete independent columns. The imported literature reduction and algebraic normality assumptions are stated rather than concealed.

## Originality — PASS, subject to residual search risk

The central source is Uppal, arXiv:2311.07317v1, Theorem 1.2 and §§9.3--9.5. Its established degree-two smooth-point theorem excludes fields of size \(2\) and \(4\); the residual \(\mathbf F_4\) cases are precisely \(A_2\) and \(A_4\). The present claim resolves those residual cases and upgrades the size exclusion to \(q=2\) alone. Tamanoi, arXiv:2101.03350v4, Theorems 1.1--1.3, addresses degree-two unirationality and gives finite-field sufficient bounds; these do not cover the claimed universal \(\mathbf F_4\) smooth-point result. Blache--Hallouin, arXiv:2301.13582v1, classifies singular del Pezzo arithmetic types in degrees \(3\) and higher, not this claim. Searches for equivalent degree-two \(\mathbf F_4\) smooth-point assertions and Artin--Schreier double-plane descriptions found no covering statement. An unindexed or more recent equivalent proof remains possible; no failure of search is treated as proof of absolute novelty.

## Value — PASS

The statement closes the only nonbinary field-size gap in a natural published point-existence theorem for singular Fano surfaces and supplies a structural mechanism that prevents a geometrically integral double plane over \(\mathbf F_4\) from having an anisotropic quadratic coefficient and no unramified rational point. This is not merely a computational count of isolated examples or an arbitrary parameter slice. It also identifies the genuine binary-field boundary, where counterexamples exist.

## Verification boundaries

The rank certificate is exhaustive finite linear algebra, not finite sampling of arbitrary surfaces. All conclusions about arbitrary surfaces follow from the algebraic kernel description plus the cited geometric reduction; no external independent validation is asserted. The original papers' theorems are used as mathematical inputs, not presented as newly proved. No claim of unirationality or classification of the counterexamples over \(\mathbf F_2\) is made.

Self-review: passed. Independent audit: not yet performed.
