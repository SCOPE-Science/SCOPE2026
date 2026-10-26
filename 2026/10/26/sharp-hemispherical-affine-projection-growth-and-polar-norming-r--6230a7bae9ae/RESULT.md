# Sharp hemispherical affine-projection growth and polar norming rigidity

## Finding

Let \(H_d=\{a\in S^{d-1}:a_d\ge0\}\), \(d\ge3\), with normalized surface probability \(\sigma_d\). Let \(P_d:L^\infty(H_d)\to C(H_d)\) be the restriction of the \(L^2(\sigma_d)\)-orthogonal projection to \(\mathcal A_d=\operatorname{span}\{1,y_1,\ldots,y_d\}\). Its evaluation norm is \(\Lambda_d(a)=\int_{H_d}|K_d(a,y)|\,d\sigma_d(y)\), where \(K_d\) is the reproducing kernel. Put \(\mu=\sqrt{2/\pi}\), \(v=1-2/\pi\), and take independent standard normal random variables \(Z,Z'\). Define, for \(0\le t\le1\),
\[
F(t)=\mathbb E\left|\sqrt{1-t^2}\,Z+\frac{t}{v}(|Z'|-\mu)\right|.
\]
Then the full spatial profile converges uniformly:
\[
\lim_{d\to\infty}\sup_{a\in H_d}\left|\frac{\Lambda_d(a)}{\sqrt d}-F(a_d)\right|=0.
\]
Moreover, \(F\) is strictly increasing on \([0,1]\), giving the sharp leading norm and an if-and-only-if near-maximizer classification:
\[
\lim_{d\to\infty}\frac{\|P_d\|_{L^\infty\to L^\infty}}{\sqrt d}
=F(1)=\frac{4\{\varphi(\mu)-\mu[1-\Phi(\mu)]\}}{v}
=1.3281520621815\ldots,
\]
where \(\varphi\) and \(\Phi\) denote the standard normal density and distribution function. For any sequence \(a^{(d)}\in H_d\),
\[
\frac{\Lambda_d(a^{(d)})}{\|P_d\|_{L^\infty\to L^\infty}}\longrightarrow1
\quad\Longleftrightarrow\quad a_d^{(d)}\longrightarrow1.
\]
In particular, this is asymptotic concentration of all norming locations at the north pole, not a claim of exact finite-dimensional pole maximality.

## Assumptions and scope

The underlying measure is *normalized surface area*, the fitted space consists of restrictions of ambient affine polynomials, and the norm is the real (equivalently complex) essential-supremum operator norm. All dimensions are integers at least three, and the asymptotic varies the dimension while the polynomial degree remains one. A measurable kernel-sign function is permitted in the input unit ball of \(L^\infty\); the projection output is continuous. For complex inputs the same row absolute integral remains the operator norm.

## Proof

**1. Exact kernel.** For \(Y\sim\sigma_d\), symmetry gives \(\mathbb EY_i=0\) for \(i<d\), \(\mathbb EY_iY_j=\delta_{ij}/d\), and \(\mathbb EY_iY_d=0\) for \(i<d\). The remaining moments are
\[
m_d=\mathbb E Y_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
\operatorname{Var}(Y_d)=\frac{v_d}{d},\quad v_d=1-dm_d^2>0.
\]
Inverting the diagonal covariance Gram matrix for \(1,Y_1,\ldots,Y_d\) yields
\[
K_d(a,y)=1+d\sum_{i=1}^{d-1}a_i y_i+\frac{d}{v_d}(a_d-m_d)(y_d-m_d).
\]
This is an exact identity for all \(d\ge3\) and all \(a,y\in H_d\); the normalized measure makes the constant reproducing term equal to one. Hence \(\|P_d\|=\sup_{a\in H_d}\Lambda_d(a)\), by kernel-row sign choices.

**2. Uniform Gaussian limit.** By rotations of the first \(d-1\) coordinates, the row norm at \(a\) depends only on \(t=a_d\); take \(a=(\sqrt{1-t^2},0,\ldots,0,t)\). Put \(R_{d,1}=\sqrt d\,Y_1\), \(R_{d,d}=\sqrt d\,Y_d\), and \(\mu_d=\sqrt d\,m_d\). The exact row expression is
\[
\frac{K_d(a,Y)}{\sqrt d}=\frac1{\sqrt d}+\sqrt{1-t^2}\,R_{d,1}
+\frac{t-m_d}{v_d}(R_{d,d}-\mu_d).
\]
Use independent standard Gaussians \(G_1,G_2,\ldots\) and represent the hemisphere law in dimension \(d\) by the coordinates \((G_1,G_3,\ldots,G_d,|G_2|)/(\sum_{i=1}^dG_i^2)^{1/2}\). On this single probability space,
\[
(R_{d,1},R_{d,d})\longrightarrow(G_1,|G_2|)
\]
almost surely and in \(L^1\). Indeed, the strong law gives the denominator limit after division by \(\sqrt d\); each rescaled coordinate has exactly unit second moment, uniformly in \(d\), implying uniform integrability. Thus \(\mu_d\to\mu\), \(v_d\to v>0\), and \(m_d\to0\). As \(\sqrt{1-t^2}\le1\), \(0\le t\le1\), and the other coefficient is uniformly bounded for sufficiently large \(d\), the inequality \(\big||x|-|y|\big|\le|x-y|\) gives convergence of absolute expectations *uniformly over* \(t\in[0,1]\). This proves the displayed local profile.

**3. Strict increase: an explicit positive certificate.** Write \(R=|Z'|\), \(Y=R-\mu\), so
\[
\mathbb E Y=0,\quad \mathbb E Y^2=v,\quad
m_4:=\mathbb E Y^4=3-2\mu^2-3\mu^4.
\]
For \(r\ge0\) set \(H(r)=\mathbb E|Z+rY|\) and \(A(r)=\mathbb E e^{-r^2Y^2/2}\). Differentiation through the Gaussian integral, justified by the finite moments above, gives
\[
H(r)-rH'(r)=\mu A(r),\qquad
\frac{H'(r)}\mu=\int_0^r\mathbb E\left[Y^2e^{-s^2Y^2/2}\right]ds.
\]
Set \(u=\mu^2=2/\pi\), \(C=v-m_4/6=1/2-(2/3)u+(1/2)u^2\). The elementary bounds \(3<\pi<22/7\) imply \(7/11<u<2/3\). The polynomial
\[
C-2v^2=-\frac32+\frac{10}3u-\frac32u^2
\]
is strictly increasing on this interval and equals \(5/363>0\) at \(u=7/11\), hence \(C>2v^2\). Since \(e^{-x}\ge1-x\), for \(0<r\le1\),
\[
H'(r)/\mu\ge rv-r^3m_4/6\ge rC> v^2rA(r).
\]
For \(r\ge1\), the formula for \(H'\) and monotonicity give \(H'(r)/\mu\ge C\). The density of \(Y\) is bounded by \(\mu\), so \(A(r)\le\min\{1,2/r\}\). Consequently also here \(H'(r)>\mu v^2rA(r)\).

Now let \(s=\sqrt{1-t^2}\), \(r=t/(vs)\) for \(0<t<1\). Since \(F(t)=sH(r)\), direct differentiation together with \(H-rH'=\mu A\) yields
\[
vF'(t)=H'(r)-\mu v^2rA(r)>0.
\]
By continuity at both endpoints and strict interior increase, \(F\) is strictly increasing on the full closed interval.

**4. Sharp norm, constant, and rigidity.** Uniform profile convergence and compactness give \(\|P_d\|/\sqrt d\to F(1)\). By the symmetry and mean \(\mu\) of \(R\),
\[
\mathbb E|R-\mu|=4\left[\varphi(\mu)-\mu(1-\Phi(\mu))\right].
\]
This gives the stated sharp coefficient. If \(a_d^{(d)}\to1\), uniform profile convergence makes the row norm asymptotically maximal. Conversely, any subsequence with \(a_d^{(d)}\le1-\varepsilon\) for fixed \(\varepsilon>0\) has \(F(a_d^{(d)})\le F(1-\varepsilon)<F(1)\), contradicting norming. This proves the equivalence.

## Verification

The reproducibility program `VERIFY.py` checks the rational inequality certificate \(C>2v^2\), the explicit half-normal constant, an independently numerically integrated local profile, strict growth of sampled profile values, an exact one-coordinate spherical density, and reproduction of constants and coordinates from directly sampled hemisphere points. It uses numerical checks only as diagnostics; all universal conclusions follow from the four analytic steps above. To run: `python VERIFY.py` (Python 3, NumPy, SciPy). The sampled examples are not exhaustive and do not prove an infinite-dimensional limit.

## Relationship to prior work

Le Gia and Sloan [1] study the uniform norm of hyperinterpolation on the *full* unit sphere, fixing ambient dimension and increasing polynomial degree; their full-sphere bound does not imply a fixed-degree high-dimensional projection profile on a hemisphere. Wade [2] proves weighted-ball hyperinterpolation estimates using a sphere-to-ball correspondence, likewise with different domain, operator, and limiting parameter. The new result is instead for the exact continuous orthogonal affine projector on a half-sphere and gives a sharp constant together with uniform spatial convergence and an asymptotic norming-location classification. These differences are mathematical distinctions, not a guarantee that no equivalent older formulation exists.

## Limitations

There is no proof here that the north pole is the exact maximizing row in *every fixed dimension*. The result does not cover nonhemispherical spherical caps, varying approximation degree, noisy or discretized least squares, or alternate measures. Originality is qualified by the possibility of earlier differently indexed exact calculations; the work has received no independent scientific validation.

## References

[1] T. Le Gia and I. H. Sloan, “The uniform norm of hyperinterpolation on the unit sphere in an arbitrary number of dimensions,” *Constructive Approximation* **17** (2001), 249–265, DOI: `10.1007/s003650010025`. Author-hosted full text: `https://web.maths.unsw.edu.au/~qlegia/LG_SloanCA01.pdf`. Online publication noted in the original paper: October 11, 2000.

[2] J. Wade, “On hyperinterpolation on the unit ball,” arXiv:1209.4328 (initial public posting September 19, 2012), `https://arxiv.org/abs/1209.4328`.
