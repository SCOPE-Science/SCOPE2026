# Dimension-sharp conditioning inflation under symmetric M-matrix row-sum scaling

## Finding

The exact positive symmetric row-sum scaling of a positive definite symmetric \(M\)-matrix can increase spectral conditioning by a factor of order equal to the dimension, even when the original matrix has a dimension-independent condition number. This order is optimal uniformly over the class.

Precisely, let \(A\in\mathbb R^{d\times d}\) be symmetric positive definite with \(A_{ij}\leq0\) for \(i\neq j\). There is a unique vector \(x\in(0,\infty)^d\) such that, for \(X=\operatorname{diag}(x)\), the congruence \(B=XAX\) satisfies \(B\mathbf1=\mathbf1\). Writing \(K=\kappa_2(A)\) and defining condition numbers through the Euclidean operator norm, the following universal bounds hold:

\[
\kappa_2(X)\leq\sqrt{dK},\qquad 1\leq\kappa_2(B)\leq dK.
\]

The dimension exponents are both sharp for every fixed \(K>1\). Set \(c=(K-1)/(K+1)\in(0,1)\), choose an integer \(m\geq2\), and define the \((m+1)\)-dimensional weighted-star matrix

\[
A_m=\begin{pmatrix}1&-c\mathbf1_m^{\mathsf T}/\sqrt m\\ -c\mathbf1_m/\sqrt m&I_m\end{pmatrix},
\]

where the top-right entry denotes the row \(-c\mathbf1_m^{\mathsf T}/\sqrt m\). Its eigenvalues are \(1-c,1,1+c\), where \(1\) has multiplicity \(m-1\), so \(\kappa_2(A_m)=K\) in every dimension. For its uniquely normalized diagonal scaling \(X_m\), write \(t_m\) for the hub-to-leaf scaling ratio. Then

\[
t_m=\frac{\gamma_m+\sqrt{\gamma_m^2+4}}2,\quad
\gamma_m=\frac{c(m-1)}{\sqrt m},\quad
q_m=1-\frac{ct_m}{\sqrt m}>0.
\]

The exact scaling spread and balanced spectral condition number are

\[
\kappa_2(X_m)=t_m,\qquad
\kappa_2(X_mA_mX_m)=\frac{1+t_m^2}{q_m}-1.
\]

Consequently,

\[
\lim_{m\to\infty}\frac{\kappa_2(X_m)}{\sqrt m}=c=\frac{K-1}{K+1},\qquad
\lim_{m\to\infty}\frac{\kappa_2(X_mA_mX_m)}m
=\frac{c^2}{1-c^2}=\frac{(K-1)^2}{4K}>0.
\]

These are exact asymptotic coefficients, not merely fitted slopes. The universal order \(O(\sqrt d)\) for scaling spread and \(O(d)\) for balanced spectral conditioning cannot be improved at any fixed input condition number \(K>1\).

## Assumptions and scope

Matrices are real, finite dimensional, symmetric, positive definite, and have nonpositive off-diagonal entries. The balancing condition is **unit signed row sums of the congruence** \(XAX\), not absolute row norms, similarity balancing \(X^{-1}AX\), or the usual nonnegative Sinkhorn problem. The result is about exact positive scalings and Euclidean spectral condition numbers, not the runtime or floating-point output of any particular scaling algorithm. The star family is defined for every integer \(m\geq2\) and every fixed \(c\in(0,1)\). The upper-bound theorem also holds for reducible matrices and every dimension \(d\geq1\).

## Proof

**1. Unique existence of the exact scaling.** On the positive orthant consider the strictly convex function

\[
\Phi(x)=\tfrac12x^{\mathsf T}Ax-\sum_{i=1}^{d}\log x_i.
\]

Its Hessian \(A+\operatorname{diag}(x_i^{-2})\) is positive definite. If \(\|x\|_2\to\infty\), the positive quadratic term grows at least like \(\lambda_{\min}(A)\|x\|_2^2/2\) and dominates the logarithmic term. At a finite boundary point with some \(x_i\downarrow0\), the corresponding negative logarithm diverges to \(+\infty\). Therefore \(\Phi\) has a unique interior minimizer. Stationarity reads \(Ax=x^{-1}\) coordinatewise, or equivalently \(XAX\mathbf1=\mathbf1\).

**2. Dimension-dependent upper bounds.** Write \(\lambda_-=\lambda_{\min}(A)>0\) and \(\lambda_+=\lambda_{\max}(A)\). The normalized equations give

\[
1=x_i(Ax)_i\leq A_{ii}x_i^2\leq\lambda_+x_i^2,
\]

using the nonpositive off-diagonal entries. Also

\[
d=x^{\mathsf T}Ax\geq\lambda_-\|x\|_2^2.
\]

It follows that \(\min_i x_i^2\geq1/\lambda_+\), \(\max_i x_i^2\leq d/\lambda_-\), and \(\kappa_2(X)\leq\sqrt{d\lambda_+/\lambda_-}\). Since \(B\) has nonpositive off-diagonal entries and all row sums one, its off-diagonal entries are the negatives of the edge weights of a weighted graph, so \(B=I+L\), where \(L\succeq0\) is a graph Laplacian. Thus \(\lambda_{\min}(B)=1\). Finally,

\[
\lambda_{\max}(B)\leq\lambda_+\|X\|_2^2
\leq d\lambda_+/\lambda_-=dK,
\]

establishing both universal bounds.

