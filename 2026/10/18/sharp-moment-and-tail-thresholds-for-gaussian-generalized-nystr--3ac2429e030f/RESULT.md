# Sharp moment and tail thresholds for Gaussian generalized Nyström leave-out diagnostics

## Finding

For an identity input matrix, a Gaussian generalized Nyström leave-right-out diagnostic has an exact chi-square-ratio distribution. This yields sharp moment thresholds as the number of left-sketch columns increases. In the square fully sampled case, two alternative diagnostics introduced alongside it have much heavier tails: their squares have no moment of order at least one half, even though the original full-sketch reconstruction is exact.

**Theorem (leave-right-out law and moment boundary).** Let integers \(n\ge s\ge2\) and \(r\ge s\) be arbitrary. Draw independently two matrices \(\Omega\in\mathbb R^{n\times s}\) and \(\Phi\in\mathbb R^{n\times r}\), each with independent standard-normal entries. Take \(A=I_n\) and use exact arithmetic. Delete column \(j\) from \(\Omega\) to obtain \(\Omega_{-j}\), and set
\[
\widehat A_{-j}=\Omega_{-j}(\Phi^{\mathsf T}\Omega_{-j})^\dagger\Phi^{\mathsf T},\qquad
Q_j=\|(I_n-\widehat A_{-j})\omega_j\|_2^2,\qquad
R=\frac1s\sum_{j=1}^s Q_j.
\]
The dagger denotes the Moore–Penrose inverse, and \(\omega_j\) is column \(j\) of \(\Omega\). Define \(d=n-s+1\), \(k=s-1\), and \(\nu=r-s+2\). For every individual index \(j\),
\[
Q_j\ \stackrel{\mathrm d}=\ X_d\left(1+\frac{Y_k}{V_\nu}\right),
\]
where \(X_d,Y_k,V_\nu\) are mutually independent chi-square variables with their respective subscripts as degrees of freedom. This statement is marginal: the \(Q_j\) need not be mutually independent. For each real \(q>0\),
\[
\mathbb E[R^q]<\infty\quad\Longleftrightarrow\quad q<\frac{r-s+2}{2}.
\]
The mean is infinite when \(r=s\); when \(r>s\), it is exactly
\[
\mathbb ER=(n-s+1)\left(1+\frac{s-1}{r-s}\right).
\]
The second moment is finite exactly when \(r\ge s+3\). When \(r=s\) the mean is infinite (so the conventional variance is undefined); when \(s+1\le r\le s+2\), the mean is finite but the variance is infinite. Each individual summand obeys the sharp regularly varying tail
\[
\Pr(Q_j>t)\sim C_{d,k,\nu}\,t^{-\nu/2},\qquad
C_{d,k,\nu}=\frac{2^{\nu/2}\Gamma((k+\nu)/2)\Gamma((d+\nu)/2)}{\Gamma(k/2)\Gamma(d/2)\Gamma(\nu/2+1)}.
\]
The pooled diagnostic satisfies \(\Pr(R>t)=\Theta(t^{-\nu/2})\); no assertion of independent summands or an exact pooled tail constant is made.

**Theorem (square fully sampled pair/twin laws).** In the special case \(s=r=n\ge2\), the full generalized Nyström approximation equals \(I_n\) almost surely. For each \(1\le j,\ell\le n\), define
\[
B_{j\ell}=\phi_\ell^{\mathsf T}\left(I_n-\Omega_{-j}(\Phi_{-\ell}^{\mathsf T}\Omega_{-j})^{-1}\Phi_{-\ell}^{\mathsf T}\right)\omega_j,
\]
where \(\Phi_{-\ell}\) deletes its \(\ell\)-th column; inverses exist almost surely. Define the source's pair and twin **squared** scores by
\[
P=\frac1{n^2}\sum_{j=1}^n\sum_{\ell=1}^n B_{j\ell}^2,\qquad
T=\frac1n\sum_{j=1}^n B_{jj}^2.
\]
For each pair,
\[
B_{j\ell}^2\ \stackrel{\mathrm d}=\ \frac{Z_1^2Z_2^2}{C^2},\qquad
C^2\sim\operatorname{Beta}\left(\frac12,\frac{n-1}{2}\right),
\]
where \(Z_1,Z_2\) are independent standard normals, independent of \(C\). Consequently, for every \(q>0\),
\[
\mathbb E[P^q]<\infty\quad\Longleftrightarrow\quad
\mathbb E[T^q]<\infty\quad\Longleftrightarrow\quad q<\frac12.
\]
In particular, both squared scores have infinite means. The individual pair terms obey
\[
\Pr(B_{j\ell}^2>t)\sim
\frac{4\Gamma(n/2)}{\pi^{3/2}\Gamma((n-1)/2)}t^{-1/2},
\]
and \(\Pr(P>t)=\Theta(t^{-1/2})\), \(\Pr(T>t)=\Theta(t^{-1/2})\).

