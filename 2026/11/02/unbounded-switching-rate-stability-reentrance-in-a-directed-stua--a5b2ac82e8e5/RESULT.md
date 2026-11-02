# Unbounded switching-rate stability reentrance in a directed Stuart–Landau triad

## Finding

**Theorem (exact Floquet criterion and arbitrarily many alternating windows).** Fix any positive dissipative coupling \(u>0\). For each positive reactive coupling \(v>0\) and half-switching period \(\tau>0\), consider three complex oscillators \(z_j\), indexed modulo three, evolving by
\[
\dot z_j=(1+i-|z_j|^2)z_j+(u+iv)\bigl(z_{j+s(t)}|z_{j+s(t)}|^2-z_j|z_j|^2\bigr),
\]
where \(s(t)=+1\) during \(2k\tau\le t<(2k+1)\tau\), and \(s(t)=-1\) during \((2k+1)\tau\le t<(2k+2)\tau\), for every integer \(k\). The exactly synchronized motion \(z_0=z_1=z_2=e^{it}\) is a periodic solution in each switched system (the forcing period need not be commensurate with \(2\pi\), but this is a relative equilibrium under common phase rotation).

Set
\[
\lambda=-\frac32+\frac{\sqrt3}{2}i,\quad B=2+6u,\quad
\Delta=\sqrt{(-1+u\lambda)^2-3v^2\lambda^2}=\xi+i\eta,
\]
choosing the square-root branch with \(\xi\ge0\). Let
\[
h=1+3u+3u^2-9v^2,\qquad R=\sqrt{h^2+9v^2},\qquad r=\frac hR.
\]
Then \(-1<r<1\), \(\xi>0\), and the synchronized solution is *locally orbitally exponentially attracting* if and only if
\[
\boxed{\left|(1+r)\cosh(2\xi\tau)+(1-r)\cos(2\eta\tau)\right|<2\cosh(B\tau).}
\tag{1}
\]
If the strict reverse inequality holds, it is transversely linearly unstable. Equality is a nonhyperbolic Floquet boundary; no nonlinear stability claim is made there.

For every \(u>0\) and every positive integer \(N\), **there exists a single finite \(v>0\)** for which, as \(\tau\) increases, at least \(N\) distinct open intervals of transverse exponential attraction are separated by distinct open intervals of transverse instability. In fact, for sufficiently large \(v\), the alternating sample times
\[
\tau_n^+=\frac{\pi n}{|\eta|},\qquad
\tau_n^-=\frac{\pi(n+1/2)}{|\eta|}
\]
have instability at each \(\tau_n^+\) and attraction at each \(\tau_n^-\) for any prescribed finite consecutive set of sufficiently large integers \(n\). The individual clockwise and anticlockwise autonomous networks are then both linearly unstable near synchrony, while the averaged transverse network is exponentially stable for every \(u,v>0\). Thus the number of stability reversals is unbounded as the reactive coupling increases; the theorem does **not** assert infinitely many windows at one fixed \(v\).

## Assumptions and scope

Time is real; coefficients \(u,v,\tau\) are strictly positive; states are complex triples with standard Euclidean topology. The prescribed switching is periodic, piecewise constant and right continuous, with two equal-duration orientations. The phrase *orbitally exponentially attracting* concerns perturbations transverse to the exact common-phase family \(\{e^{i\phi}(1,1,1):\phi\in\mathbb R\}\), in the co-rotating state variables. This is a linearized Floquet criterion implying local nonlinear orbital exponential attraction of the normal modes by standard smooth-in-state periodic dynamics. It is not a claim of global synchronization. The phase-neutral direction is exempt from strict attraction. Although the laboratory-frame solution has period \(2\pi\), the autonomous rotating-frame synchronous equilibrium is common to both switching states, permitting Floquet analysis with period \(2\tau\) for arbitrary \(\tau\).

## Proof

