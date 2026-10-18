# Boundary-vanishing order controls Schatten decay for harmonic Bergman commutators

## Finding
Fix \(\alpha>-1\), \(\beta>0\), and a real continuous function \(v:[0,1]\to\mathbb R\) with \(v(1)\ne0\). The weighted harmonic Bergman projection \(P_\alpha\) acts on \(L^2(\mathbb D,d\mu_\alpha)\), where normalized area \(dA=dx\,dy/\pi\) and \(d\mu_\alpha=(\alpha+1)(1-|z|^2)^\alpha dA\). Define the bounded radial multiplier
\[
u(z)=(1-|z|^2)^\beta v(|z|^2),\qquad K=[M_u,P_\alpha]=M_uP_\alpha-P_\alpha M_u.
\]
Put
\[
\kappa_{\alpha,\beta}=\left[\frac{\Gamma(\alpha+2\beta+1)}{\Gamma(\alpha+1)}-\left(\frac{\Gamma(\alpha+\beta+1)}{\Gamma(\alpha+1)}\right)^2\right]^{1/2}>0.
\]
Writing singular values in nonincreasing order with multiplicity gives the exact leading law
\[
\boxed{\lim_{n\to\infty}n^\beta s_n(K)=4^\beta|v(1)|\kappa_{\alpha,\beta}.}
\]
Thus, for every \(p>0\),
\[
K\in\mathcal S_p\quad\Longleftrightarrow\quad \beta p>1,
\qquad K\in\mathcal S_{1/\beta,\infty}\setminus\mathcal S_{1/\beta}.
\]
At the critical power there is an exact logarithmic spectral residue:
\[
\boxed{\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=1}^N s_n(K)^{1/\beta}=4\bigl(|v(1)|\kappa_{\alpha,\beta}\bigr)^{1/\beta}.}
\]
Equivalently, the positive operator \(|K|^{1/\beta}\) has the displayed common value under normalized Dixmier traces on the weak trace ideal.

## Assumptions and scope
All Hilbert spaces are complex. The projection is onto the **harmonic**, not merely analytic, square-integrable functions on the disk; it contains both \(z^m\) and \(\bar z^m\). The value of \(v\) away from the boundary may be arbitrary, subject only to real continuity. No monotonicity or differentiability of \(v\) is assumed. Singular values include algebraic multiplicities. The multiplier is bounded and the commutator is a bounded operator. The theorem refers to the canonical singular-value ordering, not merely individual angular blocks.

## Proof
**1. Exact angular reduction.** In polar coordinates, use \(t=|z|^2\) and angular Fourier modes \(e^{im\theta}\), \(m\in\mathbb Z\). In the mode indexed by \(m\), the harmonic Bergman space has one-dimensional span of the unit vector \(q_m(t)e^{im\theta}\), where
\[
q_m(t)=\frac{t^{|m|/2}}{\sqrt{(\alpha+1)B(|m|+1,\alpha+1)}}.
\]
The radial probability density \(|q_m(t)|^2(\alpha+1)(1-t)^\alpha\,dt\) is the beta density with parameters \((|m|+1,\alpha+1)\). Denote its expectation by \(\mathbb E_{|m|}\). Since \(u\) is real, let \(a_m=\mathbb E_m[u]\), \(h_m=(u-a_m)q_m\), and \(\sigma_m=\|h_m\|=[\mathbb E_m(u^2)-a_m^2]^{1/2}\). The commutator vanishes on the orthogonal complement of \(\operatorname{span}\{q_m,h_m\}\), and relative to the orthonormal pair \((q_m,h_m/\sigma_m)\) it has matrix
\[
\begin{pmatrix}0&-\sigma_m\\ \sigma_m&0\end{pmatrix}.
\]
Each angular mode contributes precisely two positive singular values \(\sigma_{|m|}\). Thus \(m=0\) contributes two, while the two modes \(m\) and \(-m\) contribute four when \(m\ge1\). Every \(\sigma_m\) is positive because \(u\) is continuous and nonconstant near \(t=1\).

**2. The boundary moment lemma.** For every real \(\gamma>0\), beta integration gives
\[
\mathbb E_m[(1-t)^\gamma]
=\frac{\Gamma(\alpha+\gamma+1)}{\Gamma(\alpha+1)}
 \frac{\Gamma(m+\alpha+2)}{\Gamma(m+\alpha+\gamma+2)},
\]
and hence
\[
\lim_{m\to\infty}m^\gamma\mathbb E_m[(1-t)^\gamma]
=\frac{\Gamma(\alpha+\gamma+1)}{\Gamma(\alpha+1)}.
\]
For bounded continuous \(v\), this remains true with an extra factor \(v(t)\) inside the expectation, multiplying the limit by \(v(1)\). Indeed split the integral at \(t=1-\delta\): the part below the split is bounded by a polynomial in \(m\) times \((1-\delta)^m\); continuity controls the other part. Apply this assertion with \(\gamma=\beta\), factor \(v\), and with \(\gamma=2\beta\), factor \(v^2\). It follows that
\[
\lim_{m\to\infty}m^{2\beta}\sigma_m^2
=v(1)^2\left[\frac{\Gamma(\alpha+2\beta+1)}{\Gamma(\alpha+1)}-\left(\frac{\Gamma(\alpha+\beta+1)}{\Gamma(\alpha+1)}\right)^2\right].
\]
Strict log-convexity of \(\Gamma\) makes the bracket positive, since \(\alpha+1>0\) and \(\beta>0\). In particular \(\sigma_m\sim |v(1)|\kappa_{\alpha,\beta}m^{-\beta}\).

