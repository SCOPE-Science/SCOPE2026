# Uniform second-order chord-entropy law at the radial-mean endpoint

## Finding
Let \(K\subset\mathbb R^d\), \(d\ge2\), be any full-dimensional compact convex body. Define \(T_\epsilon(K)=\epsilon^{1/(\epsilon-1)}R_{-1+\epsilon}K\) for \(0<\epsilon<1\), where \(R_pK\) is the Gardner–Zhang radial \(p\)-mean body, and \(L(K)=|K|\Pi^\circ K\), the volume-scaled polar projection body. For each unit \(u\), let \(Y\) be uniform on the orthogonal projection \(P_{u^\perp}K\); write \(\ell_u(Y)\) for the length of the corresponding chord parallel to \(u\), \(\mu_u=\mathbb E\ell_u=|K|/|P_{u^\perp}K|\), and \(Z_u=\ell_u/\mu_u\). Define the chord-entropy loss and its logarithmic variance by
\[
J_K(u)=-\mathbb E\log Z_u,\qquad V_K(u)=\operatorname{Var}(\log Z_u).
\]

**Uniform second-order theorem.** There exists a finite constant \(C_d\), depending only on the dimension, such that for *every* \(K\), every unit \(u\), and \(0<\epsilon\le1/4\),
\[
\left|\log\frac{\rho_{T_\epsilon(K)}(u)}{\rho_{L(K)}(u)}-\epsilon J_K(u)-\epsilon^2\left(J_K(u)-\frac12V_K(u)\right)\right|\le C_d\epsilon^3.
\]
Moreover, uniformly over all convex bodies,
\[
0\le J_K(u)\le H_{d-1}-\log d,\qquad H_{d-1}=\sum_{j=1}^{d-1}\frac1j.
\]
Both endpoint bounds are attained directionally. The lower equality is equivalent to constant parallel-chord length almost everywhere, or equivalently an oblique prism along \(u\). The upper equality is equivalent to a conical roof chord-length function (and is attained by a double pyramid along \(u\)). The sharp maximal first-order loss approaches the Euler–Mascheroni constant \(\gamma\) as \(d\to\infty\).

For the entire negative-parameter range, the already-known Berwald inequality yields the sharp directional envelope, included here to calibrate the new expansion:
\[
1\le\frac{\rho_{T_\epsilon(K)}(u)}{\rho_{L(K)}(u)}\le\mathcal B_{d,\epsilon},\qquad
\mathcal B_{d,\epsilon}=\left(\frac{\binom{d-1+\epsilon}{d-1}}{d^\epsilon}\right)^{1/(1-\epsilon)}.
\]
The lower equality is the prism case and the upper equality is the conical-chord case. The first-order coefficient detects chord nonconstancy quantitatively:
\[
J_K(u)\ge \frac1{2d^2}\mathbb E\left[(Z_u-1)^2\right].
\]

Writing \(d\sigma\) for ordinary spherical surface measure, the associated uniform volume expansion is
\[
\begin{split}
|T_\epsilon(K)|={}&|L(K)|+\epsilon\int_{\mathbb S^{d-1}}\mu_u^dJ_K(u)\,d\sigma(u)\\
&+\epsilon^2\int_{\mathbb S^{d-1}}\mu_u^d\left[J_K(u)-\frac12V_K(u)+\frac d2J_K(u)^2\right]d\sigma(u)
+O_d(\epsilon^3|L(K)|).
\end{split}
\]
Its first-order coefficient is strictly positive for every full-dimensional \(K\).

