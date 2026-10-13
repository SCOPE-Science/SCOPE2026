# Scientific review of the double-star transfer classification

## Correctness — PASS

The proof starts from the actual normalized-Laplacian matrix, not the combinatorial Laplacian. The four-dimensional Jacobi quotient has exact spectrum \(\{0,1-c,1+c,2\}\) with \(c^2=pq/((p+1)(q+1))\); the remaining leaf-difference space has eigenvalue one. The positive stationary eigenvector forces equal degrees and fixes the transfer phase. Projector comparisons exclude all pairs except same-hub twins at a size-two pendant group and balanced hub pairs; the latter fail a two-phase power identity. For size-two twins, nonzero quotient spectral weights reduce PGST to simultaneous odd-phase approximation for \(t\) and \(ct\). Irrational rotations give the positive cases, while rationality of \(c\) is equivalent to a Pell equation whose even/odd parity excludes PGST as well as PST. The all-parameter proof is self-contained modulo the classical Pell solution description and irrational-circle rotation density. The exact-rational and numerical code checks cover representative cases only.

## Originality — PASS, with residual risk

Coutinho–Baptista (arXiv:2209.04668, Sections 3–5) explicitly leave the normalized-Laplacian tree PST question open and give general necessary spectral criteria, not this exhaustive bistar family and arithmetic PGST classification. Kirkland–Monterde–Plosker (arXiv:2201.02720, Sections 5–6) furnish general transfer tests for weighted-graph twins; weighted adjacency could instantiate the present normalized operator but their inspected explicit applications treat double cones rather than double stars. Fan–Godsil (arXiv:1206.0082) classify adjacency, not normalized-Laplacian, double-star transfer. The verified novelty being assessed is the combined family-wide explicit parameter criterion, Pell exclusions and all-pair classification, not the background spectral transfer criterion. Residual risk is an unlocated prior specialized application, or a published broader theorem whose explicit conclusion already includes this Pell classification; absence from a search alone is not proof of novelty.

## Value — PASS

The 2022 normalized-Laplacian study motivates classifying PST on minimally connected quantum networks. A diameter-three tree family is a natural infinite test case: this finding closes its finite-time question and determines which quantum-communication links can achieve arbitrarily high fidelity. The infinite Pell obstruction makes the answer structurally nonroutine: adding leaves can alternate between enabling and prohibiting PGST in a precise arithmetic pattern. Neither programmatic reproducibility nor correctness alone is offered as its mathematical significance.

## Limitations and comparison

No claim concerns general trees or finite-time cost bounds. The similarity with known weighted-twin formalism remains a recognized originality risk. Independent scientific validation is absent.

Self-review: passed. Independent audit: not yet performed.
