# Sharp frequency feasibility and inverse fibers for stable Kottler circular geodesics

## Finding

**Theorem (exact frequency image, ambiguity fiber, and one-observable recovery).** In the positive-mass, positive-cosmological-constant Kottler family defined below, the coordinate-time azimuthal frequency \(\Omega\) and the infinitesimal radial epicyclic frequency \(\kappa\) of a strictly stable, equatorial, timelike circular geodesic are jointly realizable **if and only if** \(0<\kappa<\Omega\). Set
\[
\rho=\frac{\kappa^2}{\Omega^2},\qquad q=\frac{1-\rho}{6}.
\]
For each such observed pair, the **entire** family of compatible triples \((M,\Lambda,r)\) consists of exactly one triple for each \(x\in(0,q)\):
\[
 a(x)=\frac{3x(1-3x)}{4-\rho-15x},\quad
 r(x)=\frac{\sqrt{a(x)}}{\Omega},\quad
 M(x)=x r(x),\quad
 \Lambda(x)=\Omega^2\frac{1-\rho-6x}{1-3x}.
\]
All three functions are smooth; \(r\) and \(M\) increase strictly with \(x\), while \(\Lambda\) decreases strictly. Consequently the sharp, **unattained** bounds are
\[
0<r<\frac{\sqrt q}{\Omega},\qquad
0<M<\frac{q^{3/2}}{\Omega},\qquad
0<\Lambda<\Omega^2-\kappa^2.
\]
Every value in each of these three open intervals arises, and **knowledge of any one** of \(r\), \(M\), or \(\Lambda\), together with the frequency pair, determines the other two uniquely whenever that known value lies in its indicated interval. Frequencies alone leave a smooth one-dimensional continuum of physically distinct backgrounds.

In particular, when \(r\) is known, put \(a=\Omega^2r^2\) and \(b=\kappa^2r^2\). The exact necessary-and-sufficient data condition is
\[
0<a<\frac16,\qquad 0<b<a(1-6a).
\]
The unique reconstruction is
\[
 x=\frac{1+5a-\sqrt{1-6a+25a^2+4b}}6,\qquad
 M=rx,\qquad \Lambda=\frac{3(x-a)}{r^2}.
\]
For known \(\Lambda\), setting \(\lambda=\Lambda/\Omega^2\) gives the explicit parameter \(x=(1-\rho-\lambda)/(6-3\lambda)\). For known \(M\), the strictly increasing function \(M(x)\) above has a unique inverse on \((0,q)\).

## Assumptions and scope

Fix geometrized units \(G=c=1\). The exact four-dimensional Schwarzschild–de Sitter (Kottler) metric is
\[
 ds^2=-f(r)\,dt^2+f(r)^{-1}dr^2+r^2(d\theta^2+\sin^2\theta\,d\phi^2),\qquad
 f(r)=1-\frac{2M}{r}-\frac{\Lambda r^2}{3},
\]
where \(M>0\), \(\Lambda>0\), and \(r>0\). The time coordinate has precisely the displayed Kottler normalization; the theorem does **not** identify these frequencies with redshift-independent observations by a distant observer in de Sitter space. The particle is uncharged, spinless, and follows a future-directed timelike circular geodesic in the static region \(f(r)>0\). By strictly stable we mean a positive second radial variation of the standard geodesic effective potential, equivalent to \(\kappa^2>0\). Both \(\Omega=d\phi/dt>0\) (orientation fixed) and the infinitesimal radial oscillation frequency \(\kappa>0\) are measured in the same coordinate \(t\); vertical and eccentric-orbit frequencies are not additional data. All inequalities are strict: marginally stable orbits and boundary spacetimes \(M=0\), \(\Lambda=0\) are excluded.

## Proof

