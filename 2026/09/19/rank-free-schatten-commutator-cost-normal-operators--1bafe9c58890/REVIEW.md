# Review: rank-free mixed Schatten commutator cost

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the level of each operator-ideal step.

The lower bound follows directly from Schatten Hölder and the triangle inequality: if 1/r=1/p+1/q, then AB and BA lie in S_r and ||[A,B]||_r is at most 2||A||_p||B||_q.

For the upper bound, normality is used essentially. Writing T=U|T| and setting X=U|T|^{r/p}, Y=|T|^{r/q} gives XY=YX=T because the polar part commutes with |T|. The exponents satisfy (r/p)p=(r/q)q=r, so ||X||_p||Y||_q=||T||_r exactly. Tensoring X,Y with any S_p,S_q factorization of a rank-one projection P yields [X tensor C, Y tensor Z]=T tensor P and multiplies the Schatten norms. A finite-rank normal operator on an infinite-dimensional Hilbert space, and more generally a normal compact operator with infinite-dimensional kernel, is unitarily equivalent to T tensor P because the nonzero spectral multiplicities are unchanged and both zero eigenspaces are infinite-dimensional. Thus the upper estimate is valid.

The exact positive finite-rank threshold uses a separate classical fact: Brown's theorem excludes nonzero-trace finite-rank commutators [S_p,S_q] when 1/p+1/q is at least 1/2, while Anderson gives the converse existence on the strict side. Since a nonzero positive finite-rank operator has positive trace, the obstruction applies exactly where stated.

No step uses an unverified complementability or inheritance assertion. Compactness and ideal membership are explicit from Schatten membership. The extension to infinite-rank compact normal targets is deliberately restricted to infinite-dimensional kernel, which is exactly what the tensor-unitary-equivalence argument needs.

## Originality

The novelty claim was stress-tested against several nearby literatures and formulations.

- Anderson (1977) and Brown (1994), as summarized explicitly in Dykema--Figiel--Weiss--Wodzicki (2004, Remark 7.12), already determine when a nonzero-trace finite-rank operator can occur in [S_p,S_q]. This threshold is treated as prior art, not as a new theorem.
- Dykema--Figiel--Weiss--Wodzicki develop the much broader commutator structure of operator ideals and include Anderson-type tensor constructions. The claimed contribution is therefore not ideal membership itself, but the quantitative mixed factor-norm gauge and its rank-free identification with the target S_r norm on normal operators.
- Loreaux--Patnaik--Petrovic--Weiss study modern refinements and limitations of Anderson's approach and record Schatten-class obstructions, but the inspected material did not state this mixed infimum-product norm estimate.
- Tran's 2026 result defines and controls an operator-norm commutator cost for finite matrices. Liu's 2026 result gives an operator-norm factor bound for compact targets and a finite-rank tensorization mechanism. Neither inspected paper states a mixed Schatten factorization cost comparable to an S_r target norm.
- Targeted searches for “mixed Schatten commutator”, “commutator factorization Schatten norm”, “Schatten commutator cost”, and infimum/product-norm formulations did not locate the theorem above. Results with similar words concerned norms of a prescribed commutator [M_b,T], Böttcher--Wenzel-type estimates, or commutators as bounded operators on the Banach space S_p, which are different questions.

The principal residual risk is older operator-ideal literature: an equivalent quantitative norm estimate could exist under different notation. Salinas's 1974 *Ideals of commutators of compact operators* was inspected as a particularly nearby source; its stated results concern ideal membership, commutator spans/closures, and Schatten ideals, and no mixed infimum-product factorization gauge was located in the inspected text. The 2004 Dykema--Figiel--Weiss--Wodzicki primary source and modern Anderson-related work were also inspected around the relevant single-commutator/Schatten statements.

One older paper remains a specific access uncertainty: J. H. Anderson, *Commutators in ideals of trace class operators II*, Indiana Univ. Math. J. 35 (1986), 373--378, MR 833400, Zbl 0602.47033. Its bibliographic record and later citations were inspected, but the full article text was not successfully inspected. It is scientifically relevant because it treats commutators inside trace-class ideals and is therefore a plausible place for a differently formulated quantitative observation. No evidence of actual coverage was found; this is a residual risk rather than evidence that the present estimate is known. Accordingly the originality claim is only to the best of our knowledge.

## Value

The result gives a quantitative strengthening of a classical existence threshold in a natural regime. It identifies the correct target norm, S_r with 1/r=1/p+1/q, and shows that for normal finite-rank targets the factorization cost has no hidden dependence on rank or spectral spread. The proof also isolates a reusable tensor-transfer mechanism: a universal rank-one commutator can transport any commuting Schatten factorization of the target.

The positive-target corollary makes the Brown--Anderson hyperbola an actual phase transition for a normed factorization problem rather than only an existence boundary. This connects directly to the current dimension-free commutator-cost literature while retaining genuinely operator-ideal information.

## Limitations

No sharp value of the constant c_{p,q}=Gamma_{p,q}(P) is obtained. No claim is made for injective infinite-rank compact normal targets, because tensoring with a rank-one projection changes kernel multiplicity. No exact threshold is claimed for trace-zero finite-rank targets. The result is a quantitative refinement in a structured class, not a replacement for the general commutator-ideal classification.
