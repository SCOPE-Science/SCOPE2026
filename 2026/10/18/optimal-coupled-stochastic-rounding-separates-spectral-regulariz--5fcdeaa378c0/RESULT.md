# Optimal coupled stochastic rounding separates spectral regularization from finite-sample rank recovery

## Finding

For a rank-one matrix consisting of identical two-coordinate rows, coupling the two unbiased stochastic-rounding decisions changes the least singular value of the rounded matrix, even though the marginal rounding law of each entry is fixed. The exact optimal coupling is the admissible Fréchet coupling that most nearly cancels the total Gram off-diagonal. Its almost-sure limiting squared least singular value is at most twice that produced by independent entrywise rounding, and the factor two is attained.

For a symmetric midpoint family, however, the coupling that maximizes the limiting least singular value is *not* the coupling that minimizes finite-sample rank-deficiency probability. The spectral optimum is perfectly antithetic, while the unique rank-recovery optimum distributes probability equally among three distinct row directions. This gives a sharp and explicit conflict between two natural measures of numerical regularization.

## Assumptions and scope

Choose real numbers \(\ell_1,\ell_2\in\mathbb R\), steps \(h_1,h_2>0\), and marginal high-rounding probabilities \(p,q\in(0,1)\). Each coordinate rounds between two neighboring representable values, \(\ell_j\) and \(\ell_j+h_j\), with its prescribed unbiased Bernoulli probability. Set \(u=\ell_1+h_1p\) and \(v=\ell_2+h_2q\). For every integer \(n\ge1\), the unrounded real matrix \(A_n\in\mathbb R^{n\times2}\) has every row equal to \((u,v)\), and has rank one provided \((u,v)\ne(0,0)\), which we assume throughout.

The rounded row is \((\ell_1+h_1X,\ell_2+h_2Y)\), with \(\Pr(X=1)=p\), \(\Pr(Y=1)=q\) and arbitrary within-row dependence. Write \(\tau=\Pr(X=1,Y=1)\). Nonnegative joint atom probabilities require exactly
\[
\tau_-:=\max\{0,p+q-1\}\le\tau\le\tau_+:=\min\{p,q\}.
\]
For every fixed \(\tau\), rows are independent and identically distributed, and their joint law remains fixed as \(n\) grows. No independence is assumed between the two coordinates of the same row. Denote the rounded matrix by \(\widetilde A_n(\tau)\). For every row count, define its smallest *column* singular value by \(\sigma_{\min}(B):=\sqrt{\lambda_{\min}(B^\mathsf TB)}\), including when there is only one row. The baseline called 'independent rounding' is \(\tau_0=pq\).

## Proof

### Population Gram and exact optimal dependence

The four row states, indexed by \((X,Y)=(0,0),(0,1),(1,0),(1,1)\), have respective probabilities
\[
1-p-q+\tau,\quad q-\tau,\quad p-\tau,\quad\tau.
\]
The row second-moment matrix is the explicitly computable positive-semidefinite matrix
\[
G(\tau)=\begin{pmatrix}
 u^2+h_1^2p(1-p)&uv+h_1h_2(\tau-pq)\\
 uv+h_1h_2(\tau-pq)&v^2+h_2^2q(1-q)
\end{pmatrix}.
\]
The strong law of large numbers applied to each of its three independent-across-row empirical moments, followed by continuity of ordered eigenvalues, proves
\[
\frac{\sigma_{\min}(\widetilde A_n(\tau))^2}{n}
\xrightarrow[n\to\infty]{\text{a.s.}}\lambda_{\min}(G(\tau)).
\]
The diagonal entries of \(G\) do not depend on \(\tau\). For a real symmetric two-by-two matrix with fixed diagonal entries \(a,b\), its smallest eigenvalue equals
\[
\frac{a+b-\sqrt{(a-b)^2+4c^2}}2,
\]
which is strictly decreasing with \(|c|\). Since the Gram off-diagonal is the strictly increasing affine function \(c(\tau)=uv+h_1h_2(\tau-pq)\), the unique optimizer over every admissible coupling is
\[
\boxed{\tau_{\mathrm{spec}}=
\operatorname{proj}_{[\tau_-,\tau_+]}\left(pq-\frac{uv}{h_1h_2}\right).}
\]
Here projection onto a closed interval means clipping below to the left endpoint and above to the right endpoint. This is the complete optimal-coupling formula, including both boundary cases and the possible interior optimizer. In particular, when both lower rounding endpoints are positive the Gram cross-moment \(uv+h_1h_2(\tau-pq)\) is positive for every admissible \(\tau\); then the optimizer simplifies to the maximally anticorrelated Fréchet endpoint \(\tau_-=\max\{0,p+q-1\}\).

