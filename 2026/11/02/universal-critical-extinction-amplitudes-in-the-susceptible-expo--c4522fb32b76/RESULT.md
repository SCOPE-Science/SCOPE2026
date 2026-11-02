# Universal critical extinction amplitudes in the susceptible–exposed–infectious–fomite model

## Finding
For the four-compartment epidemic model of González, Laguna and Abramson [1], at its exact critical reproduction threshold, all seeded biologically feasible trajectories with initially positive susceptible abundance have the same explicit inverse-time extinction profile. Write
\[
D=1+\frac{\mu}{\gamma}+\frac{\beta_f\rho}{\omega^2},\qquad
K=1+\frac{\mu}{\gamma}+\frac{\mu}{r}.
\]
Then for every such trajectory,
\[
\lim_{t\to\infty}t\bigl(1-S(t),E(t),I(t),F(t)\bigr)
=\left(\frac D\mu,\frac D{\gamma K},\frac D{\mu K},\frac{\rho D}{\omega\mu K}\right).
\]
In particular, the exact coefficient for infected hosts is \(D/(\mu K)\), and contaminated environmental material decays at the same inverse-time rate, even when direct transmission is absent.

## Assumptions and scope
The state is \(S,E,I,F\), respectively susceptible, exposed, infectious hosts and environmental fomites. The ODE is
\[
\begin{aligned}
\dot S &= r(S+E)(1-S-E-I)-S(\beta_1I+\beta_fF),\\
\dot E &= S(\beta_1I+\beta_fF)-\gamma E,\\
\dot I &= \gamma E-\mu I,\\
\dot F &= \rho I-\omega F.
\end{aligned}
\]
Assume \(r,\gamma,\mu,\rho,\omega,\beta_f>0\), \(\beta_1\ge0\), and the exact critical condition \(\beta_1+\beta_f\rho/\omega=\mu\). Initial data satisfy \(S(0)>0\), \(E(0),I(0),F(0)\ge0\), \(S(0)+E(0)+I(0)\le1\), and \(E(0)+I(0)+F(0)>0\). All limits are in the original ODE time units. The theorem includes the purely environmental transmission boundary \(\beta_1=0\), but excludes absent fomite transmission and infection-free initial states.

## Proof
**1. Invariant biological domain and extinction.** Writing \(N=S+E+I\) and \(\Lambda=\beta_1I+\beta_fF\), one has \(\dot N=r(S+E)(1-N)-\mu I\). Thus the nonnegative set \(N\le1\) is forward invariant. Fomites are bounded by the linear equation \(\dot F=\rho I-\omega F\); consequently all forward trajectories are precompact. Also \(S(t)>0\) since \(\dot S\ge-S\Lambda\) on this domain.

Set
\[
W=E+I+\frac{\beta_f}{\omega}F,\qquad u=1-S.
\]
At the critical parameter equality, direct differentiation gives the *exact*, not asymptotic, identity
\[
\dot W=-u\Lambda. \tag{1}
\]
Since \(0\le S\le1\), \(W\) is nonincreasing; the seeded assumption ensures \(W(t)>0\) at each finite time by positivity and uniqueness. On the set \(u\Lambda=0\), every complete forward-invariant trajectory must have \(E=I=F=0\): if \(u=0\), then \(S=1\) forces \(E=I=0\) and \(F>0\) would make \(\dot S<0\); if \(\Lambda=0\), positivity of \(\beta_f\) forces \(F=0\) and the invariant evolution \(\dot F=\rho I\) forces \(I=0\), then \(\dot I=\gamma E\) forces \(E=0\). LaSalle's argument applied to (1) therefore proves \(W(t)\to0\). The susceptible differential inequality
\[
\dot S\ge S\bigl(r(1-S-E-I)-\Lambda\bigr)
\]
and \(E+I+\Lambda\to0\), together with \(S\le1\), show by comparison with perturbed logistic equations that \(S(t)\to1\). Thus \(u(t)\to0\).

**2. Direction of the slow infection mode.** Let \(Z=(E,I,F)^{\mathsf T}\). Its equation is
\[
\dot Z=AZ-u\Lambda e_1,\qquad
A=\begin{pmatrix}-\gamma&\beta_1&\beta_f\\\gamma&-\mu&0\\0&\rho&-\omega\end{pmatrix}.
\]
The positive vectors \(v=(\mu/\gamma,1,\rho/\omega)^{\mathsf T}\), \(\ell=(1,1,\beta_f/\omega)^{\mathsf T}\) satisfy \(Av=0\), \(\ell^{\mathsf T}A=0\), and \(\ell^{\mathsf T}v=D\). The matrix is irreducible Metzler, so zero is its simple Perron eigenvalue and the other eigenvalues have strictly negative real part.

