# Scientific review: Boolean signed-chain incenter locus

## Correctness — PASS

Each signed chain inequality has a \(0/1\) normal with squared norm equal to its length. Full chains give the sharp inradius and force their coordinate sums to vanish at every optimal center. Adjacent exchanges of maximal Boolean chains propagate equality across each rank via connected Johnson graphs. Removing a single rank forces the coordinate cap. Conversely the convexity inequality \(m(1-\sqrt{1/h})\le1-\sqrt{1-m/h}\) with the complementary-rank sum proves feasibility for **all** shorter chains. Box-section vertex formulas follow by counting independently saturated inequalities. The exact rational matrix-rank and finite-chain slack checks support, but do not substitute for, the all-dimensional proof.

## Originality — PASS

The public thesis of Hlavacek (2023), Chapter 5.6, and Beck–Hlavacek (2023), Section 6, define and investigate the two-sided signed-chain model but do not provide the Boolean Euclidean incenter locus. The original Stanley chain body is one-sided and nonnegative; the enriched chain body uses absolute coordinate values inside every chain constraint. Even where a known enriched-chain inradius formula implies the same numeric radius via containment, its **unique** Boolean incenter cannot imply the present entire positive-dimensional locus. Comparisons include the exact central-section formulation, possible enriched-chain containment, and broader poset theory rather than title matching. Remaining risk: another specialized Euclidean study, not identified in inspected sources, may contain an equivalent result.

## Value — PASS

This is a complete, natural family classification: the nonunique incenter locus has dimension \(d\) inside ambient dimension \(2^d\), admits explicit equations, and has parity-dependent vertex counts. The sharp higher-dimensional nonuniqueness contrasts with the enriched and ordinary chain polytope models on the same canonical Boolean poset. The claim is a structural Euclidean invariant of an established lattice-polytope construction rather than a recomputation of published combinatorial or Ehrhart data.

## Closest literature and limitations

Hlavacek's dissertation (2023-08-01) precedes the related Beck–Hlavacek arXiv version (2023-11-08); Chapter 5 and Section 6, respectively, provide the exact comparison definitions. Stanley's 1986 model is the nonnegative one-sided analogue. The result uses the standard orthonormal coordinates, and does not classify other signed posets. The verifier only covers finite dimensions; arbitrary dimension is proved symbolically.

Same-model review: passed. Independent audit: not yet performed.
