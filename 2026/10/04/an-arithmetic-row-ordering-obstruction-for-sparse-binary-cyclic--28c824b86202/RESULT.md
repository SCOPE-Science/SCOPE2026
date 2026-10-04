# An arithmetic row-ordering obstruction for sparse-binary cyclic permutation tests
## Finding
Consider the cyclic permutation test (CPT) of Lei and Bickel in the scalar case \(p=r=1\) with the saturated choice \(m=n-1\), so that the marginal-rank test uses \(n\) cyclic statistics and has nominal level \(\alpha=1/n\). Let the design column \(x\in\{0,1\}^n\) contain exactly two ones. After an irrelevant cyclic shift, place them at positions \(0\) and \(d\), where \(1\le d\le n-1\), and write
\[
g=\gcd(n,d),\qquad N=\frac{n}{g}.
\]
Let \(O^*(x)\) denote the normalized signal-gap proxy defined by Theorem 2 of Lei and Bickel. Then
\[
O^*(x)=0\quad\text{if \(N\) is even},
\]
and, if \(N\) is odd,
\[
(O^*(x))^2=\frac{4n}{nN-1}.
\]
Thus the row-ordering problem is solved exactly for this sparse binary design. Every ordering has zero proxy if and only if \(n\) is a power of two. Otherwise, if \(q\) is the smallest odd prime factor of \(n\),
\[
\max_{\text{row orderings}} O^*(x)=\sqrt{\frac{4n}{nq-1}},
\]
and the maximizers are exactly the cyclic separations with \(\gcd(n,d)=n/q\).

At nominal level \(0.05\), the saturated case is \(n=20\). Here \(q=5\). Only \(d\in\{4,8,12,16\}\) give a positive proxy, all with
\[
O^*(x)=\sqrt{\frac{80}{99}}\approx 0.898933149950989.
\]
The other \(15\) of the \(19\) oriented nonzero cyclic separations give \(O^*(x)=0\).

## Assumptions and scope
The design has one tested predictor and no nuisance predictors beyond the intercept, \(n\ge3\), and exactly two entries of the tested design column equal one. The CPT uses \(m=n-1\), which is the saturated scalar setting of the source construction; if the null statistics have no ties, its marginal-rank calibration is exact at \(\alpha=1/n\). The theorem concerns the source paper's design-based proxy \(O^*\), not the complete power function of every possible CPT implementation. In particular, \(O^*=0\) means that the source's condition-C3 signal gap cannot be made positive for that ordering; it is not asserted here that no other statistic or test can have power.

## Proof
For \(m=n-1\), let \(v_j\) be the \(j\)-th cyclic shift of \(x\), with \(j=0,\ldots,n-1\). Theorem 2 of Lei and Bickel writes \(O^*\) as the norm of the residual after regressing the first cyclic-difference column on the remaining cyclic-difference columns. Equivalently,
\[
O^*(x)=\operatorname{dist}\!\left(v_0,\operatorname{aff}\{v_1,\ldots,v_{n-1}\}\right).
\]

Define the unnormalized discrete Fourier transform
\[
\widehat x_k=\sum_{j=0}^{n-1}x_j\exp\!\left(-\frac{2\pi i k j}{n}\right),\qquad k=0,\ldots,n-1.
\]
The cyclic-shift matrix with columns \(v_j\) is circulant. If every non-DC coefficient \(\widehat x_k\), \(1\le k\le n-1\), is nonzero, Fourier diagonalization of that circulant matrix gives the exact altitude identity
\[
(O^*(x))^2
=\frac{n}{\displaystyle\sum_{k=1}^{n-1}|\widehat x_k|^{-2}}.
\]
One direct derivation is to choose the affine-hyperplane normal \(a\) so that the vector of inner products with the cyclic shifts is \(e_0-n^{-1}\mathbf 1\). Its non-DC unitary-Fourier coordinates have modulus \(n^{-1/2}|\widehat x_k|^{-1}\), so the squared norm of \(a\) is \(n^{-1}\sum_{k=1}^{n-1}|\widehat x_k|^{-2}\); the affine gap in this normalization is one. If some non-DC \(\widehat x_k\) vanishes, a real Fourier null vector has coefficient sum zero and nonzero coefficient at the zeroth shift, giving an affine dependence that places \(v_0\) in the affine hull of the other shifts. Hence \(O^*(x)=0\).

