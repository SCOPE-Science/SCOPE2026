# An exact submodularity phase diagram for two-site variational Gaussian-process pivot gains

## Finding

The inducing-subset variational free energy of Gaussian-process regression is monotone but need not be submodular, even for a strictly positive two-by-two kernel with an arbitrarily small positive off-diagonal correlation. The complete two-site submodularity region is determined exactly by two rotated response coordinates.

Let \(\sigma^2>0\) be the observation-noise variance, \(\tau>0\) the signal-to-noise ratio, and \(0<r<1\) the kernel correlation. Set
\[
K=\sigma^2\tau\begin{pmatrix}1&r\\r&1\end{pmatrix},\qquad z=y/\sigma,\qquad z_\pm=(z_1\pm z_2)/\sqrt2.
\]
For an inducing subset \(S\subseteq\{1,2\}\), let \(Q_S=K_{:,S}K_{S,S}^{-1}K_{S,:}\) and \(Q_\varnothing=0\). Define the variational objective, omitting constants independent of \(S\), by
\[
F(S)=-\tfrac12\bigl[\log\det(\sigma^2 I+Q_S)+y^{\mathsf T}(\sigma^2 I+Q_S)^{-1}y+\sigma^{-2}\operatorname{tr}(K-Q_S)\bigr].
\]
Put \(D=1+\tau(1+r^2)\) and \(H_\pm=1+\tau(1\pm r)\). Its unique two-element submodularity defect is exactly
\[
\Gamma=F(\{1\})+F(\{2\})-F(\varnothing)-F(\{1,2\})
=C+A_+z_+^2-A_-z_-^2,
\]
where
\[
C=\tau r^2-\log D+\tfrac12\log(H_+H_-),\qquad
A_+=\frac{r\tau(1+r)(2\tau+1)}{2H_+D},\qquad
A_-=\frac{r\tau(1-r)(2\tau+1)}{2H_-D}.
\]
All three coefficients are strictly positive. Therefore \(F\) is submodular **if and only if**
\[
\boxed{z_-^2\le(C+A_+z_+^2)/A_-.}
\]
In particular, for \(\tau=1\), \(r=1/2\), \(\sigma^2=1\), and \(y=(1,-1)^{\mathsf T}\), the kernel is strictly positive definite, all inducing-set additions improve \(F\), but
\[
\Gamma=\tfrac1{36}+\tfrac12\log(20/27)<0.
\]
For fixed \(\tau>0\) and fixed \(z_1z_2\ne0\),
\[
\lim_{r\downarrow0}\frac{\Gamma}{r}
=\frac{\tau(2\tau+1)}{(1+\tau)^2}z_1z_2.
\]
Thus every oppositely signed nonzero response pair violates submodularity for all sufficiently small positive \(r\); exact independence \(r=0\) is modular.

## Assumptions and scope

All quantities are real, arithmetic is exact, \(\tau>0\), \(\sigma^2>0\), \(0<r<1\), and the two kernel sites may both be selected. The observation-noise variance is identical at both sites. The result concerns the Titsias variational free-energy inducing-subset objective with inducing locations restricted to these two data sites, not Gaussian mutual information and not the trace residual alone. The response vector may be arbitrary. A set function on a two-element ground set is submodular precisely when its single defect \(\Gamma\) is nonnegative.

## Proof

**1. Normalization and Nyström matrices.** Factoring \(\sigma^2\) from the determinant and setting \(z=y/\sigma\) leaves an \(S\)-independent additive constant. Thus take \(\sigma^2=1\) and \(K=\tau\begin{pmatrix}1&r\\r&1\end{pmatrix}\). For \(S=\{1\}\) and \(S=\{2\}\), respectively,
\[
Q_{\{1\}}=\tau\begin{pmatrix}1&r\\r&r^2\end{pmatrix},\quad
Q_{\{2\}}=\tau\begin{pmatrix}r^2&r\\r&1\end{pmatrix},\quad
Q_{\{1,2\}}=K.
\]
Consequently \(\det(I+Q_{\{1\}})=\det(I+Q_{\{2\}})=D\) and \(\det(I+K)=H_+H_-\). Also \(\operatorname{tr}(Q_{\{1\}}+Q_{\{2\}}-K)=2\tau r^2\).

**2. Response quadratic form.** The data-dependent part of \(2\Gamma\) is \(z^{\mathsf T}M z\), with
\[
M=I+(I+K)^{-1}-(I+Q_{\{1\}})^{-1}-(I+Q_{\{2\}})^{-1}.
\]
Every matrix on the right commutes with coordinate interchange after the two singleton inverses are summed. Thus \(M\) is diagonal in the symmetric and antisymmetric unit vectors. Substitution of the two-by-two inverse formula gives its eigenvalues \(2A_+\) and \(-2A_-\), respectively. Combining the trace and log-determinant parts yields the displayed formula for \(\Gamma\).

