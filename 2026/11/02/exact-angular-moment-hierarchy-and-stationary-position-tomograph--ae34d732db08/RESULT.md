# Exact angular-moment hierarchy and stationary-position tomography for reset anisotropic Brownian particles

## Finding

Consider a passive, planar, shape-anisotropic Brownian particle for which both the position and orientation are reset simultaneously to a fixed state at independent Poisson times. Its stationary position distribution, without observing the heading, contains exact complex angular moments that permit a global inverse reconstruction of the rotational rate and both body-frame translational diffusivities, up to an unavoidable common time-scale factor. This is a population-moment identifiability statement, not a claim about statistically finite-sample estimators.

Let \(Z=X+iY\), \(m_{2n}=\mathbb E[Z^{2n}]\), and put \(\overline D=(D_\parallel+D_\perp)/2\), \(\Delta=(D_\parallel-D_\perp)/2\). For **every integer \(n\ge1\)**,

\[
m_{2n}=e^{2in\theta_0}\frac{(2n)!(2\Delta)^n}{\prod_{j=1}^n(r+4\gamma j^2)},\qquad
\mathbb E[Z^{2n+1}]=0,\qquad
S:=\mathbb E|Z|^2=\frac{4\overline D}r.
\]

For the nonisotropic model, put \(A=|m_2|\) and \(Q=m_4/m_2^2\). Then \(Q\) is positive and real, with

\[
Q=\frac{6(r+4\gamma)}{r+16\gamma}\in(3/2,6],\qquad
\frac{\gamma}r=\frac{6-Q}{16Q-24},\qquad
\frac{\overline D}r=\frac S4,\qquad
\frac{\Delta}r=\frac{3AQ}{4(4Q-6)}.
\]

The initial nematic axis is determined by \(\theta_0=\tfrac12\arg(m_2)\pmod\pi\), while \(D_\parallel/r=\overline D/r+\Delta/r\) and \(D_\perp/r=\overline D/r-\Delta/r\). Thus the three moment types \((S,m_2,m_4)\) uniquely determine all dimensionless parameters and the reset axis. If \(r\) is independently known, they also determine all physical diffusivities.

The **exact feasible region** for a complex second/fourth moment pair and radial second moment is characterized by \(S>0\), \(m_2\ne0\), \(m_4=Qm_2^2\) with real \(3/2<Q\le6\), and

\[
0<\frac{|m_2|}S<\frac{4Q-6}{3Q}.
\]

Each such triple has precisely one compatible set of dimensionless model parameters. The upper inequality is strict because both body-axis diffusivities are positive. The endpoint \(Q=6\) corresponds exactly to \(\gamma=0\); \(Q=3/2\) is an inaccessible infinite-rotation limit.

**Fourth-order necessity.** With only \(S,m_2\), for any \(0\le g<(S/A-1)/4\) one can choose \(\gamma/r=g\), \(\overline D/r=S/4\), and \(\Delta/r=A(1+4g)/4\), producing the same second moments. Hence second-order position measurements cannot separate rotational mixing from shape anisotropy, whereas the fourth angular complex moment does.

## Assumptions and scope

Let \(r>0\), \(\gamma\ge0\), \(D_\parallel>D_\perp>0\), \(\theta_0\in\mathbb R/(\pi\mathbb Z)\), and independent standard Brownian motions \(W^1,W^2,B\). Between successive joint resets, the particle starts at the origin with angle \(\theta_0\), follows \(\Theta_t=\theta_0+\sqrt{2\gamma}B_t\), and satisfies

\[
dZ_t=e^{i\Theta_t}\left(\sqrt{2D_\parallel}\,dW^1_t+i\sqrt{2D_\perp}\,dW^2_t\right).
\]

Independent Poisson resets of rate \(r\) return **both** \(Z\) and \(\Theta\) to \((0,\theta_0)\). The stationary law is the exponential-age mixture of the one-episode law, and all polynomial position moments are finite. The angles are nematic: \(\theta_0\) and \(\theta_0+\pi\) describe the same position distribution. The strict convention \(D_\parallel>D_\perp\) removes the alternative exchange-of-axes representation.

## Proof

**1. Conditional Gaussian and renewal representation.** The complex quadratic variation is

\[
d[Z,Z]_t=4\Delta e^{2i\Theta_t}\,dt.
\]

If \(T\sim\operatorname{Exp}(r)\) is independent of a fresh episode, then the stationary position equals the position at age \(T\) in distribution. Conditional on \(T\) and the complete angle path, \(Z_T\) is a centered, real two-dimensional Gaussian. Writing

\[
I_T=\int_0^T e^{2i(\Theta_s-\theta_0)}\,ds,
\]

complex Wick contractions give, for each integer \(n\ge1\),

\[
\mathbb E[Z_T^{2n}\mid T,\Theta]=(2n-1)!!(4\Delta)^n e^{2in\theta_0} I_T^n,
\]

and all conditional odd moments vanish. This remains legitimate when \(I_T\) is complex; the Gaussian moment identity uses the complex bilinear second moment, not \(\mathbb E|Z|^2\).

**2. Exact angular occupation moments.** By ordering integration times \(0\le t_1\le\cdots\le t_n\le T\), using \(\Pr(T\ge t_n)=e^{-rt_n}\), and writing the successive time increments as \(u_j=t_j-t_{j-1}\), \(t_0=0\), independent rotational Brownian increments yield

