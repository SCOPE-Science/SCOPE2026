# Exactly one free-energy crossing for a coherently prepared thermal Davies qubit

## Finding

For the finite-temperature two-level Davies thermalization model defined below, take any initial qubit with nonzero energy-basis coherence. Compare it with the unitarily equivalent state obtained by energy-basis diagonalization and complete population inversion. **Their nonequilibrium free energies cross at exactly one finite positive time.** The inverted state's free energy is strictly larger before that time and strictly smaller afterward. More strongly, the difference of their Gibbs relative entropies, divided by the longitudinal decay factor, is strictly decreasing in physical time.

This statement is global in initial purity (including pure states), orientation, bath temperature and positive thermal jump rates, subject to detailed balance and the absence of additional pure dephasing. It is not a claim about arbitrary Lindbladians or arbitrary pairs of initial qubits.

Put \(p=e^{-\Gamma t}\). If the initial Bloch vector is \((x,y,z)\), define \(R=\sqrt{x^2+y^2+z^2}\), \(c=x^2+y^2\), and \(b=\tanh(\beta\omega/2)\). Let
\[
A(p)=\sqrt{[-b+(b+z)p]^2+cp},\qquad
B(p)=|-b+(b+R)p|,
\]
and let \(S(u)=-\frac{1+u}{2}\log\frac{1+u}{2}-\frac{1-u}{2}\log\frac{1-u}{2}\), for \(0\le u\le1\), with the usual continuous endpoint convention. Writing \(\rho(t)\) for the original evolution, \(\rho_+(t)\) for the population-inverted comparison, and \(\tau_\beta\) for the Gibbs state, define
\[
\Delta(p)=D(\rho_+(t)\Vert\tau_\beta)-D(\rho(t)\Vert\tau_\beta).
\]
Then the exact all-time identity is
\[
\boxed{\Delta(p)=(R-z)\operatorname{artanh}(b)p-[S(B(p))-S(A(p))].}
\]
For \(R>z\), \(\Delta(p)/p\) is strictly increasing in \(p\in(0,1)\), hence strictly decreasing in \(t\). Its limits are
\[
\lim_{p\uparrow1}\frac{\Delta(p)}p=(R-z)\operatorname{artanh}b,
\qquad
\lim_{p\downarrow0}\frac{\Delta(p)}p
=-\frac{R^2-z^2}{2b}\operatorname{artanh}b.
\]
Consequently \(c>0\) is **necessary and sufficient** for exactly one crossing \(t_*>0\). If \(c=0\) and \(z=-R<0\), the difference stays positive at every finite time; if \(z=R\), the initial states coincide and the difference is identically zero. In the coherent case,
\[
\boxed{\Delta(e^{-\Gamma t})
=-\frac{c\operatorname{artanh}b}{2b}e^{-\Gamma t}+o(e^{-\Gamma t}).}
\]

## Assumptions and scope

Fix \(\omega>0\), \(\beta>0\), and \(\gamma_+,\gamma_->0\), with \(\gamma_+/\gamma_-=e^{-\beta\omega}\). On \(\mathbb C^2\), define \(H=\omega\sigma_z/2\) and the generator
\[
\mathcal L(\rho)=-i[H,\rho]
+\gamma_-\big(\sigma_-\rho\sigma_+-\tfrac12\{\sigma_+\sigma_-,\rho\}\big)
+\gamma_+\big(\sigma_+\rho\sigma_--\tfrac12\{\sigma_-\sigma_+,\rho\}\big).
\]
Here \(\sigma_-\) lowers the \(\sigma_z\) eigenvalue, \(\Gamma=\gamma_-+\gamma_+>0\), and \(\tau_\beta=(I-b\sigma_z)/2\), where \(b=(\gamma_--\gamma_+)/\Gamma\in(0,1)\). The initial qubit \(\rho_0=(I+x\sigma_x+y\sigma_y+z\sigma_z)/2\) obeys \(x^2+y^2+z^2\le1\); the comparison \(\rho_{+,0}=(I+R\sigma_z)/2\) has the identical eigenvalues and therefore is unitarily conjugate to \(\rho_0\). The relative entropy is \(D(\rho\Vert\tau)=\operatorname{tr}\rho(\log\rho-\log\tau)\), with natural logarithms. The nonequilibrium free energy differs from \(\beta^{-1}D(\rho\Vert\tau_\beta)\) by the same equilibrium constant for both preparations. No additional dephasing jump is present.