Let \(P=v\ell^{\mathsf T}/D\) and \(R=(\mathrm{Id}-P)Z\). Since \(\Lambda\le C W\) for a parameter-dependent constant \(C\), (1) implies \(|\dot W|/W\le Cu\to0\). Therefore, for each fixed sufficiently small \(\varepsilon>0\) and all late \(s\le t\), \(W(s)/W(t)\le e^{\varepsilon(t-s)}\). The exact evolution
\[
\dot R=AR-(\mathrm{Id}-P)e_1\,u\Lambda
\]
has an exponentially stable linear part on \(\operatorname{ran}(\mathrm{Id}-P)\); the forcing is \(o(W)\). Variation of constants, choosing \(\varepsilon\) smaller than the spectral decay rate, gives \(R(t)=o(W(t))\). Hence
\[
\frac{(E,I,F)}W\longrightarrow\frac1D\left(\frac\mu\gamma,1,\frac\rho\omega\right),\qquad
\frac\Lambda W\longrightarrow\frac\mu D. \tag{2}
\]
The last limit uses \(\beta_1+\beta_f\rho/\omega=\mu\).

**3. Susceptible deficit follows the same slow mode.** Expanding the original susceptible equation exactly yields
\[
\dot u=-ru+r(E+I)+\Lambda+r(u-E)(u-E-I)-u\Lambda. \tag{3}
\]
The last two terms are \(o(u+W)\) because \(u,W\to0\). Equation (3) and the late-time ratio estimate for \(W\) first give \(u=O(W)\) by comparison with \(\dot u\le-(r/2)u+C'W\). Indeed, the initial exponentially decaying homogeneous term is \(o(W)\) and the convolution of \(W\) is \(O(W)\). Hence the nonlinear remainder of (3) is actually \(o(W)\). The exponentially stable scalar filter and (2) give
\[
\frac uW\longrightarrow\frac1r\left[r\frac{1+\mu/\gamma}D+\frac\mu D\right]=\frac KD. \tag{4}
\]

**4. Exact amplitude.** Combining (1), (2), and (4) gives
\[
\frac{d}{dt}\left(\frac1W\right)=\frac{u\Lambda}{W^2}\longrightarrow\frac{\mu K}{D^2}>0.
\]
Cesàro averaging implies \(tW(t)\to D^2/(\mu K)\). Equations (2) and (4) yield the four asserted limits. There is no exceptional faster-decaying seeded trajectory because \(W(t)>0\) and all slow-mode limits are positive. \(\square\)

## Verification
The standalone `verify_seif.py` tests the exact weighted drift identity symbolically, the Perron vectors exactly, and long-time trajectories against the explicit coefficients for three parameter sets and two initial states in each set. Run `python verify_seif.py` after installing dependencies listed in `requirements.txt`. Finite-horizon numerical agreement is evidence about implementations only; the proof of the universal infinite-time limits is the argument above.

## Relationship to prior work
González, Laguna and Abramson [1] introduce these exact four ODEs and their critical reproduction boundary \(\mathcal R_S=1\) (Eqs. (4)–(7), (8), and (10)); they describe extinction for \(\mathcal R_S\le1\) and numerical phase regimes, but do not give this all-seeded asymptotic profile or its coefficients. Yagci Sokat and coauthors [2] compare indirect and direct infection in a different veterinary disease model, including environmental transmission, but use different demographic equations. General multistage epidemic theory [3] can imply extinction at a critical reproduction threshold under its hypotheses, not the specific slow-mode amplitudes claimed here. The formulas are not asserted to be a new universal rate for *all* epidemic models: their value is the explicit, model-specific coefficient and all-stage amplitude, including dependence on fomite clearance and host reproduction.

## Limitations
This is a deterministic, spatially homogeneous, continuous-density statement exactly on a codimension-one threshold. It does not quantify finite-population extinction times, discrete stochastic outbreaks, delays, seasonal forcing, supercritical dynamics, or the infection-free initial manifold. Positive environmental transmission and initially positive susceptibles are essential to the stated all-seeded theorem. Literature comparisons cannot exclude an unindexed equivalent center-manifold calculation; the general critical inverse-time motif by itself is not claimed as novel.

## References
[1] T. I. González, M. F. Laguna and G. Abramson, *A mean field analysis of the role of indirect transmission in emergent infection events*, arXiv:2407.09587v1 (public July 12, 2024), https://arxiv.org/pdf/2407.09587.

[2] K. Yagci Sokat, S. Edlund, K. Clarkson and J. Kaufman, *Comparing Direct and Indirect Transmission in a Simple Model of Veterinary Disease*, Mathematics 7 (2019), 1039, https://doi.org/10.3390/math7111039.

[3] *Global Dynamics of a General Class of Multistage Models for Infectious Diseases*, SIAM Journal on Applied Mathematics (2012). General threshold context; not used as a substitute for the computation here.
