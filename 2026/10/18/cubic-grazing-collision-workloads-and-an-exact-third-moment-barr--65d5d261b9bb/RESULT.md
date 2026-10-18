# Cubic grazing-collision workloads and an exact third-moment barrier in ball billiards

## Finding
Let \(d\ge2\), \(R>0\), and \(h>0\). Start a free, specularly reflected particle in the Euclidean ball \(B_R^d\) from a position uniform in the ball, with an independent, isotropically directed velocity whose speed \(V\ge0\) satisfies \(0<\mathbb E V^3<\infty\). Let \(N_h\) count its boundary reflections during the time interval \((0,h]\). Write \(v_d=\pi^{d/2}/\Gamma(1+d/2)\) for the unit \(d\)-ball volume and \(s_{d-2}=(d-1)v_{d-1}\) for the area of the unit \((d-2)\)-sphere, with \(s_0=2\).

For every fixed integer \(k\ge2\), the probability of at least \(k\) reflections has the sharp small-step law
\[
\lim_{h\downarrow0}\frac{\mathbb P(N_h\ge k)}{h^3}
=\frac{s_{d-2}\,\mathbb EV^3}{24v_dR^3}\,
\frac{2k-1}{k^2(k-1)^2}.
\]
For every fixed positive step \(h\), the full collision-count distribution has the sharp heavy tail
\[
\boxed{\lim_{k\to\infty}k^3\mathbb P(N_h\ge k)
=\frac{s_{d-2}}{12v_d}\frac{h^3\mathbb EV^3}{R^3}>0.}
\]
Therefore \(N_h\) is finite almost surely, but \(\mathbb EN_h^p<\infty\) **exactly for** \(0<p<3\); every moment of order \(p\ge3\) diverges. The expected number of reflections beyond the first nevertheless has the sharp finite small-step law
\[
\lim_{h\downarrow0}\frac{\mathbb E(N_h-1)_+}{h^3}
=\frac{s_{d-2}\,\mathbb EV^3}{24v_dR^3}.
\]

In three dimensions the underlying deterministic-speed probability has an additional exact, nonasymptotic identity: for any \(k\ge2\) and travel distance \(0\le L\le2R(k-1)\),
\[
\mathbb P(N_h\ge k\mid hV=L)
=\frac{2k-1}{16k^2(k-1)^2}\left(\frac LR\right)^3.
\]
This conditional identity assumes a uniform starting position and independent uniform velocity direction, as above.

In a **planar** disk with independent Gaussian velocity components of variance \(\sigma^2>0\), writing \(\eta=\sigma h/R\) specializes the two sharp laws to
\[
\mathbb P(N_h\ge k)\sim
\frac{2k-1}{4\sqrt{2\pi}\,k^2(k-1)^2}\,\eta^3\quad(h\downarrow0),
\qquad
\mathbb P(N_h\ge k)\sim\frac{\eta^3}{2\sqrt{2\pi}\,k^3}\quad(k\to\infty).
\]
In particular, \(\mathbb P(N_h\ge2)\sim3\eta^3/(16\sqrt{2\pi})\) and \(\mathbb E(N_h-1)_+\sim\eta^3/(4\sqrt{2\pi})\) as \(h\downarrow0\).

## Assumptions and scope
The reflection law reverses only the velocity component normal to the boundary; speed is constant between reflections. Initial position has normalized Lebesgue measure in the ball. Velocity direction is independent and uniform on the sphere, and speed is independent of position and direction. The collision count includes every genuine specular boundary encounter, without rejecting or truncating recursions. Boundary starts and exactly tangent initial states have probability zero. The third-moment assumption is on the **initial speed**; no random acceleration acts during this isolated free-flight reflection substep. The positive-step moment assertion requires \(h>0\) and \(\mathbb EV^3>0\).

## Proof
**1. Constant chord and exact event measure.** Fix a velocity direction. Decompose a starting point into a longitudinal coordinate and a perpendicular displacement \(y\in\mathbb R^{d-1}\). Put \(b=\lVert y\rVert\) and \(\ell=2\sqrt{R^2-b^2}\). For each fixed \(y\), the longitudinal coordinate is uniform over a segment of length \(\ell\). The first wall is at a distance \(u\) uniform on \((0,\ell)\) along that segment. Normal reflection on a sphere preserves the distance of every successive chord from the center: the trajectory remains in its initial two-plane and the impact-angle magnitude is preserved. All successive full chords have length \(\ell\). Consequently the \(k\)-th encounter occurs after the traveled distance \(u+(k-1)\ell\), for every integer \(k\ge1\), almost surely.

