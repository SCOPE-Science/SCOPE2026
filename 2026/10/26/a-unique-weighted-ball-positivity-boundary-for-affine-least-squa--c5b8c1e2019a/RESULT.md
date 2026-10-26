# A unique weighted-ball positivity boundary for affine least-squares projection

## Finding
Let \(B_d=\{x\in\mathbb R^d:\|x\|_2\le 1\}\), let \(d\ge1\) be an integer, and let \(\alpha>-1\). Equip \(B_d\) with the normalized radial probability measure \(d\mu_{d,\alpha}(x)=c_{d,\alpha}(1-\|x\|_2^2)^\alpha\,dx\). Let \(P_{d,\alpha}\) be the \(L^2(\mu_{d,\alpha})\)-orthogonal projection onto real affine functions. Define the effective dimension \(s=d+2\alpha+2>1\) and
\[
 C_s=\frac{\Gamma(s/2)}{\sqrt\pi\,\Gamma((s-1)/2)},\qquad
 \Phi(s)=1+2C_s\int_{1/s}^1(st-1)(1-t^2)^{(s-3)/2}\,dt.
\]
The exact endpoint norm is
\[
 \|P_{d,\alpha}\|_{L^\infty(\mu_{d,\alpha})\to L^\infty(\mu_{d,\alpha})}=\Phi(s).
\]
There is exactly one real \(\sigma\in(12,13)\) with \(\Phi(\sigma)=3\), and
\[
 \Phi(s)>3\quad\Longleftrightarrow\quad s>\sigma.
\]
Equivalently, **a measurable input \(0\le f\le1\) whose fitted affine function falls below \(-1\) exists exactly when \(d+2\alpha+2>\sigma\)**. In that regime a smooth input bounded strictly between zero and one also achieves the undershoot at an interior point of the ball. In the uniform-weight case \(\alpha=0\), the first dimension with this phenomenon is exactly \(d=11\).

The sharp minimum of the fitted value, jointly over all inputs \(0\le f\le1\) and all output locations \(x\in B_d\), is \((1-\Phi(s))/2\). In particular,
\[
 \Phi(13)=\frac{5441398251829}{1792160394037}>3,
 \qquad \Phi(12)<\frac{19136}{2079\pi}<3.
\]
For large real \(s\),
\[
 \Phi(s)=\sqrt{\frac{2s}{\pi}}\left(1+\frac{3}{4s}+O(s^{-2})\right).
\]
The integral formula itself is consistent with existing spherical projection formulas; the distinctive claim here is the **unique continuous-weight positivity boundary, its exact integer cutoff, and strict parameter ordering**. The result does not assert a new general reproducing-kernel formula.

## Assumptions and scope
Functions are real and essentially bounded with respect to \(\mu_{d,\alpha}\). The projector is the usual unweighted-in-function \(L^2\) least-squares projector using the indicated radial weight, not a metric projection onto a positivity cone. The norm is the operator norm between the corresponding \(L^\infty\) spaces. Boundary evaluation means the unique continuous affine representative, and the essential supremum on \(B_d\) equals its maximum there. The dimension \(d\) is integral, the radial exponent \(\alpha\) is any real greater than \(-1\), and all statements concerning \(s\) range over the resulting real parameters \(s>1\).

## Proof
**1. Projection kernel and exact norm.** Radial symmetry and the beta integral give \(\mathbb E_{\mu}[Y_i]=0\) and \(\mathbb E_{\mu}[Y_iY_j]=\delta_{ij}/s\). Consequently,
\[
 (P_{d,\alpha}f)(x)=\int_{B_d}(1+s\langle x,y\rangle)f(y)\,d\mu_{d,\alpha}(y).
\]
A coordinate \(T\) of \(Y\sim\mu_{d,\alpha}\) has the density \(C_s(1-t^2)^{(s-3)/2}\) on \((-1,1)\). Rotational symmetry makes the absolute kernel integral at \(x\) equal to \(\mathbb E|1+s\|x\|T|\). This is an even convex function of \(\|x\|\), hence nondecreasing on \([0,1]\), and the maximum is at the sphere. Integrating its negative part gives the displayed integral formula. Choosing the sign of the boundary kernel as input attains the operator norm. Since the kernel integrates to one, choosing the indicator of its negative set attains the minimum \((1-\Phi(s))/2\).

**2. A one-parameter stochastic representation.** Let \(Z_s=sT\). Its even density on \((-s,s)\) is
\[
 g_s(z)=\frac{C_s}{s}\left(1-\frac{z^2}{s^2}\right)^{(s-3)/2}.
\]
Symmetry gives the useful exact identity
\[
 \Phi(s)=\mathbb E\max\{1,|Z_s|\}
 =\mathbb E|Z_s|+\mathbb E(1-|Z_s|)_+,
 \qquad \mathbb E|Z_s|=\frac{2sC_s}{s-1}.
\]
Also \(\mathbb EZ_s=0\), \(\mathbb EZ_s^2=s\). For \(1<s\le8\), strict Cauchy–Schwarz yields \(\Phi(s)=\mathbb E|1+Z_s|<\sqrt{1+s}\le3\). The inequality is strict even at \(s=8\) because \(|1+Z_s|\) is not almost surely constant.

