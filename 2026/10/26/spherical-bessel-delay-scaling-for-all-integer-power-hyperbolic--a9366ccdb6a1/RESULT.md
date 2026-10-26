# Spherical-Bessel delay scaling for all integer-power hyperbolic-secant ambiguity zeros

## Finding

Fix any integer \(m\ge1\) and the real nonnegative window \(f_m(t)=\operatorname{sech}^m(t)\). Its symmetric self-ambiguity function at delay \(T\in\mathbb R\) and Doppler frequency \(\nu\in\mathbb R\) is
\[
A_m(T,\nu)=\int_{\mathbb R} f_m(t+T/2)f_m(t-T/2)e^{-2\pi i\nu t}\,dt.
\]
Put \(n=m-1\), \(k=2\pi\nu\), \(u=\pi\nu\), and let \(j_n\) be the spherical Bessel function with positive zeros \(0<y_{n,1}<y_{n,2}<\cdots\).

**Zero-delay contrast.** Every \(A_m(0,\nu)\) is strictly positive. For each fixed \(T\ne0\), the number \(N_{m,T}(R)\) of distinct positive Doppler zeros in \((0,R]\) satisfies
\[
N_{m,T}(R)=|T|R+O_{m,T}(1)\qquad(R\to\infty),
\]
and all sufficiently large such zeros are simple.

**Coalescing-delay law.** For each fixed \(j\ge1\) there is, for all sufficiently small \(T>0\), exactly one simple root \(\nu_{m,j}(T)\) in an arbitrarily small neighborhood of the rescaled target \(\pi T\nu=y_{n,j}\), with
\[
\pi T\nu_{m,j}(T)=y_{n,j}+O_{m,j}(T^2).
\]
More precisely, on every compact interval contained in \((0,\infty)\) whose endpoints are not spherical-Bessel zeros, for sufficiently small \(T\) the rescaled roots have exactly the same number, all simple, as the zeros of \(j_n\) in that interval. The statement excludes rescaled frequencies approaching zero and does not claim that the local branches are globally the first, second, etc. positive zeros for arbitrary \(m\).

**Fully explicit case.** For \(m=2\) and every \(T>0\), let \(y=\pi T\nu\). The positive Doppler zeros are exactly the simple solutions
\[
\tan y=\frac{\tanh T}{T}\,y,
\]
one in each \((j\pi,j\pi+\pi/2)\), \(j=1,2,\ldots\), and none elsewhere. In particular, the first zero obeys \(\pi T\nu_{2,1}(T)\to4.493409457909\ldots\), the first positive zero of \(j_1\).

## Assumptions and scope

All signals are real, \(L^2(\mathbb R)\), and no chirp or translation is used. The ambiguity convention includes \(e^{-2\pi i\nu t}\). Statements hold for all positive integral exponents \(m\), with constants depending on fixed \(m\); high-frequency estimates hold at fixed \(T\ne0\), and the Bessel scaling at fixed \(m,j\) as \(T\to0\). Evenness gives the same zero locations for negative delay and Doppler. The spherical Bessel function is \(j_n(y)=\sqrt{\pi/(2y)}J_{n+1/2}(y)\) for \(y>0\).

## Proof

**1. Exact closed operator expression.** The identity
\[
\cosh(t+T/2)\cosh(t-T/2)=\frac{\cosh(2t)+\cosh T}2
\]
gives \(A_m=2^m\int_{\mathbb R}(\cosh 2t+\cosh T)^{-m}e^{-ikt}\,dt\). For \(T>0\) a standard residue calculation (or the substitution \(e^{2t}=z\), followed by partial fractions) gives
\[
\int_{\mathbb R}\frac{e^{-ikt}}{\cosh 2t+\cosh T}\,dt
=\frac{\pi\sin(uT)}{\sinh T\sinh(\pi u)}.
\]
Because the denominator stays above a positive constant in the real integration variable, differentiation under the integral is justified for each fixed \(T>0\). With the fixed-frequency differentiation operator \(D_T=(\sinh T)^{-1}\partial_T\), one obtains the exact formula
\[
A_m(T,\nu)=\frac{2^m\pi(-1)^{m-1}}{(m-1)!\sinh(\pi u)}D_T^{m-1}\left[\frac{\sin(uT)}{\sinh T}\right]\quad(\nu>0,T>0).
\]
The denominator \(\sinh(\pi u)\) never vanishes for positive real \(u\); zero counting reduces to the displayed differentiated sine quotient.

**2. Zero delay.** Substitution \(x=e^{2t}\) in the original integral at \(T=0\) gives
\[
A_m(0,\nu)=2^{2m-1}B(m+i\pi\nu,m-i\pi\nu)>0,
\]
since this is \(2^{2m-1}|\Gamma(m+i\pi\nu)|^2/\Gamma(2m)\).

