# A dimension-root hierarchy for Gaussian-start Lanczos detection of an isolated negative Hessian mode

## Finding
Fix an integer \(q\ge1\) and distinct constants \(0<b_1<\cdots<b_q\). For each positive integer \(n\) in a sequence tending to infinity, choose integer multiplicities \(m_{j,n}\ge1\) satisfying \(1+\sum_{j=1}^{q}m_{j,n}=n\) and \(m_{j,n}/n\to p_j>0\), so \(\sum_jp_j=1\). Let \(a_n>0\), and define a symmetric indefinite matrix
\[
 H_n=\operatorname{diag}(-a_n,b_1I_{m_{1,n}},\ldots,b_qI_{m_{q,n}}).
\]
Launch exact-arithmetic Lanczos from one direction distributed uniformly on the unit sphere. Let \(\theta_{\ell,n}\) be the least Ritz value after \(\ell\) Krylov basis vectors. For \(1\le\ell\le q\), write \(u_\ell(z)=(1,z,\ldots,z^{\ell-1})^{\mathsf T}\). Then there are independent random variables \(U\sim\chi^2_1\) and \(Z_j\sim\chi^2_{m_{j,n}}\) such that, with
\[
 B_{\ell,n}=\sum_{j=1}^q b_jZ_j u_\ell(b_j)u_\ell(b_j)^{\mathsf T},
\]
the exact, finite-dimensional detection event is
\[
 \boxed{\theta_{\ell,n}<0\quad\Longleftrightarrow\quad
 a_nU\,u_\ell(-a_n)^{\mathsf T}B_{\ell,n}^{-1}u_\ell(-a_n)>1.}
\]
The matrix \(B_{\ell,n}\) is positive definite almost surely. The strict boundary has probability zero.

Define the deterministic positive-definite moment matrix and its last inverse diagonal entry
\[
 G_\ell=\sum_{j=1}^q b_jp_j u_\ell(b_j)u_\ell(b_j)^{\mathsf T},\qquad
 L_\ell=(G_\ell^{-1})_{\ell\ell}>0.
\]
For any sequence with \(a_n/n^{1/(2\ell-1)}\to t\) in the extended interval \([0,\infty]\), the detection probability has the sharp limit
\[
 \boxed{\lim_{n\to\infty}\mathbb P(\theta_{\ell,n}<0)=
 \begin{cases}
 0,&t=0,\\
 \mathbb P\!\left(\chi^2_1>1/(L_\ell t^{2\ell-1})\right),&0<t<\infty,\\
 1,&t=\infty.
 \end{cases}}
\]
Thus the critical spike magnitude for detection in \(\ell\) steps is \(n^{1/(2\ell-1)}\). The hierarchy ends deterministically: the \((q+1)\)-step space contains a negative-curvature direction almost surely, for every finite \(n\) and \(a_n>0\).

For two positive bands, \(0<b<c\), with asymptotic fractions \(p\) and \(1-p\), the constants become
\[
 L_1=\frac{1}{bp+c(1-p)},\qquad
 L_2=\frac{bp+c(1-p)}{bc\,p(1-p)(b-c)^2}.
\]
Consequently one step requires a spike of order \(n\) for nontrivial detection probability, two steps order \(n^{1/3}\), and three steps detect with probability one.

## Assumptions and scope
All matrices are real symmetric and the starting direction is a normalized vector of independent standard real Gaussian coordinates. The positive spectral locations \(b_j\) and number of positive bands \(q\) are fixed across \(n\), their asymptotic proportions are positive, and one negative eigenvalue has multiplicity exactly one. For \(1\le\ell\le q+1\), full Krylov dimension \(\ell\) holds almost surely because all \(q+1\) distinct spectral values have nonzero Gaussian weights. The result concerns the unmodified least Ritz value as a negative-curvature diagnostic, not a safeguarded Newton step, and is an exact-arithmetic statement.

## Proof
**1. Spectral weights and polynomial parametrization.** Take independent standard Gaussian coordinates \(g\), and normalize to \(v=g/\|g\|_2\). The negative-eigenspace squared weight before normalization is \(U=g_1^2\sim\chi^2_1\). The sum of squared coordinates in positive spectral band \(j\) is an independent \(Z_j\sim\chi^2_{m_{j,n}}\). For any polynomial \(P\) of degree at most \(\ell-1\), the Krylov vector \(P(H_n)v\) has quadratic form
\[
 \langle P(H_n)v,H_nP(H_n)v\rangle
 =\frac{-a_nU\,P(-a_n)^2+\sum_{j=1}^q b_jZ_j P(b_j)^2}{U+\sum_jZ_j}.
\]
The denominator is positive; its value does not affect whether a negative direction exists. Write \(P(z)=c^{\mathsf T}u_\ell(z)\). Its numerator is the quadratic form in \(c\) of the matrix
\[
 B_{\ell,n}-a_nU\,u_\ell(-a_n)u_\ell(-a_n)^{\mathsf T}.
\]
Because \(q\ge\ell\), the \(q\times\ell\) Vandermonde matrix of distinct positive nodes has full column rank, and every \(b_jZ_j>0\) almost surely. Hence \(B_{\ell,n}\succ0\).

