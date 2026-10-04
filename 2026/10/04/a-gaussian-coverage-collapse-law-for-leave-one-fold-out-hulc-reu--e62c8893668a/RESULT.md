# A Gaussian coverage-collapse law for leave-one-fold-out HulC reuse
## Finding
Consider \(n=Bm\) independent observations from \(N(\mu,\sigma^2)\), where \(B\ge 2\), \(m\ge 1\), and \(\sigma>0\). Split the observations into \(B\) equal disjoint folds and let \(G_i\) denote fold \(i\)'s sample mean. The ordinary univariate HulC construction applied to the independent, median-unbiased fold means uses their hull
\[
H_B^{\mathrm{ind}}=[\min_i G_i,\max_i G_i].
\]
A tempting data-reuse modification is instead to form the leave-one-fold-out means
\[
\widehat\mu_i=\frac{1}{B-1}\sum_{j\ne i}G_j
=\frac{B\overline G-G_i}{B-1}
\]
and take
\[
H_B^{\mathrm{LOFO}}=[\min_i\widehat\mu_i,\max_i\widehat\mu_i].
\]
This reuse modification has an exact finite-sample pathology. On every realized sample,
\[
|H_B^{\mathrm{LOFO}}|=\frac{|H_B^{\mathrm{ind}}|}{B-1}.
\]
Yet, writing \(\phi\) and \(\Phi\) for the standard-normal density and distribution function, its exact coverage is
\[
C_B:=\Pr\{\mu\in H_B^{\mathrm{LOFO}}\}
=1-2\int_{-\infty}^{\infty}\phi(u)\,\Phi(\sqrt{B-2}\,u)^B\,du.
\]
In particular, \(C_2=C_3=1/2\), \(C_6=0.452918829563530\ldots\), and
\[
C_B\sim 2\sqrt{\frac{\log B}{\pi B}}\longrightarrow 0.
\]
By contrast, the independent fold hull has exact Gaussian coverage
\[
\Pr\{\mu\in H_B^{\mathrm{ind}}\}=1-2^{1-B}.
\]
Thus at \(B=6\), for example, the independent hull covers with probability \(0.96875\), whereas the leave-one-fold-out reuse hull covers with probability only \(0.452918829563530\ldots\), despite being exactly five times narrower on every sample.

The expected reused width also collapses. If \(Z_1,\ldots,Z_B\) are independent \(N(0,1)\) variables, then
\[
\mathbb E|H_B^{\mathrm{LOFO}}|
=\frac{\sigma}{\sqrt m(B-1)}\,
\mathbb E\!\left[\max_i Z_i-\min_i Z_i\right]
\sim \frac{2\sigma\sqrt{2\log B}}{\sqrt m\,B}.
\]
The common grand-mean error is shared by all reused estimators and therefore largely disappears from their range; that is precisely why their narrow hull is not calibrated.
## Assumptions and scope
The statement is finite-sample for an iid Gaussian location model with known equal fold sizes and a fixed partition. It concerns the explicit leave-one-fold-out reuse rule above. It does not alter or contradict the published HulC validity result, whose univariate construction assumes independent estimators, obtainable from disjoint data batches. The Gaussian assumption is used for the exact orthant formula and the stated sharp asymptotic constant. No claim is made here for arbitrary dependent estimators, arbitrary unequal folds, or the Adaptive or Unimodal HulC variants.
## Proof
Set
\[
Z_i=\frac{\sqrt m\,(G_i-\mu)}{\sigma},\qquad S=\sum_{i=1}^B Z_i.
\]
Then the \(Z_i\) are independent standard normals and
\[
\widehat\mu_i-\mu
=\frac{\sigma}{\sqrt m(B-1)}(S-Z_i).
\]
First, since \(S-Z_i\) differs across \(i\) only through \(-Z_i\),
\[
\max_i(S-Z_i)-\min_i(S-Z_i)=\max_i Z_i-\min_i Z_i.
\]
This proves both the samplewise factor \(1/(B-1)\) between reused and independent hull widths and the exact expected-width formula.