## Assumptions and scope

The matrices and all norms are real and Euclidean/Frobenius, respectively. Every matrix inverse and pseudoinverse is mathematically exact. The randomized right and left sketches are independent and have independent standard-normal entries. The exact diagnostic definitions include *refitting after each deletion*. We make no claim for reused full-model residuals, deterministic sketches, nonidentity input matrices, complex Gaussians, finite-precision truncation, or regularized pseudoinverses. The standard chi-square and beta distributions have their usual scale parameters. All probabilistic claims are over the joint sketch distribution; all statements involving inverses exclude null sets of zero probability.

The full-sample generalized Nyström approximation for identity input is \(\widehat A=\Omega(\Phi^{\mathsf T}\Omega)^\dagger\Phi^{\mathsf T}\), whereas the leave-out diagnostics assess refitted matrices with fewer columns. Thus, even when \(\widehat A=I_n\), an infinite leave-out mean is not an assertion that the full approximation has positive error.

## Proof

**1. Orthogonal decomposition of the right leave-out residual.** Put \(k=s-1\), \(d=n-k\). Fix a deleted column index. Almost surely \(\Omega_{-j}\) has rank \(k\); let \(U\) be an orthonormal basis for its range and \(V\) an orthonormal basis for its orthogonal complement, so \([U\ V]\) is orthogonal. The pseudoinverse factorization \((\Phi^{\mathsf T}\Omega_{-j})^\dagger\) at full column rank yields the same oblique projection as
\[
\widehat A_{-j}=U(\Phi^{\mathsf T}U)^\dagger\Phi^{\mathsf T}.
\]
The equality follows by writing \(\Omega_{-j}=UC\) for an invertible \(k\)-by-\(k\) matrix \(C\) and observing that \((GC)^\dagger=C^{-1}G^\dagger\) for full-column-rank \(G\). Write \(G=\Phi^{\mathsf T}U\in\mathbb R^{r\times k}\), \(H=\Phi^{\mathsf T}V\in\mathbb R^{r\times d}\), and \(z=V^{\mathsf T}\omega_j\in\mathbb R^d\). Conditional on the retained right columns, \(G\) and \(H\) are independent matrices with independent standard-normal entries; \(z\) is an independent standard-normal vector. Direct expansion then gives the exact, orthogonal identity
\[
(I_n-\widehat A_{-j})\omega_j=Vz-UG^\dagger Hz,\qquad
Q_j=\|z\|_2^2+\|G^\dagger Hz\|_2^2.
\]
Conditional on nonzero \(z\), the vector \(h=Hz/\|z\|_2\) is \(N_r(0,I_r)\); its law does not depend on \(z\) or the retained right columns, and it is independent of \(G\). Therefore, with \(X_d=\|z\|_2^2\sim\chi_d^2\),
\[
Q_j=X_d\bigl(1+\|G^\dagger h\|_2^2\bigr),
\]
with the stated independence between \(X_d\) and the second factor.

