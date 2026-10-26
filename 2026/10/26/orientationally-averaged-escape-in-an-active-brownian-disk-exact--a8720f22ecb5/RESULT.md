# Orientationally averaged escape in an active Brownian disk: exact quadratic response and a fast-turning boundary layer

## Finding

Consider an active Brownian particle in a fully absorbing unit disk, with dimensionless propulsion \(p\geq0\) and rotational diffusivity \(\gamma\geq0\), and an initially uniform independent propulsion angle. Its dimensionless mean exit time from initial radius \(\rho\in[0,1)\) has the expansion
\[
\overline T_{p,\gamma}(\rho)=\frac{1-\rho^2}{4}+p^2G_\gamma(\rho)+O_{\gamma,\rho}(p^4),\qquad p\downarrow0.
\]
For \(\gamma>0\), with \(I_j\) denoting a modified Bessel function,
\[
G_\gamma(\rho)=\frac{1}{4\gamma}\left[\frac{I_0(\sqrt\gamma)-I_0(\rho\sqrt\gamma)}{\sqrt\gamma I_1(\sqrt\gamma)}-\frac{1-\rho^2}{2}\right],
\]
and its continuous zero-rotation limit is
\[
G_0(\rho)=-\frac{(1-\rho^2)^2}{128}.
\]
For every \(0\leq\rho<1\), the coefficient is strictly negative at all finite \(\gamma\), strictly increasing with \(\gamma\), and tends to zero as \(\gamma\to\infty\). The global bounds are sharp:
\[
-\frac{(1-\rho^2)^2}{128}\leq G_\gamma(\rho)<0 \quad (\gamma\geq0),
\]
with equality on the left precisely at \(\gamma=0\).

The coefficient has a *universal absorbing-wall layer*: for every fixed \(z\geq0\), uniformly for \(z\) in bounded intervals,
\[
\lim_{\gamma\to\infty}\gamma^{3/2}G_\gamma\!\left(1-\frac z{\sqrt\gamma}\right)=\frac{1-e^{-z}-z}{4}.
\]
In contrast, for every fixed \(\rho<1\),
\[
G_\gamma(\rho)=-\frac{1-\rho^2}{8\gamma}+\frac{1}{4\gamma^{3/2}}+O_\rho(\gamma^{-2}).
\]
The wall-layer profile is a statement about the **quadratic weak-propulsion coefficient**, with the weak-propulsion expansion taken first; no simultaneous \(p\)-\(\gamma\) remainder bound is asserted.

## Assumptions and scope

In dimensionless coordinates, the particle follows
\[
dX_t=p(\cos\Theta_t,\sin\Theta_t)\,dt+\sqrt2\,dW_t,\qquad d\Theta_t=\sqrt{2\gamma}\,dB_t,
\]
where \(W_t\) and \(B_t\) are independent standard Brownian motions. It is killed on first reaching \(|X_t|=1\); \(\Theta_0\) is uniform on the circle and independent of the noises. The dimensionless units are radius \(R\), time \(R^2/D\), with \(p=vR/D\) and \(\gamma=D_{\rm rot}R^2/D\) for \(D,R>0\). The parameter \(\gamma=0\) means a static random starting direction. The angular average is at a **fixed starting spatial point**, not a spatial average. The primary subject is stochastic transport and first passage in time-dependent nonequilibrium statistical mechanics (MSC2020 82C31).

## Proof

The backward Dirichlet equation for the mean exit time \(T_{p,\gamma}(x,\theta)\) is
\[
(\Delta_x+\gamma\partial_\theta^2+p\,e_\theta\cdot\nabla_x)T_{p,\gamma}=-1,
\quad T_{p,\gamma}|_{|x|=1}=0.
\]
The translational diffusion makes the killed resolvent regular for each fixed \(\gamma\geq0\); a bounded first-order drift perturbation has a locally convergent resolvent expansion in sufficiently small \(p\). This can alternatively be obtained recursively from elliptic Dirichlet problems, with standard elliptic estimates controlling remainders. At \(p=0\), \(T_0(r)=(1-r^2)/4\). Replacing \(p\) by \(-p\) is equivalent to rotating the initial propulsion angle by \(\pi\). Therefore the angle average is even and its next remainder after order two is \(O(p^4)\) for fixed parameters.

Write \(\phi=\theta-\arg(x)\) and \(T=T_0+pT_1+p^2T_2+\cdots\). The order-one equation is \((\Delta+\gamma\partial_\theta^2)T_1=\frac r2\cos\phi\). Hence \(T_1=f_\gamma(r)\cos\phi\), with the regular boundary-value problem
\[
f_\gamma''+r^{-1}f_\gamma'-(r^{-2}+\gamma)f_\gamma=r/2,\quad f_\gamma(0)=f_\gamma(1)=0.
\]
For \(\gamma>0\), its unique regular solution is
\[
f_\gamma(r)=\frac{1}{2\gamma}\left[\frac{I_1(\sqrt\gamma\,r)}{I_1(\sqrt\gamma)}-r\right].
\]
For \(\gamma=0\), it is \(f_0(r)=(r^3-r)/16\). The order-one solution and its Bessel formula are **previously published** (Iyaniwura--Peng, 2025); neither is claimed as new here.