**3. Strict ordering beyond effective dimension six.** On \(0<z<s\), direct differentiation gives
\[
 \frac{\partial^2}{\partial s\,\partial z}\log g_s(z)
 =\frac{z(s^2-6s+z^2)}{(s^2-z^2)^2}>0
 \qquad(s\ge6,\ z>0).
\]
Thus for every \(s_2>s_1\ge6\), the density ratio \(g_{s_2}(z)/g_{s_1}(z)\) is strictly increasing on the common positive support, and the larger parameter additionally has positive density on \((s_1,s_2)\). Normalization forces a unique density crossing; consequently \(|Z_{s_2}|\) strictly first-order stochastically dominates \(|Z_{s_1}|\). The nonconstant increasing function \(z\mapsto\max\{1,z\}\) then gives \(\Phi(s_2)>\Phi(s_1)\). This is a continuum assertion: checking finitely many dimensions would not prove it.

**4. A rational cutoff certificate.** For \(s=12\), \(C_{12}=256/(63\pi)\). The density of \(|Z_{12}|\) decreases on its positive support; on \(0\le z\le1\) it is bounded by its density at zero. The triangular correction therefore obeys
\[
 \mathbb E(1-|Z_{12}|)_+<C_{12}/12,
 \qquad \Phi(12)<\frac{2\cdot12C_{12}}{11}+\frac{C_{12}}{12}
 =\frac{19136}{2079\pi}<3,
\]
where the last inequality already follows from the classical bound \(\pi>31/10\). For \(s=13\), \(C_{13}=693/512\), and the density on \(0\le z\le1\) is bounded below by its value at one. Bernoulli's inequality yields
\[
 \Phi(13)\ge\frac{3003}{1024}+\frac{693}{6656}\left(1-\frac5{169}\right)
 =\frac{6824895}{2249728}>3.
\]
The exact value of \(\Phi(13)\) follows independently by expanding \((1-t^2)^5\) in the defining integral and integrating each monomial. Continuity of \(\Phi\), its strict growth for \(s\ge6\), the \(s\le8\) bound, and the two endpoint certificates prove existence and uniqueness of the threshold \(\sigma\), with the asserted iff. The uniform case has \(s=d+2\), so \(d=11\) is the first integer dimension above the boundary.

**5. Strictly positive smooth witness.** When \(\Phi(s)>3\), the negative-kernel indicator yields a fitted value below \(-1\) at a boundary point. Because the fitted function is affine and the inequality is strict, the same is true at an interior point nearby. Smooth functions approximating that indicator in \(L^1(\mu)\) retain the strict inequality, because the kernel is bounded for fixed \(s\). Affinely rescaling such an approximation into \((\varepsilon,1-\varepsilon)\) with sufficiently small positive \(\varepsilon\) provides the claimed smooth, strictly positive witness.

**6. Two-term asymptotic.** The gamma-ratio expansion gives \(C_s=\sqrt{s/(2\pi)}(1-3/(4s)+O(s^{-2}))\). Hence \(\mathbb E|Z_s|=\sqrt{2s/\pi}(1+1/(4s)+O(s^{-2}))\). The correction is the triangular integral
\[
 \mathbb E(1-|Z_s|)_+
 =\frac{2C_s}{s}\int_0^1(1-z)\left(1-\frac{z^2}{s^2}\right)^{(s-3)/2}dz
 =\frac{C_s}{s}(1+O(s^{-1})).
\]
Combining the two expansions gives the stated relative coefficient \(3/(4s)\).

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic to reconstruct the \(s=13\) polynomial integral and its closed rational value, and separately verifies the rational endpoint inequalities \(\Phi(12)<3<\Phi(13)\). It compares two independent quadrature expressions for \(\Phi(s)\) at several integer parameters and checks instances of the likelihood-ratio derivative sign. The global uniqueness and the asymptotic expansion are mathematical proofs above, **not conclusions from those finite tests**. Run `python verify.py` with Python 3 and its standard library.

## Relationship to prior work
Figueroa studies the weighted \(L^2\)-orthogonal polynomial projectors on the same weighted unit balls and proves Sobolev approximation estimates; these do not determine the above unique endpoint overshoot frontier. Xu provides general reproducing-kernel and Lebesgue-constant theory for ball polynomials. Defant, Galicer, Mansilla, Mastyło and Muro give exact formulas for natural orthogonal projection norms on real spheres, including degree-one spherical polynomials; using the sphere-coordinate representation, their formulas also cover the **unweighted** ball norm for integer dimensions, and certain weighted cases with integral effective dimension. Such previously available formulae are not claimed as new here. The additional likelihood-ratio comparison, unique threshold over all real weights, and sharp integer undershoot cutoff are the subject of this finding. A distinct existing simplex calculation has a different positivity cutoff. No claim of definitive bibliographic priority is made.

## Limitations
The classification concerns degree-at-most-one least-squares projection, radial beta weights, the \(L^\infty\) endpoint norm and input data between zero and one. It does not classify higher-degree projectors or nonradial weights. Numerical evaluation of \(\sigma\) is optional; the rigorous location established here is \(12<\sigma<13\). Full comparison against older inaccessible general ball-projection papers remains a literature-priority risk, particularly sources employing Jacobi-integral identities. The self-review is not an independent audit.

## References
1. L. E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit ball*, arXiv:1607.00930v1 (public July 4, 2016); Journal of Approximation Theory (2017).
2. Y. Xu, *Representation of reproducing kernels and the Lebesgue constants on the ball*, Journal of Approximation Theory **112** (2001), 295–310, doi:10.1006/jath.2001.3597.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres*, arXiv:2405.12123v1 (2024); Journal of the London Mathematical Society **113** (2026), e70429, doi:10.1112/jlms.70429.
4. B. Sündermann, *On projection constants of polynomial spaces on the unit ball in several variables* (1984); historically relevant but full text was not accessible for this comparison.
