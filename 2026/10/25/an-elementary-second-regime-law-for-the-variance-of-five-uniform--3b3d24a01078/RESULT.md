# An elementary second-regime law for the variance of five uniform observations

## Finding

Let \(X_1,\ldots,X_5\) be independent uniform random variables on \([0,1]\), and let \(S^2=\frac14\sum_{i=1}^5(X_i-\bar X)^2\). Set
\[
 r=\sqrt{4y},\qquad d=r^2-\tfrac12,\qquad
 b_5=8\sqrt{10}\left(\arccos\tfrac1{\sqrt3}-\tfrac\pi6\right).
\]
**Theorem.** Throughout the entire first regime above the classical low-variance threshold, \(1/8\le y\le1/6\), the cumulative distribution function \(F_5(y)=\Pr(S^2\le y)\) is the finite elementary expression
\[
\begin{aligned}
 F_5(y)&=\frac{\sqrt5\,\pi^2}{2}r^4-b_5r^5+C_5(y),\\
 C_5(y)&=\frac{80\pi\sqrt5}{3}\left[
 \frac{\sqrt2}{5}d^{5/2}
 +\frac{(5r^2-1)\sqrt d}{8\sqrt2}
 -\frac{3r^4}{8}\arccos\left(\frac1{\sqrt2r}\right)
 \right].
\end{aligned}
\]
For \(0\le y\le1/8\), the same formula holds with \(C_5(y)=0\). The correction is strictly positive for \(y>1/8\), and its sharp onset is
\[
 C_5(\tfrac18+\varepsilon)
 =\frac{4096\pi\sqrt{10}}{21}\varepsilon^{7/2}
 +O(\varepsilon^{9/2}),\qquad \varepsilon\downarrow0.
\]
In particular, the first new contribution is nonanalytic: the correction has three vanishing derivatives at the threshold but its fourth derivative diverges from the right. As a numerical reference, \(F_5(1/6)=0.9667437716908164451\ldots\).

## Assumptions and scope

The five observations are independent and exactly uniform on the unit interval. The variance uses divisor four (the unbiased sample variance), not divisor five. The statement holds pointwise including both endpoints; no approximation or asymptotic assumption is used for the CDF. The expansion concerns only the right-hand neighborhood of \(y=1/8\). No assertion is made for \(y>1/6\), where distinct boundary violations overlap on sets of positive measure.

## Proof

**1. Reduce the five-cube to four-dimensional contrast space.** Let
\[
 H=\{v\in\mathbb R^5:\sum_{i=1}^5v_i=0\},\qquad
 R(v)=\max_i v_i-\min_j v_j.
\]
Every \(x\in[0,1]^5\) has a unique decomposition \(x=c\mathbf1+v\) with \(v\in H\) and \(c=\bar x\). In orthonormal coordinates along \(\mathbf1/\sqrt5\) and within \(H\), Lebesgue measure is \(\sqrt5\,dc\,dv\). Given \(v\), the allowable \(c\)-interval has length \((1-R(v))_+\). Since \(\sum_i(x_i-\bar x)^2=\|v\|^2\),
\[
 F_5(y)=\sqrt5\int_{H\cap\{\|v\|\le r\}}(1-R(v))_+\,dv,\qquad r=\sqrt{4y}.
\]

**2. Isolate the known low-regime polynomial without extrapolating it as a CDF.** The identity \((1-z)_+=1-z+(z-1)_+\) gives
\[
 F_5(y)=\underbrace{\sqrt5\int_{\|v\|\le r}(1-R(v))\,dv}_{P_5(r)}
 +\sqrt5\int_{\|v\|\le r}(R(v)-1)_+\,dv.
\]
The four-dimensional unit ball has volume \(\pi^2/2\); homogeneity of \(R\) implies
\[
 P_5(r)=\frac{\sqrt5\pi^2}{2}r^4-b_5r^5.
\]
The constant \(b_5\) is the exact integrated-range coefficient established for five coordinates by Ali and Richards (1975), quoted explicitly in Osan (2026, Remark 2). It can also be independently checked via Gaussian order statistics: the projection of five independent standard Gaussians onto \(H\) preserves their range, and the projected Gaussian has an independent \(\chi_4\) radius and uniform spherical direction. Therefore
\[
 b_5=\frac{\sqrt5}{5}\,\lvert S^3\rvert\,
 \frac{\mathbb E[\max_{i\le5}G_i-\min_{i\le5}G_i]}{\mathbb E\chi_4},
\]
which agrees with the stated closed expression (see verification program). This is a check of the cited constant, not a claim to a new evaluation of it.

**3. Establish the entire disjoint-violation interval.** For any two *distinct* ordered pairs \((i,j)\ne(k,l)\), suppose both \(v_i-v_j>1\) and \(v_k-v_l>1\). Put \(a_{ij}=e_i-e_j\in H\). Their Gram matrix has diagonal entries two and off-diagonal entry
\[
 q=\langle a_{ij},a_{kl}\rangle\in\{-2,-1,0,1\}.
\]
The case \(q=-2\) consists of opposite ordered pairs and their inequalities are contradictory. Otherwise, the least squared norm of any vector satisfying both weak inequalities is \(2/(2+q)\), obtained by orthogonal projection onto the two constraint normals; thus it is at least \(2/3\). (Equivalently, for feasible positive constraints, the Gram inverse applied to \((1,1)\) gives nonnegative multipliers.) Hence within \(\|v\|\le r\le\sqrt{2/3}\), no two strict inequalities can hold at once. The finitely many equality surfaces have four-dimensional measure zero. As \(R(v)\) is the largest ordered coordinate difference, it follows throughout the ball that
\[
 (R(v)-1)_+=\sum_{i\ne j}(v_i-v_j-1)_+
\]
almost everywhere. Conversely, the two directed inequalities from \((i,j)=(1,2)\) and \((1,3)\) first meet at \(v=(2/3,-1/3,-1/3,0,0)\), of squared norm \(2/3\). Thus \(r^2=2/3\), or \(y=1/6\), is exactly the first multiple-violation threshold.

