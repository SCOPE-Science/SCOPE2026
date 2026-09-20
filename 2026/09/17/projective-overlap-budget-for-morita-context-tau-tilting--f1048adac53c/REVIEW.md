# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof separates into two finite-dimensional algebra facts and one support-\(\tau\)-tilting count.

First, \(\Lambda=e\Lambda\oplus f\Lambda=F_AA\oplus F_BB\). Full faithfulness of \(F_A,F_B\) preserves indecomposable projectives and their isomorphism distinctions within each corner, while Krull--Schmidt shows that every indecomposable projective \(\Lambda\)-class occurs in at least one of the two induced families. Therefore
\[
\omega=|A|+|B|-|\Lambda|.
\]
Passing to \(S=\Lambda/J(\Lambda)\), with \(J(e\Lambda e)=eJ(\Lambda)e\), identifies the overlap classes with simple Artinian factors on which both complementary idempotents remain nonzero. In such a factor \(S_i\), nonzero \(f_i\) is full, so \(S_if_iS_i=S_i\), which forces \(e_iS_if_iS_ie_i\neq0\) whenever \(e_i\neq0\). Hence the connecting-map images are radical-valued exactly when there are no mixed factors, i.e. when \(\omega=0\).

Second, for a \(\tau\)-rigid directly induced module \(Z\), adjunction identifies the projectives orthogonal to \(Z\) exactly with the union of the surviving corner-projective sets \(\iota_A(\mathcal R_X)\cup\iota_B(\mathcal R_Y)\). Inclusion--exclusion gives
\[
|P^\perp_Z|=r_X+r_Y-d_P,\qquad |Z|=|X|+|Y|-d_Z.
\]
After substituting the definitions of \(\delta_X,\delta_Y,\beta_X,\beta_Y\), this becomes
\[
|Z|+|P^\perp_Z|=|A|+|B|-\Delta.
\]
The standard \(\tau\)-rigid-pair summand bound then gives \(\Delta\ge\omega\), and equality is equivalent to the support-\(\tau\)-tilting count. If \(Z\) is already support \(\tau\)-tilting, every projective orthogonal to \(Z\) must belong to its projective complement; otherwise one could enlarge the pair past \(|\Lambda|\). Thus the equality criterion is two-sided.

The strict \(M_2(k)\) example was checked directly: \(\omega=1\), the only nonzero defect is \(\beta_Y=1\), and \(F_Ak\) is the unique indecomposable projective class, so equality holds exactly as predicted. Direct products give sharp examples with arbitrary overlap number.

## Originality

**PASS, to the best of our knowledge.**

Zhang's arXiv:2609.18746v1 explicitly isolates the radical condition as the ingredient needed for the summand count in the converse and gives \(M_2(k)\) as the obstruction. Its arbitrary-connecting-map Lemma 5.4 supplies only the \(\tau\)-rigidity criterion. The inspected paper does not introduce a numerical projective-overlap invariant, decompose the failed count into nonnegative defects, or give an equality criterion outside the radical-valued case.

Targeted searches for Morita-context support-\(\tau\)-tilting overlap criteria, projective-complement defects, and direct-induction summand overlap found the Zhang preprint, triangular/zero-product silting results, and classical Morita-context literature, but no matching six-term identity or condition-free support-\(\tau\)-tilting characterization.

### Residual literature risk

The full text of A. D. Sands, *Radicals and Morita contexts*, J. Algebra 24 (1973), 335--345, DOI 10.1016/0021-8693(73)90143-9, was not inspected. It may contain an equivalent formulation of the structural zero-overlap/radical equivalence. No novelty is claimed for that classical ring-theoretic ingredient in isolation. Because arXiv:2609.18746 is a very recent preprint, a concurrent revision or independent extension is also possible.

## Value

**PASS.**

The result gives a quantitative replacement for the hypothesis that fails in the newest direct-induction theorem. Instead of merely saying that the converse can fail outside the radical case, it identifies a finite overlap budget
\[
\omega=|A|+|B|-|\Lambda|
\]
and shows exactly how that budget is consumed by corner support defects, failed projective-side compatibility, and duplicate induced summands. This yields a necessary-and-sufficient numerical criterion for direct support-\(\tau\)-tilting induction with arbitrary connecting maps.

The formula also explains the published \(M_2(k)\) obstruction without special pleading and gives a stability statement near the radical case: when \(\omega\) is small, the total amount of all six failure modes is forced to be equally small.

## Scope of the claim

No novelty is claimed for Morita-context radical formulas, the Adachi--Iyama--Reiten summand bound, Zhang's \(\tau\)-rigidity test, or the \(M_2(k)\) counterexample themselves. The claimed contribution is the projective-overlap interpretation, the exact nonnegative budget identity, and the resulting condition-free direct-induction characterization.
