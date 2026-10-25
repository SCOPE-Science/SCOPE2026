# A logarithmic boundary law for the first Fourier zero of generalized Gaussians

## Finding
For each fixed integer dimension \(d\ge1\), define \(f_{p,d}(x)=e^{-\|x\|_2^p}\) on \(\mathbb R^d\), with Fourier convention
\[
\widehat f_{p,d}(\xi)=\int_{\mathbb R^d}e^{-\|x\|_2^p}e^{-ix\cdot\xi}\,dx.
\]
Let \(R_d(p)=\inf\{r>0:\widehat f_{p,d}(re_1)=0\}\), whenever this set is nonempty. For \(\varepsilon=p-2\downarrow0\), put \(L=\log(1/\varepsilon)\). Then the set is nonempty for all sufficiently small positive \(\varepsilon\), and
\[
\boxed{\frac{R_d(2+\varepsilon)^2}{4}=L+\frac{d+2}{2}\log L+\log\frac{2}{\Gamma((d+2)/2)}+o(1).}
\]
Thus the first real Fourier zero escapes at square-root-logarithmic scale, with an explicit dimension-dependent second term and constant.

## Assumptions and scope
The dimension \(d\) is fixed while \(\varepsilon\to0^+\). The Euclidean norm is used, and the Fourier transform has no \(2\pi\) in its exponential. Radial symmetry makes \(\widehat f_{p,d}(re_1)\) real for real \(r\). The result concerns the first positive radial zero only; it does not assert uniqueness of all zeros, simplicity, or a description of later zeros.

## Proof
Write \(F_{p,d}(r)=\widehat f_{p,d}(re_1)\). At the Gaussian endpoint,
\[
F_{2,d}(r)=\pi^{d/2}e^{-r^2/4}>0.
\]
Differentiating under the integral at \(p=2\) gives
\[
\left.\partial_pF_{p,d}(r)\right|_{p=2}=-\widehat{g_d}(re_1),\qquad g_d(x)=\|x\|_2^2\log\|x\|_2\,e^{-\|x\|_2^2}.
\]
The homogeneous-distribution identity, for \(\xi\ne0\), is
\[
\mathcal F(\|x\|_2^\alpha)(\xi)=2^{\alpha+d}\pi^{d/2}\frac{\Gamma((\alpha+d)/2)}{\Gamma(-\alpha/2)}\|\xi\|_2^{-\alpha-d}.
\]
Differentiating at \(\alpha=2\), where \(1/\Gamma(-\alpha/2)=(\alpha-2)/2+O((\alpha-2)^2)\), yields the leading tail coefficient
\[
C_d=2^{d+1}\pi^{d/2}\Gamma((d+2)/2)>0.
\]
A smooth cutoff near the origin and the expansion \(e^{-\|x\|_2^2}=1+O(\|x\|_2^2)\) show that
\[
\left.\partial_pF_{p,d}(r)\right|_{p=2}=-C_dr^{-d-2}+O(r^{-d-4}\log r).
\]
The same homogeneous-distribution estimate, differentiated twice in the exponent, gives uniformly for \(2\le q\le2+\varepsilon_0\) and \(r\ge2\)
\[
|\partial_q^2F_{q,d}(r)|\le C r^{-d-2}(1+\log^2r),
\]
where \(C\) depends only on \(d\) and a fixed small \(\varepsilon_0>0\). Taylor's theorem therefore gives the uniform high-frequency expansion
\[
F_{2+\varepsilon,d}(r)=\pi^{d/2}e^{-r^2/4}-\varepsilon C_dr^{-d-2}
+O\!\left(\varepsilon r^{-d-4}\log r+\varepsilon^2r^{-d-2}(1+\log^2r)\right).
\]
Fix \(\delta>0\), set \(c_d=\log(2/\Gamma((d+2)/2))\), and define \(r_\pm\) by
\[
\frac{r_\pm^2}{4}=L+\frac{d+2}{2}\log L+c_d\pm\delta.
\]
Then \(r_\pm\sim2\sqrt L\). The ratio of the Gaussian term to the leading negative tail is
\[
Q_\varepsilon(r)=\frac{\pi^{d/2}e^{-r^2/4}}{\varepsilon C_dr^{-d-2}}
=\frac{r^{d+2}e^{-r^2/4}}{2^{d+1}\Gamma((d+2)/2)\varepsilon},
\]
so \(Q_\varepsilon(r_-)\to e^{\delta}\) and \(Q_\varepsilon(r_+)\to e^{-\delta}\). Moreover, \(Q_\varepsilon\) decreases for \(r>\sqrt{2(d+2)}\). The remainder above is uniformly smaller than the leading tail by a factor tending to zero on fixed-to-\(O(\sqrt L)\) frequency intervals after the fixed lower endpoint is chosen sufficiently large. On the remaining compact interval, \(F_{2+\varepsilon,d}\to F_{2,d}\) uniformly, and the Gaussian limit is strictly positive. Consequently \(F_{2+\varepsilon,d}(r)>0\) for every \(0\le r\le r_-\), while \(F_{2+\varepsilon,d}(r_+)<0\) for sufficiently small \(\varepsilon\). Continuity puts the first zero in \((r_-,r_+)\). Since \(\delta>0\) was arbitrary, the boxed asymptotic follows.