**2. The exact event.** For a positive-definite \(B\) and \(s\ge0\), the rank-one downdate \(B-suu^{\mathsf T}\) has a negative eigenvalue if and only if \(s\,u^{\mathsf T}B^{-1}u>1\). This follows by congruence with \(B^{-1/2}\), whose resulting matrix has eigenvalues \(1\) except for \(1-s\|B^{-1/2}u\|_2^2\). The least Ritz value is negative precisely when the Rayleigh quotient of some nonzero vector in the Krylov space is negative. Combining these observations proves the finite-\(n\) identity. Conditional on all \(Z_j\), the boundary fixes one value of the continuously distributed \(U\), so it has probability zero.

**3. Limiting critical scales.** By concentration of chi-square variables with degrees \(m_{j,n}\to\infty\), one has \(Z_j/n\to p_j\) in probability. Thus \(B_{\ell,n}/n\to G_\ell\) and its inverse converges to \(G_\ell^{-1}\) in probability. To check \(G_\ell\succ0\), again use the full-rank Vandermonde argument with strictly positive weights \(b_jp_j\). Setting \(a_n=n^{1/(2\ell-1)}t_n\), when \(t_n\to t\in(0,\infty)\), expand the polynomial
\[
 \frac{a_n}{n}u_\ell(-a_n)^{\mathsf T}(B_{\ell,n}/n)^{-1}u_\ell(-a_n).
\]
Its highest degree in \(a_n\) is \(a_n^{2\ell-1}/n\), with leading coefficient tending in probability to \(L_\ell\); every lower power vanishes after division by \(n\). The expression therefore converges to \(t^{2\ell-1}L_\ell\). If \(t_n\to0\), the positive quadratic form is bounded in probability by \(C a_n(1+a_n^{2\ell-2})/n\to0\). If \(t_n\to\infty\), the normalized leading coefficient stays bounded away from zero in probability and the expression diverges to infinity. Multiplying by the independent \(U\sim\chi^2_1\), then using continuity and positivity of its law, proves all three probability limits. The case \(\ell=1\) is included; the polynomial contains a single constant monomial.

**4. Guaranteed detection after \(q+1\) steps.** The polynomial \(P(z)=\prod_{j=1}^q(z-b_j)\) has degree \(q\). It annihilates every positive spectral band and does not annihilate the negative mode since \(P(-a_n)\ne0\). Consequently the nonzero Krylov vector \(P(H_n)v\) lies entirely in the negative eigenspace almost surely, has negative Rayleigh quotient, and gives \(\theta_{q+1,n}=-a_n<0\).

**5. Two-band constants.** With \(u_2(z)=(1,z)^{\mathsf T}\), the determinant of \(G_2\) is \(bc\,p(1-p)(b-c)^2\). The lower-right entry of its inverse is its upper-left entry divided by that determinant, giving the stated \(L_2\). The \(\ell=1\) identity is immediate.

## Verification
The companion `check.py` computes the exact rank-one statistic and the actual symmetric Krylov-compressed Ritz eigenvalues for multiple randomly selected small spectra, weights, negative spikes, and Krylov dimensions; it checks a rational symbolic identity, the full Krylov exhaustion in a two-positive-band example, and one large-dimensional chi-square probability calculation. It requires Python 3, NumPy, and SciPy and runs with `python check.py`. It is supplementary numerical checking: the finite-dimensional equivalence and asymptotic trichotomy are established analytically above, not by experimental enumeration.

## Relationship to prior work
Ansari-Önnestam, Forsgren, and Gill (2026) analyze modified Newton-CG and Lanczos-based handling of nonpositive curvature, including possible early termination. Their work does not provide an exact finite-dimensional Gaussian-start detection probability for an isolated negative mode, nor the dimension-root sequence of critical spike scales in the unmodified Ritz diagnostic.

The classical randomized-Lanczos literature, including Kuczyński and Woźniakowski (1992, 1994) and van Dorsselaer, Hochstenbach, and van der Vorst (1999), studies eigenvalue approximation probabilities and probabilistic spectral bounds. The present assertion is more specialized: an exact sign-detection event for one negative spectral spike against finitely many positive bands, together with explicit critical scaling limits. The rank-one downdate identity and polynomial moments themselves are classical and are not claimed as new.

## Limitations
The theorem does not cover a continuously varying positive spectral distribution, a growing number of positive spectral bands, negative eigenvalues of higher multiplicity, correlated starting directions, adaptive changes to the Hessian, or floating-point rounding. The detection diagnostic is not a guarantee for any particular modified Newton algorithm. The random-start spectral hierarchy may follow from an unlocated specialized result in the older Lanczos literature; publication priority is not independently established.

## References
1. A. Ansari-Önnestam, A. Forsgren, and P. E. Gill, *On Modified Newton Methods for Unconstrained Optimization Based on Lanczos Tridiagonalization* (2026), arXiv:2610.31110, first public 2026-10-22. https://arxiv.org/abs/2610.31110
2. J. L. M. van Dorsselaer, M. E. Hochstenbach, and H. A. van der Vorst, *Computing probabilistic bounds for extreme eigenvalues of symmetric matrices with the Lanczos method* (1999), CWI MAS-R9934. https://ir.cwi.nl/pub/4505/04505D.pdf
3. J. Kuczyński and H. Woźniakowski, *Estimating the largest eigenvalue by the power and Lanczos algorithms with a random start* (1992), SIAM J. Matrix Anal. Appl. 13, 1094–1122. https://doi.org/10.1137/0613066
4. J. Kuczyński and H. Woźniakowski, *Probabilistic bounds on the extremal eigenvalues and condition number by the Lanczos algorithm* (1994), SIAM J. Matrix Anal. Appl. 15, 672–691. https://doi.org/10.1137/S0895479892230456
