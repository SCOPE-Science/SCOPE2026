# Universal nonlinear period softening at nondegenerate FitzHugh–Nagumo Hopf points

## Finding
For the planar FitzHugh–Nagumo oscillator
\[
\dot u=u-u^3/3-v+I,\qquad \dot v=\varepsilon(u+\alpha-\beta v),
\]
fix \(\varepsilon,\beta>0\) and \(\alpha\in\mathbb R\). Put \(c=\varepsilon\beta\), and assume \(0<c<1\) and \(\omega^2=\varepsilon-c^2>0\). Choose either Hopf equilibrium voltage \(s=\sqrt{1-c}\) or \(s=-\sqrt{1-c}\). Define the current unfolding by
\[
U(\mu)=\operatorname{sgn}(s)\sqrt{1-c-\mu},\qquad
I(\mu)=U(\mu)^3/3-U(\mu)+(U(\mu)+\alpha)/\beta.
\]
Write
\[
m=\frac{\omega^2-2c(1-c)}{4\omega^2},\qquad
K=\frac{(1-c)(c^2+\omega^2)}{6\omega^4}.
\]
If \(m\ne0\), a unique small nonconstant periodic orbit (up to time translation) bifurcates near this equilibrium, for \(\mu/m>0\) sufficiently small. Using its *positive first voltage Fourier-harmonic amplitude* \(r\) as the orbit parameter,
\[
\mu=m r^2+O(r^3),\qquad
T(r)=\frac{2\pi}{\omega}\bigl(1+K r^2+O(r^3)\bigr).
\]
**The coefficient \(K\) is strictly positive for every admissible pair \((c,\omega)\)**, independent of which Hopf voltage was chosen and independent of the sign of \(m\). The orbit is locally asymptotically stable if \(m>0\) and unstable if \(m<0\).

In particular, for \(m<0\), the orbit occurs at \(\mu<0\): its period satisfies \(T(r)>2\pi/\omega\), whereas the oscillation period inferred from the *contemporaneous linearized equilibrium* is strictly *smaller* than \(2\pi/\omega\). Thus nonlinear period softening reverses the linear-frequency prediction along the subcritical branch.

## Assumptions and scope
Time is the original nondimensional FHN time; no time change or singular limit is taken. The equilibrium is \((U(\mu),(U(\mu)+\alpha)/\beta)\), and \(\mu\) is exactly its Jacobian trace. Its determinant is \(\omega^2-c\mu\). The chosen branch of \(U\) is real and smooth for sufficiently small \(|\mu|\). The current is a genuine local parameter because
\[
\left.\frac{dI}{d\mu}\right|_{\mu=0}=-\frac{\omega^2}{2cs}\ne0.
\]
Let \(x(t)=u(t)-U(\mu)\) and \(\tau=2\pi t/T\). The harmonic amplitude \(r>0\) is specified by the phase choice
\[
\frac1\pi\int_0^{2\pi}x(\tau)\cos\tau\,d\tau=r,\qquad
\int_0^{2\pi}x(\tau)\sin\tau\,d\tau=0.
\]
The conclusions are local to each of the two nondegenerate Hopf points; they do not concern global cycles, canard explosions, or the generalized-Hopf boundary \(m=0\).

## Proof
Translate the recovery coordinate by \(q=v-(U(\mu)+\alpha)/\beta\). The exact translated equations are
\[
\dot x=(c+\mu)x-q-U(\mu)x^2-x^3/3,\qquad
\dot q=\varepsilon x-cq.
\]
Eliminating \(q\), without approximation, gives
\[
\ddot x+\omega^2 x=\mu\dot x+c\mu x-2U(\mu)x\dot x-x^2\dot x-cU(\mu)x^2-(c/3)x^3.
\]
Conversely \(q=(c+\mu)x-U(\mu)x^2-x^3/3-\dot x\) reconstructs any solution, so elimination creates no extraneous periodic orbits.

Seek a small periodic branch in Poincaré–Lindstedt form
\[
x=r\cos\tau+r^2X_2(\tau)+r^3X_3(\tau)+O(r^4),\quad
\mu=mr^2+O(r^3),\quad
\Omega=\frac{2\pi}{T}=\omega+\nu r^2+O(r^3),\quad \tau=\Omega t.
\]
The phase and amplitude conditions remove first harmonics from \(X_2,X_3\). At second order the exact inhomogeneous harmonic solution is
\[
X_2(\tau)=-\frac{cs}{2\omega^2}+\frac{cs}{6\omega^2}\cos(2\tau)-\frac{s}{3\omega}\sin(2\tau).
\]
At third order, the coefficient of \(\sin\tau\) in the right-hand forcing is
\[
\frac{\omega^2-2cs^2-4m\omega^2}{4\omega},
\]
and that of \(\cos\tau\) is
\[
\frac{10c^2s^2+12cm\omega^2-3c\omega^2+4s^2\omega^2}{12\omega^2}.
\]
Removal of the resonant sine term fixes \(m=(\omega^2-2cs^2)/(4\omega^2)\). Including the left-hand frequency correction, cosine solvability sets the displayed cosine coefficient plus \(2\omega\nu\) to zero. Substitution gives
\[
\nu=-\frac{s^2(c^2+\omega^2)}{6\omega^3}<0.
\]
The analytic, nondegenerate Hopf theorem (with trace crossing speed \(1\)) and the nonzero cubic radial coefficient \(m\) justify the unique local periodic branch and these asymptotic expansions. The bifurcating orbit lies on the \(\mu/m>0\) side. For \(m>0\) it surrounds an unstable equilibrium and is attracting; for \(m<0\) it surrounds a stable equilibrium and is repelling.