\[
\mathbb E\exp\!\left(2i\sum_{k=1}^n(\Theta_{t_k}-\theta_0)\right)
=\exp\!\left(-4\gamma\sum_{j=1}^n(n-j+1)^2u_j\right).
\]

Integrating the \(n\) independent increments gives the exact identity

\[
\mathbb E[I_T^n]=\frac{n!}{\prod_{j=1}^n(r+4\gamma j^2)}.
\]

Absolute integrability follows from \(|I_T|\le T\) and the finite moments of an exponential random variable. Combining these steps and \((2n-1)!!\,n!=(2n)!/2^n\) proves the claimed all-order product. The trace identity follows directly from \(d[Z,\overline Z]_t=4\overline D\,dt\), giving \(S=4\overline D\mathbb E T=4\overline D/r\).

**3. Independent stationary generator proof.** After rotating the initial axis to zero, set \(F_{n,k}=\mathbb E[Z^{2n}e^{2ik\Theta}]\). For \(n\ge1\), Itô's formula and the reset generator give

\[
(r+4\gamma k^2)F_{n,k}=4n(2n-1)\Delta F_{n-1,k+1},\qquad
F_{0,k}=\frac r{r+4\gamma k^2}.
\]

Iteration from \((n,k)=(n,0)\) proves the same formula by a second calculation, independent of Gaussian Wick/order-statistics integration. In this rotated calculation \(Z\) denotes the rotated complex position and \(\Theta\) denotes the relative angle.

**4. Inverse and feasibility.** At orders two and four the formula reduces to \(m_2=4\Delta e^{2i\theta_0}/(r+4\gamma)\) and \(m_4=96\Delta^2 e^{4i\theta_0}/[(r+4\gamma)(r+16\gamma)]\). Division yields \(Q=6(r+4\gamma)/(r+16\gamma)\), strictly decreasing from \(6\) to \(3/2\) as \(g=\gamma/r\) increases from zero to infinity. Algebra gives the reconstruction formulas. Conversely, any triple in the displayed feasible region sets \(g=(6-Q)/(16Q-24)\ge0\), \(\overline D/r=S/4\), and \(\Delta/r=A(1+4g)/4\), with \(0<\Delta<\overline D\). Choosing a positive time scale \(r\) and \(\theta_0=\arg(m_2)/2\) constructs the desired stochastic model. Exact uniqueness follows from the same inversion.

**5. Sharp degeneracies.** If \(\Delta=0\), the spatial process is isotropic Brownian motion between position resets and its stationary spatial distribution is independent of \(\theta_0,\gamma\); no angular information remains. If \(r\) is not calibrated, multiplying \((r,\gamma,D_\parallel,D_\perp)\) by any common positive constant leaves the spatial stationary law invariant. These are structural obstructions, not numerical artifacts.

## Verification

The included standalone `verify_moments.py` uses only the Python standard library. It independently reconstructs the moments through the stationary generator and via the ordered-time Wick product using exact rational arithmetic through degree thirty-two. It checks the inverse formulas, strict feasible-region inequalities, and physical edge case \(\gamma=0\), and independently simulates rotational Brownian paths over exponentially distributed reset ages to check the first two occupation-integral moments. The script produces **98 passing assertions** in the recorded run. Randomized calculations are diagnostics and are **not** used to establish any all-order identity, uniqueness, or exact boundary statement.

## Relationship to prior work

Chaki, Olsen and Löwen (2024), *Anisotropic Brownian particles under resetting*, analyze precisely the full position-and-orientation resetting model and derive the renewal representation and stationary second moments (Section III, equations 17–25), together with a perturbative stationary density (Section III.1). Those model and second-order formulas are prior work. The result established here supplies the all-order **complex angular** moment product, fourth-to-second ratio inversion, precise attainable moment region, and sharp second-order identifiability obstruction, none of which is stated in the inspected source sections.

Kurzthaler and Franosch (arXiv:1911.03425), *Intermediate scattering function of an anisotropic Brownian circle swimmer*, give a general no-reset Fourier propagator and a **rotationally averaged radial** mean-quartic displacement (Section III and Appendix D). This is a plausible broader formal representation from which some moment ingredients might be recoverable, but it does not itself state a fixed-reset-heading Poisson stationary complex-moment hierarchy or the stated inverse theorem. Ghosh and Mandal (2025), *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, study an actively propelled extension and calculate lower position moments and a perturbative density; their treatment does not state the passive fourth-angular inversion.

## Limitations

The result concerns an exact stationary population distribution with deterministic joint Poisson resets and an independent, direction-symmetric rotational Brownian motion. It does not cover position-only resetting, orientation-only resetting, self-propulsion, biased/chiral rotation, orientation-dependent reset locations, measurement error, or finite-sample estimator performance. Recovering physical rather than normalized rates requires an external measurement of \(r\). The axis is identifiable only modulo \(\pi\). The inverse becomes ill-conditioned as \(Q\downarrow3/2\); in particular \(|d(\gamma/r)/dQ|=9/[32(Q-3/2)^2]\). A generic exact propagator and renewal theorem can encode these moments implicitly; independent investigation is needed to settle absolute publication priority.

## References

- S. Chaki, K. S. Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v1, 25 June 2024. https://arxiv.org/html/2406.17550v1
- C. Kurzthaler and T. Franosch, *Intermediate scattering function of an anisotropic Brownian circle swimmer*, arXiv:1911.03425v1, 8 November 2019. https://arxiv.org/abs/1911.03425
- A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149v1, 9 January 2025. https://arxiv.org/html/2501.05149v1
