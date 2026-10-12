# Residual-spectrum convex ordering and the exact Gaussian sketch failure law

## Finding
Fix the row-space dimension \(r\) and independent Gaussian testing dimension \(\ell\ge r\) in an exact-arithmetic, two-sided low-rank reconstruction. The normalized **squared Frobenius** reconstruction error has a complete spectral mixing law. Its expected value, when finite, is independent of the residual singular spectrum, but its convex risk is ordered by that spectrum: concentrating residual energy can only make the error riskier in convex order. The maximally concentrated (rank-one residual) case has an exact beta-prime/F distribution, and every nonzero residual has the same sharp moment-existence cutoff.

Specifically, with \(\nu=\ell-r+1\), any nonzero residual satisfies \(\mathbb E R^q<\infty\) exactly for \(0<q<\nu/2\). In the rank-one case,
\[
R-1\;\stackrel{d}{=}\;\operatorname{BetaPrime}(r/2,\nu/2)
\;\stackrel{d}{=}\;\frac r\nu F_{r,\nu}.
\]
When \(\nu>2\), \(\mathbb E R=1+r/(\nu-2)\); this **mean identity is prior work**, not an originality claim. When \(\nu>4\), the error-ratio variance is a strictly increasing affine function of the residual spectral concentration \(\sum_j\lambda_j^2\).

## Assumptions and scope
Let \(m,n,r,\ell\) be integers with \(1\le r<m\), \(n\ge1\), and \(\ell\ge r\). Fix a real \(m\)-by-\(n\) matrix \(A\), and an \(m\)-by-\(r\) matrix \(Q\) satisfying \(Q^\mathsf TQ=I_r\). Define the orthogonal residual \(B=(I_m-QQ^\mathsf T)A\) and assume \(B\ne0\). Draw \(Y\in\mathbb R^{m\times\ell}\) with independent \(N(0,1)\) entries, independent of \(Q\) if that space was randomized. Form
\[
\widehat A=Q(Y^\mathsf TQ)^\dagger Y^\mathsf TA,\qquad
R=\frac{\|A-\widehat A\|_F^2}{\|B\|_F^2}.
\]
All pseudoinverses and norms are exact; \(Y^\mathsf TQ\) has rank \(r\) almost surely. Let \(d=\operatorname{rank}B\), \(s_1,\ldots,s_d>0\) its nonzero singular values and \(\lambda_j=s_j^2/\sum_i s_i^2\). To compare spectra of unequal ranks, pad them with zeros to a common length. Majorization \(\lambda\succ\mu\) means sorted partial sums of \(\lambda\) dominate those of \(\mu\), with equal totals one. Convex order \(U\preceq_{\rm cx}V\) means \(\mathbb E\phi(U)\le\mathbb E\phi(V)\) for all convex real \(\phi\) with both expectations defined, and requires finite, equal means. Accordingly its assertion below is restricted to \(\ell\ge r+2\).

For the usual generalized Nyström method, take a right test matrix \(X\), set \(Q=\operatorname{orth}(AX)\) whenever \(AX\) has column rank \(r\), and choose an independent \(Y\). The stated laws then hold conditional on \(X\); unconditional comparisons require appropriate control of the random residual spectra and are not asserted.

## Proof
**1. Exact independent-Gaussian decomposition.** Choose a thin singular-value decomposition \(B=U\operatorname{diag}(s_1,\ldots,s_d)V^\mathsf T\). Orthogonality gives \(Q^\mathsf TU=0\). Write \(G=Y^\mathsf TQ\), \(H=Y^\mathsf TU=[h_1,\ldots,h_d]\). Orthogonal invariance of a standard Gaussian shows \(G\) and all columns \(h_j\) are independent standard-Gaussian matrices/vectors, even jointly. Since \(G^\dagger G=I_r\) almost surely,
\[
\widehat A=QQ^\mathsf TA+QG^\dagger Y^\mathsf TB
=QQ^\mathsf TA+QG^\dagger H\operatorname{diag}(s_j)V^\mathsf T.
\]
The first difference term \(B\) is orthogonal in the Frobenius inner product to the second term (whose columns lie in \(\operatorname{range}Q\)). Thus the Pythagorean identity and right orthogonality of \(V\) yield
\[
\|A-\widehat A\|_F^2=\|B\|_F^2+
\sum_{j=1}^d s_j^2\|G^\dagger h_j\|_2^2.
\]
Dividing by \(\|B\|_F^2\) proves the distributional representation, with \(Z_j=\|G^\dagger h_j\|_2^2\). Conditional on \(G\), these are independent and identically distributed; unconditionally they are exchangeable (not in general independent).

**2. Spectral convex order.** Suppose \(\lambda\succ\mu\), after zero padding both to length \(d\). By the Hardy–Littlewood–Pólya characterization, \(\mu\) is a convex combination of coordinate permutations of \(\lambda\). For each deterministic vector \(z\) and any convex \(\phi\), Jensen's inequality bounds \(\phi(1+\mu\cdot z)\) by the corresponding convex combination of \(\phi(1+\lambda\cdot Pz)\). Average over the exchangeable vector \((Z_1,\ldots,Z_d)\); every permutation has the same expectation as the original. This proves \(R_\mu\preceq_{\rm cx}R_\lambda\) whenever the mean is finite. Among probability weights of length \(d\), the equal vector \((1/d,\ldots,1/d)\) is least in majorization order, and \((1,0,\ldots,0)\) is greatest; hence these give respectively the smallest and largest convex risks among realizable fixed-test-dimension residual profiles supported on at most \(d\) singular modes. This is a convex-risk assertion, **not** stochastic dominance of every upper tail or quantile.

