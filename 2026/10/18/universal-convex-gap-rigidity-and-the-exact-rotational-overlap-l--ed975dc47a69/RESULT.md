# Universal convex-gap rigidity and the exact rotational overlap law of unequal regular tangential polygons

## Finding
Fix integers \(3\le n<m\), a real inradius \(r>0\), and two regular polygons \(P_n,P_m\) centered at the origin, each tangent to the circle of radius \(r\). Normalize the outward side normals of \(P_m\) to arguments \(2\pi j/m\), and rotate \(P_n\) through \(\theta\). Write
\[
d=\gcd(n,m),\quad q=n/d,\quad h=\frac{2\pi d}{nm},\quad b=\frac{2\pi}{m}=qh,
\]
and let \(t\in[0,h)\) represent \(-\theta\pmod h\). Extend expressions continuously to \(t=h\), identifying this with \(t=0\).

**Universal gap law.** Let \(f:[0,b]\to\mathbb R\) be continuous and convex with \(f(0)=0\). Define \(E_f(\theta)\) as the sum of \(f(g)\) over the consecutive positive angular gaps \(g\) between the distinct outer normals of the intersection \(P_m\cap R_\theta P_n\). Then
\[
\boxed{E_f(t)=(m-n)f(b)+d\sum_{k=1}^{q}\left[f(kh-t)+f((q-k)h+t)\right].}\tag{1}
\]
Every convex \(f\) obeys \(E_f(h/2)\le E_f(t)\le E_f(0)=E_f(h)\). For strictly convex \(f\), equality on the left occurs precisely at \(t=h/2\pmod h\), and equality on the right precisely at \(t=0\pmod h\). The intersection has exactly \(n+m\) sides except at common-normal orientations, when it has \(n+m-d\) sides.

**Exact overlap law and sharp orientation classification.** The area \(A(\theta)=\operatorname{area}(P_m\cap R_\theta P_n)\) is obtained by putting \(f(x)=\tan(x/2)\) in (1) and multiplying by \(r^2\). Consequently it has the unique minimum and maximum orientation classes just stated, with values
\[
\boxed{\begin{aligned}
A_{\max}/r^2&=(m-n+d)\tan(\pi/m)+2d\sum_{k=1}^{q-1}\tan(kh/2),\\
A_{\min}/r^2&=(m-n)\tan(\pi/m)+2d\sum_{k=0}^{q-1}\tan((k+1/2)h/2).
\end{aligned}}\tag{2}
\]
For uniformly random relative orientation \(\Theta\), the *exact mean* is
\[
\boxed{\mathbb EA(\Theta)=r^2\left[(m-n)\tan\frac{\pi}{m}-\frac{2nm}{\pi}\log\cos\frac{\pi}{m}\right].}\tag{3}
\]
In particular, the mean has no dependence on \(\gcd(n,m)\), whereas the extrema do.

The complete area distribution is determined by (1) without numerical integration. For \(A_{\min}<y<A_{\max}\), there is exactly one \(t_y\in(0,h/2)\) satisfying \(A(t_y)=y\), and
\[
\boxed{\mathbb P\{A(\Theta)\le y\}=1-\frac{2t_y}{h}.}\tag{4}
\]
Its cumulative distribution is zero below \(A_{\min}\) and one above \(A_{\max}\); both endpoints have probability zero. Writing \(\kappa=A''(h/2)>0\), its lower-end asymptotic is
\[
\mathbb P\{A(\Theta)\le A_{\min}+\varepsilon\}
\sim\frac2h\sqrt{\frac{2\varepsilon}{\kappa}},\qquad
\kappa=r^2d\sum_{k=1}^{q}\sec^2\!\left(\frac{(k-1/2)h}{2}\right)
\tan\!\left(\frac{(k-1/2)h}{2}\right).\tag{5}
\]
The area law has a finite upper-end density \(4/[hdr^2\tan^2(\pi/m)]\).

For each fixed \(n\), as \(m\to\infty\) through any integers larger than \(n\), the oscillation has the **sharp arithmetic asymptotic**
\[
\boxed{A_{\max}-A_{\min}
=\frac{\pi^3r^2\gcd(n,m)^2}{4nm^3}+O_n(r^2m^{-5}).}\tag{6}
\]
The constant is uniform over all values of \(\gcd(n,m)\) dividing fixed \(n\).

## Assumptions and scope
The polygons are closed, convex, regular, centered at the origin, and have exactly the same incircle; no translation or rescaling is permitted after setup. Side normals refer to unit outward normals to the polygon edges. Their intersection always contains the incircle and is circumscribed about it. We require strictly unequal side orders \(3\le n<m\); the equal-order rotation problem is not claimed here. The relative angle is uniform under Haar measure on planar rotations when probabilities are discussed. The shape of any convex \(f\) is arbitrary within the stated interval, but the gap energy counts only distinct normals; the normalization \(f(0)=0\) handles coincident normals. A strictly convex \(f\) gives unique phase classes even when it is not increasing. The asymptotic holds for fixed \(n\), not jointly growing orders. The density at its boundary is understood one-sidedly, and (4) is an exact implicit distribution rather than an assertion of an elementary closed-form inverse for every polygon pair.