## Proof

**1. Exact Bloch evolution.** Direct substitution into the master equation yields
\[
z_t=-b+(z+b)e^{-\Gamma t},\quad
x_t+iy_t=(x+iy)e^{-(\Gamma/2+i\omega)t}.
\]
The comparison has \(z_{+,t}=-b+(R+b)e^{-\Gamma t}\) and no transverse component. Thus their Bloch radii are \(A(p)\) and \(B(p)\). Since \(\log\tau_\beta=\alpha I-\operatorname{artanh}(b)\sigma_z\), the relative-entropy difference gives the displayed exact expression for \(\Delta(p)\).

**2. A positive radius gap.** Elementary algebra, using \(c=R^2-z^2\), gives
\[
\boxed{A(p)^2-B(p)^2=(R-z)(R+z+2b)p(1-p).}
\]
The coefficient is nonnegative because \(-R\le z\le R\) and \(b>0\). Both squared radii lie in \([0,1]\) for \(0\le p\le1\) by complete positivity and trace preservation.

**3. A strictly monotone normalized difference.** Define
\[
h(q)=\frac{\operatorname{artanh}\sqrt q}{2\sqrt q}
=\frac12\int_0^1\frac{ds}{1-qs^2},\qquad 0\le q<1,
\]
with \(h(0)=1/2\). The identity \(\frac{d}{dq}S(\sqrt q)=-h(q)\), integration over the squared-radius interval, and step 2 imply that, whenever \(R>z\),
\[
\frac{\Delta(p)}{(R-z)p}=\operatorname{artanh}b
-(R+z+2b)\int_0^1\!\int_0^1
\frac{1-p}{2[1-s^2Q_\theta(p)]}\,ds\,d\theta,
\]
where \(Q_\theta(p)=(1-\theta)B(p)^2+\theta A(p)^2\).