Let \(G_\gamma(r)\) be the initial-angle average of \(T_2\). Since \(e_\theta\cdot\nabla_x[f_\gamma(r)\cos\phi]=f_\gamma'(r)\cos^2\phi+(f_\gamma(r)/r)\sin^2\phi\), the order-two equation gives
\[
G_\gamma''+r^{-1}G_\gamma'=-\tfrac12(f_\gamma'+f_\gamma/r),
\quad G_\gamma'(0)=0,\quad G_\gamma(1)=0.
\]
Integrating the exact radial divergence identity yields \(G_\gamma'(r)=-f_\gamma(r)/2\) and
\[
G_\gamma(r)=\tfrac12\int_r^1 f_\gamma(s)\,ds.
\]
The Bessel antiderivative \(\frac d{ds}I_0(\sqrt\gamma s)=\sqrt\gamma I_1(\sqrt\gamma s)\) proves the announced formula; directly integrating \(f_0\) proves the zero-rotation formula.

For sign and strict parameter monotonicity, define the positive Dirichlet Bessel operator on regular radial first harmonics,
\[
A_\gamma=-\partial_r^2-r^{-1}\partial_r+r^{-2}+\gamma.
\]
The one-dimensional maximum principle (or its positive Green kernel) gives \(A_\gamma^{-1}r>0\) on \((0,1)\). Since \(f_\gamma=-\tfrac12 A_\gamma^{-1}r\), the resolvent identity gives
\[
\partial_\gamma f_\gamma=\tfrac12 A_\gamma^{-2}r>0
\]
in the interior, including the one-sided derivative at \(\gamma=0\). Integrating over \([\rho,1]\) gives strict negativity and strict increase of \(G_\gamma(\rho)\). The Bessel formula gives convergence to zero and the sharp endpoint bound.

Finally let \(k=\sqrt\gamma\). For fixed \(\rho<1\), standard large-argument modified-Bessel asymptotics give \(I_0(k)/I_1(k)=1+1/(2k)+O(k^{-2})\) and \(I_0(k\rho)/I_1(k)=o(k^{-m})\) for each fixed \(m>0\), which proves the bulk expansion. With \(\rho=1-z/k\) and \(z\) bounded, the uniform ratio asymptotics \(I_0(k-z)/I_1(k)\to e^{-z}\) and \(I_0(k)/I_1(k)\to1\), together with \((1-\rho^2)/2=z/k+O(k^{-2})\), imply the announced wall-layer limit uniformly on compact \(z\)-sets.

## Verification

The accompanying standalone `verify.py` independently checks the Bessel quadrature identity, the first-harmonic differential equation, zero-rotation polynomial, sign and monotone sample values, and the wall-layer convergence at high precision. Those finite numerical checks are supporting diagnostics; the maximum principle, exact radial integration, and Bessel asymptotic argument above are the infinite-parameter proofs. Run `python verify.py` with Python and `mpmath`.

## Relationship to prior work

Di Trapani, Franosch and Caraglio (2023), arXiv:2306.12702v1, formulate the same absorbing-disk active-Brownian dynamics and construct a full time-dependent propagator and first-passage-time distribution. Iyaniwura and Peng (2025), arXiv:2506.15813v1, derive the same backward MFPT equation and **explicitly compute the order-one radial Bessel function** displayed above; they observe that an initially uniform orientation removes this term and leaves an order-two correction, but do not supply its explicit coefficient. Iyaniwura and Peng (2023/2024), arXiv:2310.04446, derive second-order corrections for a different **one-dimensional**, discrete-direction process. The present result isolates the missing two-dimensional uniform-orientation coefficient, proves its strict sign and rotational-diffusion order, and resolves its fast-turning absorbing-wall transition. The full propagator of 2023 determines MFPT implicitly, so it is not asserted that the coefficient could not have been derived from prior machinery.

## Limitations

This is a small-propulsion result for an entirely absorbing circle with translational Brownian diffusion. It does not address reflecting windows, interacting particles, chiral drift, general domains, or nonperturbative propulsion. The fast-turning limit concerns the computed second derivative at \(p=0\), not an unproved uniform two-parameter error estimate. The Bessel first-order coefficient is prior work. General resolvent or hidden supplementary calculations may imply the explicit second-order coefficient; identifying an unindexed exact equivalent remains a residual originality risk.

## References

- F. Di Trapani, T. Franosch and M. Caraglio, *Active Brownian Particles in a Circular Disk with an Absorbing Boundary*, arXiv:2306.12702v1 (2023), https://arxiv.org/html/2306.12702v1 .
- S. A. Iyaniwura and Z. Peng, *Mean first passage time of active Brownian particles in two dimensions*, arXiv:2506.15813v1 (2025), https://arxiv.org/html/2506.15813v1 .
- S. A. Iyaniwura and Z. Peng, *Asymptotic Analysis and Simulation of Mean First Passage Time for Active Brownian Particles in 1-D*, arXiv:2310.04446 (2023), https://arxiv.org/abs/2310.04446 .
- MSC2020, *82C31: Stochastic methods applied to time-dependent statistical mechanics*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C31 .
