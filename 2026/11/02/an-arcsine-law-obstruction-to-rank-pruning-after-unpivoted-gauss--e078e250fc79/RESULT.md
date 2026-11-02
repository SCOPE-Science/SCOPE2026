# An arcsine-law obstruction to rank pruning after unpivoted Gaussian QB blocks

## Finding

For the matrix-free Frobenius QB method of Smith, Do and Chen [1], unpivoted thin QR can make the final row-norm rank-pruning step retain two columns even when a rank-one approximation meets the prescribed tolerance. This occurs with a **nonvanishing, exactly determined limiting probability**, although the residual indicator at the pruning step is exactly zero.

For each \(0<c<1\), let
\[
A_{\tau,c}=\operatorname{diag}(1,c\tau,0,0),\qquad b=2,\qquad0<\tau<1/\sqrt2,
\]
and use **absolute** Frobenius tolerance \(\tau\). The best rank-one approximation has error \(c\tau<\tau\), while rank zero is infeasible. Write \(\delta=c\tau\) and
\[
t=\frac{\tau^2-\delta^2}{1-\delta^2},\quad
P_0(\tau,c)=\frac2\pi\left[\arctan\!\left(\frac1\delta\sqrt{\frac{1-t}{t}}\right)-\arctan\!\left(\frac1\delta\sqrt{\frac{t}{1-t}}\right)\right].
\]
Let \(R_{\tau,c}\) be the event that the first sketch is accepted for expansion, after which the zero second residual causes the prescribed final-block pruning to retain **both** columns. Then
\[
P_0(\tau,c)-(1-e^{-\tau^2})\le\Pr(R_{\tau,c})\le P_0(\tau,c),
\qquad
\lim_{\tau\downarrow0}\Pr(R_{\tau,c})=\frac2\pi\arcsin c.
\]
For \(c=1/2\), this limit is \(1/3\). Every probability strictly between zero and one occurs as the limit for a suitable \(c\). The failure is of **rank optimality**, not of the achieved Frobenius approximation tolerance.

## Assumptions and scope

All operations are over the reals in exact arithmetic. Each random test block has independent \(\mathcal N(0,1/b)\) entries with \(b=2\). The basis expansion uses unpivoted thin QR, not SVD orthogonalization, and the Frobenius pruning rule of [1, Algorithm 3] discards the smallest coefficient rows only while the accumulated squared residual is strictly below \(\tau^2\). The normalized Gaussian block and its QR column order follow the accompanying source implementation [2]. There is a second independent Gaussian sketch used for lookahead.

The event \(R_{\tau,c}\) explicitly requires the first norm estimate to exceed or equal \(\tau\). This excludes a possible premature initial stopping branch, whose probability is bounded below. The \(4\times4\) setting ensures two allowed block iterations in the released implementation; no hypothetical infinite continuation past its block cap is needed. With probability one the first sketched block has exact rank two, so its thin QR produces two columns spanning the image of \(A_{\tau,c}\).

## Proof

Write the two relevant entries of the first Gaussian sketch column, ignoring their common \(1/\sqrt2\) scale, as independent standard normals \(X,Y\). The first column of the unpivoted thin QR basis is proportional to
\[
(X,\delta Y,0,0)^{\mathsf T}.
\]
Apart from signs, the second column is its orthogonal complement in the first two coordinates. With \(D=X^2+\delta^2Y^2\), the coefficient block \(B=Q^{\mathsf T}A_{\tau,c}\) has row norms
\[
w_1^2=\frac{X^2+\delta^4Y^2}{D},\qquad
w_2^2=\frac{\delta^2(X^2+Y^2)}{D},\qquad
w_1^2+w_2^2=1+\delta^2.
\]
Defining \(Z=\delta^2Y^2/D\), equivalently
\[
w_1^2=\delta^2+(1-\delta^2)(1-Z),\qquad
w_2^2=\delta^2+(1-\delta^2)Z.
\]
Because both columns exactly span the range, the next lookahead residual \((A_{\tau,c}-QB)\Omega_2\) is zero for every second sketch. The pruning procedure can discard one coefficient row exactly when its squared norm is strictly below \(\tau^2\). Since \(\tau^2<1/2\), it cannot discard both. Up to probability-zero equality cases, it therefore retains both precisely when
\[
t<Z<1-t,
\qquad t=\frac{\tau^2-\delta^2}{1-\delta^2}\in(0,1/2).
\]
With \(C=Y/X\), the ratio \(C\) has the standard Cauchy distribution, and
\[
Z=\frac{\delta^2C^2}{1+\delta^2C^2}.
\]
Thus the two-column pruning event, considered without the initial stopping decision, is
\[
\sqrt{\frac{t}{1-t}}<\delta|C|<\sqrt{\frac{1-t}{t}}.
\]
The absolute-Cauchy CDF is \(\Pr(|C|\le a)=2\arctan(a)/\pi\) for \(a\ge0\). Integration yields exactly \(P_0(\tau,c)\) above.

The initial sketch is \(Y_1=A_{\tau,c}\Omega_1\). A premature first stop implies
\[
\frac{G_{11}^2+G_{12}^2}{2}<\tau^2,
\]
where the two \(G\)'s are independent standard normals. Since their sum of squares has a chi-square law with two degrees of freedom,
\[
\Pr(\|Y_1\|_F<\tau)\le1-e^{-\tau^2}.
\]
Intersecting the rank-two pruning event with survival of the initial test gives the stated **finite-tolerance two-sided probability enclosure**.