## Assumptions and scope
For \(-1<p<0\), set \(\ell_K(x,u)=\max\{s\ge0:x+su\in K\}\) and use the standard radial-mean normalization
\[
\rho_{R_pK}(u)^p=\frac1{|K|}\int_K\ell_K(x,u)^p\,dx.
\]
The polar projection body has radial function \(\rho_{\Pi^\circ K}(u)=1/|P_{u^\perp}K|\). Every formula uses Lebesgue volume and unit Euclidean directions. Chords are positive for almost every projected point. The dimension-only error constant is existential, not claimed optimal. A conical roof on a projection domain \(D\) means \(\ell_u(y)=M(1-g_{D-z}(y-z))\) for some interior maximizer \(z\) and its Minkowski gauge \(g_{D-z}\), up to null sets. Equality of the Berwald comparison characterizes such roofs.

## Proof
**Exact chord reduction.** Fubini gives, for \(p>-1\), \(p\ne0\),
\[
\rho_{R_pK}(u)^p=\frac{\mathbb E\ell_u^{p+1}}{(p+1)\mu_u}.
\]
Indeed on a chord of length \(a\), the integral of the positive exit distance to exponent \(p\) equals \(a^{p+1}/(p+1)\). With \(p=\epsilon-1\), it follows *exactly* that
\[
\frac{\rho_{T_\epsilon(K)}(u)}{\mu_u}=\left(\mathbb E Z_u^\epsilon\right)^{1/(\epsilon-1)}.
\]
This identity also fixes the scaling \(\rho_{L(K)}(u)=\mu_u\).

**Universal small-chord tails.** The chord function \(f(y)=\ell_u(y)\) is concave over the convex projection domain \(D\). Let \(M=\max_D f\), attained at \(z\). For \(0<t<1\), concavity shows that \(\{f\ge tM\}\) contains \(z+(1-t)(D-z)\). Hence, with \(m=d-1\),
\[
\Pr(f(Y)<tM)\le1-(1-t)^m\le mt.
\]
Integrating these level sets gives \(M/d\le\mu_u\le M\), so \(0<Z_u\le d\) and, uniformly in \(K,u\),
\[
\Pr(Z_u<t)\le (d-1)t\quad(0<t<1).
\]
In particular \(\Pr(-\log Z_u>s)\le(d-1)e^{-s}\) for \(s>0\), while \(\log Z_u\le\log d\). Every fixed logarithmic moment and the derivatives through order three of \(\Phi_u(s)=\log\mathbb E Z_u^s\), for \(0\le s\le1/4\), are therefore bounded by constants depending only on \(d\). The denominator \(\mathbb E Z_u^s\) is bounded away from zero by Jensen and the entropy bound proved below. One may also obtain that lower bound directly from the tail distribution.

**The second-order law.** At zero,
\[
\Phi_u(0)=0,\quad\Phi_u'(0)=-J_K(u),\quad\Phi_u''(0)=V_K(u).
\]
Uniform Taylor's theorem gives \(\Phi_u(\epsilon)=-\epsilon J_K(u)+\epsilon^2V_K(u)/2+O_d(\epsilon^3)\). Dividing by \(\epsilon-1\) proves the announced uniform second-order radial formula.

**Sharp entropy bounds and equality models.** Since \(\mathbb EZ_u=1\), Jensen gives \(J_K(u)\ge0\), with equality only for constant chords. The concave-function Berwald inequality, in base dimension \(m=d-1\), states that \(\left[\binom{m+s}{m}\mathbb Ef^s\right]^{1/s}\) decreases with \(s>0\). Compare \(s=\epsilon<1\) with \(s=1\) and use the exact chord reduction to get the displayed finite-parameter sharp envelope. Letting \(\epsilon\downarrow0\), \(\frac{d}{ds}\log\binom{m+s}{m}|_{s=0}=H_m\), gives \(J_K(u)\le H_m-\log(m+1)\). Berwald equality for distinct positive exponents characterizes conical roof functions. For such a roof, \(f/M\) has distribution \(\operatorname{Beta}(1,m)\), so \(J=H_m-\log(m+1)\) and \(V=\sum_{j=1}^m j^{-2}\), and the finite-parameter bound is an equality. A double pyramid with a suitable projection base realizes this profile; a parallel prism realizes constant chords. The harmonic-number upper endpoint increases to \(\gamma\) as \(d\to\infty\).