**3. Strict coefficient signs.** The formulas give \(A_+>0\) and \(A_->0\). Direct differentiation of \(C\) with respect to \(\tau\) gives
\[
\frac{\partial C}{\partial\tau}=
\frac{r^2\tau[(1-r^4)\tau^2+(r^2+3)\tau+(r^2+1)]}{H_+H_-D}>0.
\]
Since \(C=0\) at \(\tau=0\), it follows that \(C>0\) for \(\tau>0\). The exact necessary-and-sufficient inequality follows by rearranging \(\Gamma\ge0\).

**4. Monotonicity despite failure of diminishing returns.** For \(S\subseteq T\), the Nyström covariance increment \(E=Q_T-Q_S\) is positive semidefinite, by Schur-complement projection onto nested feature subspaces. Writing \(B=I+Q_S\), the increase of twice the normalized objective equals
\[
\operatorname{tr}E-\log\det(I+B^{-1/2}EB^{-1/2})
+z^{\mathsf T}[B^{-1}-(B+E)^{-1}]z.
\]
Both terms are nonnegative: \(\log\det(I+X)\le\operatorname{tr}X\le\operatorname{tr}E\) for \(X=B^{-1/2}EB^{-1/2}\ge0\), and inversion reverses the positive-semidefinite order. This proves monotonicity without invoking submodularity.

**5. Explicit non-submodular instance.** For the specified example, \(D=9/4\), \(H_+=5/2\), \(H_-=3/2\), \(A_+=1/5\), \(A_-=1/9\), and \(z_+=0\), \(z_-^2=2\). Therefore \(\Gamma=1/36+\log(20/27)/2\). The elementary bound \(\log(1-u)\le-u\) with \(u=7/27\) makes this expression strictly negative.

**6. The weak-correlation boundary.** Expanding the explicit analytic coefficients at \(r=0\) gives
\[
C=\frac{\tau^2(2\tau+1)}{2(1+\tau)^2}r^2+O(r^4),\qquad
A_\pm=\frac{\tau(2\tau+1)}{2(1+\tau)^2}r+O(r^2).
\]
Because \(z_+^2-z_-^2=2z_1z_2\), the claimed limit follows. At \(r=0\), the two inducing coordinates are independent and all selection gains add, so \(\Gamma=0\). This completes the classification.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The script reconstructs each Nyström matrix, determinants, inverse and trace for 1,343 deterministic parameter/response cases, compares the resulting set-function defect with the closed form, checks all subset-monotonicity inequalities, verifies the exact counterexample numerically and checks weak-correlation limits. It is independent numerical corroboration; the proof above establishes the quantifiers and strict inequalities over the entire parameter domain.

## Relationship to prior work

Schaub and Zaspel (2026, arXiv:2606.01821) derive and optimize the single-pivot variational free-energy increment for pivoted Cholesky, establishing monotonicity; their inspected derivations and conclusions do not establish the two-site submodularity region above. Cao, Brubaker, Fleet and Hertzmann derive related sparse-GP variational inducing-set optimization formulas and selection procedures; their inspected treatment does not supply this phase diagram. Titsias (2009) establishes the foundational sparse-GP variational objective. The classical submodularity of Gaussian-process **mutual information** in sensor placement (Krause, Singh and Guestrin, 2008) is about a different set function; it cannot be transferred to the response-dependent variational objective by replacing the names of the functions. The present result separates monotonicity from diminishing returns and explicitly quantifies when the latter fails.

## Limitations

The complete classification is for exactly two inducing candidates with equal diagonal kernel entries and positive correlation. It is not a characterization of submodularity for arbitrary large kernels, noise heteroscedasticity, or general inducing locations. Gaussian mutual-information greedy approximation guarantees are unaffected. Prior specialized inducing-subset literature could contain an equivalent two-site statement; historical originality has not been independently established. Matrix checks at finitely many parameters do not replace the proof.

## References

1. L. Schaub and P. Zaspel, *Variational Free Energy Pivot Selection for Pivoted Cholesky*, arXiv:2606.01821 (first publicly posted 2026-06-01), https://arxiv.org/abs/2606.01821.
2. Y. Cao, M. A. Brubaker, D. J. Fleet and A. Hertzmann, *Efficient Optimization for Sparse Gaussian Process Regression*, arXiv:1310.6007, https://arxiv.org/abs/1310.6007.
3. M. Titsias, *Variational Learning of Inducing Variables in Sparse Gaussian Processes*, Proceedings of AISTATS 2009, https://proceedings.mlr.press/v5/titsias09a.html.
4. A. Krause, A. Singh and C. Guestrin, *Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies*, JMLR 9 (2008), https://www.jmlr.org/papers/v9/krause08a.html.