For two ones at positions \(0\) and \(d\),
\[
|\widehat x_k|^2
=|1+e^{-2\pi i k d/n}|^2
=4\cos^2\!\left(\frac{\pi k d}{n}\right).
\]
Write \(d=g d'\) and \(n=gN\), so \(\gcd(d',N)=1\). If \(N\) is even, then \(d'\) is odd and \(k=N/2\) makes the cosine zero, so \(O^*=0\).

Suppose \(N\) is odd. Multiplication by \(d'\) permutes the nonzero residues modulo \(N\). Among \(k=1,\ldots,n-1\), residue zero modulo \(N\) occurs \(g-1\) times and every nonzero residue occurs \(g\) times. Using the standard trigonometric identity
\[
\sum_{r=0}^{N-1}\sec^2\!\left(\frac{\pi r}{N}\right)=N^2\qquad(N\text{ odd}),
\]
which follows from the shifted cosecant-square multiplication formula, yields
\[
\sum_{k=1}^{n-1}|\widehat x_k|^{-2}
=\frac14\left[(g-1)+g(N^2-1)\right]
=\frac{nN-1}4.
\]
Substitution into the altitude identity proves
\[
(O^*)^2=\frac{4n}{nN-1}.
\]

For fixed \(n\), a positive proxy requires an odd divisor \(N>1\) of \(n\), and the displayed value decreases strictly as \(N\) increases. Therefore positive proxy is impossible for every ordering exactly when \(n\) has no odd divisor greater than one, i.e. exactly when \(n\) is a power of two. Otherwise the smallest feasible \(N\) is the smallest odd prime factor \(q\), giving the stated maximum. The condition \(N=q\) is equivalent to \(\gcd(n,d)=n/q\).

## Verification
The accompanying `verify.py` independently constructs the Theorem-2 residual using Gram--Schmidt projection and compares it with the Fourier formula. It exhaustively checks every two-one separation for each \(3\le n\le30\), checks the parity/gcd closed form, checks the global optimizer, and checks the \(n=20\) corollary. Replaying the packaged script returns `VERIFY_OK`.

The proof itself is algebraic and does not depend on finite enumeration. The computation is a consistency check, not a substitute for the Fourier and number-theoretic argument.

## Relationship to prior work
Lei and Bickel define \(O^*(X)\) as a proxy for signal strength, give its general least-squares residual representation in Theorem 2, emphasize that it changes under row permutations, and formulate maximizing it over row orderings as a nonlinear traveling-salesman problem. They use heuristics for that general problem and do not state the Fourier altitude identity or the two-one binary gcd/parity classification above. Their article contains no substantive use of “Fourier”, “circulant”, “greatest common divisor”, or a two-one binary design in this analysis.

The discrete-Fourier diagonalization of a circulant matrix is classical; Gray's review is a standard reference for that ingredient. The contribution here is the exact specialization of the CPT power proxy to the cyclic-orbit altitude and, crucially, the complete arithmetic solution of the row-ordering problem for a natural sparse binary predictor. Related later work on permutation-test power and fixed-row permutations studies different testing constructions and does not supply this CPT binary-spacing law.

## Limitations
This theorem is restricted to one tested predictor, no nuisance predictors, the saturated choice \(m=n-1\), and exactly two ones in the design column. The arithmetic collapse is a statement about the source's proxy \(O^*\); it does not by itself identify the full rejection probability under alternatives. The saturated choice forces \(\alpha=1/n\), so the directly common \(5\%\) instance is the minimal sample \(n=20\). Extending the exact arithmetic classification to \(n>(m+1)\), more than two active rows, or nuisance covariates remains open here.

## References
1. L. Lei and P. J. Bickel, “An assumption-free exact test for fixed-design linear models with exchangeable errors,” *Biometrika* 108(2), 397–412 (2021). DOI 10.1093/biomet/asaa079. First public preprint: arXiv:1907.06133, 2019-07-13.
2. R. M. Gray, “Toeplitz and Circulant Matrices: A Review,” *Foundations and Trends in Communications and Information Theory* 2(3), 155–239 (2006). DOI 10.1561/0100000006.
3. N. W. Koning and J. Hemerik, “More efficient exact group-invariance testing: using a representative subgroup,” *Biometrika* 111(2), 441–458 (2024). DOI 10.1093/biomet/asad050.