Each \(Q_\theta\) is a quadratic in \(p\), with nonnegative quadratic coefficient
\[
a_\theta=(1-\theta)(R+b)^2+\theta(z+b)^2\ge0.
\]
Its endpoint is \(Q_\theta(1)=R^2\le1\), so the **exact quadratic identity** is
\[
Q_\theta(p)+(1-p)Q_\theta'(p)
=R^2-a_\theta(1-p)^2\le1.
\]
For \(0<p<1\), \(0\le s<1\), and any \(\theta\in[0,1]\), direct differentiation gives
\[
\frac{d}{dp}\frac{1-p}{1-s^2Q_\theta(p)}
=-\frac{1-s^2[Q_\theta(p)+(1-p)Q_\theta'(p)]}
{[1-s^2Q_\theta(p)]^2}<0.
\]
This proves the integral decreases strictly with \(p\), hence \(\Delta(p)/[(R-z)p]\) increases strictly with \(p\). Integrability holds throughout \(0<p<1\), even for pure initial states, because the evolved state is full-rank at positive time. The limiting case \(s=1\) is immaterial for integration.

**4. Endpoint values and classification.** At \(p=1\) the two preparations have identical entropy, so \(\Delta(1)=(R-z)\operatorname{artanh}b\). At \(p=0\), \(A(0)=B(0)=b\); therefore the normalized integral tends to \(\operatorname{artanh}(b)/(2b)\), giving
\[
\lim_{p\downarrow0}\frac{\Delta(p)}{(R-z)p}
=-\frac{R+z}{2b}\operatorname{artanh}b.
\]
If \(c=R^2-z^2>0\), then \(-R<z<R\), so the two normalized endpoint signs are strictly opposite. Strict monotonicity and continuity yield exactly one root \(p_*\in(0,1)\), with \(t_*=-\Gamma^{-1}\log p_*\). The sign is positive for \(0\le t<t_*\) and negative for \(t>t_*\). The negative small-\(p\) limit gives the stated sharp long-time expansion. When \(c=0\), the only possibilities are \(z=R\), giving equal states, or \(z=-R<0\); in the second case the normalized limit at zero is zero and strict monotonicity keeps it positive at every \(p>0\). The maximally mixed case \(R=0\) also gives identical states.

## Verification

The accompanying `check.py` checks exact polynomial identities symbolically, then computes quantum relative entropy by evolving actual two-by-two density matrices under a separately assembled Lindblad superoperator. It tests many mixed and pure Bloch vectors, signs of the normalized difference and both noncoherent boundaries. The reproducible example \(b=1/2\), \(R=4/5\), \(z=0\), \(\Gamma=1\) has
\[
p_*=0.429931729726472137323127158320\ldots,\qquad
t_*=0.844128850977486206855403711207\ldots.
\]
The checker reports 505 successful assertions. These finite computations are diagnostics; the monotonicity identity in step 3 is the proof for all allowed parameters. The root is implicitly specified and no elementary closed form is claimed.

## Relationship to prior work

Moroder, Culhane, Zawadzki and Goold, *Thermodynamics of the quantum Mpemba effect* (arXiv:2403.16959, first public 2024-03-25), develop Davies-map mode suppression, construct a unitary population-inverted comparison (their Appendix A), and exhibit a free-energy crossing for a single-qubit example (their Fig. 2). Their analysis supplies the physical construction; it does not state the all-state **exactly-one-crossing theorem**, the strictly monotone decay-normalized relative-entropy difference, or its exact leading asymptotic coefficient. Summer et al., *A resource theoretical unification of Mpemba effects: classical and quantum* (arXiv:2507.16976, 2025), also use thermal qubit Davies dynamics and illustrate metric-dependent crossover times without an all-state uniqueness classification. Chatterjee, Takada and Hayakawa, *Multiple quantum Mpemba effect: exceptional points and oscillations* (arXiv:2311.01347, 2023), report single relative-entropy crossings in illustrated driven two-level dissipative settings, but the models allow drives and variable dissipation and their observed single crossing is not the present all-initial-state thermal Davies sign theorem. The main ingredients (qubit entropy, detailed-balance Bloch evolution, a resolvent integral) are standard; their combined strict global crossing proof is the new claim subject to independent literature assessment.

## Limitations

The scope excludes zero-temperature/nonfaithful Gibbs limits, extra pure dephasing (which changes the relation between population and coherence rates), non-Davies dissipators, driven Hamiltonians, many-qubit systems and arbitrary initial-state pairs. The theorem gives an implicit crossing equation and exact uniqueness, not an explicit elementary crossing-time expression or a uniform bound on \(t_*\) for all initial states. Literature comparisons are evidence of a distinct statement, not proof of publication priority or independent certification.

## References

1. M. Moroder, O. Culhane, K. Zawadzki and J. Goold, *Thermodynamics of the quantum Mpemba effect*, arXiv:2403.16959, first public 2024-03-25, https://arxiv.org/abs/2403.16959 ; main text and Appendices A–C in https://arxiv.org/html/2403.16959v3 .
2. A. K. Chatterjee, S. Takada and H. Hayakawa, *Multiple quantum Mpemba effect: exceptional points and oscillations*, arXiv:2311.01347, first public 2023-11-02, https://arxiv.org/abs/2311.01347 .
3. A. Summer, M. Moroder, L. P. Bettmann, X. Turkeshi, I. Marvian and J. Goold, *A resource theoretical unification of Mpemba effects: classical and quantum*, arXiv:2507.16976, first public 2025-07-22, https://arxiv.org/abs/2507.16976 .