Finally, as \(\tau\downarrow0\) with \(\delta=c\tau\),
\[
\frac{1}{\delta}\sqrt{\frac{t}{1-t}}\longrightarrow\frac{\sqrt{1-c^2}}{c},
\qquad
\frac{1}{\delta}\sqrt{\frac{1-t}{t}}\longrightarrow+\infty.
\]
The initial-stop probability bound tends to zero. Hence
\[
\lim_{\tau\downarrow0}\Pr(R_{\tau,c})
=\frac2\pi\left(\frac\pi2-\arctan\frac{\sqrt{1-c^2}}c\right)
=\frac2\pi\arcsin c.
\]
Every \(c\in(0,1)\) gives a nontrivial limiting failure probability; choosing \(c=\sin(\pi p/2)\) realizes any \(p\in(0,1)\). In each rank-two event, the returned approximation is exact, yet its rank exceeds the optimum by one.

For comparison, compute a thin SVD of the **already available** coefficient block \(B\). Because the two columns of \(Q\) span the range, the nonzero singular values of \(B\) are exactly \(1\) and \(\delta\). Orthogonally rotating \(Q\) by its two left singular vectors and retaining only the leading rotated column gives Frobenius error exactly \(\delta<\tau\). No additional product with \(A_{\tau,c}\) or its adjoint is needed. This is a standard SVD postprocessing observation; only its role in the quantified obstruction is claimed here.

## Verification

The standalone `VERIFY.py` executes four symbolic equalities, 2,016 exact-rational rank-pruning equivalences, 180 direct QR/SVD calculations, and 480,000 seeded Gaussian draws. Exact rational checks verify the finite indicator equivalence but do not prove the universal or probability statements; those follow from the argument above. The tests use NumPy and SymPy. Invoke `python VERIFY.py` in a Python environment with both packages installed.

## Relationship to prior work

Smith, Do and Chen [1, §3.1–3.2, Algorithms 2–3] define the exact row-norm pruning rule, describe rank efficiency numerically, and explicitly target ranks near the truncated-SVD optimum. Their released implementation [2–3] uses unpivoted thin QR and row-norm pruning. The present calculation identifies the sharp nonvanishing over-retention probability for a natural two-singular-value test matrix with a zero final lookahead residual. It is not implied by their Pythagorean error identity, which guarantees the error of *selected rows*, not optimality among arbitrary rotated bases.

The original rank-estimation work [4] estimates singular values from double-sided sketches; the blocked randomized factorization [5], randUTV method [6], and strong randomized rank-revealing QR [7] analyze different rank-revealing strategies. Their singular-value transformations illustrate why row norms in an arbitrary orthonormal basis need not represent smallest achievable truncation error. Their inspected results do not supply this algorithm-specific probability law. Foster's classic QR-diagonal probability work [8] concerns another rank diagnostic; a complete comparison with that inaccessible full text remains a priority risk.

## Limitations

The result is for a real rank-two matrix embedded in size four, Gaussian block width two, absolute tolerance, exact arithmetic, unpivoted QR and the source's final-block row-norm pruning. It does not address finite-precision underflow, larger block widths, rank deficiency during QR, relative tolerance, or the source's adjoint-free variant, whose row-norm estimators are also randomized. It neither proves a global rank-efficiency lower bound nor says SVD improvement is novel. The initial premature-stop event is excluded by definition and controlled quantitatively. Full inspection of Foster [8] was prevented by access restrictions, and independent mathematical verification is unperformed.

## References

[1] A. I. Smith, E. Do and C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758v1, submitted 2026-07-07, https://arxiv.org/html/2607.06758v1 .

[2] Source authors, `randQB_MF_Fro.m`, https://github.com/SMART-Algebra/Adaptive-Matfree-Lowrank/blob/main/randQB_MF_Fro.m (implementation of the Frobenius matrix-free QB method).

[3] Source authors, `Prune_Rank_Fro.m`, https://github.com/SMART-Algebra/Adaptive-Matfree-Lowrank/blob/main/Prune_Rank_Fro.m .

[4] M. Meier and Y. Nakatsukasa, *Fast Randomized Numerical Rank Estimation for Numerically Low-Rank Matrices*, arXiv:2105.07388, https://arxiv.org/abs/2105.07388 .

[5] P.-G. Martinsson and S. Voronin, *A Randomized Blocked Algorithm for Efficiently Computing Rank-Revealing Factorizations of Matrices*, arXiv:1503.07157, https://arxiv.org/abs/1503.07157 .

[6] P.-G. Martinsson, G. Quintana-Ortí and N. Heavner, *randUTV: A Blocked Randomized Algorithm for Computing a Rank-Revealing UTV Factorization*, arXiv:1703.00998, https://arxiv.org/abs/1703.00998 .

[7] L. Grigori and Z. Xue, *Randomized Strong Rank-Revealing QR for Column Subset Selection and Low-Rank Matrix Approximation*, arXiv:2503.18496v1, https://arxiv.org/html/2503.18496v1 .

[8] L. V. Foster, *The Probability of Large Diagonal Elements in the QR Factorization*, SIAM J. Sci. Stat. Comput. 11 (1990), 531–544, DOI:10.1137/0911030 (abstract accessible; full text not examined).
