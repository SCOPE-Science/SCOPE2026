# A nonzero Floquet correction for a curved-space drive

## Finding

For every nonconstant smooth periodic profile \(g\) on \(\mathbb T\), the formal cosine-drive Floquet correction \(\frac{\epsilon^2}{4\omega^2}[B_g,[A,B_g]]\), with \(A=-\partial_x^2\) and \(B_g=-2g'\partial_x-g''\), has principal coefficient \(a_2(x)=8(2(g''(x))^2-g'(x)g'''(x))\) that is not identically zero; \(a_2\equiv0\) holds only when \(g\) is constant. Since the moment term \(C_g=-(g')^2\) is multiplication-only, the moment-averaged operator is not the complete formal Floquet expansion for any nonconstant smooth periodic profile; the result does not assert convergence of the full unbounded-operator series.


## Assumptions and scope

Work on the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) and the common invariant core \(C^\infty(\mathbb T)\). Set \(V=0\), \(A=-\partial_x^2\), \(B_g=-2g'\partial_x-g''\), and \(C_g=-(g')^2\), as in the transformed differential operator of the cited Floquet-geometric construction. Let \(\bar\gamma=\epsilon g\), where \(g\) is any real-valued smooth periodic function, and take \(f(t)=\cos(\omega t)\) with \(\omega>0\). The claim concerns an exact differential-operator identity and a formal high-frequency coefficient on smooth periodic functions. It does not assert convergence of the full Magnus series or an operator-norm error bound for the unbounded, potentially non-self-adjoint evolution.

## Proof

The transformed generator is

\[
H'(t)=A+\epsilon\cos(\omega t)B_g+\epsilon^2\cos^2(\omega t)C_g.
\]

Its mean is \(H_0=A+\epsilon^2C_g/2\), and its first Fourier harmonics are \(H_1=H_{-1}=\epsilon B_g/2\). The formal van Vleck coefficient at order \(\epsilon^2\omega^{-2}\) is

\[
\sum_{m=\pm1}\frac{[H_{-m},[H_0,H_m]]}{2(m\omega)^2}
=\frac{\epsilon^2}{4\omega^2}[B_g,[A,B_g]].
\]

Only the stated coefficient is identified; this is not a convergence or remainder assertion. Replacing \(H_0\) by \(A\) inside the nested commutator is exact at order \(\epsilon^2\), because the \(C_g\) part first contributes at order \(\epsilon^4\).

Write \(D=\partial_x\). Using \(Df=fD+f'\) on \(C^\infty(\mathbb T)\) gives

\[
[A,B_g]=4g''D^2+4g'''D+g''''.
\]

A second commutation shows that the coefficient of \(D^2\) in \([B_g,[A,B_g]]\) is

\[
a_2(x)=16(g''(x))^2-8g'(x)g'''(x)=8\bigl(2(g''(x))^2-g'(x)g'''(x)\bigr).
\]

We classify when this principal coefficient vanishes identically. Put \(p=g'\). If \(a_2\equiv0\), then \(p p''=2(p')^2\). On every connected component of \(\{x:p(x)\ne0\}\),

\[
\left(\frac{p'}{p^2}\right)'=\frac{p p''-2(p')^2}{p^3}=0,
\]

so \(p'/p^2\) is constant there. Solving this first-order equation shows that \(p\) is either a nonzero constant or has the form \(p(x)=-1/(cx+d)\) on that component. Neither form can approach zero at a finite endpoint of the component. Therefore, if \(p\) is nonzero anywhere, it must be nonzero on the entire circle and have constant sign. But a periodic derivative satisfies \(\int_0^{2\pi}p(x)\,dx=0\), contradicting constant sign. Hence \(p\equiv0\) and \(g\) is constant. Conversely, constant \(g\) gives \(B_g=0\), so the principal coefficient vanishes. Thus every nonconstant smooth periodic profile has a nonzero principal coefficient somewhere.

For the illustrative profile \(g(x)=\cos x\), the full commutator is

\[
[B_g,[A,B_g]]=(8+8\cos^2x)D^2-16\sin x\cos x\,D+2\sin^2x-4\cos^2x.
\]

Equivalently,

\[
[B_g,[A,B_g]]=D\!\left((8+8\cos^2x)D\right)+(2\sin^2x-4\cos^2x).
\]

The coefficient \(a_2\) is a second-order differential term, whereas \(C_g=-(g')^2\) is multiplication-only. Consequently, the nonzero order-\(\epsilon^2\omega^{-2}\) term cannot be absorbed into the moment-averaged operator \(A+\epsilon^2C_g/2\) as a scalar potential. Time symmetry removes the second Magnus term but does not make all higher Floquet coefficients vanish.

## Verification

The commutator identities follow by exact differential-operator algebra on \(C^\infty(\mathbb T)\). The classification uses only the displayed scalar ODE and periodicity of \(g'\); no numerical truncation is used as proof. The frequency-dependent statement is limited to the formal high-frequency coefficient. No convergence of the infinite expansion or continuum propagator error bound is claimed.

## Relationship to prior work

Alperin's 2025 paper derives the transformed generator and then states that for time-symmetric drives higher-order Magnus terms may be discarded while calling the resulting stroboscopic Hamiltonian exact. Systematic high-frequency expansions already provide the nested-commutator method. The result here adds a profile-independent classification in one dimension: among smooth periodic profiles, only constants can make the principal coefficient of this order-\(\epsilon^2\omega^{-2}\) correction vanish identically. It is not a claim to invent the general Floquet expansion.

## Limitations

The classification is for one-dimensional smooth periodic profiles and the principal coefficient at the stated formal order; it does not classify every profile for which the full nested commutator might have special lower-order cancellations on nonperiodic domains. Because the generator is unbounded and may be non-self-adjoint, rigorous propagator-level control requires domain and regularity hypotheses beyond this calculation. The result does not establish convergence of the Magnus series or a global error bound for the full continuum evolution.

## References

1. S. Alperin, “Non-Hermitian Realization of Quantum Dynamics on Embedded Manifolds,” arXiv:2510.11845v1 (13 October 2025). https://arxiv.org/abs/2510.11845
2. A. Eckardt and E. Anisimovas, “High-frequency approximation for periodically driven quantum systems from a Floquet-space perspective,” arXiv:1502.06477v4 (15 June 2015). https://arxiv.org/abs/1502.06477
3. D. Burgarth, R. Hillier, D. Lonigro, and L. Richter, “The Floquet–Magnus expansion of unbounded operators,” arXiv:2605.23734v1 (22 May 2026). https://arxiv.org/abs/2605.23734