**2. Gaussian least-squares coefficient distribution.** Let \(x=G^\dagger h\). Conditional on the full-rank \(r\)-by-\(k\) Gaussian matrix \(G\), \(x\) is centered Gaussian with covariance \((G^{\mathsf T}G)^{-1}\). Integrating its density against the standard Gaussian density of \(G\) gives
\[
f(x)\propto\int_{\mathbb R^{r\times k}}\det(G^{\mathsf T}G)^{1/2}\exp\!\left[-\frac12\operatorname{tr}\bigl(G(I_k+xx^{\mathsf T})G^{\mathsf T}\bigr)\right]\,dG.
\]
The change of variables \(B=G(I_k+xx^{\mathsf T})^{1/2}\) contributes a Jacobian factor \(\det(I_k+xx^{\mathsf T})^{-r/2}\); the square-root Gram determinant contributes a further \(\det(I_k+xx^{\mathsf T})^{-1/2}\). By the determinant lemma, \(f(x)\propto(1+\|x\|_2^2)^{-(r+1)/2}\). This is the isotropic multivariate Student density with \(\nu=r-k+1\) degrees of freedom and the normalization \(x\stackrel{\mathrm d}=g/\sqrt{V_\nu}\), where \(g\sim N_k(0,I_k)\) is independent of \(V_\nu\sim\chi_\nu^2\). Hence \(\|x\|_2^2\stackrel{\mathrm d}=Y_k/V_\nu\), proving the marginal law.

**3. Moment thresholds and exact mean.** For every \(q>0\), all strictly positive moments of chi-square variables are finite. The chi-square lower-tail density shows \(\mathbb E[V_\nu^{-q}]<\infty\) exactly for \(q<\nu/2\). Since \(X_d\), \(Y_k\), and \(V_\nu\) are independent and positive almost surely, \(\mathbb E[Q_j^q]<\infty\) exactly on this range. For finitely many nonnegative variables, the inequalities
\[
\max_j Q_j/s\le R\le\max_j Q_j
\]
show the same sharp threshold for \(R\), without assuming the summands independent. If \(\nu>2\), \(\mathbb EV_\nu^{-1}=1/(\nu-2)\), \(\math EX_d=d\), and \(\math EY_k=k\). These identities yield the displayed mean, including its divergence when \(\nu=2\). The variance is finite precisely when the second moment is, namely \(\nu>4\); all squared scores are nonnegative, so infinite second moment and finite mean imply infinite variance.

**4. Exact tail exponent and single-term coefficient.** Near zero the chi-square cumulative distribution satisfies
\[
\Pr(V_\nu\le\varepsilon)\sim\frac{\varepsilon^{\nu/2}}{2^{\nu/2}\Gamma(\nu/2+1)}.
\]
Condition on the independent \(X_d,Y_k\), use \(Q_j=X_d+X_dY_k/V_\nu\), and split the Gaussian tails to justify dominated regular-variation asymptotics. The tail coefficient is
\[
\frac{\mathbb E[(X_dY_k)^{\nu/2}]}{2^{\nu/2}\Gamma(\nu/2+1)}=C_{d,k,\nu}.
\]
For the pooled score, \(\Pr(Q_1>st)\le\Pr(R>t)\le s\Pr(Q_1>t)\) gives the claimed two-sided order without any assumption about dependence.

**5. Square leave-pair-out and leave-twins-out terms.** Now set \(n=s=r\). Almost surely both \(\Omega\) and \(\Phi\) are invertible; their original full-sketch approximation is exactly \(I_n\). For fixed \(j,\ell\), choose unit normals \(b\) and \(a\) to the respective column spans of \(\Omega_{-j}\) and \(\Phi_{-\ell}\). These are independent uniform directions on the unit sphere (their arbitrary signs are immaterial). The rank-one complement of the refitted oblique projection is
\[
I_n-\widehat A_{-j,-\ell}=\frac{ab^{\mathsf T}}{b^{\mathsf T}a},
\]
so
\[
B_{j\ell}=\frac{(\phi_\ell^{\mathsf T}a)(b^{\mathsf T}\omega_j)}{b^{\mathsf T}a}.
\]
Because the two deleted Gaussian columns are independent of their corresponding retained columns, the numerator factors are independent standard normals, independent of the two random directions. Rotational invariance gives \((b^{\mathsf T}a)^2\sim\operatorname{Beta}(1/2,(n-1)/2)\). The beta density behaves as a positive constant times \(u^{-1/2}\) near zero; thus the inverse-square angular factor has finite \(q\)-th moment exactly for \(q<1/2\). Finite sums of the nonnegative pair terms retain the same threshold (and do not require independence), establishing the pair and twin assertions.