**4. Integrate one congruent cap.** There are \(5\cdot4=20\) ordered coordinate pairs. Fix one and use the unit-normal coordinate \(t=(v_i-v_j)/\sqrt2\). The remaining cross section within the four-dimensional ball is a three-dimensional ball of radius \(\sqrt{r^2-t^2}\), with volume \(\frac{4\pi}{3}(r^2-t^2)^{3/2}\). Consequently, whenever \(1/\sqrt2\le r\le\sqrt{2/3}\),
\[
 C_5(y)=\frac{80\pi\sqrt5}{3}\int_{1/\sqrt2}^{r}
 (\sqrt2t-1)(r^2-t^2)^{3/2}\,dt.
\]
This also proves \(C_5>0\) in the interior. The two elementary antiderivatives needed are
\[
 \int_{1/\sqrt2}^{r} t(r^2-t^2)^{3/2}dt=\frac{d^{5/2}}5,
\]
and
\[
 \int_{1/\sqrt2}^{r}(r^2-t^2)^{3/2}dt
 =\frac{3r^4}{8}\arccos\frac1{\sqrt2r}
 -\frac{(5r^2-1)\sqrt d}{8\sqrt2}.
\]
Substitution proves the displayed elementary formula. For \(r\le1/\sqrt2\), the range never exceeds one, so \(C_5=0\).

**5. Compute the onset coefficient and its exponent.** Set \(y=1/8+\varepsilon\) and \(h=r-1/\sqrt2=2\sqrt2\,\varepsilon+O(\varepsilon^2)\). In the positive correction integral set \(t=1/\sqrt2+hs\), \(0\le s\le1\). Uniformly in \(s\), the leading integrand, including \(dt\), is \(\sqrt2\,(\sqrt2)^{3/2}h^{7/2}s(1-s)^{3/2}ds\); the remainder has relative size \(O(h)\). Using \(\int_0^1s(1-s)^{3/2}ds=4/35\) gives the stated coefficient \(4096\pi\sqrt{10}/21\) and \(O(\varepsilon^{9/2})\) remainder.

## Verification

The accompanying `verify.py` independently checks the exact \(b_5\) coefficient by a one-dimensional Gaussian-order-statistic quadrature, enumerates every pair of twenty ordered coordinate differences using rational Gram matrices, compares the cap-integral representation with the closed elementary expression at seven thresholds, checks the differential identity and monotonicity at sample points, and probes the onset coefficient. Its reproducible output reports **406 passed assertions**. These finite computations corroborate identities and values; the global no-overlap argument and integration proof establish the continuum claim. The verifier requires Python and `mpmath` and can be run as `python verify.py`.

## Relationship to prior work

Ali and Richards (1975) computed the low-variance piece for general sample size and gave the exact \(n=5\) integrated-range constant used above. Royen (2007, 2008) supplied general Fourier-series representations of the uniform sample-variance law, not a finite second-regime primitive. Osan (2026, arXiv:2610.15174v1) derives an elementary *full-support* CDF for \(n=4\) and discusses \(n=5\) as beyond the demonstrated elementary regimes; his discussion and Appendix are explicitly compared here. The result proved above is the first **post-low-regime elementary piece for five observations**, not the existing low piece, a specialization of the four-observation result, or a claim of full-support closure.

## Limitations

The statement does not cover the subsequent higher-overlap regimes beyond \(y=1/6\) or arbitrary polynomial parent densities. The classification is specific to the unbiased variance of exactly five independent uniform samples. The earliest 1975 geometric paper was not available in full during comparison; its treatment is known through the explicit quotation and citation in the inspected 2026 primary source, so historical priority remains a limited risk. No independent audit or external certification has been performed. The numerical output is a reproducibility check rather than proof of an infinite-dimensional assertion.

## References

1. Remus Osan, *Closed forms all the way up: the sample variance of four observations*, arXiv:2610.15174v1 (first posted 2026-10-10), especially Introduction, Remark 2, Sections 4 and 8; https://arxiv.org/html/2610.15174v1.
2. M. M. Ali and W. A. Richards, *On a conjecture concerning the common content of an N-cube and a diagonal cylinder*, Annals of the Institute of Statistical Mathematics **27** (1975), 281–287; DOI:10.1007/BF02504647 (cited coefficient; full text unavailable in this comparison).
3. T. Royen, *On the Laplace transform of some quadratic forms and the exact distribution of the sample variance from a gamma or uniform parent distribution*, arXiv:0710.5749v1 (2007), Section 4; https://arxiv.org/html/0710.5749v1.
4. T. Royen, *The exact distribution of the sample variance from bounded continuous random variables*, arXiv:0810.1572v1 (2008), Sections 1–3; https://arxiv.org/html/0810.1572v1.
