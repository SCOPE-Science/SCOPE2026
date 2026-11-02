# Mathematical review: higher-leg spider deformation characters

## Correctness — PASS

For every integer \(r\ge4\) and each tuple of lengths \(a_i\ge2\), the monomial basis of the quotient is exactly \(1,x_i^s\), with \(1\le s<a_i\). Pairwise least-common-multiple syzygies generate all relations of the monomial ideal. Syzygies between a pure-power generator and a mixed quadratic force images into the subspaces \(V_i\) written in RESULT.md. Mixed-quadratic syzygies sharing one variable force images into the spaces \(W_{ij}\). Remaining pairwise syzygies vanish automatically. Thus every coefficient listed by the full torus character corresponds to an actual tangent homomorphism, not just a numerical upper bound. The standard cotangent-complex five-term sequence and the explicit derivation kernel establish the first-order abstract deformation character; its dimension is the stated specialization.

The independent verifier generates the syzygy matrices from the monomial ideal without using the claimed character, computes exact finite-field nullspaces weight by weight, and calculates the coordinate-derivation image rank. It returns VERIFY_OK in seven cases, including four and five legs. These examples corroborate, but do not prove, the all-parameter claim. No higher obstruction or smoothing dimension follows.

## Originality — PASS, with limits

Turturean (arXiv:2603.00886v1, Sections 2 and 9.4) provides a motivating family and specifically points to deformation-theoretic \(T^1\) and \(T^2\) as further questions. Hu (arXiv:2101.05236, Section 4.5.2) and Jelisiejew–Ramkumar–Sammartano (arXiv:2409.17009, Examples 5.9–5.10) already establish the three-leg tangent excess of six, which is excluded from the claimed novelty. Proposition 2.5 in the latter paper gives a general algorithm to calculate monomial tangent weights; the present work instead evaluates a complete symbolic closed character uniformly for all \(r\ge4\), and also gives the abstract \(T^1\) character by identifying coordinate-change derivations. The inspected relevant portions do not state either universal higher-leg formula. Existing general methods may imply it after nontrivial specialization; absolute literature priority is not certified.

## Value — PASS

The result answers a deformation-theoretic question posed in the motivating higher-leg spider setting and gives explicit multigraded data usable for local Hilbert-scheme and deformation-theory computations. The constant \(r\)-dependent tangent excess is structurally informative across infinitely many lengths, and the distinction between embedded and intrinsic \(T^1\) tangent characters is mathematically substantive. This is not a renaming of the previously known three-leg count or a single arbitrary numerical test.

## Risks and boundaries

The prime-field checks cannot establish formulas for all parameters; that follows from the symbolic syzygy argument. No calculation of \(\mathbb T^2\), formal deformation bases, component multiplicities or smoothability dimension is claimed. Priority could be affected by a general monomial-Hilbert tangent character formula in related literature. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
