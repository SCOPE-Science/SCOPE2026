# Scientific review: Five minimal-fort orbits and eleven minimum-zero-forcing orbits of \(Q_4\)

## Correctness (PASS)
For the precisely labelled 4-cube, prove the fort duality, all-subset recurrence, upward-closure of forcing, and complete automorphism description. The fort algorithm checks each of 65536 masks (348 minimal forts: 28,32,288) while a separate direct synchronous forcing algorithm independently checks each mask (2360 minimal zero forcing sets, all size eight), and a third verifier checks all 65536 Boolean decisions for exact equality. The explicit five and eleven group-orbit representatives are tested against all 384 automorphisms and exhaust their respective sets. This is an exhaustive finite proof with standalone checked programs; it is not extrapolated to Q_d for other d.

The fort predicate checks all neighbors outside each candidate set. Its all-proper-subset recurrence is necessary because fortness is not inclusion-monotone. The direct black-coloring checker and the independent fort-complement checker agree on **every one of 65536 cases**; all group images and sizes are checked from explicit generators. The proof is finite and exact, and no claim is made beyond \(Q_4\).

## Originality (PASS; priority risk remains)
The retained claim is orbit-resolved structural classification, not the known scalar Z(Q4)=8 or known total 348 minimal forts. The 2025 closest full text explicitly states 348 in the conclusion but does not supply the two new orbit tables or well-forcedness, and states complete enumeration of minimum zero forcing sets remains unresolved. The 2023 thesis contains an exact probability plot for 16-vertex cube, mathematically encoding the polynomial, which is fully acknowledged rather than ignored. The novel conjunction of five and eleven orbit decompositions and well-forcedness is not implied by those covered scalar/probability results, nor by the 2018 zero-forcing polynomial framework. An unindexed source or dataset may still supersede the structural classification.

Closest inspected primary full texts: AIM's foundational paper (doi:10.1016/j.laa.2007.10.009); Boyer et al. (arXiv:1801.08910); Becker et al. (arXiv:2404.05963); Brimkov–Cameron–Grubbs (arXiv:2507.10826); and Lawrence's 2023 thesis (Chapter 5). **The total \(348\) minimal forts is not original**, nor is the zero-forcing number \(8\). A published exact probability graph also implicitly represents the polynomial. The new finding is the complete **five- and eleven-orbit structure and well-forcedness** with exact certificates. Earlier unindexed supplementary computations may exist.

## Value (PASS)
The four-cube is the exceptional hypercube with two types of minimum forts and is explicitly the small open complete-structure test case in the 2025 primary paper. Resolving all five minimal-fort and eleven minimum-forcing orbits, including 288 large minimal forts, the uniform size-eight inclusion-minimality and propagation profile gives a natural complete classification rather than a gratuitous slice or only a recomputed aggregate. The five orbit generators form a compact exact obstruction certificate, useful for future hypercube and fort-transversal questions without asserting a downstream theorem.

## Limitations and inspection
The result is not a dimension-independent hypercube classification. Exhaustive finite verification and this assessment are not a substitute for an independently conducted mathematical audit or historical-priority check. Reproduce with the three standalone programs and compare `CLASSIFICATION.json`.

Self-review: passed. Independent audit: not yet performed.
