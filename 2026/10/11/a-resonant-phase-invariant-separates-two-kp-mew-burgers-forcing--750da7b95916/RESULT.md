# A resonant phase invariant separates two KP-MEW-Burgers forcing diagnostics

## Finding
For the autonomous forcing extension used by Liu–Feng–Chen–Huang, let \(W=w+ip\) and \(V=q+iz\). On the resonant slice \(\omega_2=2\omega_1\), the quantities \(I_1=|W|^2\), \(I_2=|V|^2\), and \(K=V\overline{W}^{2}\) are exact first integrals. On the unit-amplitude leaf \(I_1=I_2=1\), the printed nonautonomous forcing \(\varepsilon_1\cos(\omega_1\zeta)+\varepsilon_2\sin(2\omega_1\zeta)\), even after an arbitrary common translation of \(\zeta\), lies on the resonant leaf \(K=1\). The oscillator initial state \(w=z=4/5\), \(p=q=3/5\) used for the Lyapunov-exponent panel of Figure 11 instead has \(K=(117-44i)/125\). Hence no time translation identifies the autonomous trajectory family used for Figure 11(b) with the periodically forced equation used for Figure 11(a): the two panels use different relative forcing phases. This does not assert that either numerical panel is individually wrong; it shows that their pointwise comparison is not a comparison of the same periodically forced ODE unless invariance with respect to the relative phase is established separately.

## Assumptions and scope
The primary source considers the periodically forced traveling-wave equation
\[
\dot u=v,\qquad
\dot v=A u-Bu^{n+1}-Dv+\varepsilon_1\cos(\omega_1\zeta)+\varepsilon_2\sin(\omega_2\zeta),
\]
and its six-dimensional autonomous extension
\[
\dot w=-\omega_1p,\quad \dot p=\omega_1w,\qquad
\dot z=\omega_2q,\quad \dot q=-\omega_2z,
\]
with the same \(u,v\) equations after replacing the two forcing functions by \(w,z\). The finding concerns only the resonant case \(\omega_2=2\omega_1\) with \(\omega_1\ne0\), in particular the source's Figure 11 choice \(\omega_1=1.25\), \(\omega_2=2.5\). No claim is made about the incommensurate-frequency experiment in Figure 13.

The source's Figure 11(a) is a bifurcation diagram of the printed nonautonomous equation with initial state \( (u,v)=(1,-0.42)\). Figure 11(b) is a Lyapunov-exponent diagram of the autonomous extension with initial state \( (u,v,w,z,p,q)=(1,-0.42,0.8,0.8,0.6,0.6)\).

## Proof
Set
\[
W=w+ip,\qquad V=q+iz.
\]
The oscillator equations give
\[
\dot W=i\omega_1W,\qquad \dot V=i\omega_2V.
\]
Therefore \(I_1=W\overline W=w^2+p^2\) and \(I_2=V\overline V=z^2+q^2\) are first integrals. When \(\omega_2=2\omega_1\),
\[
K=V\overline W^2
\]
also satisfies
\[
\dot K=i\omega_2V\overline W^2-2i\omega_1V\overline W^2=0.
\]
In real coordinates,
\[
\operatorname{Re}K=q(w^2-p^2)+2zwp,
\]
\[
\operatorname{Im}K=z(w^2-p^2)-2qwp.
\]

The printed forcing corresponds to \(w=\cos(\omega_1\zeta)\), \(p=\sin(\omega_1\zeta)\), \(z=\sin(2\omega_1\zeta)\), and \(q=\cos(2\omega_1\zeta)\). Thus \(W=e^{i\omega_1\zeta}\), \(V=e^{2i\omega_1\zeta}\), and \(K=1\). Replacing \(\zeta\) by \(\zeta+\tau\) multiplies \(W\) by \(e^{i\omega_1\tau}\) and \(V\) by \(e^{2i\omega_1\tau}\), so \(K\) remains exactly \(1\). Hence \(K=1\) characterizes the relative phase of every common time translate of the printed resonant forcing on the unit-amplitude torus.

For the autonomous initial values used in Figure 11(b),
\[
W_0=\frac45+\frac35i,\qquad V_0=\frac35+\frac45i.
\]
Both have unit modulus, but
\[
K_0=V_0\overline W_0^2
=\frac{117-44i}{125}\ne1.
\]
Equivalently, the relative phase \(\arg V-2\arg W\) is nonzero and is invariant under the resonant autonomous flow. Thus this initial condition cannot be obtained from the printed forcing by choosing another origin of \(\zeta\).

It follows that Figure 11(a) and Figure 11(b) are generated on different resonant phase leaves. A Lyapunov diagram on the latter leaf cannot, without an additional relative-phase-independence theorem, be used as a pointwise diagnostic of the former periodically forced equation.

## Verification
The bundled `verify.py` uses exact rational polynomial arithmetic. It verifies that the Lie derivatives of \(I_1\), \(I_2\), \(\operatorname{Re}K\), and \(\operatorname{Im}K\) vanish identically for \(\omega_2=2\omega_1\); checks the identity \(|K|^2=I_1^2I_2\); and evaluates the source's oscillator initial state to \(K=(117-44i)/125\). Running `python verify.py` returns `VERIFY_OK`.

The proof is algebraic and does not depend on numerical integration, finite-time Lyapunov estimation, or a visual reading of Figure 11.

## Relationship to prior work
Liu, Feng, Chen, and Huang introduce the autonomous system and describe it as equivalent to the periodically forced planar system. Their Section 4 writes the oscillator substitution explicitly, while the Figure 11 caption gives the distinct initial data used for the bifurcation and Lyapunov panels. The paper does not state the resonant first integral \(K\), enforce the phase leaf \(K=1\) in Figure 11(b), or prove that the diagnostics are invariant under changing \(K\).

Saha's earlier work studies periodic perturbations of the generalized KP-MEW-Burgers equation and is the antecedent cited for the forced dynamics, but no inspected statement identifies or removes the resonant relative-phase degree of freedom in the later six-dimensional autonomous embedding. Semantic searches for the source title, autonomous embedding, harmonic-oscillator phase invariants, and Lyapunov-spectrum comparisons found no result implying the source-specific value \(K=(117-44i)/125\) or the Figure 11 mismatch.

## Limitations
The result is a structural comparison theorem, not a recomputation of the source's numerical dynamics. It does not prove that the bifurcation thresholds or Lyapunov exponents shown in Figure 11 are numerically incorrect. A separate theorem showing that the relevant asymptotic diagnostics are independent of the resonant relative phase could restore comparability, but no such theorem is supplied or established here. The claim is restricted to the \(2:1\) resonance used in Figure 11 and does not treat the incommensurate experiment in Figure 13.

## References
1. A. Liu, X. Feng, B. Chen, X. Huang, “Geometric analysis of traveling wave solutions for the generalized KP-MEW-Burgers equation,” *Discrete and Continuous Dynamical Systems - S* 18 (2025), 379–404. DOI: 10.3934/dcdss.2024065. Early access: 2024-05-12.
2. A. Saha, “Dynamics of the generalized KP-MEW-Burgers equation with external periodic perturbation,” *Computers & Mathematics with Applications* 73 (2017), 1879–1885. DOI: 10.1016/j.camwa.2017.02.017.
