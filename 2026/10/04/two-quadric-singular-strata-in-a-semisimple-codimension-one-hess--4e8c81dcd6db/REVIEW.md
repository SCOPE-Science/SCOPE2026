# Same-model review

## Correctness
PASS. The flag condition, projection to line--hyperplane incidence, singularity criterion for the two bilinear equations, and fiber reconstruction were re-derived directly. The local eigenbasis chart reduces the germ to \(\mathbb A^2\times\{py+qz=0\}\), and `artifacts/verify.py` independently replays the local symbolic identities and the published patch normal form. The proof is global for this exact variety; the finite symbolic checks are not used to infer untested cases.

## Originality
PASS. The closest exact source, Insko--Precup Example 5.5, supplies the benchmark variety, one patch polynomial, and eight singular torus-fixed points but not its full singular locus. Escobar--Precup--Shareshian later prove only a containment for general semisimple codimension-one singular loci, with equality for nilpotent operators. Exact-object, alias, determinantal-cone, quadric-stratum, and ordinary-double-point searches found no prior statement of the two \(\mathbb P^1\times\mathbb P^1\) components or uniform transversal. The inaccessible full text of Cummings's 2024 thesis is retained as a literature risk because its accessible abstract concerns semisimple patch radicality.

## Value
PASS. This is a complete singular-stratum and local-type classification for a published irreducible singular semisimple Hessenberg benchmark. It explains the previously reported eight singular torus-fixed points, distinguishes the semisimple case from the equality theorem available for nilpotent codimension-one varieties, and gives normality as a geometric consequence.

## Closest literature and limitations
The result is specific to \(S=\operatorname{diag}(1,1,-1,-1)\) and \(h=(3,4,4,4)\). No generalization to other spectra or Hessenberg functions is claimed, and no resolution is constructed. The full Cummings thesis was unavailable, so an equivalent special-case computation under different terminology cannot be ruled out completely.

Same-model review: passed. Independent audit: not yet performed.