**3. Positive definiteness and exact hub/leaf scaling of the star.** Let \(m\geq2\). The star matrix \(A_m\) is the identity minus a rank-two symmetric matrix with nonzero eigenvalues \(\pm c\), so its spectrum is \(\{1-c,1,1+c\}\) with the stated multiplicities. Uniqueness and invariance under permutations of leaves force the scaling vector to have the form \(x=(a,b,\ldots,b)\), \(a,b>0\). The row-sum equations reduce to

\[
a^2-c\sqrt m\,ab=1,\qquad
b^2-\frac{c}{\sqrt m}ab=1.
\]

With \(t=a/b\), equating the two expressions for \(b^{-2}\) yields \(t^2-\gamma_m t-1=0\). Its unique positive root is the stated \(t_m\). Since the polynomial is negative at zero and positive at \(\sqrt m/c\), one has \(0<t_m<\sqrt m/c\) and hence \(q_m>0\). Then \(b^2=q_m^{-1}\), \(a^2=t_m^2q_m^{-1}\). For \(m>1\), \(\gamma_m>0\), so \(t_m>1\) and \(\kappa_2(X_m)=t_m\).

**4. Complete balanced spectrum.** On the \((m-1)\)-dimensional subspace of zero-sum leaf vectors, \(B_m=X_mA_mX_m\) acts by \(b^2=q_m^{-1}>1\). On the complementary hub-plus-uniform-leaves plane its matrix is

\[
\begin{pmatrix}a^2&-cab\\-cab&b^2\end{pmatrix}.
\]

As \(B_m\mathbf1=\mathbf1\), one eigenvalue there is \(1\); the other is its trace minus one, namely \(a^2+b^2-1\). The hub equation gives \(a^2-1=c\sqrt m\,ab>0\), so \(a^2+b^2-1>b^2>1\). Therefore its exact extreme eigenvalues are \(1\) and \(a^2+b^2-1\), proving the stated condition-number formula.

**5. Limiting constants and sharpness of the dimension exponents.** From \(\gamma_m/\sqrt m\to c\), the explicit positive root satisfies \(t_m/\sqrt m\to c\). Hence \(q_m\to1-c^2\), which is strictly positive. Thus \(\kappa_2(X_m)/\sqrt m\to c\) and

\[
\frac{a^2+b^2-1}{m}
=\frac{t_m^2/m+1/m}{q_m}-\frac1m
\longrightarrow\frac{c^2}{1-c^2}.
\]

Since \(\kappa_2(A_m)=K\) is independent of \(m\), no universal bound with a smaller power of the dimension can hold at this fixed \(K>1\). Substituting \(c=(K-1)/(K+1)\) yields \(c^2/(1-c^2)=(K-1)^2/(4K)\).

## Verification

The standalone `CHECK.py` implements the hub/leaf equations and closed-form eigenvalue calculation in 70-digit decimal arithmetic for three coupling parameters and seven increasing star sizes. `CHECK_OUTPUT.txt` records its run. All checked equations and the input-condition-number bound match the analytic identities to the stated precision, and the normalized asymptotic coefficients approach their exact limits. This finite replay is independent supporting evidence; the theorems for all dimensions follow from the analytic proof above. Invoke `python3 CHECK.py` using Python's standard library.

## Relationship to prior work

Liu, Sidford and Tu [1] develop a polylogarithmic-iteration algorithm for exactly the symmetric positive definite \(M\)-matrix row-sum-scaling problem. They explicitly track the diagonal scaling spread in the precision analysis, but the inspected main theorem and scaling-spread lemma do not quantify the sharp dimension-order inflation of the *balanced matrix's* spectral condition number. Vladu [2] studies an earlier interior-point approach to the same exact scaling objective; his stated results concern algorithmic complexity rather than the exact spectrum of a scaled weighted star. The general observation that scaling may harm conditioning is older; the finding here is the **quantitative matching upper bound and bounded-condition-number star witness for this specific signed symmetric congruence problem**, not the general warning. The eigenvalue problems and diagonal transformations discussed for similarity balancing [3] concern a distinct objective and do not imply these exact congruence results.

## Limitations

Neither the factor \(dK\) nor \(\sqrt{dK}\) is asserted to have a sharp constant for every fixed dimension or input condition number. What is sharp is their dimension **exponent** at each fixed \(K>1\), and the star family has explicit asymptotic leading coefficients. No claim concerns nonlinear convergence rates, the stability of an implementation, approximate row-sum scaling, or the efficiency of using the balancing transform as a preconditioner for all right-hand sides. Related matrix-equilibration literature may contain equivalent star counterexamples under a different description; this remains an originality risk. Independent verification has not been performed.

## References

[1] C.-H. Liu, A. Sidford and T.-W. Tu, *Near-Optimal Parallel M-Matrix Scaling* (first publicly posted 2026-10-15), arXiv:2610.22302, especially Section 1, Theorem 3.9 and Claim 3.8. https://arxiv.org/pdf/2610.22302

[2] A. Vladu, *Breaking the Barrier of Self-Concordant Barriers: Faster Interior Point Methods for M-Matrices* (2025), arXiv:2504.20619, especially Section 1.1, Theorem 1. https://arxiv.org/pdf/2504.20619

[3] R. James, J. Langou, B. R. Lowery, *On matrix balancing and eigenvector computation* (2014), arXiv:1401.5766. https://arxiv.org/abs/1401.5766
