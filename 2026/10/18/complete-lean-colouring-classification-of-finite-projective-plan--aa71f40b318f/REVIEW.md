# Scientific review: complete lean-colouring classification of finite projective planes

## Correctness — PASS

The new theorem is proved directly from projective-plane incidence axioms. The proof separately rules out two monochromatic lines, classifies colourings with zero or exactly one monochromatic line, constructs both families, and derives the exact falling-factorial palette count by disjoint cases. The degree comparison uses incidence degree \(q+1\), not the degree \(q^2+q\) of the two-section graph. The attached Python verifier independently reconstructs small prime-field planes, checks their axioms, checks all claimed constructive witnesses in four orders, and enumerates every set partition of the Fano plane's seven points. All these new checks passed. They are corroborative, not a substitute for the unbounded proof.

## Originality — PASS, with specified priority risk

The 2026 initiating paper [1] was compared in its full accessible HTML sections defining lean colourings, connected-uniform bounds, wide-path and \(r\)-complete results, and two-section and degree bounds. Its valid general theorems do not imply the claimed value or full colouring classification for projective planes: distinct lines intersect once, and noncollinear triples prevent \(r\)-completeness. The incidence-degree bound asserted in its Corollary 4.3.1 is contradicted, with the invalid degree identification visible in its proof. The 2020/2021 rainbow-free projective-plane study [2] was inspected in full text and asks for opposite line constraints, so its chromatic objective and results do not cover the lean spectrum. Search comparisons also considered Fano-plane line colourings, mixed hypergraph colourings, and published mathematical research records; none yielded a statement implying this exact classification. Residual risk: an equivalent elementary fact under a less searchable name may exist.

## Value — PASS

Finite projective planes are canonical symmetric block designs. Their exact lean chromatic spectrum is an intrinsically motivated invariant of the new colouring concept, not an arbitrary parameter slice. The two-point spectrum with \(q-1\) missing feasible colour counts is a sharp structural phenomenon; the formula enumerates every colouring over any named palette. The family also pinpoints an unbounded failure of a recently proposed incidence-degree upper bound and distinguishes incidence degree from two-section degree. The infinite result holds even without Desarguesian assumptions.

## Closest work and limits

[1] H. J. Piehowski, *The Lean Number of a Hypergraph*, arXiv:2607.14015 (July 15, 2026), especially sections 1, 3, 4. [2] Z. L. Blázsik et al., *On the balanced upper chromatic number of finite projective planes* (2020 preprint / 2021 publication). These are distinct constraints as explained above. The independent audit remains unperformed. An unindexed equivalent classification cannot be excluded by negative searches alone.

Self-review: passed. Independent audit: not yet performed.
