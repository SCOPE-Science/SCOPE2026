# Antipodal Bessel boundary layer for three-dimensional truncated Poisson kernels

## Finding

Define \(P_n\) to be the Legendre polynomial normalized by \(P_n(1)=1\), and define the degree-\(N\) three-dimensional projected Poisson kernel
\[
G_N(r,t)=\sum_{n=0}^{N}(2n+1)r^nP_n(t),\qquad 0\le r<1,\ -1\le t\le1.
\]
Fix any real \(c\) and any \(z\ge0\). For integers \(N\ge3\), sufficiently large that the following radius is in \((0,1)\), write
\[
r_N(c)=1-\frac{2\log N-\log\log N+c}{N},\qquad t_N(z)=-\cos(z/N).
\]
Then the following **parity-sensitive boundary-layer law** holds:
\[
\boxed{\frac{N}{\log N}G_N(r_N(c),t_N(z))
=\frac12+(-1)^N\mathrm e^{-c}J_0(z)+o(1),}
\]
where \(J_0\) is the ordinary Bessel function of the first kind of order zero. The \(o(1)\) is along either parity; for fixed \(c,z\), it can be taken uniformly across both parities.

Let \(R_N\) be the largest radius such that \(G_N(r,t)\ge0\) for every \(0\le r\le R_N\) and every \(t\in[-1,1]\). Put
\[
\gamma_\mathrm e=\log(-2J_0(4))=-0.230294534094651\ldots.
\]
Then \(J_0(4)<-1/3\), and the boundary-layer law gives the **even-degree obstruction**
\[
\boxed{\liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}
\big[N(1-R_N)-2\log N+\log\log N\big]\ge\gamma_\mathrm e.}
\]
In particular, for every \(0<\beta<2\), \(G_N(1-\beta\log N/N,-\cos(4/N))<0\) for all sufficiently large even \(N\). For comparison, the same law with odd \(N\) and \(z=0\) gives
\[
\liminf_{\substack{N\to\infty\\N\ \mathrm{odd}}}
\big[N(1-R_N)-2\log N+\log\log N\big]\ge\log2.
\]
These are **one-sided obstructions**, not an asymptotic equality for \(R_N\). In particular, the result does not prove that the two parity subsequences have distinct actual second-order constants.

## Assumptions and scope

The setting is the unit ball in \(\mathbb R^3\), exact spherical-harmonic projection onto all degrees through \(N\), and exact arithmetic. Boundary data may be any continuous real-valued function. The projected harmonic extension at an interior point is integration of the boundary function against the normalized zonal kernel \(G_N\). Since this kernel has integral one, its nonnegativity characterizes the maximum-principle property for all continuous boundary data at that radius. A negative kernel value can be exposed by nonnegative continuous data supported near the corresponding direction. The maximal radius \(R_N\) exists, and positivity at an outer radius implies positivity at all smaller radii by the harmonic maximum principle, as established in the cited motivating paper.

No numerical quadrature, finite-degree interpolation, nonunit ball, or arbitrary spatial dimension is included. The asymptotics are for fixed \(c,z\), not for angles varying more rapidly than the specified \(N^{-1}\) scale.

## Proof

**Step 1: full kernel and integral representation.** For \(t\in[-1,1]\) and \(0\le r<1\), the standard Legendre generating function and a derivative give
\[
\sum_{n=0}^\infty(2n+1)r^nP_n(t)
=\frac{1-r^2}{(1-2rt+r^2)^{3/2}}=:G_\infty(r,t).
\]
For \(\theta\in[0,\pi]\), introduce
\[
q_\theta(\phi)=\cos\theta+i\sin\theta\cos\phi,
\qquad 0\le\phi\le\pi.
\]
The Laplace integral formula is
\[
P_n(\cos\theta)=\frac1\pi\int_0^\pi q_\theta(\phi)^n\,d\phi.
\]
It can be verified without a separate special-function theorem: sum the integrals of \(s^nq_\theta^n\) for small \(s\), evaluate the integral of \((1-sq_\theta)^{-1}\) using the tangent-half-angle substitution, and obtain \((1-2s\cos\theta+s^2)^{-1/2}\), the generating function of the \(P_n\). Thus the identity holds coefficientwise. Also \(|q_\theta(\phi)|\le1\).

**Step 2: exact omitted-tail identity.** For \(\theta=z/N\) and \(t=-\cos\theta\), use \(P_n(-u)=(-1)^nP_n(u)\). Writing \(q=q_\theta(\phi)\), the absolutely convergent omitted tail has the exact formula
\[
\begin{aligned}
T_N(r,z)&:=G_\infty(r,-\cos(z/N))-G_N(r,-\cos(z/N))\\
&=\frac{(-r)^{N+1}}\pi\int_0^\pi q^{N+1}
\left[\frac{2N+3}{1+rq}-\frac{2rq}{(1+rq)^2}\right]d\phi.
\end{aligned}
\]
Indeed, after factoring \((-rq)^{N+1}\), the remaining power series sums to
\( (2N+3)/(1+rq)-2rq/(1+rq)^2 \). This identity is valid for every \(r\in(0,1)\) and integer \(N\ge0\).

