# Scientific review: Unlabeled projection-width laws determine every isosceles trapezoid

## Correctness — PASS
For every nondegenerate isosceles trapezoid, vertex projections yield two cosine branches. The exact change-of-variables density and its two regimes have a complete proof in RESULT.md. Interior versus endpoint stationary points contribute distinct normalized pole coefficients; the remaining recovery cases follow from the support minimum, its finite right density, and subtraction of two known radical branches. The case of equal bases is handled separately. Thirteen representative phase-boundary and interior cases passed a deterministic standard-library numerical checker, including an independently evaluated angular-preimage CDF. The analytic proof, not the checker, establishes the all-parameter theorem.

## Originality — PASS (provisional historical priority)
Akiyama and Kamae, *Width deviation of convex polygons* (arXiv:2201.06736, 2022), is the closest same-observable paper inspected. Its general edge decomposition, moment identities, and local triangle truncation findings are expressly prior. The present contribution is a global **inverse** classification of all positive-height isosceles trapezoids from the full direction-unlabeled width law, including the boundary phase cases. Martirosyan's *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral* (DOI:10.3103/S1068362323060055, 2023) uses different data, with a randomized offset conditional on each direction. Indexed published inverse results for triangles and parallelograms do not, on their stated claims, cover proper unequal-base trapezoids; only their rectangle boundary case is prior-covered. Related abstracts were available without full manuscript access, and historic equivalent derivations remain possible. No absolute priority is claimed.

## Mathematical value — PASS
The full inverse theorem is a natural complete classification, not an arbitrary slice: it recovers all three metric parameters from an unlabeled random projection and distinguishes every regime, including coincident poles and a finite-jump hidden beneath another singularity. It provides exact observable signatures for an asymmetrical convex polygon family and separates this measurement from directional chord tomography. No general quadrilateral theorem or statistical noise guarantee is claimed.

## Limits and evidence
Reproducibility: `python3 check.py` from the embedded package. Source evidence: arXiv:2201.06736, especially the width decomposition and §§6–7; Martirosyan's 2023 open-access full text; published indexed abstracts of related triangle/parallelogram inverse results. The script verifies finite representative configurations, not a symbolic quantifier over all parameters. The global proof is supplied separately, and independent mathematical validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
