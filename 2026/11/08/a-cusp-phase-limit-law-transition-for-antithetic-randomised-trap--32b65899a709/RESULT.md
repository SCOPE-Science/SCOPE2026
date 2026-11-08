# A cusp-phase limit-law transition for antithetic randomised trapezoidal quadrature

## Finding

For every \(0<\gamma\le 2\) and integer \(n\ge 1\), let \(U_{n,0},\ldots,U_{n,n-1}\) be independent uniform random variables on \([0,1]\). Consider the complementary, independently stratified two-point estimator of the centered power cusp:

\[
 f_\gamma(x)=|x-\tfrac12|^\gamma,\quad
 Q_{n,\gamma}=\frac1{2n}\sum_{j=0}^{n-1}
 \left[f_\gamma\!\left(\frac{j+U_{n,j}}n\right)
 +f_\gamma\!\left(\frac{j+1-U_{n,j}}n\right)\right],
 \quad I_\gamma=\int_0^1f_\gamma(x)\,dx=\frac{2^{-\gamma}}{\gamma+1}.
\]

Write \(E_{n,\gamma}=Q_{n,\gamma}-I_\gamma\). Define, with \(U\sim\mathrm{Uniform}[0,1]\),

\[
 Z_{\gamma,a}(U)=\frac{(a+U)^\gamma+(a+1-U)^\gamma}{2}
 -\int_a^{a+1}t^\gamma\,dt,\qquad a\ge0,
\]
\[
 H_\gamma(U)=|U-\tfrac12|^\gamma-\frac{2^{-\gamma}}{\gamma+1}.
\]

Every variable in these definitions is centered. All terms displayed in a common infinite series below are mutually independent and have the indicated uniform sampling laws.

**Non-Gaussian phase:** If \(0<\gamma<\tfrac32\), then along even and odd grid sizes respectively,

\[
 n^{\gamma+1}E_{n,\gamma}\ \Rightarrow\
 L_\gamma^{\mathrm{even}}=\sum_{j=0}^\infty
 (Z_{\gamma,j}(U_j^L)+Z_{\gamma,j}(U_j^R)),
\]
\[
 n^{\gamma+1}E_{n,\gamma}\ \Rightarrow\
 L_\gamma^{\mathrm{odd}}=H_\gamma(U_*)+\sum_{j=0}^\infty
 (Z_{\gamma,j+1/2}(U_j^L)+Z_{\gamma,j+1/2}(U_j^R)).
\]

Both series converge in \(L^2\). If \(\gamma\ne1\), both limits are nondegenerate and non-Gaussian; at \(\gamma=1\) the even-grid error is identically zero, while **at every odd grid size** \(n^2E_{n,1}\) is exactly uniform on \([-1/4,1/4]\), not merely asymptotically so. The scaled variances converge to the corresponding series variances along each parity.

**Critical Gaussian phase:** At \(\gamma=\tfrac32\), with no parity restriction,

\[
 \frac{n^{5/2}}{\sqrt{\log n}}E_{n,3/2}
 \Rightarrow\mathcal N\!\left(0,\frac1{640}\right),\qquad
 \operatorname{Var}(E_{n,3/2})\sim\frac{\log n}{640n^5}.
\]

**Smooth-side Gaussian phase:** For \(\tfrac32<\gamma\le2\), with no parity restriction,

\[
 n^{5/2}E_{n,\gamma}\Rightarrow\mathcal N(0,c_\gamma),\qquad
 \operatorname{Var}(E_{n,\gamma})\sim c_\gamma n^{-5},
 \quad c_\gamma=\frac{2^{4-2\gamma}\gamma^2(\gamma-1)^2}{720(2\gamma-3)}.
\]

In particular, \(c_2=1/180\). All weak limits refer to the randomness of the estimator, not random integrands or random mesh locations.

## Assumptions and scope

The target is one fixed deterministic scalar function on \([0,1]\), with the cusp at the rational grid point \(x=1/2\). Within each mesh cell the paired sample locations are complementary, and pairs in distinct cells are independent. No cross-grid coupling assumption is needed, because only distributions and second moments are asserted as \(n\to\infty\). The mesh is uniform, with exactly \(n\) cells; it is essential to distinguish even and odd \(n\). All numerical constants refer to this precise normalization, without an additional rescaling of the function or interval. The classification is proved for \(0<\gamma\le2\), including the exactly affine-on-each-side case \(\gamma=1\).

## Proof

