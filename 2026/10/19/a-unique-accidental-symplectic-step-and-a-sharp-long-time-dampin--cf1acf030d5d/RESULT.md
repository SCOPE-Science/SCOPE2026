# A unique accidental symplectic step and a sharp long-time damping law for Gaussian RBF-RK2 oscillators

## Finding

For the third-order two-stage Gaussian radial-basis-function Runge–Kutta method of Gu, Chen and Jung, there is **exactly one positive frequency-scaled step** at which a harmonic oscillator's numerical one-step map preserves its quadratic energy and is symplectic. Every smaller positive step strictly damps the energy, and every larger step strictly amplifies it. Energy damping attains a unique maximum in the interior of the stable interval. No single positive step can make this method symplectic for two harmonic oscillators of unequal frequencies. On a small fixed step, the artificial energy decay accumulates on the sharp physical-time scale \(h^{-3}\).

More precisely, define, for \(s\ge 0\),
\[
H(s)=4s-15+6e^{-2s/9}+9e^{-4s/9},\qquad Q(s)=1+\frac{sH(s)}{16}.
\]
There is a unique positive zero \(s_*\) of \(H\), with
\[
1.577421180854<s_*<1.577421180856,\qquad \sqrt{s_*}=1.25595429090982\ldots.
\]
Also, \(Q\) has exactly one minimizer \(s_{\mathrm d}>0\), characterized by \(H(s_{\mathrm d})+s_{\mathrm d}H'(s_{\mathrm d})=0\), with
\[
1.026544029217<s_{\mathrm d}<1.026544029219,\quad
Q(s_{\mathrm d})=0.97339259930514\ldots.
\]
The claims below hold for all oscillator frequencies and all initial states, not merely for sampled data.

## Assumptions and scope

Let \(m\ge1\), let \(\omega_j>0\) for \(j=1,\ldots,m\), and consider the real canonical oscillator system
\[
\dot z_j=\omega_jJz_j,\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad z_j\in\mathbb R^2.
\]
For fixed \(h>0\), apply the two-stage Gaussian RBF-RK2 formula, separately and simultaneously to all modal components:
\[
\begin{aligned}
k_{1,j}&=\omega_jJz_j,\\
k_{2,j}&=\omega_jJ\left(e^{-\epsilon_j^2(2h/3)^2}z_j+\frac{2h}{3}k_{1,j}\right),\\
z_j^+&=z_j+h\left(\frac14 k_{1,j}+\frac34 k_{2,j}\right),
\end{aligned}
\]
where \(\epsilon_j^2=\omega_j^2/2\). This is the constant value prescribed by the source's local-error-cancelling rule \(\epsilon^2=-u''/(2u)\) whenever an oscillator component is nonzero; here it is defined by continuous extension at its zeros. The modal shape parameter is supplied exactly; no numerical derivative estimation is assumed. The same \(h\) is used for all modes. Physical modal energy is \(\mathcal E_j(z_j)=\omega_j\|z_j\|_2^2/2\), with the zero initial mode remaining zero.

The symplecticity assertion refers **only** to these fixed linear harmonic systems, not to arbitrary Hamiltonian systems or a generally symplectic nonlinear integrator. All statements concern exact arithmetic.

## Proof

**Exact one-step map.** Since \(J^2=-I\), with \(x_j=h\omega_j\) the stage equations give
\[
M_j(x_j)=\left(1-\frac{x_j^2}{2}\right)I+
\frac{x_j}{4}\left(1+3e^{-2x_j^2/9}\right)J.
\]
For every \(z_j\), direct multiplication yields
\[
M_j^{\mathsf T}M_j=\det(M_j)I=Q(x_j^2)I,
\qquad
\mathcal E_j(z_j^{(n)})=Q(x_j^2)^n\mathcal E_j(z_j^{(0)}).
\]
The identity follows from the squares of the two scalar coefficients; expanding them yields the stated \(H\). Since the coefficient of \(J\) is strictly positive for \(x_j>0\), \(Q(s)>0\) for every \(s\ge0\).

**Exactly one positive energy-preserving step.** We have
\[
H(0)=0,\quad H'(0)=-\frac43,\quad
H''(s)=\frac8{27}e^{-2s/9}+\frac{16}{9}e^{-4s/9}>0,
\quad \lim_{s\to\infty}H(s)=+\infty.
\]
Thus \(H'\) increases strictly from a negative value to \(4\); \(H\) first decreases, then increases without bound, and has exactly one zero \(s_*>0\). Hence \(0<Q(s)<1\) for \(0<s<s_*\), \(Q(s_*)=1\), and \(Q(s)>1\) for \(s>s_*\). In two canonical dimensions \(M_j^{\mathsf T}JM_j=(\det M_j)J\). Therefore for a given \(\omega_j\), \(h=\sqrt{s_*}/\omega_j\) is the unique positive energy-preserving and symplectic step. At that step \(M_j\) is a proper rotation, not necessarily the exact-time flow. In fact its rotation angle \(\theta_*\) is strictly greater than \(\sqrt{s_*}\): since \(s_*<2\), both angles lie in \((0,\pi/2)\), and
\[\cos\theta_*=1-s_*/2<\cos(\sqrt{s_*}).\]
The strict inequality is the elementary cosine bound \(\cos x>1-x^2/2\) for \(x>0\) in this range. Numerically \(\theta_*=1.35790236243961\ldots\), so exact energy preservation here does **not** imply phase fitting.

For a block-diagonal system, the numerical map is symplectic precisely if every modal determinant is one. If two frequencies differ, their unique requirements \(h\omega_j=\sqrt{s_*}\) cannot both hold at a common positive step. This proves the multifrequency obstruction, regardless of initial amplitudes.

**Unique maximum one-step damping.** Write \(Q'(s)=K(s)/16\) with \(K(s)=H(s)+sH'(s)\). Let \(s_m>0\) be the unique minimum point of \(H\) (the zero of \(H'\)). For \(0<s\le s_m\), both \(H(s)\) and \(sH'(s)\) are negative. On \(s\ge s_m\),
\[
K'(s)=2H'(s)+sH''(s)>0\quad(s>s_m),
\]
and \(K(s_m)=H(s_m)<0\), while \(K(s)\to\infty\). Therefore \(K\) has exactly one positive zero \(s_{\mathrm d}\), and this is the unique global minimizer of \(Q\). Because \(K(s_*)=s_*H'(s_*)>0\), \(0<s_{\mathrm d}<s_*\). Exact-rational alternating Taylor bounds for the exponentials certify the numerical enclosures above; see the standalone verifier.

**Long-time damping law.** Taylor expansion gives
\[
Q(s)=1-\frac{s^2}{12}+\frac{7s^3}{108}+O(s^4),\qquad
\log Q(s)=-\frac{s^2}{12}+O(s^3)
\quad(s\downarrow0).
\]
For a fixed \(\omega>0\), let \(n_h=\lfloor\tau h^{-4}\rfloor\) with fixed \(\tau\ge0\). As \(h\downarrow0\), the physical elapsed time is \(n_hh\sim\tau h^{-3}\) for \(\tau>0\), and the exact modal-energy ratio satisfies
\[
\frac{\mathcal E(z^{(n_h)})}{\mathcal E(z^{(0)})}
=Q(\omega^2h^2)^{n_h}\longrightarrow
\exp(-\tau\omega^4/12)
\]
for nonzero initial energy. For comparison, the classical two-stage second-order Runge–Kutta stability polynomial on a harmonic mode has energy factor \(1+x^4/4\), hence leads on the same time scale to \(\exp(+\tau\omega^4/4)\). This comparison uses only the textbook stability polynomial, not a claimed new method.

## Verification

Run `python3 verify.py` using only the Python standard library. It reconstructs the RBF stages independently of the closed map, verifies modal energy factors for 750 seeded test triples, rigorously brackets both positive roots with exact rational alternating-series enclosures, and checks the long-time asymptotic numerically without iterating billions of steps. The analytic convexity arguments—not numerical sampling—establish existence, uniqueness, global signs and the infinite-frequency scope. The executed verifier reported 1,537 passing assertions.

## Relationship to prior work

Gu, Chen and Jung (2024, preprint; 2025 online journal publication) define the two-stage RBF-RK2 construction and explicitly provide its scalar stability function \(R(z)=1+(1+3e^{2z^2/9})z/4+z^2/2\). Their stability-region figure and Duffing experiment illustrate qualitative stability and bounded-but-nonconserved energy. Those expressions and qualitative observations are not claimed as new. The present contribution is the proof of a *unique nonzero harmonic symplectic step*, the *unique strongest energy-damping step*, the *impossibility of a common symplectic step for distinct frequencies*, and the exact \(h^{-3}\) energy-decay limit. This is an analytical refinement of the already-known RBF stability function, not an independently developed integrator.

Earlier exponentially fitted Runge–Kutta literature studies oscillatory phase fitting and constructs genuinely symplectic fitted methods. Those are different constructions and do not establish the present Gaussian RBF-RK2 phase diagram. The published Gaussian RBF paper itself notes possible future work on generally symplectic RBF-RK2; the isolated harmonic-step coincidence obtained here does not accomplish that general objective.

## Limitations

The result assumes exactly known positive frequencies, decoupled canonical harmonic blocks, fixed steps, exact modal shape values, and exact arithmetic. It does not give symplecticity for general Hamiltonian systems, conservation for nonlinear oscillators, phase accuracy at the exceptional step, or invariant preservation with inaccurately estimated shape parameters. For equal-frequency blocks a common special step exists; for distinct-frequency blocks it does not. When a modal initial energy is zero, energy-ratio statements for that mode are vacuous. Absolute bibliographic priority has not undergone independent assessment; the source's plotted stability boundary already gives a qualitative precursor.

## References

- J. Gu, X. Chen, and J.-H. Jung, “Explicit radial basis function Runge-Kutta methods,” arXiv:2403.08253v1, first public posting 2024-03-13, especially §§3.1, 5, 6. https://arxiv.org/abs/2403.08253
- J. Gu, X. Chen, and J.-H. Jung, “Explicit radial basis function Runge–Kutta methods,” *Numerical Algorithms*, published online 2025-06-23, doi:10.1007/s11075-025-02121-w, especially §§3.1, 5 and Example 5. https://link.springer.com/article/10.1007/s11075-025-02121-w
- “Structure preservation of exponentially fitted Runge–Kutta methods,” *Journal of Computational and Applied Mathematics* 218 (2008), 421–434, doi:10.1016/j.cam.2007.05.016 (related, distinct fitted methods). https://doi.org/10.1016/j.cam.2007.05.016
