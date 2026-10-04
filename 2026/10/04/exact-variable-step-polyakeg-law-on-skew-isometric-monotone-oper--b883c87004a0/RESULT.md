# Exact variable-step PolyakEG law on skew-isometric monotone operators
## Finding

Let \(m\ge 1\), let \(J\in\mathbb R^{2m\times 2m}\) satisfy
\[
J^T=-J,\qquad J^TJ=I,
\]
and fix \(L>0\) and \(x_\star\in\mathbb R^{2m}\). Then \(J^2=-I\), and
\[
F(x)=LJ(x-x_\star)
\]
is monotone, \(L\)-Lipschitz, has the unique zero \(x_\star\), and is not strongly monotone.

For deterministic PolyakEG, write
\[
\widehat x_k=x_k-\gamma_kF(x_k),\qquad
\alpha_k=
\frac{\langle F(\widehat x_k),x_k-\widehat x_k\rangle}
{\|F(\widehat x_k)\|^2},
\qquad
x_{k+1}=x_k-\alpha_kF(\widehat x_k).
\]
Put \(e_k=x_k-x_\star\) and \(s_k=L\gamma_k\). Then, for every \(e_k\ne0\),
\[
\alpha_k=\frac{\gamma_k}{1+s_k^2},
\qquad
e_{k+1}=\frac{I-s_kJ}{1+s_k^2}e_k,
\]
and therefore
\[
\|e_{k+1}\|^2=\frac{\|e_k\|^2}{1+s_k^2}.
\]
Consequently, for every integer \(K\ge1\),
\[
\|e_K\|
=
\|e_0\|
\prod_{k=0}^{K-1}(1+s_k^2)^{-1/2}.
\]

The paper's critical condition with parameter \(A\in(0,1]\),
\[
\|F(\widehat x_k)-F(x_k)\|\le A\|F(x_k)\|,
\]
holds here if and only if \(s_k\le A\). Under \(0<s_k\le A\le1\) and \(e_0\ne0\),
\[
x_k\to x_\star
\quad\Longleftrightarrow\quad
\sum_{k=0}^\infty s_k^2=\infty.
\]
Thus a decreasing schedule may have \(\sum_k s_k=\infty\) yet fail to converge when \(\sum_k s_k^2<\infty\). For a constant admissible step \(s_k=s\), the exact linear factor is
\[
q(s)=\frac1{\sqrt{1+s^2}},
\]
which is strictly decreasing in \(s>0\). Hence the unique best constant step allowed by the critical condition is \(s=A\), with
\[
q_\star(A)=\frac1{\sqrt{1+A^2}}.
\]

## Assumptions and scope

The statement is in exact arithmetic on finite-dimensional Euclidean space. The structural assumption \(J^T=-J\) and \(J^TJ=I\) means that \(J\) is an orthogonal complex structure; equivalently it is a direct orthogonal sum of quarter-turn blocks. The result therefore covers every dimension \(2m\), not only a single planar example.

The zero is unique because \(J\) is invertible. Monotonicity follows from
\[
\langle F(x)-F(y),x-y\rangle
=
L\langle J(x-y),x-y\rangle
=
0,
\]
so the example is exactly at the non-strongly-monotone rotational boundary. The result concerns the deterministic PolyakEG update of Yoon--Choudhury--Greenberg--Loizou and does not assert the same law for classical equal-step extragradient, stochastic variants, constrained projections, or non-isometric skew operators.

## Proof

Since \(J^T=-J\) and \(J^TJ=I\),
\[
-J^2=I,
\]
so \(J^2=-I\). With \(s_k=L\gamma_k\),
\[
\widehat e_k=(I-s_kJ)e_k.
\]
Hence
\[
F(\widehat x_k)
=
LJ\widehat e_k
=
L(J+s_kI)e_k,
\]
and
\[
x_k-\widehat x_k=s_kJe_k.
\]
Using \(\langle e_k,Je_k\rangle=0\) and \(\|Je_k\|=\|e_k\|\),
\[
\langle F(\widehat x_k),x_k-\widehat x_k\rangle
=
Ls_k\|e_k\|^2
\]
while
\[
\|F(\widehat x_k)\|^2
=
L^2(1+s_k^2)\|e_k\|^2.
\]
Therefore
\[
\alpha_k
=
\frac{s_k}{L(1+s_k^2)}
=
\frac{\gamma_k}{1+s_k^2}.
\]
Substitution into the update gives
\[
e_{k+1}
=
e_k-\frac{s_k}{1+s_k^2}(J+s_kI)e_k
=
\frac{I-s_kJ}{1+s_k^2}e_k.
\]
Because
\[
(I-s_kJ)^T(I-s_kJ)
=
(I+s_kJ)(I-s_kJ)
=
(1+s_k^2)I,
\]
we obtain
\[
\|e_{k+1}\|^2
=
\frac{\|e_k\|^2}{1+s_k^2},
\]
and iteration yields the product formula.