For the tail constant, the density of \(C=b^{\mathsf T}a\) at zero equals \(\Gamma(n/2)/(\sqrt\pi\Gamma((n-1)/2))\). Therefore \(\Pr(1/C^2>t)\sim 2f_C(0)t^{-1/2}\). Multiplication by independent \(Z_1^2Z_2^2\), which has half-moment \(2/\pi\), gives the displayed coefficient. A finite-union argument yields \(\Theta(t^{-1/2})\) for each pooled score, including the twin diagonal subset.

## Verification

The standalone `verify.py` carries out direct refitting of the generalized Nyström estimator in exact-matrix formulas evaluated numerically, compares residuals to two independent coordinate decompositions and to the efficient inverse formula for the square case, compares pair/twin rank-one formulas, and checks the needed inverse chi-square moments by numerical integration. It uses fixed seeded Gaussian matrices and NumPy/SciPy. Running `python verify.py` produced `PASS checks=16453 maximum_numerical_discrepancy=1.76e-08` before packaging. This is finite corroboration of algebraic identities, not a proof of any infinite-tail or global distribution statement; the distribution and moment claims are proved analytically above.

## Relationship to prior work

Lazzarino, Pearce and Pritchard, *Efficient error estimators for Generalized Nyström* (2026), introduce the leave-right-out, leave-pair-out and leave-twins-out scores, including efficient inverse-based computational expressions. The present theorems examine the exact Gaussian laws and moment thresholds of those specific scores at a transparent identity-matrix benchmark. They do not claim to introduce the diagnostic algorithms or the underlying Gaussian inverse-Wishart law.

Nakatsukasa's general Gaussian generalized-Nyström expectation bounds concern different approximation/error objects and explicitly require rank oversampling. Epperly and Tropp establish general unbiasedness for randomized leave-one-out squared errors but do not thereby ensure that such expectations are finite in the zero-oversampling identity case. The cited parameter-dependent randomized approximation analysis provides broad bounds under its own oversampling assumptions. None of these more general results implies the displayed pair/twin angular distribution and its half-order moment boundary. Existing classical multivariate Student and beta-prime identities are background, not claimed novel independently.

## Limitations

The input matrix is exactly identity and the sketches are independent real standard Gaussians. Different input spectra, non-Gaussian sketches, truncation/stabilization, floating-point pseudoinverses, and alternative validation estimands may have different tails. Pooling creates dependencies; only exact **marginal** laws and pooled moment/tail orders are asserted. A distributional identity does not by itself prove a universal algorithmic performance bound. Overlap with an earlier equivalent calculation outside the inspected primary sources remains possible; novelty has not been independently certified.

## References

1. Lazzarino, Pearce, and Pritchard, *Efficient error estimators for Generalized Nyström*, arXiv:2601.11493 (first public version, 2026-01-16), especially Sections 2–4, equations (2.3), (3.1), (3.2), (3.14), (3.15). https://arxiv.org/abs/2601.11493
2. Y. Nakatsukasa, *Fast and stable randomized low-rank matrix approximation*, arXiv:2009.11392, especially the Gaussian expectation theorem. https://arxiv.org/abs/2009.11392
3. E. N. Epperly and J. A. Tropp, *Efficient Error and Variance Estimation for Randomized Matrix Computations*, arXiv:2207.06342, especially the leave-one-out unbiasedness theorem. https://arxiv.org/abs/2207.06342
4. *Randomized low-rank approximation of parameter-dependent matrices*, Numerical Linear Algebra with Applications, doi:10.1002/nla.2576, especially the oversampled expectation estimates. https://doi.org/10.1002/nla.2576
