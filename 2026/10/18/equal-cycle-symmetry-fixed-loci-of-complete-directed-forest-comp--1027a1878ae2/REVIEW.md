# Scientific review

## Correctness — PASS
The claim concerns the geometric fixed set, for which ordinary pointwise-fixed simplicial vertices would give the wrong model. Orbit barycentric coordinates give an exact homeomorphism with the simplicial orbit-face complex. Equivariant parent maps show precisely \(d\) independent phase choices per oriented arc of a quotient forest; arcs within a cycle are forbidden and quotient cycles correspond exactly to actual cycles. The pure base directed-forest complex is shellable by Kozlov's theorem. The expansion shelling is reconstructed ridge by ridge, so the fixed complex is a wedge of top-dimensional spheres. The signed rooted-forest determinant is evaluated using the eigenvalues \(0,k,\ldots,k\) of \(kI-J\), yielding the nonnegative sphere multiplicity \((kd-1)^{k-1}\) with correct parity. The attached standard-library verifier checks twelve finite cases, two by direct enumeration before passing to the quotient.

## Originality — PASS, with residual risk
The 2026 primary study proves a nonequivariant homotopy classification and identifies the canonical forest core, but does not describe fixed-point homotopy types for equal-length cycle permutations. Classical shellability and expansion results alone do not identify the fixed locus or calculate its specific number of spheres. The closest related published character formula treats a subcomplex requiring an isolated vertex and records rational traces rather than fixed-point topology. Actual mathematical and historical comparison searches found no matching fixed-space classification. Residual risks are a possibly unindexed application of the expansion theorem or an implicit discussion in historical directed-tree literature that was not fully available during review.

## Value — PASS
The result determines the full integral homotopy type of a natural, infinite family of symmetry-fixed spaces arising from a recently studied discrete-Morse model, not merely their Euler characteristics. The theorem turns a highly nonfree vertex-relabeling action on an exponentially larger forest complex into a shellable object of dimension determined by the number of permutation cycles, with an exact rank that varies nontrivially with both cycle length and count. The phase-color identification supplies a structural explanation and can inform analysis of other fixed spaces. It does not claim to classify all cycle types or full strong Morse complexes.

## Limits
No independence of validation is claimed. Finite checks supplement but do not replace the written proof. There is residual literature coverage risk, especially for older directed-tree treatments and full-text availability.

Self-review: passed. Independent audit: not yet performed.