For coverage, \(\mu\) lies in the reused hull exactly when the numbers \(S-Z_i\) are not all strictly positive and not all strictly negative. By symmetry,
\[
C_B=1-2\Pr\{S-Z_i>0\text{ for every }i\}.
\]
The Gaussian vector \((S-Z_i)_{i=1}^B\) has variance \(B-1\) in each coordinate and covariance \(B-2\) between distinct coordinates. Its common correlation is therefore
\[
\rho_B=\frac{B-2}{B-1}.
\]
After division by \(\sqrt{B-1}\), an equicorrelated representation is
\[
Y_i=\sqrt{\rho_B}\,U+\sqrt{1-\rho_B}\,\varepsilon_i,
\]
where \(U,\varepsilon_1,\ldots,\varepsilon_B\) are independent standard normals. Conditioning on \(U=u\) gives
\[
\Pr\{Y_i>0\ \forall i\mid U=u\}=\Phi(\sqrt{B-2}\,u)^B,
\]
which yields the displayed one-dimensional integral. For the independent fold hull, symmetry and independence instead give miscoverage \(2(1/2)^B\), proving \(1-2^{1-B}\).

For the coverage asymptotic, write \(\overline Z=S/B\), \(R_i=Z_i-\overline Z\), \(M_B=\max_iR_i\), and \(m_B=\min_iR_i\). The scalar \(U_0=S/\sqrt B\) is independent of the residual vector \((R_i)\), and
\[
S-Z_i=\frac{B-1}{\sqrt B}U_0-R_i.
\]
Hence, with \(a_B=\sqrt B/(B-1)\),
\[
C_B=\mathbb E\left[\Phi(a_BM_B)-\Phi(a_Bm_B)\right].
\]
A third-order Taylor bound for \(\Phi\) at zero gives
\[
C_B=\phi(0)a_B\,\mathbb E(M_B-m_B)
+O\!\left(a_B^3\,\mathbb E\max_i|R_i|^3\right).
\]
Centering does not change the range, symmetry gives
\[
\mathbb E(M_B-m_B)=2\,\mathbb E\max_i Z_i,
\]
and standard Gaussian extreme-value estimates give
\[
\mathbb E\max_i Z_i\sim\sqrt{2\log B},\qquad
\mathbb E\max_i|R_i|^3=O((\log B)^{3/2}).
\]
Since \(a_B\sim B^{-1/2}\), the remainder is lower order and therefore
\[
C_B\sim 2\sqrt{\frac{\log B}{\pi B}}.
\]
The same extreme-value estimate in the exact width identity gives the displayed expected-width asymptotic.
## Verification
The accompanying verifier evaluates the one-dimensional Gaussian integral by deterministic Simpson quadrature and checks the coverage anchors for \(B\in\{2,3,6,10,20,100\}\). It also checks the samplewise range identity on a fixed numerical vector, the independent-hull coverage anchor at \(B=6\), and finite-\(B\) sanity against the asymptotic scale. These computations corroborate, but do not replace, the analytic proof.
## Relationship to prior work
Kuchibhotla, Balakrishnan, and Wasserman introduce HulC confidence regions from convex hulls. In the univariate construction they explicitly assume independent estimators and explain that these can be obtained by splitting the observations into disjoint batches; their Lemma 1 uses independence, and the paper's conclusion again describes estimates constructed on independent subsamples. For independent median-unbiased estimators, their formula reduces to the exact Gaussian fold-hull coverage \(1-2^{1-B}\).

The present result studies a different, deliberately dependent reuse rule: each candidate mean uses all but one fold. Its covariance reduction leads to an equicorrelated Gaussian orthant probability. Classical work of Steck analyzes orthant probabilities for equicorrelated normal vectors and therefore supplies background for the one-dimensional integral once this covariance structure is identified. The new method-level statement is the combination of the exact leave-one-fold-out HulC mapping, its samplewise \(B-1\) width shrinkage, and the sharp coverage-collapse law \(2\sqrt{\log B/(\pi B)}\).
## Limitations
This result should not be read as evidence against the published HulC algorithm: independence is part of that algorithm's validity argument. The result does not characterize all possible forms of overlapping data reuse and does not establish a general theorem for non-Gaussian distributions. Classical equicorrelated-normal orthant theory covers a core probability calculation, so the originality is in the data-reuse geometry and its exact/asymptotic consequence for this confidence-hull construction. A residual literature risk is that an older discussion of dependent convex-hull confidence intervals may contain an equivalent special case under different terminology; targeted searches did not locate one.
## References
1. A. K. Kuchibhotla, S. Balakrishnan, and L. Wasserman, “The HulC: Confidence Regions from Convex Hulls,” arXiv:2105.14577, first posted 2021-05-30; Journal of the Royal Statistical Society Series B 86 (2024), 586–622, DOI 10.1093/jrsssb/qkad134.
2. G. P. Steck, “Orthant probabilities for the equicorrelated multivariate normal distribution,” Biometrika 49 (1962), 433–445, DOI 10.1093/biomet/49.3-4.433.
