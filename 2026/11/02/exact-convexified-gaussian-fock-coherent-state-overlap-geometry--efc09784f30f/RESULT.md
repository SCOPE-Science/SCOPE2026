# Exact convexified Gaussian Fock coherent-state overlap geometry

## Finding

For the Gaussian Fock space with reproducing kernel \(K(z,w)=e^{z\overline w}\), let \(k_z\) denote the **normalized** kernel at \(z\), and fix a counterclockwise rotation \(0<\theta<\pi\). The set of coherent-state rotation overlaps is
\[
\mathcal S_\theta=\{\langle k_{e^{i\theta}z},k_z\rangle:z\in\mathbb C\}.
\]
Put \(a=\tan(\theta/2)>0\). Then \(\mathcal S_\theta=\{s_a(t):t\ge0\}\), where \(s_a(t)=e^{(-a+i)t}\). Let \(\mathcal K_a\) be the **closed convex hull** of \(\mathcal S_\theta\). There is a unique \(T_a\in(\pi,2\pi)\) satisfying
\[
e^{aT_a}(\cos T_a-a\sin T_a)=1.
\]
The entire boundary of \(\mathcal K_a\) is the **first spiral arc** \(s_a([0,T_a])\), together with the line segment joining \(s_a(T_a)\) to \(1\); this segment is tangent to the spiral at its nontrivial endpoint. In particular, the later windings of the spiral contribute no boundary points.

The area and perimeter have the following **exact one-variable formulas**:
\[
\operatorname{Area}(\mathcal K_a)=
\frac{1-e^{-2aT_a}}{4a}-\frac{e^{-aT_a}\sin T_a}{2},
\]
\[
\operatorname{Perimeter}(\mathcal K_a)=
\frac{\sqrt{1+a^2}}a(1-e^{-aT_a})+
\left|1-e^{(-a+i)T_a}\right|.
\]
The bodies are strictly nested: if \(0<a<b\), then \(\mathcal K_b\subsetneq\mathcal K_a\), and their areas satisfy
\[
\operatorname{Area}(\mathcal K_a)=\pi-2\pi^2a+O(a^{3/2})\quad(a\downarrow0),
\qquad
\operatorname{Area}(\mathcal K_a)=\frac1{4a}+O(e^{-\pi a}/a)\quad(a\to\infty).
\]
Their perimeters tend to \(2\pi\) and \(2\), respectively, as \(a\downarrow0\) and \(a\to\infty\).

For irrational \(\theta/(2\pi)\), the Fock rotation composition operator \(U_\theta f(z)=f(e^{i\theta}z)\) has \(\overline{W(U_\theta)}=\overline{\mathbb D}\), whereas its closed convexified Berezin range is exactly \(\mathcal K_a\). Thus the **area deficit** between the two convex sets is strictly positive and equals \(\pi-\operatorname{Area}(\mathcal K_a)\), including the small-angle law \(\pi-\operatorname{Area}(\mathcal K_a)=\pi^2\theta+O(\theta^{3/2})\) along irrational angles approaching zero.

## Assumptions and scope

The Fock Hilbert space consists of entire \(f(z)=\sum_{n\ge0}c_nz^n\) with \(\|f\|^2=\sum_{n\ge0}n!|c_n|^2\). The inner product is linear in the first entry. The normalized kernels are \(k_z(w)=e^{w\overline z-|z|^2/2}\). Angles in the main result obey \(0<\theta<\pi\), so \(a=\tan(\theta/2)>0\). The analogous lower-half-plane rotations are complex conjugates. The compact set \(\mathcal K_a\) includes the limiting spiral point \(0\), not attained by a finite parameter. Area means planar Lebesgue area; perimeter means ordinary convex-body boundary length. No claim is made for arbitrary affine composition symbols or non-Gaussian kernels.

## Proof

