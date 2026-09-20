# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The proof has four independent structural checks.

First, the descended map is well defined. Generalized Dixmier averaging places \(T_M(x)\) in the norm-closed convex hull of unitary conjugates of \(x\). Every norm-closed two-sided ideal is invariant under unitary conjugation, hence \(T_M(J)\subseteq J\).

Second, the center identification is valid for an arbitrary norm-closed ideal. If \(q(x)\) is central, then \(uxu^*-x\in J\) for every unitary \(u\in M\). Therefore every finite convex average of the unitary orbit is congruent to \(x\) modulo \(J\). Norm convergence of such averages to \(T_M(x)\) gives \(T_M(x)-x\in J\), so \(q(x)=q(T_M(x))\in q(Z(M))\).

Third, the single-commutator characterization uses exactly Wang's hypothesis. Necessity follows from \(T_M([B,C])=0\). If \(\overline T(q(x))=0\), then \(T_M(x)\in J\), and \(x-T_M(x)\) is a trace-zero lift of the same quotient element. Wang's theorem makes that lift a single commutator. No passage from sums of commutators to a single commutator is hidden in the argument.

Fourth, the metric formula follows from a contractive idempotent: for \(k\in\ker\overline T\),
\[
\|\overline T(a)\|\le\|a-k\|,
\]
while \(a-\overline T(a)\in\ker\overline T\). Hence equality holds.

The reduced-product refinement was checked separately. The norm formula
\[
\|[(y_i)]\|=\inf_{S\in\mathcal I}\sup_{i\notin S}\|y_i\|
\]
follows directly from the definition of \(\mathcal J_{\mathcal I}\). After deleting an \(\mathcal I\)-small set, one has a coordinatewise trace-zero representative uniformly within \(\varepsilon\) of the quotient norm. Wang applies to each finite-dimensional coordinate. Reciprocal scalar rescaling balances the two commutator factors coordinatewise, making both factor sequences bounded and preserving the original product bound \(K\).

The matrix-corona projection example does not conflict with positivity: the descended central tracial projection is not faithful. A rank-one projection sequence has norm one but normalized traces tending to zero, so its quotient class is nonzero positive and belongs to the single-commutator kernel.

## Originality

**PASS, to the best of our knowledge.**

The primary new input is Jiaqi Wang's arXiv:2609.16932v1 (submitted 2026-09-15), which proves a universal operator-norm bound for expressing every center-valued-trace-zero element of a finite von Neumann algebra as one commutator.

The following surrounding literature was checked for coverage:

- generalized Dixmier averaging for finite von Neumann algebras, including the modern statement in *Elementary equivalence and disintegration of tracial von Neumann algebras*, Theorem 2.7;
- Masamichi Takesaki's 1971 *The quotient algebra of a finite von Neumann algebra*;
- center quotient property / weak centrality literature for C*-algebras;
- older single-commutator work in finite and II_1 factors;
- searches combining finite von Neumann algebra, quotient, closed ideal, center-valued trace, single commutator, reduced product, matrix corona, and equivalent terminology;
- Tuan Tran's arXiv:2609.20161v1, whose matrix theorem has a tracial matrix ultraproduct consequence.

No source located stated the theorem for arbitrary operator-norm C*-quotients \(M/J\), the equality of the single-commutator set with the kernel of the descended central projection, the exact distance formula, or the matrix-corona positive-projection consequence.

The center-lifting step is deliberately not claimed as new: it is a short generalized-Dixmier argument and belongs to known center-quotient territory. Likewise, the ideal quotient norm formula and coordinate balancing are standard devices. The originality claim is restricted to the single-commutator consequences made available by the new uniform theorem and their quantitative reduced-product form.

Residual risk remains that older center-quotient/Dixmier-property or abstract commutator literature contains an equivalent nonquantitative quotient statement under different language. Because Wang's all-finite-von-Neumann single-commutator theorem is very recent, direct prior coverage of the full combined statement appears unlikely, but this is not treated as proof of originality.

No highly plausible inaccessible paper was identified that specifically claims the present theorem. Takesaki's 1971 paper was inspected through accessible bibliographic/full-text descriptions sufficient to identify its quotient construction and was not used for a negative full-text claim.

## Value

**PASS.**

The result converts a new theorem internal to finite von Neumann algebras into a structural theorem for all their norm-closed C*-quotients. In these quotients, an ordinarily nonlinear set—the image of the single-commutator map—is forced to be a closed linear subspace, with an exact quotient-distance formula. The reduced-product refinement preserves the universal constant rather than losing the generic factor \(2\), and the matrix corona gives a concrete qualitative phenomenon: a nonzero positive projection can be one additive commutator.

The theorem also separates two quotient regimes that can otherwise look similar: tracial matrix ultraproducts, governed by a \(2\)-norm ideal, versus operator-norm coronas and arbitrary norm-closed ideals.

## Limitations

The descended central tracial projection need not be faithful. No optimal value of Wang's universal constant is obtained. The generic \(2K\) quotient estimate may not be optimal. Properly infinite von Neumann algebras are outside the statement. The reduced-product sharp-\(K\) assertion is proved only for the norm reduced products described in the result. Very recent or poorly indexed follow-up work may not yet be discoverable.

Cross-model review has not been performed.
