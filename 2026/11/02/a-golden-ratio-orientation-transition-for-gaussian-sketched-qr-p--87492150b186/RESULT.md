# A golden-ratio orientation transition for Gaussian-sketched QR pivot regret

## Finding

Fix an integer \(m\geq2\) and a real matrix \(M\in\mathbb R^{m\times2}\) whose Gram matrix \(G=M^{\mathsf T}M\) has eigenvalues \(L>1\) and \(1\). Draw \(\Omega\in\mathbb R^{2\times m}\) with independent standard real Gaussian entries. Let \(J\in\{1,2\}\) be the first max-column-norm QR pivot of the sketch \(\Omega M\), using arbitrary tie-breaking. Define the squared-first-pivot regret

\[
\mathcal L(M,\Omega)=\max_{j=1,2}\|Me_j\|_2^2-\|Me_J\|_2^2.
\]

Thus \(\mathcal L\) measures the loss in the squared first QR diagonal that results from selecting the first pivot using the sketch instead of exact column norms. Set \(\delta=|G_{11}-G_{22}|\), so \(0\leq\delta\leq L-1\). The complete expected-regret law is

\[
\mathbb E\mathcal L=\frac{\delta}{2}\left(1-\frac{\delta}{\sqrt{\delta^2+4L}}\right).
\]

Let \(s=(\sqrt5-1)/2\) and \(L_c=2+\sqrt5\). At fixed singular-value squares \(L,1\), the **sharp maximum over all column orientations** is

\[
\sup_{M:\operatorname{spec}(M^{\mathsf T}M)=\{L,1\}}
\mathbb E\mathcal L
=\begin{cases}
\dfrac{L-1}{L+1},&1<L\leq L_c,\\[4pt]
 s^{5/2}\sqrt L,&L\geq L_c.
\end{cases}
\]

For \(1<L\leq L_c\), equality holds exactly when the Gram matrix is diagonal, up to swapping the columns. For \(L>L_c\), equality holds exactly when

\[
|G_{11}-G_{22}|=2\sqrt{sL}.
\]

Equivalently, if \(G=R_\theta\operatorname{diag}(L,1)R_\theta^{\mathsf T}\) for a real planar rotation, all maximizing orientations satisfy \(|\cos(2\theta)|=2\sqrt{sL}/(L-1)\) in the latter regime. At the transition, the two descriptions coincide. In particular, the worst expected loss grows as \(s^{5/2}\sqrt L\approx0.3002831060\sqrt L\) even though the column-aligned orientation has expected loss approaching \(1\).

## Assumptions and scope

All statements concern real matrices, exactly two columns, exactly two independent Gaussian sketch rows, a full-rank input, ordinary max-squared-column-norm first-pivot selection, and exact arithmetic. The number of original matrix rows may be any integer at least two. Any global multiplication of the sketch by a positive scalar leaves the pivot and regret unchanged. The Gram eigenvalues are fixed at \(L\) and \(1\), setting the overall scale; for eigenvalues \(a>b>0\), multiply the displayed regret by \(b\) and replace \(L\) by \(a/b\).

The regret measures the loss of the first squared QR diagonal, **not** the final rank-one projection error, the quality of the second pivot, or full QR factorization stability. The sampled-pivot rule is the first QRCP decision used in Gaussian-sketch QR algorithms; default implementations may use larger sketches or further safeguards.

## Proof

Write \(g_j=G_{jj}\). First assume \(g_1>g_2\), so \(\delta=g_1-g_2>0\). The two entries of one row of \(\Omega M\) form a centered Gaussian vector with covariance \(G\). The difference between the two sketched squared column norms equals a sum of two independent copies of the quadratic form with signature \(\operatorname{diag}(1,-1)\). Its coefficient matrix is similar to \(G^{1/2}\operatorname{diag}(1,-1)G^{1/2}\), which has trace \(\delta\) and determinant \(-\det G=-L\). Its eigenvalues are therefore \(\alpha>0\) and \(-\beta<0\), where

\[
\alpha=\frac{\sqrt{\delta^2+4L}+\delta}{2},\qquad
\beta=\frac{\sqrt{\delta^2+4L}-\delta}{2}.
\]

Orthogonal Gaussian invariance, separately in each sketch row, yields an exact distributional identity for the sketch norm difference:

\[
\|\Omega Me_1\|_2^2-\|\Omega Me_2\|_2^2
\ \overset{\mathrm d}=\ \alpha X-\beta Y,
\]

where \(X,Y\) are independent chi-square variables with two degrees of freedom. Their densities are \(\frac12e^{-x/2}\) for \(x>0\). Since the second pivot is selected exactly when \(\alpha X<\beta Y\), integration gives

