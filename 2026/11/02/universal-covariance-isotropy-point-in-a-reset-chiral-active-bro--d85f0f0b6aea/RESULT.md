# Universal covariance-isotropy point in a reset chiral active Brownian particle

## Finding
For a two-dimensional chiral active Brownian particle whose position and orientation are **both** reset to a fixed position and heading at Poisson rate \(r>0\), the exact centered stationary covariance tensor has a universal isotropy point:
\[
\boxed{\Sigma\text{ is proportional to }I_2\quad\Longleftrightarrow\quad r=2D_r.}
\]
This holds for every nonzero angular drift \(\Omega\), every active speed \(v>0\), and every isotropic translational diffusivity \(D_t\geq0\), provided the angular diffusivity \(D_r>0\). At that point the stationary spatial distribution need **not** be rotationally invariant; only its **centered covariance** is isotropic. The formula remains valid at \(\Omega=0\) as a boundary case, but the chiral \(\Omega\ne0\) range is the primary result.

Write \(Z=X+iY\) in laboratory coordinates aligned with the reset heading. Define
\[
A=r+D_r,\qquad B=r+4D_r,\qquad
m=\mathbb E Z,\qquad Q=\mathbb E[(Z-m)^2],\qquad V=\mathbb E|Z-m|^2.
\]
Then the complete exact stationary second-moment law is
\[
\boxed{m=\frac{v}{A-i\Omega},\qquad
Q=\frac{v^2(r-2D_r)}{(A-i\Omega)^2(B-2i\Omega)},\qquad
V=\frac{4D_t}{r}+\frac{v^2(r+2D_r)}{r(A^2+\Omega^2)}.}
\]
The centered covariance matrix, in reset-heading coordinates, is
\[
\boxed{\Sigma=\frac12\begin{pmatrix}V+\Re Q&\Im Q\\\Im Q&V-\Re Q\end{pmatrix}.}
\]
Its two eigenvalues are \((V+|Q|)/2\) and \((V-|Q|)/2\), so their separation is \(|Q|\). In particular, \(|Q|\) is nonzero for all \(r\ne2D_r\). The transverse covariance changes sign under \(\Omega\mapsto-\Omega\), while the eigenvalue gap is invariant under this reversal. For the achiral boundary case \(\Omega=0\), the larger principal variance switches between the reset-heading axis and its perpendicular precisely at \(r=2D_r\).

## Assumptions and scope
Consider, between resets, the Itô system
\[
dZ_t=v e^{i\theta_t}\,dt+\sqrt{2D_t}(dB_t^{(1)}+i\,dB_t^{(2)}),\qquad
d\theta_t=\Omega\,dt+\sqrt{2D_r}\,dW_t.
\]
Here \(v>0\), \(D_r>0\), \(D_t\ge0\), \(r>0\), and \(\Omega\ne0\) are constants; the three standard real Brownian motions and the rate-\(r\) Poisson reset clock are mutually independent. Every reset maps \((Z,\theta)\mapsto(0,0)\) modulo \(2\pi\). This is the freely moving, spatially unconfined, constant-speed, constant-chirality model. The stationary law is understood in the full position-and-orientation state space, with position measured from the reset location and heading measured from the reset orientation. Its nonchiral \(\Omega=0\) limit obeys the same algebraic formulas.

## Proof
**1. Stationary renewal law and moments.** Couple any two realizations using the same reset times and subsequent independent Brownian increments. At the first common reset their states agree under this coupling, which proves uniqueness of the invariant law. A two-sided stationary Poisson clock supplies a stationary version: at observation time the last-reset age has density \(re^{-rt}\) and the process since that reset has the unreset law started from \((0,0)\). The exponential age and bounded-speed drift give all stationary spatial moments finite (a Gaussian term also has moments of every finite order).

**2. Fourier and position equations.** The generator of the reset process acts on the angular Fourier functions by
\[
0=\bigl(ik\Omega-k^2D_r-r\bigr)\mathbb E e^{ik\theta}+r,
\qquad\mathbb E e^{ik\theta}=\frac{r}{r+k^2D_r-ik\Omega},\quad k\in\mathbb Z.
\]
Here the reset contribution is \(r(f(0,0)-f(Z,\theta))\). Applying stationarity to \(Z\) gives \(r\mathbb E Z=v\mathbb E e^{i\theta}\), hence \(m=v/(A-i\Omega)\).