For a fixed travel distance \(L\ge0\), define
\[
c_k(L,\ell)=\min\{\ell,\max\{0,L-(k-1)\ell\}\}.
\]
Since the starting position is uniform in volume, integrating the admissible longitudinal length gives the **exact** conditional probability for \(k\ge2\):
\[
F_{k,d}(L):=\mathbb P(N_h\ge k\mid hV=L)
=\frac1{v_dR^d}\int_{\lVert y\rVert<R}
 c_k(L,2\sqrt{R^2-\lVert y\rVert^2})\,dy.
\]
Radial integration in the \((d-1)\)-dimensional transverse space gives
\[
\boxed{F_{k,d}(L)=\frac{s_{d-2}}{4v_dR^d}
\int_0^{2R}\ell\bigl(R^2-\ell^2/4\bigr)^{(d-3)/2}
 c_k(L,\ell)\,d\ell.}\tag{1}
\]
For \(d=2\), the integrable upper-endpoint singularity is interpreted as an ordinary improper integral; the small-distance arguments below have support bounded away from that endpoint.

**2. The universal cubic coefficient.** If \(k\ge2\), the integrand in (1) vanishes unless \(\ell<L/(k-1)\). Splitting at \(\ell=L/k\) gives the exact elementary identity
\[
\int_0^\infty\ell c_k(L,\ell)\,d\ell
=\int_0^{L/k}\ell^2\,d\ell
+\int_{L/k}^{L/(k-1)}\ell\bigl(L-(k-1)\ell\bigr)\,d\ell
=\frac{L^3(2k-1)}{6k^2(k-1)^2}.\tag{2}
\]
For each fixed \(k\ge2\), the factor \((R^2-\ell^2/4)^{(d-3)/2}\) equals \(R^{d-3}(1+O_{d,k}(L^2/R^2))\) uniformly over the nonzero support as \(L\downarrow0\). Hence
\[
F_{k,d}(L)=\frac{s_{d-2}}{24v_dR^3}
\frac{2k-1}{k^2(k-1)^2}L^3(1+O_{d,k}(L^2/R^2)).\tag{3}
\]
The same calculation applies for fixed \(L>0\) as \(k\to\infty\), because the support then contracts to zero. Formula (2) gives
\[
\lim_{k\to\infty}k^3 F_{k,d}(L)
=\frac{s_{d-2}}{12v_dR^3}L^3.\tag{4}
\]
For \(d=3\), the exponent \((d-3)/2\) in (1) is zero. Thus (2) is **exactly**, rather than asymptotically, applicable whenever \(L/(k-1)\le2R\). Substituting \(s_1=2\pi\) and \(v_3=4\pi/3\) proves the stated three-dimensional formula.

**3. Passing to random speed and summing counts.** There exists a finite constant \(C_d\), depending only on \(d\), such that for every \(k\ge2\) and \(L\ge0\),
\[
0\le F_{k,d}(L)\le C_d\left(\frac{L}{R(k-1)}\right)^3.\tag{5}
\]
To see this, if \(L\ge R(k-1)\), use \(F_{k,d}(L)\le1\). Otherwise the integral's support lies in \(\ell<R\), where the radial prefactor in (1) is bounded by a dimension-dependent multiple of \(\ell/R^3\); identity (2) then supplies (5). Because \(\mathbb EV^3<\infty\), this bound justifies dominated convergence in (3) with \(L=hV\) after division by \(h^3\), and in (4) after multiplication by \(k^3\). Both displayed probability limits follow.

The positive heavy-tail coefficient implies that \(\mathbb P(N_h=\infty)=0\), and, for each \(p>0\), the tail-sum identity
\[
\mathbb EN_h^p=\sum_{k\ge1}
\bigl(k^p-(k-1)^p\bigr)\mathbb P(N_h\ge k)
\]
converges exactly for \(p<3\), because its summands are asymptotic to a positive constant times \(k^{p-4}\). Also \(\mathbb E(N_h-1)_+=\sum_{k\ge2}\mathbb P(N_h\ge k)\); (5) bounds the scaled summands by a summable multiple of \((k-1)^{-3}\). Therefore the termwise small-step limit is legitimate. Finally,
\[
\frac{2k-1}{k^2(k-1)^2}=
\frac1{(k-1)^2}-\frac1{k^2},\qquad
\sum_{k=2}^\infty\frac{2k-1}{k^2(k-1)^2}=1,
\]
which proves the expected-extra-reflections coefficient.