**3. Exact rank-one distribution.** Fix one unit residual direction and let \(h\sim N_\ell(0,I_\ell)\) independent of \(G\). The vector \(z=G^\dagger h\), conditional on \(S=G^\mathsf TG\), is Gaussian \(N_r(0,S^{-1})\); \(S\) is a real Wishart matrix with \(\ell\) degrees of freedom and identity scale. Integrating the normal density \(\det(S)^{1/2}\exp(-z^\mathsf TSz/2)\) against the Wishart density uses the positive-definite gamma integral and \(\det(I_r+zz^\mathsf T)=1+\|z\|_2^2\). The resulting normalized density is
\[
 f_z(z)=\frac{\Gamma((\ell+1)/2)}{\pi^{r/2}\Gamma((\ell-r+1)/2)}
 (1+\|z\|_2^2)^{-(\ell+1)/2}.
\]
Radial integration of \(T=\|z\|_2^2\), with \(\nu=\ell-r+1\), gives
\[
 f_T(t)=\frac{t^{r/2-1}}{B(r/2,\nu/2)(1+t)^{(r+\nu)/2}},\qquad t>0.
\]
This is the beta-prime law with shapes \((r/2,\nu/2)\), equivalently \(T\stackrel d=(r/\nu)F_{r,\nu}\). In particular,
\[
 \Pr(R>1+t)\sim\frac{2}{\nu B(r/2,\nu/2)}t^{-\nu/2}
 \qquad (t\to\infty)
\]
for a rank-one residual.

**4. Sharp moments for any residual.** The rank-one beta-prime density has finite moment of positive order \(q\) precisely when \(q<\nu/2\). For any nonzero finite residual spectrum \(\lambda\), at least one weight \(\lambda_j>0\), and
\[
 1+\lambda_j Z_j\le R\le1+\sum_{j=1}^dZ_j.
\]
The lower bound forces divergence at and above \(\nu/2\); finite sums of nonnegative variables with finite \(q\)-moments have finite \(q\)-moment, giving the converse. No independence among the \(Z_j\) is needed for this final comparison. For \(\nu>2\), the beta-prime mean of each \(Z_j\) is \(r/(\nu-2)\), reproducing the previously known expectation formula.

**5. Variance and strict comparison.** When \(\nu>4\), the squared beta-prime moment exists, so all following terms are finite. Conditional on \(S=G^\mathsf TG\), the Gaussian quadratic-form identities yield
\[
 \mathbb E[Z_j\mid S]=\operatorname{tr}(S^{-1}),\qquad
 \operatorname{Var}(Z_j\mid S)=2\operatorname{tr}(S^{-2}).
\]
The \(Z_j\) are conditionally independent. Taking total variance of \(\sum_j\lambda_jZ_j\), using \(\sum_j\lambda_j=1\), gives
\[
 \operatorname{Var}(R)=
 \operatorname{Var}[\operatorname{tr}(S^{-1})]
 +2\mathbb E[\operatorname{tr}(S^{-2})]\sum_j\lambda_j^2.
\]
The second coefficient is strictly positive. Strict majorization without permutation strictly increases the sum of squares, hence variance. If \(\nu\le4\), \(R\) has infinite second moment, so the displayed finite-variance formula is not used.

## Verification
The embedded `verify.py` runs two exact rational decomposition identities; 240 exact rational Jensen/permutation comparisons; 540 seeded Gaussian-matrix direct reconstructions; a 35,000-sample distribution diagnostic for the beta-prime identity; and 44 rational parameter-pair checks for its first two moments. Reproduce using the dependencies in `requirements.txt` and `python verify.py`. Exact identities and the analytic proof justify the infinite-dimensional quantifiers; finite Monte Carlo draws do not prove distributional equality, convex ordering, or infinite-tail assertions.

## Relationship to prior work
Tropp, Yurtsever, Udell, and Cevher (2017, arXiv:1609.00048), Lemmas A.3–A.5 and Theorem 4.3, already derive the same Gaussian two-sided reconstruction, the Pythagorean error split, and its **exact first expectation** when the inverse-Wishart mean exists. These results are expressly excluded from the novel increment. Nakatsukasa (2020, arXiv:2009.11392), section 3.4 and Theorem 3.2, analyzes the generalized Nyström formula and Frobenius error bounds, using the earlier work; it does not state the full residual-spectrum convex-risk order or the all-positive-order moment cutoff shown here. The present conclusion connects the algorithm-specific Gaussian factor geometry to matrix-spectrum majorization and a sharp beta-prime failure law. Classical Wishart integration and convex-order/majorization facts are tools, not claimed as inventions.

## Limitations
This result concerns **exact-arithmetic** reconstruction, real independent standard Gaussian tests, a fixed/conditioned \(Q\), and a squared Frobenius **ratio to a nonzero orthogonal residual**. It does not claim unconditional spectrum ordering over arbitrary random range finders, stable finite-precision behavior of a pseudoinverse, analogous laws for non-Gaussian sketches, high-dimensional asymptotic claims, or quantile stochastic dominance. No statement is made for zero residual because the ratio is undefined. Novelty remains subject to discovery of specialized prior distributional treatments not indexed in the inspected literature.

## References
1. Y. Nakatsukasa, *Fast and stable randomized low-rank matrix approximation*, arXiv:2009.11392v1 (first public 2020-09-23), sections 2 and 3.4; https://arxiv.org/abs/2009.11392.
2. J. A. Tropp, A. Yurtsever, M. Udell, and V. Cevher, *Practical sketching algorithms for low-rank matrix approximation*, arXiv:1609.00048 (first public 2016-08-31), Lemmas A.3–A.5; https://arxiv.org/abs/1609.00048.
3. Classical Hardy–Littlewood–Pólya majorization theorem, Gaussian/Wishart calculus, and beta-prime distribution identities (standard mathematical ingredients).
