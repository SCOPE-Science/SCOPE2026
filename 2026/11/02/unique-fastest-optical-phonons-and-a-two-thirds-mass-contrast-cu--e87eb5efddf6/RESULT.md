# Unique fastest optical phonons and a two-thirds mass-contrast cusp in a diatomic harmonic lattice

## Finding
For every nonzero mass contrast in a two-species, one-dimensional *harmonic* chain, the optical phonon group-speed magnitude has precisely one maximizing Bloch wavenumber. This optimizer is governed by an explicitly solvable cubic and undergoes a non-analytic, two-thirds-power approach to the folded Brillouin-zone edge as the masses become equal.

Let \(c=|m_1-m_2|/(m_1+m_2)\), \(0<c<1\). Let \(u_c\in(c,1)\) be the unique solution of
\[
u_c^3+c^2u_c=2c^2.
\]
The maximizing dimensionless wavenumber and peak magnitude of the optical group velocity are exactly
\[
q_c=2\arcsin\sqrt{\frac{1-u_c^2}{1-c^2}},\qquad
V_c=\frac{a\Omega}{4}\sqrt{(1-u_c)\left(1-\frac{c^2}{u_c^2}\right)}.
\]
Here \(a\) is the two-particle cell length and \(\Omega=\sqrt{K(m_1^{-1}+m_2^{-1})}\). With the long-wavelength acoustic sound speed \(v_s=a\Omega\sqrt{1-c^2}/(2\sqrt2)\), the global, sharp contrast-independent bound is
\[
0<\frac{V_c}{v_s}<\frac1{\sqrt2},\qquad
\lim_{c\downarrow0}\frac{V_c}{v_s}=\frac1{\sqrt2}.
\]
Furthermore,
\[
u_c=2^{1/3}c^{2/3}+O(c^{4/3}),\quad
\pi-q_c=2^{4/3}c^{2/3}+O(c^{4/3}),\quad
\frac{4V_c}{a\Omega}=1-\frac3{2^{5/3}}c^{2/3}+O(c^{4/3}).
\]
All asymptotics are for the positive contrast \(c\downarrow0\); the equal-mass crossing itself does not have a smoothly separated optical branch at the Brillouin edge.

## Assumptions and scope
The lattice is indexed by \(n\in\mathbb Z\), with repeated cell \(n\) containing positive masses \(m_1,m_2\), no onsite pinning, and every nearest-neighbor bond having the same spring constant \(K>0\). Its period is \(a>0\). Each displacement is small so all dynamics are linear. The two components are separated by the usual Bloch ansatz, and the reduced first-zone wavenumber is \(q=ka\in[0,\pi]\). Masses differ strictly, hence \(c\in(0,1)\). Define acoustic and optical branches by smaller/larger eigenfrequencies at each wavenumber. We maximize the **magnitude** of the optical group velocity, not its signed derivative, wave-packet energy flux, thermal conductivity, or nonlinear propagation rate.

## Proof
The mass-weighted Bloch dynamical matrix is Hermitian:
\[
D(q)=K\begin{pmatrix}
2/m_1&-(1+e^{-iq})/\sqrt{m_1m_2}\\
-(1+e^{iq})/\sqrt{m_1m_2}&2/m_2
\end{pmatrix}.
\]
Its two eigenvalues give, on writing \(u(q)=\sqrt{1-(1-c^2)\sin^2(q/2)}\),
\[
\omega_\pm(q)=\Omega\sqrt{1\pm u(q)}.
\]
Here \(u(q)\) decreases strictly from \(1\) to \(c\) as \(q\) increases from \(0\) to \(\pi\). Differentiation, with \(dq/dk=a\), gives
\[
|v_+(q)|=a\Omega\frac{(1-c^2)\sin q}{8u(q)\sqrt{1+u(q)}}.
\]
Elementary elimination of \(q\) yields the key dimensionless identity
\[
\left(\frac{4|v_+(q)|}{a\Omega}\right)^2
=(1-u)\left(1-\frac{c^2}{u^2}\right)=:F_c(u),\qquad u\in[c,1].
\]
Both endpoint values vanish. Differentiating,
\[
F_c'(u)=\frac{2c^2-c^2u-u^3}{u^3}.
\]
The numerator is strictly decreasing on \((c,1)\), is positive at \(u=c\), because it equals \(2c^2(1-c)\), and is negative at \(u=1\), because it equals \(c^2-1\). Hence exactly one root \(u_c\in(c,1)\), strictly maximizing \(F_c\). Inverting the monotone expression \(u(q)\) establishes unique \(q_c\) and the exact formulas.