**1. Exact invariant synchronization and its variational splitting.** Write \(z_j=e^{it}(1+\rho_j+i\varphi_j)+O(\|\rho,\varphi\|^2)\), where \(\rho_j,\varphi_j\in\mathbb R\). The local vector field supplies the diagonal block \(J_0=\begin{pmatrix}-2&0\\0&0\end{pmatrix}\). Differentiating \(z|z|^2\) at \(z=1\) gives \(3\rho+i\varphi\). Therefore the derivative of the nonlinear directed coupling is \(J_h=\begin{pmatrix}3u&-v\\3v&u\end{pmatrix}\) times \(P_s-I\), where \(P_s\) denotes the forward or backward cyclic permutation. All three permutations commute and share Fourier vectors. The common Fourier vector has Floquet exponents \(-2\) and \(0\). Each of the two transverse Fourier modes has ordered half-period matrices \(A_+=J_0+\lambda J_h\) and \(A_-=J_0+\overline\lambda J_h\), in either order depending on the Fourier mode. The two ordered products have identical eigenvalues by cyclic similarity, so it suffices to analyze \(M=e^{\tau A_-}e^{\tau A_+}\).

**2. Exact trace and determinant.** The trace of \(A_+\) has real part \(-B\). Its traceless component is
\[
C=A_+-\frac{\operatorname{tr}A_+}{2}I
=\begin{pmatrix}-1+u\lambda&-v\lambda\\3v\lambda&1-u\lambda\end{pmatrix}.
\]
It satisfies \(C^2=\Delta^2 I\). Consequently
\[
e^{\tau A_+}=e^{\tau\operatorname{tr}A_+/2}
\left(\cosh(\Delta\tau)I+\frac{\sinh(\Delta\tau)}{\Delta}C\right),
\]
and the reverse half-period uses the complex conjugate expression. Direct multiplication, using \(\operatorname{tr}(\overline C C)=2h\), gives
\[
\det M=e^{-2B\tau},\qquad
\operatorname{tr}M=e^{-B\tau}\left((1+r)\cosh(2\xi\tau)+(1-r)\cos(2\eta\tau)\right).
\tag{2}
\]
Indeed \(|\Delta|^4-h^2=9v^2\), or \(R^2-h^2=9v^2\), and hence \(r=h/R\). For \(v>0\), the square-root argument cannot lie on the nonpositive real axis: its imaginary part vanishes only at \(v^2=u(3u+2)/9\), where its real part is \(1+2u>0\). Thus \(\xi>0\). The Floquet characteristic polynomial \(x^2-(\operatorname{tr}M)x+\det M\) has **real** coefficients and \(0<\det M<1\). The strict Schur criterion is \(|\operatorname{tr}M|<1+\det M\), which is precisely (1). When (1) is violated strictly, at least one transverse Floquet multiplier has modulus greater than one. At equality it has modulus one.

**3. Fast-switching stability and slow-switching instability.** The averaged transverse generator is \(\overline A=J_0-\tfrac32J_h\), with
\[
\operatorname{tr}\overline A=-B<0,\qquad
\det\overline A=3u+\frac{27}{4}(u^2+v^2)>0.
\]
Thus sufficiently rapid switching is stable for each finite \(v\). For \(v\to\infty\), \(\xi/v\to3/2\), and eventually \(2\xi>B\). At each such fixed \(v\), the positive coefficient \(1+r\) of \(\cosh(2\xi\tau)\) makes the left side of (1) dominate \(2\cosh(B\tau)\) as \(\tau\to\infty\); sufficiently slow switching is unstable. The autonomous half-network generator also has positive spectral abscissa \(\xi-B/2>0\) at these parameters.