**1. Exact localization and unbiasedness.** On each cell \([j/n,(j+1)/n]\), both \(U_{n,j}\) and \(1-U_{n,j}\) are uniform on \([0,1]\), so the paired-cell estimate is unbiased for that cell integral. Independence across cells makes the total error a sum of independent centered errors. The identity \(|x-1/2|^\gamma=n^{-\gamma}|nx-n/2|^\gamma\) reduces every cell, exactly, to a power function at a translated distance from the midpoint. For \(n=2m\), the middle of the grid is a cell boundary and the pairs of left and right cells at successive outward distances have offsets \(0,1,\ldots,m-1\). Hence

\[
 n^{\gamma+1}E_{n,\gamma}\ \overset{d}=\
 \sum_{j=0}^{m-1}[Z_{\gamma,j}(U_j^L)+Z_{\gamma,j}(U_j^R)]. \tag{1}
\]

For \(n=2m+1\), the middle cell is centered at the cusp. Its exact error is \(n^{-\gamma-1}H_\gamma(U_*)\), and all other offsets are \(1/2,3/2,\ldots,m-1/2\), each appearing twice. Therefore

\[
 n^{\gamma+1}E_{n,\gamma}\ \overset{d}=\
 H_\gamma(U_*)+\sum_{j=0}^{m-1}
 [Z_{\gamma,j+1/2}(U_j^L)+Z_{\gamma,j+1/2}(U_j^R)]. \tag{2}
\]

Equations (1)--(2) are finite-size distributional equalities, not limiting approximations.

**2. A uniform local moment expansion.** Put \(w=U-1/2\) and \(b=a+1/2\). For every fixed \(\gamma\in(0,2]\) and \(a\ge1\), symmetric Taylor expansion of the two samples about \(b\), followed by integration over \([-1/2,1/2]\), gives the uniform estimate

\[
 Z_{\gamma,a}(U)
 =\frac{\gamma(\gamma-1)}2 b^{\gamma-2}
 \left(w^2-\frac1{12}\right)
 +O_\gamma(b^{\gamma-4}). \tag{3}
\]

The error is uniform in \(U\in[0,1]\). Indeed the fourth derivative of the power function is bounded by \(C_\gamma b^{\gamma-4}\) over this fixed-radius interval for \(b\ge3/2\); the second-order remainder has exactly the stated centered form. Because \(\mathbb E w^2=1/12\), \(\mathbb E w^4=1/80\), and \(\operatorname{Var}(w^2)=1/180\), equation (3) yields

\[
 v_{\gamma,a}:=\operatorname{Var}(Z_{\gamma,a})
 =\frac{\gamma^2(\gamma-1)^2}{720}
 (a+\tfrac12)^{2\gamma-4}
 +O_\gamma((a+\tfrac12)^{2\gamma-6}). \tag{4}
\]

For \(\gamma=1\), all \(Z_{1,a}\) vanish identically, so (4) is interpreted as the exact zero statement. For \(\gamma=2\), equation (3) is exact, with \(Z_{2,a}=w^2-1/12\) for all offsets including \(a=0\). The finitely many small offsets have finite moments and do not affect the large-offset asymptotic. Equation (4) also entails uniform boundedness of \(Z_{\gamma,a}\) over \(a\ge0\) when \(3/2\le\gamma\le2\).

**3. Below the threshold.** For \(0<\gamma<3/2\), the exponent \(2\gamma-4<-1\), so (4) implies \(\sum_{j\ge0}v_{\gamma,j}<\infty\) and \(\sum_{j\ge0}v_{\gamma,j+1/2}<\infty\). The independent centered finite sums (1)--(2) consequently converge in \(L^2\) under a canonical coupling, proving both asserted weak limits and variance limits. For \(\gamma\ne1\), the variable \(Z_{\gamma,0}(U)\) is bounded and nonconstant: as a function of \(|U-1/2|\), its derivative has the strict sign of \(\gamma-1\) away from zero. It is independent of the remaining terms in the even series. Cramér's normal-decomposition theorem says that, were the total sum Gaussian, this nonconstant bounded summand would have to be Gaussian, a contradiction. The same reasoning applies to the independent bounded nonconstant central term \(H_\gamma(U_*)\) of the odd series. At \(\gamma=1\), the power function is affine on every noncentral cell, making \(Z_{1,a}=0\); the sole odd-center contribution \(H_1=|U_*-1/2|-1/4\) is uniform on \([-1/4,1/4]\).