Also,
\[
F(\widehat x_k)-F(x_k)
=
Ls_ke_k,
\qquad
\|F(x_k)\|=L\|e_k\|,
\]
so the critical-condition ratio is exactly \(s_k\). This proves the claimed equivalence with \(s_k\le A\).

For \(0\le u\le A^2\),
\[
\frac{u}{1+A^2}\le \log(1+u)\le u.
\]
Thus
\[
\sum_k\log(1+s_k^2)=\infty
\quad\Longleftrightarrow\quad
\sum_k s_k^2=\infty.
\]
The product formula tends to zero exactly when the logarithmic sum diverges, proving the convergence criterion for \(e_0\ne0\). Finally \(q(s)=(1+s^2)^{-1/2}\) is strictly decreasing for \(s>0\), proving optimality of the largest constant admissible step.

## Verification

The standalone script `artifacts/verify_skew_isometry.py` checks the algebra in exact rational arithmetic on the canonical \(2\times2\) quarter-turn block for several rational values of \(s\) and verifies the multi-step product identity. This finite replay is a consistency check; the proof above establishes the quantified all-dimension statement.

The same norm law also applies to residuals because
\[
\|F(x_k)\|=L\|e_k\|.
\]

## Relationship to prior work

Yoon, Choudhury, Greenberg, and Loizou define PolyakEG by exactly the extrapolation and projection-correction formulas used here, and their Theorem 3.4 gives generic \(O(1/K)\) best-iterate squared-residual bounds under the critical condition for monotone operators. Their full text uses the planar rotation \(F(u,v)=(-v,u)\) as the canonical example explaining why ordinary forward iteration diverges, but it does not state the product law, the square-summability convergence criterion, or the exact constant-step factor above.

The projection correction itself is older and is explicitly credited in that paper to projection-type methods including Solodov--Svaiter and Solodov--Tseng. Those sources establish global or linear convergence under broader structural/error-bound conditions; the checked statements do not give this exact variable-step law on orthogonal skew operators.

Two nearby exact-rate records concern different algorithms: one analyzes FRB/RFB on a skew-rotation inclusion and obtains a characteristic-root optimum; another solves a degree-two minimax problem for unequal-step extragradient on normal strongly monotone systems. Neither update is PolyakEG's projection correction, and neither implies the product criterion above.

The result sharpens a natural benchmark suggested by the source's own rotational discussion: it identifies the complete deterministic trajectory law at the maximally rotational, non-strongly-monotone boundary rather than merely a best-iterate sublinear estimate.

## Limitations

The exact formula uses both skew-symmetry and isometry. General skew-symmetric operators with unequal singular values need not share one scalar contraction factor. The result is deterministic, unconstrained, and exact-arithmetic. It does not claim a worst-case rate over all monotone operators satisfying the critical condition.

Older projection-method literature is broad. The checked primary statements establish the method family and general convergence principles, but an uninspected specialized linear-algebra treatment could conceivably contain an equivalent skew-isometry product formula; this remains the principal residual originality risk.

## References

1. T. Yoon, S. Choudhury, E. Greenberg, N. Loizou, *Polyak-Type Extragradient Methods for Monotone Root-Finding Problems*, arXiv:2609.26581v1, 2026.
2. M. V. Solodov, B. F. Svaiter, *A New Projection Method for Variational Inequality Problems*, SIAM Journal on Control and Optimization 37(3), 765--776, 1999. DOI: 10.1137/S0363012997317475.
3. M. V. Solodov, P. Tseng, *Modified Projection-Type Methods for Monotone Variational Inequalities*, SIAM Journal on Control and Optimization 34(5), 1814--1830, 1996.
4. P. Tseng, *On Linear Convergence of Iterative Methods for the Variational Inequality Problem*, Journal of Computational and Applied Mathematics 60(1--2), 237--252, 1995. DOI: 10.1016/0377-0427(94)00094-H.