### Universal sharp factor two

Put \(s_1=h_1\sqrt{p(1-p)}\), \(s_2=h_2\sqrt{q(1-q)}\), and \(c=h_1h_2(\tau-pq)\). The noise covariance matrix is
\[
\Sigma(\tau)=\begin{pmatrix}s_1^2&c\\c&s_2^2\end{pmatrix},
\qquad G(\tau)=\begin{pmatrix}u\\v\end{pmatrix}(u,v)+\Sigma(\tau).
\]
Since this is a covariance matrix, \(|c|\le s_1s_2\). Its comparison to the independent-noise covariance \(\Sigma_0=\operatorname{diag}(s_1^2,s_2^2)\) obeys
\[
2\Sigma_0-\Sigma(\tau)=
\begin{pmatrix}s_1^2&-c\\-c&s_2^2\end{pmatrix}\succeq0.
\]
It follows that \(G(\tau)\preceq2G(pq)\), because the remaining difference contains the nonnegative outer product \((u,v)^\mathsf T(u,v)\). By monotonicity of the smallest eigenvalue under Loewner order,
\[
\boxed{\lambda_{\min}(G(\tau))\le2\lambda_{\min}(G(pq))\quad\text{for every admissible }\tau.}
\]
The independent matrix is positive definite because \(p,q\in(0,1)\), so this is also a finite bound on the ratio. Attainment is shown below.

### Sharp symmetric midpoint model and finite-sample separation

Specialize to equal positive lower endpoints \(\ell_1=\ell_2=L>0\), equal positive steps \(h_1=h_2=h>0\), and midpoint marginals \(p=q=1/2\). Thus \(u=v=L+h/2\) and \(0\le\tau\le1/2\). The population Gram has identical diagonal entries and positive off-diagonal entry \(u^2+h^2(\tau-1/4)\). Its antisymmetric eigenvector \((1,-1)\) therefore yields the smaller eigenvalue
\[
\boxed{\lambda_{\min}(G(\tau))=h^2(1/2-\tau).}
\]
Consequently the unique spectral optimum \(\tau_{\mathrm{spec}}=0\) has value \(h^2/2\), whereas independent rounding \(\tau=1/4\) gives \(h^2/4\): the factor two is attained exactly for every \(L,h>0\).

For finite \(n\), rounded rows occupy one of three *positive rays*. The two diagonal states \((L,L)\) and \((L+h,L+h)\) lie on the same ray and have combined probability \(2\tau\). The remaining states \((L+h,L)\) and \((L,L+h)\) generate two distinct rays, each of probability \(1/2-\tau\). Any two vectors from different such rays are linearly independent: this uses \(L>0\) and \(h>0\). Hence the rounded matrix has rank below two if and only if **all** of its \(n\) rows lie on the **same** ray. Independence of the rows proves the exact formula for every integer \(n\ge1\):
\[
\boxed{\Pr\{\operatorname{rank}\widetilde A_n(\tau)<2\}
=(2\tau)^n+2(1/2-\tau)^n.}
\]
For \(n\ge2\), strict convexity of \(x\mapsto x^n\) and the fact that the three ray masses sum to one imply a **unique** probability minimum when all three masses equal \(1/3\). The unique rank-optimal coupling is therefore \(\tau_{\mathrm{rank}}=1/6\), with
\[
\boxed{\min_{0\le\tau\le1/2}\Pr\{\operatorname{rank}\widetilde A_n(\tau)<2\}=3^{1-n}.}
\]
The spectral optimum \(\tau=0\) instead incurs rank-deficiency probability \(2^{1-n}\), strictly larger for all \(n\ge2\), although its normalized asymptotic squared least singular value \(h^2/2\) strictly exceeds the rank-optimal value \(h^2/3\). Independent rounding has probability \(2^{-n}+2^{1-2n}\) and asymptotic squared least singular value \(h^2/4\). These are different and noninterchangeable optimization objectives.