**4. Critical and Gaussian regimes.** Let \(S_{n,\gamma}=n^{\gamma+1}E_{n,\gamma}\), as represented in (1)--(2). Set \(d_\gamma=\gamma^2(\gamma-1)^2/720\). For \(\gamma=3/2\), (4) says \(v_{\gamma,a}=d_\gamma/a+O(a^{-2})\) as \(a\to\infty\), where \(d_{3/2}=1/1280\). Two copies of the harmonic sum occur for both parities, so

\[
 \operatorname{Var}(S_{n,3/2})
 =\frac1{640}\log n+O(1). \tag{5}
\]

For \(3/2<\gamma\le2\), the integral comparison for the power sum, again twice, yields

\[
 \operatorname{Var}(S_{n,\gamma})
 \sim\frac{2d_\gamma}{2\gamma-3}
 \left(\frac n2\right)^{2\gamma-3}. \tag{6}
\]

The first terms and (for odd \(n\)) the central term only contribute bounded variance. Every summand in (1)--(2) is uniformly bounded, whereas the total variance diverges by (5)--(6). The triangular arrays therefore satisfy the Lindeberg condition; Lindeberg--Feller gives the standardized Gaussian limit. Multiplying (5)--(6) by the relevant powers of \(n\) proves both claimed normalizations and constants. The same equations give the sharp variance limits, since all errors are centered. This completes the proof.

## Verification

The accompanying `verify.py` uses only the Python standard library. Running `python verify.py` performs 356 deterministic algebraic and numerical checks. Tests compare direct finite-grid evaluation with exact offset decompositions for even and odd meshes, verify the exact affine parity effect, check the elementary uniform moments, and compare finite-size variances with the asymptotic constants. The numerical variance calculations approximate one-dimensional integrals for diagnostics; they do **not** prove (4)--(6), the Lindeberg condition, or the non-Gaussian claims. The displayed proof supplies those infinite statements independently.

## Relationship to prior work

Yue Wu, *A randomised trapezoidal quadrature* (first public 2020-11-30), defines precisely the complementary within-cell randomisation in its equation (4), proves unbiasedness and fractional-Sobolev \(L^p\)/almost-sure error estimates in Theorems 3.2--3.3, and reports numerical tests on the endpoint functions \(t^\gamma\). These results do not present distributional limit laws or grid-parity cusp effects. A related endpoint-power analysis supplies exact second-moment asymptotics for a different singularity location, but a variance statement alone does not determine weak limits, a non-Gaussian limiting series, or odd-versus-even cusp placement. Goda, Kazashi and Suzuki study a different randomized trapezoid on the real line under Gaussian weight, with random mesh count and a global shift; their worst-case RMSE bounds do not imply the present local-pair cusp law. Casarin, Craiu, Frattarolo and Robert establish a Gaussian limit for generalized Latin-hypercube antithetic sampling; its fixed bounded-integrand sampling design and \(\sqrt{n}\) scaling do not address a vanishing-width cusp, non-Gaussian limits, or parity-dependent strata. Classical independent-array limit theory is used in the proof and is not itself claimed as new.

## Limitations

The theorem is confined to one centered power cusp and the independently drawn complementary-pair quadrature on a uniform grid. A translated cusp at a general irrational location may have a nonconvergent sequence of mesh phases; that case is not classified. The theorem does not assert pathwise convergence under arbitrary couplings across grid sizes, nor joint limits over multiple powers or nodes. The Gaussian limiting variance is a second-moment statement, not an exact finite-grid error bound or a confidence-interval coverage theorem. The literature comparison leaves a residual risk of an equivalent result stated in broader stratified-sampling terminology. No independent validation has been performed.

## References

1. Y. Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086 (public 2020-11-30), https://arxiv.org/abs/2011.15086 ; later *International Journal of Computer Mathematics* 99 (2022), 680--692.
2. T. Goda, Y. Kazashi, Y. Suzuki, *Randomizing the trapezoidal rule gives the optimal RMSE rate in Gaussian Sobolev spaces*, arXiv:2212.11476 (public 2022-12-22), https://arxiv.org/abs/2212.11476.
3. R. Casarin, R. V. Craiu, L. Frattarolo, C. P. Robert, *Living on the Edge: An Unified Approach to Antithetic Sampling*, arXiv:2110.15124 (public 2021-10-28), https://arxiv.org/abs/2110.15124.
4. H. Cramér, *Über eine Eigenschaft der normalen Verteilungsfunktion*, Mathematische Zeitschrift 41 (1936), 405--414 (normal-decomposition theorem).
5. Classical Lindeberg--Feller central limit theorem for independent triangular arrays, used in its standard bounded-summand form.