**3. Anisotropic complex second moment.** For \(Z e^{i\theta}\), ordinary Itô multiplication gives no mixed quadratic variation because the angular and translational noises are independent. Consequently
\[
(A-i\Omega)\mathbb E[Ze^{i\theta}]=v\mathbb E[e^{2i\theta}]
=\frac{vr}{B-2i\Omega}.
\]
The generator for \(Z^2\) has active drift \(2vZe^{i\theta}\), reset term \(-rZ^2\), and translational Itô correction \(dZ\,dZ=0\) because the two positional Brownian components have equal diffusivities. Thus
\[
\mathbb E Z^2=\frac{2v}{r}\mathbb E[Ze^{i\theta}]
=\frac{2v^2}{(A-i\Omega)(B-2i\Omega)}.
\]
Subtracting \(m^2\) and using \(2A-B=r-2D_r\) gives the displayed exact expression for \(Q\). All denominators are nonzero for \(r,D_r>0\); with \(v>0\), this shows \(Q=0\) if and only if \(r=2D_r\).

**4. Radial second moment and tensor.** Stationarity of \(Ze^{-i\theta}\) yields
\[
(A+i\Omega)\mathbb E[Ze^{-i\theta}]=v.
\]
Since \(dZ\,d\bar Z=4D_t\,dt\), stationarity of \(|Z|^2\) gives
\[
r\mathbb E|Z|^2=4D_t+2v\Re\mathbb E[Ze^{-i\theta}]
=4D_t+\frac{2v^2 A}{A^2+\Omega^2}.
\]
Subtract \(|m|^2=v^2/(A^2+\Omega^2)\) to obtain \(V\). Expanding \(Q=\mathbb E[(X-\mathbb EX)^2-(Y-\mathbb EY)^2+2i(X-\mathbb EX)(Y-\mathbb EY)]\) yields the covariance matrix. A real symmetric two-by-two matrix has equal eigenvalues precisely when its traceless part vanishes, i.e. precisely when \(Q=0\). Its eigenvalue gap equals \(|Q|\). Under reversal of chirality, all complex expressions are conjugated, giving the stated parity. At \(\Omega=0\), \(Q\) is real with the sign of \(r-2D_r\), giving the indicated principal-axis exchange. This completes the proof.

## Verification
The accompanying \`verify.py\` computes the independent finite-reset-age representation of \(\mathbb E Z\), \(\mathbb E Z^2\), and \(\mathbb E|Z|^2\) by numerical quadrature against the exponential age law and compares them to the stationary generator formulas. It also checks covariance positive semidefiniteness, chirality reversal, eigenvalue gap, and the critical-isotropy identity across parameter choices, including nonzero chirality. The verifier reports 84 successful finite checks. These checks test coefficients and normalizations, while the generator proof establishes the continuum and all-parameter statements.

## Relationship to prior work
Amir Shee, *Steering chiral active Brownian motion via stochastic position–orientation resetting*, arXiv:2508.12223, originally submitted 2025-08-17, derives the model's renewal law, mean displacement, scalar mean-squared displacement, orientation correlations, and higher radial moments. Its accessible full HTML text, including the lower-order moment and fourth-moment appendices, was examined. The present claim retains those established ingredients as prior work and evaluates the complete **centered Cartesian second-moment tensor**, especially its zero-anisotropy factor \(r-2D_r\); the inspected source does not explicitly state this universal chiral covariance-isotropy line.

Ghosh, Mandal and Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149 (2025), study several resetting protocols with anisotropic particle mobility and report direction-dependent fluctuations and effective diffusion. Their considered model does not have the independent constant chiral angular drift used here. The accessible abstract was examined; its full primary text was not accessible in this pass, so no claim of comprehensive exclusion is made. Standard generator and renewal methods account for the basic formulas, but neither these techniques nor scalar mean-squared displacement alone displays the factorized zero of the centered anisotropy for nonzero chirality. Priority beyond the inspected sources remains subject to independent literature review.

## Limitations
The covariance-isotropy line is **not** rotational invariance of the full stationary probability density, and does **not** say that the stationary mean vanishes. It is a statement only about centered second moments in a homogeneous isotropic translational-noise model. The law need not survive correlated translational/rotational noise, anisotropic mobility, heterogeneous resetting, non-Poisson reset times, or random reset headings. No finite-data inference rate or real-world implementation analysis is proved; this is a mathematically exact idealized-model result.

## References
- A. Shee, *Steering chiral active Brownian motion via stochastic position–orientation resetting*, arXiv:2508.12223, first version 2025-08-17. https://arxiv.org/abs/2508.12223 . Full HTML: https://arxiv.org/html/2508.12223 .
- A. Ghosh, S. Mandal and S. Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149, first version 2025-01-09. https://arxiv.org/abs/2501.05149 .