A concrete exact binary floating-point example uses the adjacent precision-two numbers \(L=1\) and \(L+h=3/2\), with midpoint \(5/4\). The three respective normalized squared least-singular limits for spectral-optimal, rank-optimal and independent coupling are \(1/8\), \(1/12\), and \(1/16\). For four rows, their respective rank-deficiency probabilities are \(1/8\), \(1/27\), and \(9/128\).

## Verification

The accompanying `check.py` uses only the Python standard library, including exact rational arithmetic. Run `python check.py` to reproduce the 58,566 checks of joint probability atoms, exact second moments, the optimal-coupling and covariance comparisons, finite-row enumeration, and sampled Gram limits. Output includes all six exact constants in the concrete example. Finite calculations check the derived identities but are **not** the proof of the almost-sure limit or of the universal quantifiers; those follow from the strong law, matrix Loewner comparison, and elementary exact enumeration of row rays.

## Relationship to prior work

Dexter, Boutsikas, Ma, Ipsen and Drineas (2024 preprint; 2025 journal publication) introduced stochastic rounding as a mechanism increasing small singular values for tall-and-thin matrices. Their Section 2.2 explicitly treats independent entrywise rounding errors. Ma, Yu and Drineas (first public preprint 2026-05-29) broadened the spectral-regularization analysis to wider aspect ratios and tail spectral clusters; Section 2.2 explicitly assumes rounding errors independent across coordinate indices and a diagonal noise Gram expectation. The present result **changes the model** by allowing correlated coordinate decisions within each independently sampled row. It does not claim to improve or invalidate those papers' guarantees for independent rounding. Classical Fréchet bounds already characterize feasible joint Bernoulli couplings; the proposed new synthesis concerns the *exact spectral optimizer*, *universal sharp factor-two bound*, and *incompatible finite-sample rank optimizer* under identical marginals. Existing broad random-matrix and antithetic-variates theory can overlap conceptually without yielding this exact combined statement.

## Limitations

Only two columns, two-point unbiased rounding at fixed representable adjacent endpoints, fixed joint coupling across independently sampled rows, and a nonzero rank-one repeated-row input are analyzed. The strong-law limit is for a fixed coupling as the number of rows tends to infinity. The finite-sample rank optimum is proved only for symmetric midpoint inputs (and \(n\ge2\)). Finite-sample singular-value expectations and quantiles are not optimized. Correlated stochastic rounding is a deliberate alternative to independent-entry schemes; the result does not establish its benefit for arbitrary matrix problems, practical hardware, or downstream optimization accuracy.

## References

1. Linkai Ma, Tingzhou Yu and Petros Drineas, *Stochastic Rounding Increases Small Singular Values*, arXiv:2606.00312 (first public preprint 2026-05-29), https://arxiv.org/abs/2606.00312 . Relevant: Section 2.2 and conclusions.
2. Gregory Dexter, Christos Boutsikas, Linkai Ma, Ilse C. F. Ipsen and Petros Drineas, *Stochastic Rounding Implicitly Regularizes Tall-and-Thin Matrices*, arXiv:2403.12278 (first posted 2024-03-18), https://arxiv.org/pdf/2403.12278 ; later *SIAM Journal on Matrix Analysis and Applications* 46 (2025), 341–369, https://doi.org/10.1137/24M1647679 . Relevant: Section 2.2, Theorem 2 and Section 4.