For the quantitative lower bound, apply the pointwise second-derivative estimate to \(g(z)=z-1-\log z\): since \(0<z\le d\), \(g''(z)=z^{-2}\ge d^{-2}\), thus \(g(z)\ge(z-1)^2/(2d^2)\). Its expectation equals \(J\).

**Volume and strictness.** The 2026 convexity theorem ensures \(R_pK\) and hence \(T_\epsilon(K)\) are convex bodies in the negative-parameter range. Apply polar integration \(|T|=d^{-1}\int_{\mathbb S^{d-1}}\rho_T(u)^d\,d\sigma(u)\), expand the exponential of the radial logarithmic law uniformly, and integrate to obtain the volume formula with error \(O_d(\epsilon^3|L|)\). To prove strictness, choose \(u\) in the direction of a diameter of \(K\). A chord of length equal to the diameter exists. If every parallel chord had this length, two distinct parallel chords would have opposite endpoints whose distance exceeds that diameter (by the Pythagorean identity), a contradiction. Thus \(J_K(u)>0\). The function \(u\mapsto J_K(u)\) is continuous by Hausdorff-continuity of rotated convex chord profiles and the uniform logarithmic-tail estimate above, hence it is positive on a nonempty open spherical set. Consequently the first-order volume coefficient is strictly positive.

## Verification
Run the included standard-library script `checks/verify.py` with Python 3. It checks the exact beta/gamma sharpness model in dimensions 2 through 19, the first two asymptotic coefficients, a non-extremal disk profile, and prism and planar-square extremizers at multiple parameters. These computations are consistency checks; the proof uses full-domain concavity, Berwald's published theorem, exact Fubini identities and uniform Taylor bounds, rather than numerical extrapolation.

## Relationship to prior work
Gardner and Zhang (1998) introduced radial mean bodies, established the chord-moment identity, and used Berwald's inequality for scale-corrected inclusions. Langharst and Putterman (2025) proved weighted Berwald and equality cases, including negative parameters. Langharst (first submitted March 14, 2026) proves convexity for the entire negative interval and identifies the qualitative polar-projection limit. The *finite-parameter Berwald envelope* and its cone equality example are consequences of established theory and are **not** claimed new. The present quantitative contribution is the two-coefficient logarithmic chord-entropy and volume expansion with a dimension-only third-order remainder valid uniformly over every body and direction, together with the resulting explicit positive volume approach rate and chord-variance stability interpretation.

## Limitations
The coefficient \(C_d\) is not optimized; the theorem is about fixed dimension, uniform in shape and direction, not dimension-uniform third-order constants. The proof does not reconstruct \(K\) from its chord-entropy profile or establish a sharp global normalized volume deficit. Historical priority of a potentially equivalent unindexed endpoint expansion remains unverified. Finite checks are not proofs of infinite-dimensional statements.

## References
1. R. J. Gardner and G. Zhang, “Affine inequalities and radial mean bodies,” *American Journal of Mathematics* **120** (1998), 505–528.
2. D. Langharst and E. Putterman, “Weighted Berwald’s Inequality,” *Indiana University Mathematics Journal* **74** (2025), 47–90; arXiv:2210.04438, first posted 2022-10-10, full HTML https://arxiv.org/html/2210.04438v7.
3. D. Langharst, “Radial Mean Bodies Are Convex” (formerly “Convexity of Radial Mean Bodies via an Extension of Ball’s Bodies”), arXiv:2603.14134, first posted 2026-03-14, full HTML https://arxiv.org/html/2603.14134v4.
4. “A discrete approach to Zhang’s projection inequality,” *Canadian Journal of Mathematics*, 2025, DOI 10.4153/S0008414X25101624; full HTML https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/discrete-approach-to-zhangs-projection-inequality/53287E6D1D42114A0996881A9D2C0363.