**3. Fixed-delay high-frequency count.** Let \(n=m-1\). For fixed \(T>0\), Leibniz's rule applied \(n\) times gives, as \(u\to+\infty\),
\[
(-1)^nD_T^n[\sin(uT)/\sinh T]
=\frac{(-1)^nu^n}{\sinh^{n+1}T}\sin(uT+n\pi/2)+O_{m,T}(u^{n-1}).
\]
The derivative with respect to \(u\) has leading term \(T(-1)^nu^n\cos(uT+n\pi/2)/\sinh^{n+1}T\) and an \(O(u^{n-1})\) error. Outside \(O(1/u)\) neighborhoods of the zeros of the leading sine, its sign fixes the sign of the exact expression. Inside each such neighborhood, the derivative has a fixed nonzero sign for sufficiently large \(u\), and the values at its two endpoints have opposite signs. Hence exactly one simple zero occurs near each sufficiently large reference zero, and there are no others. Reference zeros have spacing \(\pi/T\) in \(u\); since \(u=\pi\nu\), their Doppler density is \(T\), proving the count and simplicity.

**4. Singular small-delay scaling.** Put \(n=m-1\), \(y=uT\), and define
\[
F_{m,T}(y)=(-1)^nT^{2n+1}D_\tau^n[\sin((y/T)\tau)/\sinh\tau]_{\tau=T},
\]
where each \(\tau\) derivative holds the frequency \(y/T\) fixed. Set \(r=\tau/T\), \(h_T(r)=\sinh(Tr)/T\). An exact change of variables gives
\[
F_{m,T}(y)=(-1)^n[(h_T(r)^{-1}\partial_r)^n (\sin(yr)/h_T(r))]_{r=1}.
\]
For \(r\) in a fixed neighborhood of \(1\), the smooth function \(h_T(r)=r+O(T^2)\), together with all fixed-order derivatives, converges to \(r\), uniformly as \(T\to0\). For each compact complex \(y\)-set this gives the locally uniform limit with an \(O_{m,K}(T^2)\) error,
\[
F_{m,T}(y)\longrightarrow (-1)^n[(r^{-1}\partial_r)^n(\sin(yr)/r)]_{r=1}
= y^{n+1}j_n(y).
\]
The last equality is the spherical-Bessel derivative identity \(j_n(y)=(-y)^n(y^{-1}\partial_y)^n(\sin y/y)\). Each strictly positive Bessel zero is simple. Local uniform convergence plus Rouché's theorem on a sufficiently small complex circle around each such zero implies exactly one nearby zero counted with multiplicity. Conjugation symmetry forces it to be real, and the derivative estimate plus simplicity yields the \(O(T^2)\) displacement. Compact intervals disjoint from zero have no additional zeros by the same argument, establishing the stated local census.

**5. Exactly solved second power.** For \(m=2\), the differentiated sine quotient is proportional to \(u\sinh T\cos(uT)-\cosh T\sin(uT)\). The equation in positive \(y=uT\) is \(\tan y=(\tanh T/T)y\) (the cosine cannot vanish at a zero). Because \(0<\tanh T/T<1\), there is no positive root on \((0,\pi)\). On each \((j\pi,j\pi+\pi/2)\), the function \(\tan y-(\tanh T/T)y\) rises strictly from negative to positive infinity; it is negative on the intervening right half-period. Thus exactly the asserted simple roots occur. Sending \(T\to0\) yields \(\tan y=y\), whose positive roots are the positive zeros of \(j_1\).

## Verification

The standalone \`check.py\` evaluates the original integral against the differentiated formula for \(m=1,2,3\), checks the scaled roots near the first two spherical-Bessel zeros for \(m=1,2,3,4\), and verifies the stated \(m=2\) root intervals. This is a numerical consistency test only: the all-order assertions are established in the proof above. The exact derivative structure, scaling order, and normalization can be independently replayed from the included code.

## Relationship to prior work

Kloos and Stöckler (arXiv:1311.7359v1, publicly submitted 2013-11-28) analyze Gabor/Zak frames of totally positive and exponential-spline windows, and explicitly mention the hyperbolic-secant window; their inspected introduction addresses lattice frame bounds rather than ambiguity zeros, integer-power secant windows, or the Bessel delay limit. Gröchenig, Jaming and Malinnikova (arXiv:1811.03937, 2018) analyze zero-free ambiguity and Wigner transforms of Gaussian and exponential-convolution windows, and their inspected examples do not contain this integer-power secant nodal census. Boyadzhiev (arXiv:0903.0117, 2009) gives classical derivative-polynomial techniques for hyperbolic functions, relevant to the differentiation step but not the coupled large-frequency/small-delay zeros. Classical beta and spherical-Bessel formulas are used as standard identities; no priority over these techniques is claimed.

## Limitations

The novelty comparison is a best-knowledge, non-exhaustive literature assessment; an older radar-pulse or special-function derivation could imply the formula or its scaling limit. The theorem does not classify all finite positive real zeros for arbitrary powers \(m\ge3\), does not count possible small-delay zeros with \(\pi T\nu\to0\), and does not give estimates uniform in increasing \(m\). It does not claim an application-dependent optimal pulse or a global new special-function identity.

## References

- T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1 (2013-11-28), https://arxiv.org/abs/1311.7359.
- K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937v1 (2018-11-09), https://arxiv.org/abs/1811.03937.
- K. N. Boyadzhiev, *Derivative Polynomials for tanh, tan, sech and sec in Explicit Form*, arXiv:0903.0117v1 (2009-03-01), https://arxiv.org/abs/0903.0117.
- Standard identities for Euler's beta integral and spherical Bessel functions \(j_n\).