**Step 3: uniform angular limit of the tail.** For any fixed \(z\ge0\), uniformly over \(\phi\in[0,\pi]\),
\[
q_{z/N}(\phi)=1+\frac{iz\cos\phi}{N}+O_z(N^{-2}),
\qquad q_{z/N}(\phi)^{N+1}\longrightarrow
\mathrm e^{iz\cos\phi}.
\]
Whenever \(r=r_N(c)\), one also has \(r\to1\), \(1+rq\to2\) uniformly and the quantity in square brackets, divided by \(N\), tends uniformly to one. Consequently,
\[
\frac{T_N(r_N(c),z)}{(-1)^{N+1}Nr_N(c)^{N+1}}
\longrightarrow\frac1\pi\int_0^\pi\mathrm e^{iz\cos\phi}\,d\phi=J_0(z).
\]
The last equality is the usual integral definition of \(J_0\); the imaginary part vanishes by reflection \(\phi\mapsto\pi-\phi\).

**Step 4: the critical logarithmic scale.** Set \(\delta_N=1-r_N(c)\). Then
\[
N\delta_N=2\log N-\log\log N+c,
\quad N\delta_N^2\to0,
\quad \frac{N^2r_N(c)^{N+1}}{\log N}\longrightarrow\mathrm e^{-c}.
\]
At \(t_N(z)=-\cos(z/N)\),
\[
G_\infty(r_N(c),t_N(z))
=\frac{1-r_N(c)^2}{(1+2r_N(c)\cos(z/N)+r_N(c)^2)^{3/2}}
=\frac{\delta_N}{4}(1+o(1)),
\]
so \(NG_\infty/\log N\to1/2\). Subtracting the tail from Step 3 proves the boxed parity-sensitive law.

**Step 5: an explicit negative even-degree direction.** The power series
\[
J_0(4)=\sum_{k=0}^\infty\frac{(-1)^k4^k}{(k!)^2}
\]
has partial sum through \(k=4\) equal to \(-1/3\). Starting at that index the absolute terms decrease strictly, and the next term is negative. The alternating-series remainder therefore yields \(J_0(4)<-1/3<0\). Hence for every \(c<\gamma_\mathrm e\), the limit at even \(N\), \(z=4\) is strictly negative. For all sufficiently large even \(N\), the kernel is negative at the corresponding radius. By the definition of \(R_N\),
\[
N(1-R_N)>2\log N-\log\log N+c.
\]
Letting \(c\) tend upward to \(\gamma_\mathrm e\) yields the even-degree liminf inequality. The odd-degree inequality follows the same argument with \(z=0\), \(J_0(0)=1\), and \(c<\log2\).

For the separate assertion with \(0<\beta<2\), repeat Steps 2--3 at \(r=1-\beta\log N/N\). The normalized full kernel is negligible:
\(G_\infty(r,t_N(4))/(Nr^{N+1})=O(\log N\,N^{\beta-2})\to0\). Thus along even \(N\), \(G_N(r,t_N(4))/(Nr^{N+1})\to J_0(4)<0\), as claimed.

## Verification

The accompanying standalone `check.py` independently evaluates finite sums with high-precision Legendre recurrences and confirms the omitted-tail identity through high-precision quadrature for several small degrees. It also checks the sign at several even degrees and the limit constants from the stated formulas. These computations are diagnostics only. Steps 1--5 prove the universal conclusions analytically; neither finite testing nor numerical Bessel evaluation is used to certify the sign of \(J_0(4)\).

## Relationship to prior work

Reusken (2026), arXiv:2610.13540v1, studies the same \(d=3\) kernel and discrete maximum-principle radius. Its Lemma 11 establishes a leading logarithmic obstruction for **odd** truncation degrees; Remark 7.3 explicitly distinguishes the untreated even-degree case and reports finite-degree parity differences. Its global positivity estimate gives a complementary upper bound on \(1-R_N\), but does not imply the even-degree obstruction or the fixed-angle \(\log\log N\) profile. The present result derives an angular \(N^{-1}\) antipodal scaling law for both parities, with an explicit negative Bessel direction for even degrees.

Reusken (2025), arXiv:2511.01616v1, treats finite Fourier projection on planar discs, not three-dimensional Legendre truncation. Classical Legendre generating functions, the Laplace integral and the Bessel integral are standard tools; their individual formulas are not claimed to be new. The new claim is their quantitative combination at the critical \(r_N(c)\) scaling and the resulting even-degree maximum-principle obstruction.

## Limitations

The theorem supplies an **upper bound for the positivity radius** (equivalently, a lower bound for its deficit), not an asymptotic equality or a classification of all minimizing angles. The constant \(\gamma_\mathrm e\) arises from the explicitly chosen angle \(z=4\); no claim is made that this gives the globally optimal second-order constant. Fixed-angle convergence does not establish uniformity over unbounded \(z\). No conclusion is asserted for nonprojected kernels, higher dimensions, or finite-precision discretizations. The earliest verified public source date is the arXiv version date listed below; mathematical priority outside the inspected materials remains a literature limitation.

## References

1. A. Reusken, *On a maximum principle in discretization with spherical harmonics*, arXiv:2610.13540v1 (first public October 9, 2026), Sections 4--8; specifically Lemma 11, Remark 7.3 and Corollary 12. https://arxiv.org/html/2610.13540v1
2. A. Reusken, *Analysis of a Schwarz-Fourier domain decomposition method*, arXiv:2511.01616v1 (November 3, 2025), especially Sections 4--5. https://arxiv.org/html/2511.01616v1
3. NIST Digital Library of Mathematical Functions, Legendre generating functions and classical Bessel-function representations, https://dlmf.nist.gov/14 and https://dlmf.nist.gov/10 . The identities used here are also derived in the proof.