**3. Rearrangement and sharp ideals.** The direct sum of finite-rank mode blocks is compact because \(\sigma_m\to0\). Let \(N(t)=\#\{n:s_n(K)>t\}\). For each fixed \(\varepsilon\in(0,1)\), eventually
\[
(1-\varepsilon)c m^{-\beta}\le\sigma_m\le(1+\varepsilon)c m^{-\beta},
\qquad c=|v(1)|\kappa_{\alpha,\beta}.
\]
Counting angular blocks, with four singular values per \(m\ge1\), then letting \(\varepsilon\downarrow0\), gives \(N(t)\sim4(c/t)^{1/\beta}\) as \(t\downarrow0\). Inverting this counting relation yields \(s_n(K)\sim4^\beta c n^{-\beta}\), without needing the individual \(\sigma_m\) to be monotone. Comparing the resulting positive sequence with \(n^{-\beta}\) establishes all stated Schatten and weak-Schatten assertions. Finally \(s_n(K)^{1/\beta}\sim4c^{1/\beta}/n\); summation and \(\sum_{n\le N}1/n\sim\log N\) give the logarithmic residue and measurability of \(|K|^{1/\beta}\).

## Verification
For \(v\equiv1\), the full radial-mode variance is explicit. Define
\[
b_m(\gamma)=\frac{\Gamma(\alpha+\gamma+1)}{\Gamma(\alpha+1)}
\frac{\Gamma(m+\alpha+2)}{\Gamma(m+\alpha+\gamma+2)}.
\]
Then \(\sigma_m^2=b_m(2\beta)-b_m(\beta)^2\). For example \(\alpha=0\), \(\beta=2\) gives \(\kappa_{0,2}=\sqrt{20}\), so \(s_n(K)\sim16\sqrt{20}/n^2\) and \(K\in\mathcal S_p\) precisely for \(p>1/2\). The standalone Python verifier `verify_radial_blocks.py` uses exact rational integration for several integer powers and checks the rank-two commutator block and finite-index asymptotics; run `python3 verify_radial_blocks.py`. The universal asymptotic is an analytical theorem, not an inference from finite computations.

## Relationship to prior work
Chbichib and Ghiloufi (2026, arXiv:2605.24698) prove a first-order singular-value asymptotic for commutators with multipliers harmonic off the origin, of the form \(U+\overline U+\nu\log|z|^2\). A generic radial boundary-flat function here is not harmonic off the origin; its arbitrary \(\beta\)-dependent decay and spectral residue are not statements of the cited theorem. Wu (1996) gives a Schatten \(p>1\) criterion for **harmonic symbols**, which does not include nonconstant bounded radial symbols here. Miao (2007) gives Schatten membership conditions for Hankel operators on harmonic Bergman spaces for \(2\le p<\infty\), overlapping some qualitative cases but not giving the stated full singular-value asymptotic, explicit coefficient, or the range \(0<p<2\) in its announced theorem. Stroethoff (1997) treats compact Hankel operators on weighted harmonic Bergman spaces, without an explicit asymptotic law in its published abstract. The fourfold multiplicity reflects two harmonic angular directions and two singular values in each radial commutator block, and is essential for the leading constant.

## Limitations
The theorem assumes radiality, a fixed positive boundary-vanishing exponent, and a nonzero leading boundary factor. If \(v(1)=0\), higher-order boundary information is needed; no assertion is made about arbitrary nonradial symbols or their exact singular profiles. The cited 2026 paper and a relevant older source could not be inspected in complete text; consequently an equivalent specialized formula in uninspected material remains a bibliographic risk. Independent validation has not been performed.

## References
1. K. Chbichib and N. Ghiloufi, *Spectral properties of commutators on harmonic Bergman spaces of the unit disk*, preprint posted 23 May 2026, arXiv:2605.24698, https://arxiv.org/abs/2605.24698.
2. J. Miao, *Schatten Class Hankel Operators on the Harmonic Bergman Space of the Unit Ball*, Integral Equations and Operator Theory 59 (2007), 53–65, https://doi.org/10.1007/s00020-007-1508-y.
3. K. Stroethoff, *Compact Hankel operators on weighted harmonic Bergman spaces*, Glasgow Mathematical Journal 39 (1997), 77–84, https://doi.org/10.1017/S0017089500031931.
4. M. Bourass, O. El-Fallah, I. Marrhich, H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743 (2021), https://arxiv.org/abs/2102.01743.
5. Z. Wu, *Operators on harmonic Bergman spaces*, Integral Equations and Operator Theory 24 (1996), 352–371, https://doi.org/10.1007/BF01204606.