**1. Circular-geodesic and stability identities.** For angular momentum per unit test-particle mass \(L\), the radial effective potential is \(V(r)=f(r)[1+L^2/r^2]\). Solving \(V'(r)=0\) for the circular orbit yields, with \(x=M/r\) and \(y=\Lambda r^2/3\),
\[
 E^2=\frac{f(r)^2}{1-3x},\qquad
 L^2=\frac{r^2(x-y)}{1-3x}.
\]
Therefore a circular timelike orbit with nonzero angular frequency requires \(x<1/3\) and \(a=x-y>0\). Direct evaluation of \(f'(r)/(2r)\) and the coordinate-time second radial variation gives
\[
 \Omega^2=\frac Mr^3-\frac\Lambda3,\qquad
 \kappa^2=\frac Mr^3\left(1-\frac{6M}{r}\right)-\frac\Lambda3\left(4-\frac{15M}{r}\right),
\]
where the second identity may also be checked by
\[
 \kappa^2=\tfrac12\bigl[f f''-2(f')^2+3 f f'/r\bigr].
\]
Thus, writing \(a=\Omega^2r^2=x-y\) and \(b=\kappa^2r^2\),
\[
 b=x(1-6x)-y(4-15x)=9x^2-(15a+3)x+4a.\tag{1}
\]

**2. A necessary stable compactness bound.** Strict positivity \(b>0\) and \(0<y<x<1/3\) imply \(x<1/6\). Indeed, for \(1/6\le x\le4/15\) both terms in \(x(1-6x)-y(4-15x)\) are nonpositive. For \(4/15<x<1/3\), since \(4-15x<0\) and \(y<x\), one has \(b<x(1-6x)-x(4-15x)=x(9x-3)<0\), again impossible. Consequently \(0<a<x<1/6\) and \(f(r)=1-2x-y>1-3x>0\). Thus every tuple constructed below lies in the static region with positive circular-orbit energy and angular momentum.

**3. Complete frequency-only image and fiber.** Divide (1) by \(a>0\) and set \(b=\rho a\). Solving for \(a\) gives
\[
 a=\frac{3x(1-3x)}{4-\rho-15x}.\tag{2}
\]
Also \(y=x-a=x(1-\rho-6x)/(4-\rho-15x)\). Because \(0<x<1/6\) the denominator \(4-\rho-15x\) is strictly positive if \(0<\rho<1\). A stable orbit necessarily satisfies \(b<a(1-6a)<a\): for fixed \(a\), the right-hand side of (1) is strictly decreasing in \(x\in(a,1/6)\) since its derivative is \(18x-15a-3<0\), and its value at \(x=a\) equals \(a(1-6a)\). Hence \(0<\rho<1\). Conversely, given any \(\Omega>0\), \(0<\rho<1\), choose any \(x\in(0,q)\). The denominator in (2) is positive, \(a>0\), and \(0<y=x-a\) holds precisely because \(x<q\). Let \(r=\sqrt a/\Omega\), \(M=xr\), and \(\Lambda=3y/r^2\). Then \(f>0\), \(x<1/6\), and the forward formulas return exactly \(\Omega^2\) and \(\kappa^2=\rho\Omega^2\). Conversely all stable circular Kottler data produce this \(x\), so the parametrization is exhaustive and injective in \(x\).

**4. Monotone tradeoff and sharp endpoints.** Differentiating (2),
\[
 \frac{da}{dx}=\frac{3[(4-\rho)(1-6x)+45x^2]}{(4-\rho-15x)^2}>0.\tag{3}
\]
Hence \(r=\sqrt a/\Omega\) and \(M=xr\) increase strictly. Substitution of (2) into \(3(x-a)/r^2\) yields the stated \(\Lambda(x)\), whose derivative is
\[
 \frac{d\Lambda}{dx}=-\frac{3\Omega^2(1+\rho)}{(1-3x)^2}<0.\tag{4}
\]
At \(x\downarrow0\), \(r,M\downarrow0\) and \(\Lambda\uparrow\Omega^2(1-\rho)\). At \(x\uparrow q\), one has \(a\uparrow q\), \(r\uparrow\sqrt q/\Omega\), \(M\uparrow q^{3/2}/\Omega\), and \(\Lambda\downarrow0\). The endpoints are excluded by the positive-mass/positive-\(\Lambda\) assumptions; each intermediate value of each variable is attained exactly once. This also proves the one-additional-scalar identifiability assertions.

**5. Closed fixed-radius inversion.** At known \(r\), the constraints \(0<a<1/6\) and \(0<b<a(1-6a)\) are necessary by the decreasing right side of (1). They are sufficient: its value at \(x=a\) exceeds \(b\), whereas at \(x=1/6\) it equals \((6a-1)/4<0<b\); strict monotonicity supplies exactly one \(x\in(a,1/6)\). Solving the quadratic (1) gives the displayed lower root, and then \(M=rx>0\), \(\Lambda=3(x-a)/r^2>0\). The upper quadratic root is outside the stable physical interval. This completes the proof.

## Verification

The accompanying standalone script `verify_kottler.py` checks by exact symbolic differentiation the two forward frequency expressions and the independent radial effective-potential second-variation identity. With a fixed random seed, it then performs 4,700 parameterized numerical comparisons: 1,500 fixed-radius inverse cases, 1,000 known-mass inversions, 1,000 frequency-only reconstructions, and 1,200 tests of the explicit monotone parameter fiber and its bounds. The program prints `PASS` and all compared configurations obey positivity and strict stability. These experiments check implementation and algebra; the continuum theorem rests on the proof above, not on finite samples.

## Relationship to prior work

Stuchlík and Hledík (1999) characterize circular effective potentials and geometric properties of Schwarzschild–de Sitter backgrounds. Kunst, Perlick, and Lämmerzahl (2015) show that different eccentric bound orbits in a *fixed* Schwarzschild–de Sitter spacetime can share orbital frequencies, a different source of isofrequency nonuniqueness; their text also discusses varying the background parameters. Boshkayev, Luongo, and Muccino (2022, Eq. 13) give general **forward** coordinate-frequency expressions, including the Kottler specialization after reconciling their different normalization of the cosmological term. Thus forward frequencies, circular stability, and generic isofrequency phenomena are **not** claimed as new. The specific assessed statement is the exact positive-parameter image, exhaustive one-dimensional inverse fiber, three simultaneous sharp bounds, strict monotone mass–cosmological tradeoff, and uniqueness after fixing any one of three physical parameters. The cited forward formulas permit a subsequent algebraic derivation of this classification; that derivation and the complete inverse statement are supplied here. A direct equivalent in earlier specialized work cannot be ruled out definitively.

## Limitations

All results concern the ideal static Kottler metric, positive \(M\) and \(\Lambda\), a single strictly stable circular **timelike** orbit, and two frequencies defined relative to the displayed coordinate \(t\). There is no physical observer at spatial infinity in Schwarzschild–de Sitter space, so this mathematical coordinate-frequency identifiability should not be represented as direct astronomical mass/\(\Lambda\) inference without a specified observational redshift and clock calibration. Finite-precision statistical identifiability, eccentric motion, spin, nonzero charge, plasma effects, and noise are not treated. The full text of the 1999 foundational effective-potential article was not available for this comparison; historical priority remains a risk.

## References

1. Z. Stuchlík and S. Hledík, “Some properties of the Schwarzschild–de Sitter and Schwarzschild–anti-de Sitter spacetimes,” *Physical Review D* **60**, 044006 (first publicly published 1999-07-08), DOI: 10.1103/PhysRevD.60.044006.
2. D. Kunst, V. Perlick, and C. Lämmerzahl, “Isofrequency pairing of spinning particles in Schwarzschild-de Sitter spacetime,” arXiv:1505.05728v1 (first posted 2015-05-21).
3. K. Boshkayev, O. Luongo, and M. Muccino, “Numerical analysis of quasi-periodic oscillations with spherical spacetimes,” arXiv:2212.10186v1 (first posted 2022-12-20), especially Eq. (13); in that equation their coefficient of the metric \(r^2\) term is our \(\Lambda/3\).