Since \(T=2\pi/\Omega\) and \(s^2=1-c\), its quadratic coefficient is exactly \(K=-\nu/\omega>0\). For the final contrast, the eigenvalues at the nearby equilibrium have imaginary part
\[
\Omega_{\mathrm{lin}}(\mu)=\sqrt{\omega^2-c\mu-\mu^2/4}.
\]
If \(m<0\), then \(\mu<0\) along the bifurcating cycle; for sufficiently small \(|\mu|\), \(\Omega_{\mathrm{lin}}(\mu)>\omega\), and therefore \(2\pi/\Omega_{\mathrm{lin}}(\mu)<2\pi/\omega<T(r)\).

## Verification
The standalone `verify.py` checks the exact second-order Fourier equation and both third-order resonance projections symbolically with SymPy, deriving the displayed \(m\) and \(\nu\) without numerical fitting. Numerical shooting of the original translated two-dimensional polynomial ODE confirms five closed orbits on both sides of the criticality boundary. All five show positive measured period corrections and agreement with \(K\) as the amplitude tends to zero. `verification_output.txt` records the numerical results. The proof of the full parameter-wide sign is symbolic; the finite numerical checks are corroboration only.

## Relationship to prior work
FitzHugh's original model established a two-variable excitability/oscillation paradigm [1]. Kostova, Ravindran and Schonbek [2] derived Lyapunov stability and Hopf criticality criteria, including both supercritical and subcritical cycles; their Appendix B computes a *real* focal coefficient, not the present amplitude-dependent physical-time period coefficient. Rocşoreanu, Giurgiţeanu and Georgescu [3] analyze degenerate Hopf/Bautin behavior; their full text could not be inspected for a direct comparison. Guckenheimer and Kuehn [4] treat singular-limit and homoclinic bifurcation geometry. Brizard [5] obtains a large-amplitude, singular-perturbation relaxation period, distinct from a small-amplitude Hopf coefficient. Bisquert and collaborators [6] discuss the FHN linear Hopf frequency and frequencies of S-type physical oscillators; the FHN harmonic approximation does not determine the present nonlinear coefficient. None of the materially inspected results entails the strictly positive physical-time \(K\) simultaneously in supercritical and subcritical FHN regimes.

## Limitations
The generalized Hopf case \(m=0\) is excluded; the result is not a classification of larger periodic orbits and is not a claim of global period monotonicity. The normalization of \(r\) and the nondimensional physical time are essential for the *numerical coefficient*, though the sign is robust under positive amplitude rescaling. Historical publication priority is not conclusively resolved because certain relevant early full texts were inaccessible. The finding has undergone self-review; an independent audit has not been performed.

## References
[1] R. FitzHugh, *Impulses and Physiological States in Theoretical Models of Nerve Membrane*, Biophysical Journal **1** (1961), 445–466, doi:10.1016/S0006-3495(61)86902-6.

[2] T. Kostova, R. Ravindran, M. E. Schonbek, *FitzHugh–Nagumo Revisited: Types of Bifurcations, Periodical Forcing and Stability Regions by a Lyapunov Functional*, Int. J. Bifurcation Chaos **14** (2004), 913–925, doi:10.1142/S0218127404009685; publicly released preprint dated 2003-02-06, https://www.its.caltech.edu/~matilde/FHNLyapunov.pdf.

[3] C. Rocşoreanu, N. Giurgiţeanu, A. Georgescu, *Degenerated Hopf Bifurcation in the FitzHugh–Nagumo System. 2. Bautin Bifurcation*, Rev. Anal. Numér. Théor. Approx. **29** (2000), 97–109, doi:10.33993/jnaat291-659.

[4] J. Guckenheimer and C. Kuehn, *Homoclinic Orbits of the FitzHugh–Nagumo Equation: The Singular-Limit*, Discrete Contin. Dyn. Syst. Ser. S **2** (2009), 851–872, doi:10.3934/dcdss.2009.2.851.

[5] A. J. Brizard, *Asymptotic Limit-cycle Analysis of the FitzHugh–Nagumo Equations*, arXiv:2107.11642 (2021).

[6] J. Bisquert, R. Fenollosa, A. Cordero, J. R. Torregrosa, *Bifurcation and Frequency Properties of S-Type Neuronic Oscillators*, J. Phys. Chem. Lett. **16** (2025), 3616–3631, doi:10.1021/acs.jpclett.5c00288.
