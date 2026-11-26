# A nonzero formal Floquet correction for a curved-space drive

## Finding

Let \(g\in C^\infty(\mathbb T;\mathbb R)\), where \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), and set \(D=\partial_x\), \(A=-D^2\), \(B=-2g'D-g''\), and \(C=-(g')^2\). On the common smooth core, consider the formal Schrödinger evolution with
\[
H(t)=A+\epsilon\cos(\omega t)B+\epsilon^2\cos^2(\omega t)C,\qquad \omega>0.
\]
In the phase-independent van Vleck convention the term of order \(\epsilon^2\omega^{-2}\) is \(\epsilon^2[B,[A,B]]/(4\omega^2)\). The coefficient of \(D^2\) in the double commutator is
\[
a_2=8\big(2(g'')^2-g'g'''\big).
\]
It vanishes identically if and only if \(g\) is constant. Thus the moment average \(A+\epsilon^2 C/2\) is not the full formal van Vleck generator for any nonconstant \(g\).

The stroboscopic generator at the cosine phase \(t=0\) is in a different convention. At order \(\omega^{-2}\), retaining degrees one and two in \(\epsilon\), its terms are
\[
-\frac{\epsilon}{\omega^2}[A,[A,B]]
+\frac{\epsilon^2}{4\omega^2}[B,[A,B]]
-\frac{\epsilon^2}{8\omega^2}[A,[A,C]].
\]
In particular the full stroboscopic coefficient of \(\epsilon^2\omega^{-2}D^2\) is \(5(g'')^2-g'g'''\), which also vanishes identically only for constant \(g\). These are identities of formal expansions, not convergence or propagator error estimates.

## Proof

**Van Vleck coefficient.** With the Fourier convention \(H(t)=\sum_m H_m e^{im\omega t}\), the nonzero harmonics are \(H_0=A+\epsilon^2C/2\), \(H_{\pm1}=\epsilon B/2\), and \(H_{\pm2}=\epsilon^2 C/4\). The standard order-\(\omega^{-2}\) formula [2, Eq. (89)] includes
\[
\sum_{m\ne0}\frac{[H_{-m},[H_0,H_m]]}{2(m\omega)^2}.
\]
Only \(m=\pm1\) with the amplitude-zero part of \(H_0\) contributes at degree two in \(\epsilon\). The other sum at this frequency order involves three nonzero Fourier factors, so cannot contribute at degree two. This gives exactly \(\epsilon^2[B,[A,B]]/(4\omega^2)\).

**Differential coefficient.** Use \(Df=fD+f'\) on the smooth core. One obtains \([A,B]=4g''D^2+4g'''D+g''''\). The \(D^2\) coefficient in the commutator of \(bD\) with \(aD^2\) is \(ba'-2ab'\); the lower-order parts in these two operators do not contribute at order two. Taking \(a=4g''\), \(b=-2g'\) gives the stated \(a_2\). Periodicity gives
\[
\int_{0}^{2\pi}a_2(x)\,dx=24\int_0^{2\pi}(g''(x))^2\,dx.
\]
For real \(g\), this integral is positive unless \(g''\equiv0\), which for a periodic function means \(g\) is constant. Conversely a constant gives \(B=0\). The principal differential term is absent from the multiplication operator \(C\), and thus cannot be reproduced by moment averaging.

**Stroboscopic phase.** In the van Vleck convention write the periodic micromotion as \(e^{-iK(t)}\), with the coefficients of \(K\) chosen to have zero time mean. The formal stroboscopic generator is \(e^{-iK(0)}H_{\mathrm{vV}}e^{iK(0)}\) [2, Eq. (101)]. Put \(\theta=\omega t\). At frequency order \(\omega^{-1}\), integration of \(H(t)-H_0\) gives
\[
K_1(t)=\frac{\epsilon}{\omega}\sin\theta\,B+\frac{\epsilon^2}{4\omega}\sin(2\theta)\,C.
\]
To find the terms of amplitude degree at most two in \(K_2\) (order \(\omega^{-2}\)), transform the generator by \(e^{-iK(t)}\). After subtracting \(\dot K_1\), the terms at frequency order \(\omega^{-1}\) are \(i[K_1,H_0]+\tfrac i2[K_1,H(t)-H_0]-\dot K_2\). Below degree three in \(\epsilon\) the second commutator vanishes (its only candidate is a self-commutator of \(B\)), and \(H_0\) in the first commutator can be replaced by \(A\). Thus \(\dot K_2=i[K_1,A]\) through the relevant degrees. Integrating with zero mean gives those terms of \(K_2\) as
\[
\frac{i\epsilon}{\omega^2}\cos\theta\,[A,B]+\frac{i\epsilon^2}{8\omega^2}\cos(2\theta)\,[A,C].
\]
Since \(K_1(0)=0\), conjugation at phase zero adds just \(-i[K_2(0),A]\) at the relevant orders. This is the sum of the two additional terms in the Finding. For multiplication by \(C\), the \(D^2\) coefficient of \([A,[A,C]]\) is \(4C''\). The quadratic stroboscopic coefficient is therefore \(a_2/4-C''/2=5(g'')^2-g'g'''\). Its integral is \(6\int_0^{2\pi}(g'')^2\,dx\), giving the same nonvanishing criterion. The waveform is time symmetric, but cancellation of the second Magnus term does not imply cancellation of these higher terms.

## Verification and scope

All commutations are exact differential-operator calculations on \(C^\infty(\mathbb T)\). The frequency statements concern coefficients in the formal expansion in inverse frequency, at the indicated degrees in amplitude. No estimate is asserted for an unbounded operator remainder or a non-self-adjoint propagator; no exact geometric mapping is ruled out by this calculation.

## Relationship to prior work

Alperin [1, p. 2, Eqs. (4)–(10)] gives the transformed generator and its leading moment average. The time-symmetry passage correctly identifies the vanishing of the second Magnus term, but describes discarding higher terms as leaving the exact stroboscopic Hamiltonian. The concrete cosine calculation shows why this truncation is not exact as a formal series in the specified one-dimensional model, even when compared in stroboscopic convention rather than van Vleck convention. It does not contest the definition of the exact period map. The general expansion and the distinction of conventions are standard [2]; the result here identifies and classifies the profile-dependent obstruction. Rigorous unbounded-operator Floquet–Magnus error bounds require additional hypotheses, as in [3].

1. S. Alperin, *Non-Hermitian Realization of Quantum Dynamics on Embedded Manifolds*, arXiv:2510.11845v1.
2. A. Eckardt and E. Anisimovas, *High-frequency approximation for periodically driven quantum systems from a Floquet-space perspective*, arXiv:1502.06477v4.
3. D. Burgarth, R. Hillier, D. Lonigro, and L. Richter, *The Floquet–Magnus expansion of unbounded operators*, arXiv:2605.23734v1.
