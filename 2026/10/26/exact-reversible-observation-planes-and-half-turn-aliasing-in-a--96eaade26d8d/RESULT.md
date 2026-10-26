# Exact reversible-observation planes and half-turn aliasing in a rotational Langevin medium

## Finding
Let \(X_t\) be the stationary three-dimensional isotropic Ornstein--Uhlenbeck process with restoring rate \(a>0\), bath diffusivity \(T>0\), and nonzero skew rotation \(M v=\boldsymbol\omega\times v\). A rank-two orthogonal observation \(Y_t=PX_t\) has a completely time-reversible stationary path law **if and only if** its observation plane contains the rotation axis \(\boldsymbol\omega\). For every sampling interval \(\Delta>0\), the *entire sampled observation sequence* \((Y_{j\Delta})_{j\in\mathbb Z}\) is reversible **if and only if** either its plane contains the axis or \(\|\boldsymbol\omega\|\Delta\in\pi\mathbb Z\). The full three-coordinate sampled sequence is reversible exactly in the latter half-turn cases even though the continuous full system has strictly positive stationary entropy production rate \(2\|\boldsymbol\omega\|^2/a\).

For any positive lag \(t\), an exact two-snapshot forward/reverse relative entropy is provided below. Its infinitesimal-lag growth \(2(\boldsymbol\omega\cdot n)^2/a\) quantifies the fraction \((\boldsymbol\omega\cdot n)^2/\|\boldsymbol\omega\|^2\) of the full entropy-production rate visible through these two-snapshot tests. This fraction is **not** asserted to equal the relative-entropy rate of the complete non-Markovian observed path.

## Assumptions and scope
Consider the Itô equation on \(\mathbb R^3\)
\[
 dX_t=(-aI_3+M)X_t\,dt+\sqrt{2T}\,dW_t,
 \qquad Mv=\boldsymbol\omega\times v,
\]
with \(a,T>0\), \(\boldsymbol\omega\in\mathbb R^3\setminus\{0\}\), and a standard three-component Wiener process. All coordinate observables are even under kinematic time reversal. Write \(\Omega=\|\boldsymbol\omega\|>0\), \(\sigma^2=T/a\). Let \(P\) be any real \(2\times3\) matrix with \(PP^{\mathsf T}=I_2\). Its row vectors \(p_1,p_2\) define oriented normal \(n=p_1\times p_2\), and \(\nu=\boldsymbol\omega\cdot n\). The Gaussian process is taken in its unique strictly stationary centered law, whose one-time covariance is \(\sigma^2I_3\). Reversibility means invariance of *all finite-dimensional path laws* under reversal of time order without a parity flip of the observed coordinates.

For \(t>0\), let \(F_t=\sigma^{-2}\mathbb E[Y_tY_0^{\mathsf T}]\) and \(b_t=((F_t)_{21}-(F_t)_{12})/2\). Define \(K_t\) as the Kullback--Leibler divergence between the ordered Gaussian pair \((Y_0,Y_t)\) and its time-reversed ordering \((Y_t,Y_0)\). The diffusion's entropy production is defined by the standard stationary quadratic current integral \(\mathcal E=\int j^{\mathsf T}(T I_3)^{-1}j/\varrho\,dx\), where \(\varrho\) is the stationary density.

## Proof
**Stationary Gaussian law.** The drift \(A=-aI_3+M\) has spectrum \(-a,-a\pm i\Omega\). Since \(M^{\mathsf T}=-M\), the unique solution to \(A\Sigma+\Sigma A^{\mathsf T}+2TI_3=0\) is \(\Sigma=\sigma^2 I_3\). Hence \(Y_t\) is centered stationary Gaussian, with isotropic one-time covariance \(\sigma^2I_2\), independent of the rotation strength and plane.

**Exact lag obstruction.** Stationarity and the propagator give \(F_t=P e^{At}P^{\mathsf T}\) for \(t\ge0\). Rodrigues' identity yields
\[
 e^{Mt}=I_3+\frac{\sin(\Omega t)}{\Omega}M+
 \frac{1-\cos(\Omega t)}{\Omega^2}M^2.
\]
Since \(PMP^{\mathsf T}=\nu\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\),
\[
 F_t-F_t^{\mathsf T}
 =2e^{-at}\frac{\sin(\Omega t)}{\Omega}PMP^{\mathsf T},
 \qquad b_t=e^{-at}\frac{\nu}{\Omega}\sin(\Omega t).
\]
For any centered stationary real Gaussian vector process, invariance of every finite-dimensional law under time reversal is equivalent to symmetry of every nonnegative-lag covariance matrix: the reversed two-time covariance forces necessity, and each entry of every reversed higher-order covariance matrix agrees when the condition holds, proving sufficiency by Gaussianity. Thus the continuously observed pair is reversible exactly when \(\nu=0\). For samples at integer multiples of \(\Delta\), covariance symmetry is equivalent to \(\nu\sin(\Omega k\Delta)=0\) for every integer \(k\). If \(\nu\ne0\), the single value \(k=1\) forces \(\Omega\Delta\in\pi\mathbb Z\), which also suffices for all integer lags. Applying the same argument with \(P=I_3\) gives the full-coordinate stroboscopic criterion.

**Nonzero thermodynamic dissipation.** The stationary probability current is \(j(x)=Mx\,\varrho(x)\); its expectation gives
\[
 \mathcal E=\frac1T\mathbb E\|MX\|^2
 =\frac1a\operatorname{tr}(M^{\mathsf T}M)
 =\frac{2\Omega^2}{a}>0.
\]
This dissipation persists even when the observed coordinates, or the half-turn sampled full coordinates, are time reversible.