For the acoustic branch, expand \(u(q)=1-(1-c^2)q^2/8+O(q^4)\). Consequently \(\omega_-(q)=\Omega q\sqrt{1-c^2}/(2\sqrt2)+O(q^3)\) as \(q\downarrow0\), and the stated \(v_s\) follows. For every fixed interior \(q\), set \(s=1-c^2\); then
\[
\left(\frac{|v_+(q)|}{v_s}\right)^2
=\frac{s\sin^2q}{8u(q)^2(1+u(q))}.
\]
This expression is strictly increasing in \(s\in(0,1)\), since its numerator increases while \(u(q)=\sqrt{1-s\sin^2(q/2)}\) and the positive denominator decrease. At \(s=1\), with \(u=\cos(q/2)\), the ratio squared becomes \((1-\cos(q/2))/2<1/2\) for interior \(q\). Therefore the global maximum is strictly below \(1/\sqrt2\) for every \(c>0\). To prove sharpness, first fix an interior \(q\) arbitrarily near \(\pi\) and then let \(c\downarrow0\); this makes the ratio arbitrarily close to \(1/\sqrt2\).

Finally put \(u_c=c^{2/3}y_c\) and \(t=c^{2/3}\). Its cubic reduces to \(y_c^3+t y_c=2\). The implicit-function theorem around \((t,y)=(0,2^{1/3})\) gives \(y_c=2^{1/3}+O(t)\), so \(u_c=2^{1/3}c^{2/3}+O(c^{4/3})\). Because
\[
\pi-q_c=2\arcsin\sqrt{\frac{u_c^2-c^2}{1-c^2}},
\]
Taylor expansion yields the stated zone-edge shift. Substitution in \(F_c(u_c)\), then expansion of the positive square root, yields the stated normalized velocity deficit. In each case the omitted terms are \(O(c^{4/3})\). No finite calculation is invoked to establish any quantifier over all \(c\in(0,1)\).

## Verification
The companion `check.py` requires Python 3, NumPy, and SciPy. Run `python check.py`. For 101 positive contrast values it compares the cubic root with an independently optimized explicit dispersion, a finite-difference derivative of independently diagonalized Hermitian Bloch matrices, derivative-root uniqueness, and the acoustic-speed bound. Six small-contrast values check three leading asymptotic coefficients. The code completes 523 deterministic checks. Numerical sampling is a diagnostic only; the full-domain statement follows from the proof above.

## Relationship to prior work
The two-branch diatomic harmonic dispersion and wave-packet/group velocity are standard lattice-dynamics formulas; those are used rather than claimed. Dhar and Saito (2008), *Heat conduction in the disordered Fermi-Pasta-Ulam chain*, analyze disordered and ordered binary-mass chains and heat-current scaling; their original four-page preprint was inspected in full. Their transport objective is not the exact unique maximum optical group speed or its singular equal-mass scaling. Qin (2015), *Wave Propagation in Diatomic Lattices*, treats nonlinear periodic traveling waves by minimax methods; its journal abstract was accessible, but not the complete original text, so stronger historical coverage by that article has **not** been ruled out. Faver and Wright (2015) study nonlinear diatomic solitary waves. Their inspected main theorem and dispersion preliminaries concern phase speed and traveling-wave existence, not a group-speed maximum; the remainder of their manuscript was not inspected exhaustively. The new claim is the exact global *optimizer plus nonanalytic contrast-cusp and sharp normalized bound*, not the dispersion relation. No claim of exhaustive historical uniqueness is made.

## Limitations
This conclusion is for an ideal infinite, lossless, unpinned harmonic chain with equal spring strengths and strictly unequal alternating masses. It is not a claim about transport coefficients, scattering, nonlinear FPU kinetics, defects, disorder, or experimentally observable bounds in dissipative solids. The equal-mass case is a band-folding degeneracy: it is treated only by a one-sided limiting law and not by smooth continuation of separated bands through the zone edge. Historical-priority risk remains, especially because some plausible original mathematical literature could not be inspected completely. No independent audit has been conducted.

## References
1. A. Dhar and K. Saito, *Heat conduction in the disordered Fermi-Pasta-Ulam chain*, arXiv:0806.4067v1, publicly posted 2008-06-25, https://arxiv.org/abs/0806.4067.
2. W.-X. Qin, *Wave Propagation in Diatomic Lattices*, SIAM J. Math. Anal. **47** (2015), 477–497, https://doi.org/10.1137/130949609, published online 2015-01-22; full original text not inspected.
3. T. E. Faver and J. D. Wright, *Exact diatomic Fermi-Pasta-Ulam-Tsingou solitary waves with optical band ripples at infinity*, arXiv:1511.00942v1 (2015), https://arxiv.org/abs/1511.00942; main theorem and spectral preliminaries inspected; other sections not fully read.