**4. Gaussian specialization and a flat-boundary contrast.** In a planar disk with velocity components distributed as independent \(N(0,\sigma^2)\), speed is Rayleigh with \(\mathbb EV^3=3\sqrt{2\pi}\sigma^3/2\). Substituting this third moment into the preceding formulas gives the stated constants. For reproducibility, the **exact** planar multi-reflection probability is the one-dimensional integral obtained from (1) by inserting the Rayleigh speed survival probability:
\[
\mathbb P(N_h\ge k)=\frac1{\pi R^2}
\int_0^{2R}\frac{\ell}{2\sqrt{R^2-\ell^2/4}}
\int_0^\ell
\exp\!\left[-\frac{(u+(k-1)\ell)^2}{2\sigma^2h^2}\right]du\,d\ell.\tag{6}
\]

For contrast, in an **interval** of length \(W>0\), with uniform starting position and scalar Gaussian velocity \(N(0,\sigma^2)\), the exact \(k\ge2\) tail is
\[
\mathbb P(N_h\ge k)=\frac1W\int_0^W
\operatorname{erfc}\!\left(\frac{(k-1)W+u}{\sqrt2\sigma h}\right)du.
\]
Gaussian-tail Laplace asymptotics at \(u=0\) yield, for fixed \(k\ge2\) as \(h\downarrow0\),
\[
\mathbb P(N_h\ge k)\sim
\frac{\sqrt{2/\pi}\,\sigma^3h^3}{(k-1)^2W^3}
\exp\!\left[-\frac{(k-1)^2W^2}{2\sigma^2h^2}\right].
\]
All moments of the interval count are finite, since \(N_h\le1+h|V|/W\) up to the harmless integer-rounding convention. This displays the change from a Gaussian rare-event mechanism at flat boundaries to a cubic grazing mechanism in balls of every dimension \(d\ge2\).

## Verification
The accompanying standard-library `verify.py` evaluates the exact conditional ball integral in dimensions \(2,3,4,7\) independently of the asymptotic coefficient, checks the exact three-dimensional cubic specialization, evaluates the Gaussian planar integral, tests high-count tail constants, and checks the one-dimensional Gaussian contrast. Exact rational telescoping identities are also checked on finite ranges. The complete proof above, not these numerical samples, establishes the limits, moment cutoff, and all-dimensional quantifiers.

## Relationship to prior work
Leimkuhler, Sharma and Tretyakov develop collision-aware integrators for confined Langevin dynamics and discuss multi-collision recursion and the option of rejecting a step when more than one reflection occurs. Their accessible discussion and empirical examples motivate quantifying the cost of this exact collision substep. The geometric billiard reflection law, constant chord in a circle, and invariant phase-volume measure are classical; Bunimovich and Dettmann use these ingredients in a different problem concerning escape through holes in a circular billiard. The contribution here is the full fixed-step collision-count tail, its sharp all-dimensional coefficient and third-moment threshold, and the finite-step work expectation. Neither ordinary finite-time weak accuracy nor circular open-hole escape probabilities imply the stated collision-workload moment theorem without an additional count-distribution analysis.

## Limitations
This is a theorem about **one free-flight/specular-collision substep** started from a uniform configuration distribution and independent isotropic velocity; forces, friction, and noise are absent *inside that substep*. It is not a proof that a complete Langevin integration algorithm has an infinite third moment of its total running time, nor does it quantify practical wall-clock time. The explicit flat interval comparison assumes Gaussian velocity. The cubic coefficient can change for starting measures concentrated near the boundary, anisotropic correlations, non-spherical boundaries, altered reflection laws, or collision-count caps. Publication-priority completeness has not been independently established.

## References
1. B. Leimkuhler, A. Sharma, M. V. Tretyakov, *Numerical integrators for confined Langevin dynamics*, arXiv:2404.16584, originally submitted 2024-04-25. https://arxiv.org/abs/2404.16584 . In particular, the multi-collision discussion in Section 3.4 and Algorithm 3.1.
2. L. A. Bunimovich, C. P. Dettmann, *A Billiard in an Open Circle and the Riemann Zeta Function*, *Experimental Mathematics*, doi:10.1080/10586458.2024.2423180, first online 2024-11-18. https://doi.org/10.1080/10586458.2024.2423180 . Its circular billiard setup supplies the classical fixed-chord and invariant-measure context; its main results concern open-hole survival rather than fixed-time collision workload.