**Two-snapshot information law.** The covariance matrices of the ordered and reversed normalized Gaussian pairs are respectively
\[
 C_t=\begin{pmatrix}I_2&F_t^{\mathsf T}\\F_t&I_2\end{pmatrix},
 \qquad C'_t=\begin{pmatrix}I_2&F_t\\F_t^{\mathsf T}&I_2\end{pmatrix}.
\]
They are positive definite since \(\|F_t\|_2\le e^{-at}<1\). The centered Gaussian relative-entropy formula gives \(K_t=\tfrac12(\operatorname{tr}((C'_t)^{-1}C_t)-4)\), as the two covariance determinants agree. Direct inversion of these two-by-two blocks simplifies exactly to
\[
 \boxed{\displaystyle K_t=\frac{4b_t^2(1-\det F_t)}{\det(I_2-F_tF_t^{\mathsf T})}.}
\]
The denominator is positive and \(1-\det F_t>0\), because the singular values of \(F_t\) are below one. Thus \(K_t>0\) if and only if \(\nu\sin(\Omega t)\ne0\). Since \(F_t=I_2+(-aI_2+\nu J)t+O(t^2)\) with \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), \(b_t=\nu t+O(t^2)\), \(1-\det F_t=2at+O(t^2)\), and \(\det(I_2-F_tF_t^{\mathsf T})=4a^2t^2+O(t^3)\). Therefore
\[
 \boxed{\displaystyle \lim_{t\downarrow0}\frac{K_t}{t}=\frac{2\nu^2}{a}.}
\]
Dividing by the full dissipation rate yields the stated exact visibility fraction.

**Why reversible observations need not be Markovian.** If the observation plane contains the rotation axis, choose orthogonal coordinates \(U\) along that axis and \(V\) perpendicular to it within the plane. Both are independent stationary centered Gaussian scalar processes with autocovariances \(\sigma^2e^{-a|t|}\) and \(\sigma^2e^{-a|t|}\cos(\Omega t)\), respectively. The second process is not Markov: at \(t=\pi/(2\Omega)\) its covariance with the initial state vanishes, whereas the covariance at \(2t\) is nonzero, contradicting the conditional covariance factorization for stationary scalar Gaussian Markov processes. Consequently the reversible observed vector process is generally non-Markovian despite its exact equilibrium-like path symmetry.

## Verification
Run `python verify.py` with NumPy and SciPy. The standalone checker reconstructs random stable Lyapunov covariances and full matrix exponentials, tests the projected antisymmetry identity, independently evaluates both Gaussian relative-entropy formulas, checks all half-turn samples, and tests the small-lag coefficient and reversible planes. A run produced 300 random parameter/projection comparisons, 240 reversible-plane checks, and 100 infinitesimal-KL checks, all passing. Matrix identities and Gaussian reversibility provide the infinite-parameter proof; numerical tests do not establish it by enumeration.

## Relationship to prior work
The physical shear-free, antisymmetric hidden-medium coupling is the zero-shear subfamily of Fernandez, Hess, and Klapp [1]: its cross-coupling matrix is skew-symmetric and its unequal couplings define a rotation axis lying in the physical observation plane. Thus this model's reported equal-time moments, Gaussian drift equations, entropy behavior, and generalized Langevin memory kernel are prior knowledge. The new statement here is the **full-path and sampled-path reversibility classification for arbitrary observation planes**, including an exact two-snapshot information visibility law and the half-turn sampling alias. In particular, the physical zero-shear observation plane in [1] is reversible at every path length even though the complete process dissipates energy. General Ornstein--Uhlenbeck covariance and current identities are known from Godrèche and Luck [2]; those generic formulas are used rather than claimed new. Loos and Klapp [3] study irreversibility in related nonreciprocal hidden-variable systems; detailed equivalence with their complete article remains a priority risk because its full text was not available for the present comparison. This analysis identifies a model-specific classification, not a new general Gaussian calculus.

## Limitations
The theorem assumes equal diagonal trap rates and isotropic white-noise diffusivity in three dimensions, a constant skew rotational drift, strictly stationary preparation, exact orthogonal planar observation, and ordinary even-parity time reversal. It does not apply without modification to finite shear, unequal bath temperatures, arbitrary memory laws, noisy observation, or nonorthogonal coordinates. The two-snapshot infinitesimal relative-entropy rate is not the entropy production of the complete projected trajectory, and reversible time series need not satisfy a Markovian fluctuation-dissipation relation. The complete Loos--Klapp hidden-variable article and any otherwise unidentified equivalent theorem present residual publication-priority uncertainty. Independent review has not been performed.

## References
[1] L. Fernandez, S. Hess, S. H. L. Klapp, *Nonequilibrium dynamics and entropy production of a trapped colloidal particle in a complex nonreciprocal medium*, Physical Review E 109, 054129 (2024), arXiv:2402.10579, https://arxiv.org/abs/2402.10579, https://doi.org/10.1103/PhysRevE.109.054129 (first public 2024-02-16).

[2] C. Godrèche and J. M. Luck, *Characterising nonequilibrium stationary states of Ornstein--Uhlenbeck processes*, Journal of Physics A 52, 035002 (2019), arXiv:1807.00694, https://arxiv.org/abs/1807.00694.

[3] S. A. M. Loos and S. H. L. Klapp, *Irreversibility, heat and information flows induced by non-reciprocal interactions*, New Journal of Physics 22, 123051 (2020), arXiv:2008.00894, https://arxiv.org/abs/2008.00894.