\[
\mathbb P(J=2)=\int_0^\infty\frac12e^{-x/2}
  \mathbb P\left(Y>\frac{\alpha x}{\beta}\right)\,dx
=\frac{\beta}{\alpha+\beta}
=\frac12\left(1-\frac{\delta}{\sqrt{\delta^2+4L}}\right).
\]

On a mistaken first pivot the loss is exactly \(\delta\); otherwise it vanishes. This proves the expectation formula. Interchanging columns gives the same answer for \(g_2>g_1\). When \(g_1=g_2\), the loss is identically zero. The allowable interval \(0\leq\delta\leq L-1\) follows from writing the real symmetric positive-definite Gram matrix as a rotation of \(\operatorname{diag}(L,1)\); every value in this interval is realized.

Set

\[
u=\frac{\delta}{\sqrt{\delta^2+4L}},\qquad
0\leq u\leq\frac{L-1}{L+1}.
\]

The expected loss becomes

\[
\mathbb E\mathcal L=\sqrt L\,u\sqrt{\frac{1-u}{1+u}}.
\]

Maximizing its square is equivalent to maximizing \(h(u)=u^2(1-u)/(1+u)\), whose derivative is

\[
h'(u)=\frac{2u(1-u-u^2)}{(1+u)^2}.
\]

The polynomial \(1-u-u^2\) has exactly one positive root \(s=(\sqrt5-1)/2\). Hence the objective increases strictly up to \(s\) and decreases strictly afterward. The upper endpoint \((L-1)/(L+1)\) reaches \(s\) precisely when \(L=2+\sqrt5\). If the root is infeasible, the maximum is at \(\delta=L-1\), producing \((L-1)/(L+1)\). Otherwise the unique maximizing gap is \(\delta=2\sqrt{sL}\). Since \(1-s=s^2\) and \(1+s=1/s\), substituting \(u=s\) yields \(s^{5/2}\sqrt L\). The strict increase/decrease proves all equality cases. The last asymptotic is immediate.

## Verification

The accompanying standard-library Python program `verify.py` checks the algebraic transition, independent exponential-density quadrature, the finite-dimensional equality formulas, a dense deterministic grid of orientation bounds, and independently sampled Gaussian sketches for several values of \(L\). It reports `VERIFY_OK` when those checks pass. The infinite family and its sharpness are proved above by probability identities and one-variable differentiation; numerical sampling is not used as an infinite proof.

## Relationship to prior work

Melnichenko, Balabanov, Murray, Demmel, Mahoney, and Luszczek describe Gaussian-sketch QRCP as the pivot-selection step of CQRRPT, and prove rank-revealing and stability statements based on restricted singular values. Martinsson, Quintana-Ortí, Heavner, and van de Geijn introduce Gaussian row-sketch pivot selection and investigate its numerical quality; Duersch and Gu analyze randomized QR with column pivoting. Those algorithmic ideas are prior art.

The Gaussian quadratic-form representation and sign-probability computation are classical rather than claimed as new: for example, Gaunt's 2024 treatment of sums of correlated-normal products and chi-square differences gives general sign probabilities. The claim assessed here is **only** the sharp fixed-spectrum orientation maximization of a natural first-pivot loss, including the optimizer change at \(2+\sqrt5\), its equality cases, and the \(\sqrt L\) worst-case scale. General subspace-embedding guarantees and the cited probability laws do not themselves state this oriented QR-pivot extremal classification. Priority beyond the searched material is not independently verified.

## Limitations

No conclusion is asserted for non-Gaussian sketches, more than two sketch rows, more than two input columns, complex-valued inputs, floating-point pivot ties, or downstream QR errors. This first-pivot squared-norm objective must not be confused with full-rank-revealing performance. The zero-regret equal-column case does not mean the selected index is deterministic. The distributional identity used in the proof is known in related probability literature; the novelty claim does not extend to that identity. An equivalent extremal characterization could exist under a different terminology.

## References

1. M. Melnichenko, O. Balabanov, R. Murray, J. Demmel, M. W. Mahoney, and P. Luszczek, *CholeskyQR with Randomization and Pivoting for Tall Matrices (CQRRPT)*, arXiv:2311.08316, first posted 2023-11-14. https://arxiv.org/abs/2311.08316
2. P.-G. Martinsson, G. Quintana-Ortí, N. Heavner, and R. van de Geijn, *Householder QR Factorization with Randomization for Column Pivoting*, arXiv:1512.02671, 2015. https://arxiv.org/abs/1512.02671
3. J. A. Duersch and M. Gu, *Randomized QR with Column Pivoting*, arXiv:1509.06820, 2015. https://arxiv.org/abs/1509.06820
4. R. E. Gaunt, *On the product of correlated normal random variables and the noncentral chi-square difference distribution*, arXiv:2408.04101, 2024, especially Theorem 2.1 and Corollary 2.11. https://arxiv.org/abs/2408.04101