## Verification
The Gaussian transform and the coefficient \(C_d\) follow analytically from the stated Fourier convention and the homogeneous-distribution formula. The sign change at \(r_+\), together with positivity on the entire interval \([0,r_-]\), proves existence and the first-zero location; no finite numerical search is used as proof. The remainder estimate is uniform for each fixed dimension and is only invoked at radii of order \(\sqrt{\log(1/\varepsilon)}\). The claim does not locate subsequent zeros or assert that the first zero is simple.

## Relationship to prior work
Pogány and Nadarajah give a closed-form characteristic-function representation for the generalized normal family, but their paper does not state a first-zero asymptotic as the exponent approaches the Gaussian value. Paris develops fixed-exponent large-frequency asymptotics and zero approximations for a related class of Fourier integrals; those estimates do not provide the joint limit in which the exponent tends to \(2\) while the first zero diverges. Dytso and coauthors prove that the generalized Gaussian characteristic function has no real zeros at or below exponent \(2\), and has a positive-to-negative zero crossing above \(2\), with fixed-parameter tail results. The present claim resolves the location of the first crossing in the singular near-threshold limit and gives its dimension-dependent constant. No assertion is made that the cited works contain this joint asymptotic.

## Limitations
The dimension is fixed; no uniformity as \(d\to\infty\) is claimed. The proof uses the standard Fourier transform of homogeneous distributions and a uniform cutoff estimate for exponent derivatives. The result gives only the first-zero asymptotic and does not classify all zeros or their multiplicities. The full text of the related 2010 characteristic-function paper was not consulted, so a hidden implication in that source remains a residual literature risk.

## References
1. T. K. Pogány and S. Nadarajah, “On the characteristic function of the generalized normal distribution,” *Comptes Rendus Mathématique* 348 (2010), 203–206. DOI: 10.1016/j.crma.2009.12.010. First public date: 2009-12-30.
2. R. B. Paris, “On the Asymptotics and Zeros of a Class of Fourier Integrals,” *European Journal of Pure and Applied Mathematics* 5(3) (2012), 260–281. Public date: 2012-07-31.
3. A. Dytso, R. Bustin, H. V. Poor, and S. Shamai, “Analytical properties of generalized Gaussian distributions,” *Journal of Statistical Distributions and Applications* 5 (2018), article 6. DOI: 10.1186/s40488-018-0088-5.
4. E. M. Stein and G. Weiss, *Introduction to Fourier Analysis on Euclidean Spaces*. Princeton University Press, 1971, chapter on homogeneous distributions.