## Proof
**1. Gaps in the union of two normal grids.** The \(m\) side normals of the fine grid are spaced by \(b=2\pi/m\); the \(n\) side normals of the coarse grid are spaced by \(2\pi/n>b\). Hence any open fine-grid gap contains at most one coarse-grid normal. As \(i\) ranges from \(0\) to \(n-1\), the residues of \(\theta+2\pi i/n\) modulo \(b\) form \(q=n/\gcd(n,m)\) equally spaced residues, each occurring \(d\) times. Choosing the phase \(t\equiv-\theta\pmod h\), they may be represented by \(kh-t\) for \(1\le k\le q\). Thus \(n\) of the fine-grid gaps split into the two subgaps \(kh-t\) and \(b-kh+t=(q-k)h+t\). The remaining \(m-n\) fine gaps retain length \(b\). At \(t=0\) or \(h\), duplicated normals simply introduce zero-length subgaps. Since \(f(0)=0\), summing proves (1) everywhere, including collisions.

**2. Universal extremizers.** On \([0,h]\), each summand \(f(kh-t)+f((q-k)h+t)\) is convex in \(t\), so their sum is convex. The substitution \(k\mapsto q+1-k\), combined with exchange of paired terms, shows \(E_f(h-t)=E_f(t)\). A convex symmetric function is smallest at its symmetry center and no larger than its equal-valued endpoints anywhere inside. If \(f\) is strictly convex, its composition with any nonconstant affine argument is strictly convex, so \(E_f\) is strictly convex; the minimum and endpoint maximum are then unique modulo the period. Every distinct supporting normal gives a genuine edge: at the tangency point \(ru\) of its line, the other distinct normal constraints are strictly slack, since \(ru\cdot v=r(u\cdot v)<r\). Exactly \(d\) normals coincide at \(t=0\pmod h\), so the number of edges is respectively \(n+m-d\) or \(n+m\).

**3. Tangential area identity.** If two consecutive tangent normals have gap \(g\in(0,\pi)\), their common vertex has tangent length \(r\tan(g/2)\) along either line from its contact point. Summing over polygon vertices gives half the perimeter \(r\sum\tan(g/2)\), and multiplying by inradius gives area \(r^2\sum\tan(g/2)\). Our gaps are at most \(b\le\pi/2\), so the tangent formula is finite and strictly convex in the gap length on \([0,b]\): \(d^2\tan(g/2)/dg^2=\frac12\sec^2(g/2)\tan(g/2)>0\) for \(g>0\). Thus the strict classes and formulas (2) follow by substituting \(t=0,h/2\) into (1).