**1. Kernel identity and reduction.** The reproducing property gives
\[
\langle k_u,k_v\rangle
=\exp\!\left(u\overline v-\frac{|u|^2+|v|^2}{2}\right).
\]
Taking \(u=e^{i\theta}z\) and \(v=z\) yields \(\exp((e^{i\theta}-1)|z|^2)\). On writing \(t=(\sin\theta)|z|^2\), we have \((e^{i\theta}-1)|z|^2=(-a+i)t\), because \((1-\cos\theta)/\sin\theta=\tan(\theta/2)\). The ray \(t\ge0\) is obtained exactly, and \(s_a(t)\to0\) as \(t\to\infty\). The compact hull is therefore \(\operatorname{conv}(\{0\}\cup s_a([0,\infty)))\).

**2. Unique terminal contact.** Define \(F_a(t)=e^{at}(\cos t-a\sin t)\). Direct differentiation gives
\[
F_a'(t)=-(1+a^2)e^{at}\sin t.
\]
Thus \(F_a\) strictly decreases on \((0,\pi)\), strictly increases on \((\pi,2\pi)\), satisfies \(F_a(0)=1\), \(F_a(\pi)<1\), and \(F_a(2\pi)=e^{2\pi a}>1\). There is exactly one \(T_a\in(\pi,2\pi)\) such that \(F_a(T_a)=1\). The chord \(1-s_a(T_a)\) is a real positive multiple of the terminal tangent \(s_a'(T_a)=(-a+i)s_a(T_a)\): indeed their cross product vanishes exactly when \(F_a(T_a)=1\), and the positive orientation follows from continuity and \(\pi<T_a<2\pi\).

**3. Global support analysis.** For a unit outward normal \(e^{i\alpha}\), its support function is
\[
h_a(\alpha)=\max_{t\ge0}e^{-at}\cos(t-\alpha).
\]
Any noninitial positive local maximum occurs at \(t=\alpha-\arctan a+2\pi j\); the first such \(t=t_0\in[0,2\pi)\) dominates every later one, whose values decrease by the factor \(e^{-2\pi a}\). At this first positive local maximum,
\[
e^{-at_0}\cos(t_0-\alpha)=\frac{e^{-at_0}}{\sqrt{1+a^2}},
\qquad
\cos\alpha=\frac{\cos t_0-a\sin t_0}{\sqrt{1+a^2}}.
\]
Consequently the supporting maximum lies at \(s_a(t_0)\) precisely when \(F_a(t_0)\le1\); otherwise the initial point \(1\) wins. By step 2, for \(0<t_0<2\pi\) this is equivalent to \(t_0\le T_a\), with equality yielding a supporting line touching both endpoints of the straight chord. The support directions expose every \(s_a(t)\), \(0<t<T_a\), and no later spiral point. The union of these exposed points, the chord, and the initial point is exactly the boundary of their convex hull. Since the spiral winds through arbitrarily small representatives of every direction, the origin is inside the hull; no additional boundary component appears.

**4. Exact area and perimeter.** Orient the boundary from \(1\) along the spiral to \(s_a(T_a)\), then return along the chord. Green's formula \(A=\tfrac12\Im\oint\overline z\,dz\) gives \(\tfrac12\int_0^{T_a}e^{-2at}\,dt\) along the spiral and \(-\tfrac12\Im s_a(T_a)\) along the closing chord. These are exactly the two displayed area terms. The spiral speed is \(\sqrt{1+a^2}e^{-at}\), yielding the displayed length, and the chord contributes \(|1-s_a(T_a)|\).

**5. Strict nesting.** If \(0<a<b\), then at every \(t\ge0\),
\[
s_b(t)=e^{-(b-a)t}s_a(t),
\]
which belongs to the segment joining \(0\) to \(s_a(t)\) and hence to \(\mathcal K_a\). Therefore \(\mathcal K_b\subseteq\mathcal K_a\). Every exposed point \(s_a(t)\) with \(0<t<T_a\) is the **unique** maximizer of its linear supporting functional over \(\mathcal K_a\). At \(t=0\) the shrinkage is zero, but its supporting functional is strictly lower than at \(t\); at every \(t>0\), the shrinkage is strict and moves the point into the interior side of that supporting line. Compactness of \(s_b([0,\infty))\cup\{0\}\) makes the inequality uniformly strict. Thus this exposed point is missing from \(\mathcal K_b\), proving proper inclusion, strict area decrease, and positivity of the area deficit.

**6. Endpoint asymptotics.** As \(a\downarrow0\), write \(T_a=2\pi-\delta\). Taking logarithms of the terminal equation gives
\[
0=a(2\pi-\delta)+\log(\cos\delta+a\sin\delta)
=2\pi a-\frac{\delta^2}{2}+O(a\delta^3+\delta^4),
\]
with the linear terms in \(a\delta\) canceling. Hence \(\delta=2\sqrt{\pi a}+O(a^{3/2})\). Substitution in the area and perimeter formulas gives \(A=\pi-2\pi^2a+O(a^{3/2})\) and \(P\to2\pi\). At the opposite endpoint define \(t_0=\pi+\arctan(1/a)\), the unique zero of \(\cos t-a\sin t\) in \((\pi,2\pi)\). The terminal equation and mean value theorem yield \(T_a=t_0+O(e^{-\pi a}/a)\). Inserting this estimate into the exact formulas gives \(A=1/(4a)+O(e^{-\pi a}/a)\) and \(P\to2\).

**7. Numerical-range comparison.** The orthonormal Fock basis \(z^n/\sqrt{n!}\) diagonalizes \(U_\theta\) with eigenvalues \(e^{in\theta}\). When \(\theta/(2\pi)\) is irrational, these eigenvalues are dense on the unit circle. Their closed convex hull is the closed unit disk, while the coherent-state diagonal values coincide with \(\mathcal S_\theta\). Strict nesting and the small-angle expansion prove the asserted gap and its coefficient, because \(a=\tan(\theta/2)=\theta/2+O(\theta^3)\).

## Verification

The independent, dependency-free `CHECK.py` reproduces the terminal root by bisection, compares the Green formula with dense polygonal quadrature, tests tangency and exposed-support inequalities against sampled later spiral windings, and checks monotonicity and both limiting area laws. Its sample computations are supplementary, not an exhaustive proof; steps 1–7 establish the universal statements for all indicated real parameters.

## Relationship to prior work

Augustine, Garayev and Shankar (arXiv:2401.03176, first posted January 6, 2024), Section 2, derive the Gaussian Fock Berezin symbol \(e^{(\zeta-1)|z|^2}\) for linear symbols and classify convexity of the original (unconvexified) Berezin set; their Theorem 2.2 and Corollary 2.3 do not give the sharp convex-hull terminal contact, exact area/perimeter, strict inclusion law or small-angle numerical-range gap derived here. Clos, Pentzien and Rodriguez (arXiv:2609.10361, publicly posted September 9, 2026) investigate the analogous convexity question for Bergman-space operators induced by unit-ball automorphisms, a different class of kernels and domains. The new quantitative geometry concerns normalized Fock coherent-state overlaps, with the rotation composition operator as a direct consequence.

## Limitations

The hull geometry is restricted to plane Gaussian Fock coherent states and rotations; an affine symbol or higher-dimensional anisotropic rotation need not give the same single-spiral support. The statement treats ordinary closed convex hulls, not all spectral or pseudospectral notions. The full text of arXiv:2609.10361 was unavailable during the comparison, so possible ancillary discussion of Fock overlaps remains an originality risk; independent mathematical validation has not occurred. Classical exact formulas for convex hulls of logarithmic spirals could also give an equivalent formulation, and a failed literature search alone does not exclude them.

## References

1. A. Augustine, M. Garayev, P. Shankar, *On the convexity of the Berezin range of composition operators and related questions*, arXiv:2401.03176 (first public version January 6, 2024), especially Section 2, Theorem 2.2 and Corollary 2.3. https://arxiv.org/abs/2401.03176
2. T. G. Clos, T. C. Pentzien, T. M. Rodriguez, *Convexity of the Berezin range of composition operators induced by automorphisms of the Unit Ball in \(\mathbb C^n\)*, arXiv:2609.10361 (first public version September 9, 2026). https://arxiv.org/abs/2609.10361
3. B. J. Carswell, B. D. MacCluer, A. Schuster, *Composition operators on the Fock space*, Acta Sci. Math. (Szeged) **69** (2003), 871–887 (boundedness of Fock composition operators).