**4. Arbitrarily many strict alternations.** The exact identity \(R^2-h^2=9v^2\) and the leading square-root asymptotics give
\[
\frac{\xi}{v}\to\frac32,\qquad \frac{|\eta|}{v}\to\frac{3\sqrt3}{2},\qquad
v^2(1+r)\to\frac1{18},\qquad 1-r\to2.
\]
At each fixed positive integer \(n\), write \(t_n=\pi n/|\eta|\). The cosine term equals \(1\) there, so
\[
\lim_{v\to\infty}v^2\left[(1+r)\cosh(2\xi t_n)+(1-r)-2\cosh(Bt_n)\right]
=\frac{\cosh(2\pi n/\sqrt3)-1}{18}
-B^2\left(\frac{2\pi n}{3\sqrt3}\right)^2=:Q_n.
\tag{3}
\]
The positive exponential in \(n\) dominates the quadratic term: there exists \(n_0(u)\) with \(Q_n>0\) for every integer \(n\ge n_0\). Thus any prescribed finite group of those positive-peak times violates the stability inequality for all sufficiently large finite \(v\). At the interlaced times \(s_n=\pi(n+1/2)/|\eta|\), the same expression inside the absolute value in (1) equals
\[
-2+(1+r)(\cosh(2\xi s_n)+1),
\]
which tends to \(-2\) **from above** and lies strictly between \(-2\) and \(2\) for each fixed \(n\) at sufficiently large \(v\). Since \(2\cosh(Bs_n)>2\), each such trough satisfies the *strict* attraction inequality. Choosing one finite \(v\) sufficiently large for all \(N\) selected peaks and troughs, then using continuity, supplies arbitrarily many separated nonempty stable and unstable open parameter intervals. This proves the quantified statement without asserting a fixed-parameter infinite sequence.

## Verification

The independently executable supplementary file `verify_switching.py` computes the two complex matrix exponentials from the traceless-matrix identity; compares their direct product with (2); verifies the exact discriminant and averaged-generator identities; and checks explicit alternating attraction/instability sample times at \(u=1/20\), \(v=1000\). Its finite numerical tests corroborate algebra but the proof of unbounded alternations is (3), not numerical enumeration. The reproducible command is `python verify_switching.py`, using only the Python standard library.

## Relationship to prior work

Segnou–Carletti–Ghosh (arXiv:2610.17150v1, 2026) prove useful averaged fast-switching synchronization conditions for general directed higher-order network systems and illustrate loss of synchronization as switching slows. Pereti–Fanelli (arXiv:1912.00939v1, 2019) analyze time-switched **undirected** Stuart–Landau networks with **linear** coupling, using monodromy products and a critical swapping rate. Zhang–Strogatz (2021) analyze optimally designed time-varying networks under resource constraints, including intermediate switching rates. The generic use of Floquet products, switching stabilization, and fast/slow distinctions is therefore not claimed as new. The result here is the **exact three-parameter criterion** for the specified *directed, three-node, amplitude-dependent coupling system* and the quantified **unbounded number of alternating stability windows as reactive coupling increases**. Relevant mathematical research records concerning static three-oscillator phase stabilization and unrelated periodic Floquet examples do not imply this claim. Priority cannot be guaranteed beyond inspected sources.

## Limitations

Only local orbital stability around exact synchrony is classified, not basins, transient growth, global synchrony, nonlinear behavior at unit-modulus boundaries, or attractors born at stability changes. The increasing number of intervals requires a coupling parameter \(v\) that may grow with the requested interval count. The model contains time-dependent **directed cubic neighbor coupling**, not the linear graph coupling of some earlier Stuart–Landau switching studies. Switching is exactly periodic with equal half-periods. Potential unindexed specialized studies of reentrant Floquet stability remain a historical-priority risk; neither a failed search nor a mathematical partition establishes uniqueness.

## References

1. Y. Segnou, T. Carletti, D. Ghosh, *Global synchronization in time-varying directed higher-order networks*, arXiv:2610.17150v1 (first public October 12, 2026), https://arxiv.org/abs/2610.17150 .
2. C. Pereti, D. Fanelli, *Stabilizing Stuart-Landau oscillators via time-varying networks*, arXiv:1912.00939v1 (2019), https://arxiv.org/abs/1912.00939 .
3. Y. Zhang, S. H. Strogatz, *Designing temporal networks that synchronize under resource constraints*, Nature Communications **12**, 3273 (2021), https://doi.org/10.1038/s41467-021-23446-9 .