**4. Haar mean and full distribution.** Uniform angle \(\Theta\) induces uniform \(t\) on \([0,h]\). Averaging (1) and integrating each affine argument separately yields for every continuous \(f\)
\[
\frac1h\int_0^hE_f(t)\,dt
=(m-n)f(b)+\frac{2d}{h}\int_0^b f(x)\,dx.
\tag{7}
\]
The integral of \(\tan(x/2)\) is \(-2\log\cos(x/2)\), and \(2d/h=nm/\pi\), giving (3). Strict convexity and symmetry imply that \(A(t)\) decreases strictly from its maximum on \([0,h/2]\) and increases strictly thereafter. The set of phases yielding area no greater than \(y\) therefore has length \(h-2t_y\), proving (4). Differentiating (1) twice at \(h/2\), with the mirrored terms paired, proves the expression for \(\kappa\) in (5). Taylor's theorem gives \(A(t)=A_{\min}+(\kappa/2)(t-h/2)^2+o((t-h/2)^2)\), hence the square-root CDF asymptotic. The one-sided derivative at an aligned phase telescopes:
\[
A'(0+)=\frac{dr^2}{2}\sum_{k=1}^q
\left[\sec^2\!\left(\frac{(q-k)h}{2}\right)-\sec^2\!\left(\frac{kh}{2}\right)\right]
=-\frac{dr^2}{2}\tan^2(\pi/m).
\]
Since the density is \(2/[h|A'(t_y)|]\) on the interior, its upper-end value is as stated.

**5. Arithmetic size of the rotational effect.** Keep \(n\) fixed as \(m\to\infty\). Then \(q=n/d\le n\) and \(b=qh=2\pi/m\). The expansion \(\tan(z/2)=z/2+z^3/24+O(z^5)\), uniformly for \(0\le z\le b\), may be substituted into (2). The linear terms cancel, while the cubic sum obeys the exact identity
\[
q^3+2\sum_{k=1}^{q-1}k^3-2\sum_{k=0}^{q-1}(k+1/2)^3
=\frac{3q^2}{4}.
\]
For example, the identity follows directly from \(\sum_{k=1}^{q-1}k^3=q^2(q-1)^2/4\) and \(\sum_{k=0}^{q-1}(k+1/2)^3=q^4/4-q^2/8\). Therefore \(A_{\max}-A_{\min}=r^2d\,h^3q^2/32+O_n(r^2 h^5)\). Substituting \(h=2\pi d/(nm)\), \(q=n/d\), and \(d\le n\) gives (6) with a uniform remainder. The proof covers all positive integers in the stated domain, not only tested instances.

## Verification
Run `python3 verify.py` (Python standard library) to reproduce the independent finite tests. Its geometric polygon-clipping implementation starts from the literal coarse polygon and applies all fine polygon tangent halfplanes, computes the resulting area by the shoelace formula, and compares it to the trigonometric expression for a range of distinct orders and orientations. It also constructs the two normal lattices directly and compares four nonlinear gap energies with (1); applies numerical Simpson quadrature to (3); and checks the first asymptotic term for five different coprimality patterns. The run returned `VERIFY_OK 5780 finite_energy_clip_mean_and_asymptotic_checks`. Finite diagnostics cannot establish the universal claims; Steps 1–5 are the proof. For \(n=3,m=4,r=1\), direct calculation gives \(A_{\min}\approx3.6263860958789023\), \(A_{\max}\approx3.6905989232414966\), and \(\mathbb EA\approx3.6476272018318188\).

## Relationship to prior work
Buck and Siddon derive the area of general polygons tangent to a circle from tangent lengths; the inradius-times-semiperimeter principle and its elementary geometric proof are prior mathematics, not claimed as new here. Mathar considers two concentric regular polygons of *unequal orders* but optimizes the size of an outer polygon constrained to contain the inner one; his angular residue analysis is structurally relevant but does not give an equal-inradius intersection's universal convex-gap extremizers, exact rotational area law, mean, or distribution. Kiss and Vidnyánszky study unions of congruent regular polygons and their perimeter-to-area relationships, again a different object and optimization. O'Rourke and Zaimi analyze side counts of intersections of rotated regular polygons under *equal circumradii*, a different normalization; those edge counts do not imply the equal-inradius area results here.

Related published treatments of expected intersections of independent random rotations of *congruent* tangential polygons, and of radial unions of congruent regular polygons, supply valuable closest comparisons. Their equal-order/congruent-copy hypotheses and objectives do not cover the strict unequal-order \(n<m\) joint normal lattice, its universal convex-gap order for every convex score, or the \(d^2m^{-3}\) anisotropy law. A separate exact result for the rotational area of Minkowski **sums** of regular polygons is not a statement about the intersection of these equal-inradius bodies; neither formula or extremizers imply the others through the basic sum/intersection identities without additional polar information.

## Limitations
The statement is restricted to concentric Euclidean regular polygons with a common inscribed circle and strictly unequal side orders. It does not optimize over translations, shapes, or independently varying side-normal positions. The full area CDF is given via a unique one-variable inverse, not a universal expression using elementary inverse functions. The fixed-order asymptotic does not permit both side orders to grow arbitrarily. Although several directly relevant primary texts and mathematical records were compared, unindexed or inaccessible historical literature might contain equivalent formulas; the provenance of priority is therefore not independently certified. No independent mathematical audit has been performed.

## References
1. Marshall W. Buck and Robert L. Siddon, *The Area of a Polygon with an Inscribed Circle*, arXiv:1203.3438v1 (first public 2012-03-15). https://arxiv.org/abs/1203.3438
2. Richard J. Mathar, *Tightly Circumscribed Regular Polygons*, arXiv:1301.6293v1 (first public 2013-01-26), especially Sections I–III. https://arxiv.org/html/1301.6293v1
3. Viktor Kiss and Zoltán Vidnyánszky, *Unions of regular polygons with large perimeter-to-area ratio*, arXiv:1402.5452v1 (first public 2014-02-21). https://arxiv.org/html/1402.5452v2
4. Joseph O'Rourke and Gjergji Zaimi, *Intersection of rotating regular polygons*, MathOverflow question and answer, 2015-10-17. https://mathoverflow.net/questions/221120/intersection-of-rotating-regular-polygons
5. *Sharp random-rotation area order and exponential shape memory for tangential polygons*, published mathematical research note (2026-10-11), publicly indexed by title.
6. *Universal radial coverage by concentric regular-polygon unions*, published mathematical research note (2026-10-11), publicly indexed by title.
