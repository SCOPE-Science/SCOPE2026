# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The proof was checked separately at the two endpoint geometries and for
\(1\leq p<\infty\). The rank-one operator
\(N_c(z,y)=(c f(y)z_0,0)\) satisfies \(N_c^2=0\), hence
\((I-N_c)^{-1}=I+N_c\). The upper bound for the inverse norm reduces exactly to
the norm of the scalar shear
\[
(a,b)\mapsto(a+cb,b)
\]
on \(\ell_p^2\). The reverse bound is obtained from a maximizing nonnegative
scalar pair and a norming sequence for the non-norm-attaining functional \(f\).
This gives \(\|T_c^{-1}\|=\kappa_p(c)\).

Nonattainment was stress-tested at \(p=1\), at \(p=\infty\), and for intermediate
finite \(p\). Equality in the norm estimate would force
\(|f(y)|=\|y\|\) for a nonzero \(y\), contradicting the choice of \(f\).
Since an invertible operator attains its minimum modulus exactly when its inverse
attains its norm, \(T_c\) is non-minimum-modulus attaining.

The compact-perturbation envelope is exact, not merely bounded below. For every
compact \(C\) on the infinite-dimensional space \(X\), compactness prevents \(C\)
from being bounded below, so unit vectors \(u_n\) exist with \(Cu_n\to0\). Hence
\(m(I+C)\leq1\). Since every \(T_c+K\) equals \(I\) plus a compact operator, its
minimum modulus is at most \(1\), while \(K=N_c\) attains \(1\).

No complementability claim beyond the explicit isometric direct-sum hypothesis is
used. The proof does not infer complementedness from an unconditional basis or
from a general subspace decomposition.

## Originality

Originality is assessed to the best of our knowledge. The full arXiv HTML of
Han's 2026 paper was inspected, including Section 3. Han's Theorem 3.4 treats
\((X\oplus_p Z,Y\oplus_q Z)\) only for \(1\leq p<q<\infty\), while Example 3.3
establishes the special failure of \((\ell_1,\ell_1)\). Thus that result does not
supply the diagonal \(p=q\) theorem proved here.

The full arXiv HTML of Raposo--Ribeiro was also inspected. Their Theorem 2.1
treats \(X=\mathbb K\oplus_\infty Y\) with \(Y\) non-reflexive and uses the
\(c=1\) rank-one shear. No finite-\(p\) diagonal extension, arbitrary nonzero
summand \(Z\), exact compact-perturbation envelope, or unbounded defect family is
stated there.

Literature searches used exact and synonymous formulations involving CPPm,
compact perturbations of the minimum modulus, \(p\)-sums/direct sums,
non-reflexivity, and rank-one shears. No prior statement matching the all-\(p\)
diagonal theorem or its quantitative envelope was located. The mechanism is a
natural extension of the recent \(\ell_\infty\) construction, so the originality
claim is deliberately limited to the strengthened theorem rather than to its
classical ingredients.

## Value

The result closes a visible direct-sum gap between Han's finite-exponent theorem,
which requires \(p<q\), and the later diagonal \(\ell_\infty\) obstruction of
Raposo--Ribeiro. It gives one reusable rank-one mechanism valid for every
\(1\leq p\leq\infty\), includes arbitrary nonzero complementary summands, and
computes the full compact-perturbation envelope rather than exhibiting only one
improving perturbation. The defect ratio can be made arbitrarily large.

The theorem also yields a substantially simpler shear witness for the classical
\(\ell_1\) failure and simultaneously recovers the \(c_0\)-type
\(\ell_\infty\)-sum mechanism.

## Source-access limitations

The complete arXiv HTML versions of Han, arXiv:2601.17316v1, and
Raposo--Ribeiro, arXiv:2605.01397v1, were inspected at the theorem level relevant
to direct sums and CPPm. The publisher record for Han's journal version was also
located. James' original reflexivity paper was located through the journal
publisher and its bibliographic identity was verified.

No inaccessible source was identified as uniquely likely to contain the same
2026-specific CPPm statement. Because CPPm terminology is recent and indexing can
lag, equivalent older results phrased only in terms of lower bounds or minimum
moduli under compact perturbations remain a residual originality risk.
