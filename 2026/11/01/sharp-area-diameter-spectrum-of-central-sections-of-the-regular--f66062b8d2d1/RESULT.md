# Sharp area–diameter spectrum of central sections of the regular octahedron

## Finding

Let \(O=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\) be the unit regular octahedron. For a plane \(H\) through the origin let \(A(H)=\operatorname{area}_2(O\cap H)\) and \(D(H)=\operatorname{diam}_2(O\cap H)\), with intrinsic Euclidean measurements. The complete set of attainable pairs \((D(H),A(H))\) is determined by the following exact envelopes.

For each \(0<q<1\), define
\[
 d(q)=\frac{2\sqrt{1+q^2}}{1+q},\qquad
 B(q,t)=\frac{2\sqrt{1+q^2+t^2}(qt+q+t)}{(q+t)(1+q)(1+t)},
\]
\[
 T(q)=\frac{(1-q)^2(1+q)+\sqrt{(1-q)^4(1+q)^2+4(q^2+q+1)q(2q^2-q+2)}}{2(q^2+q+1)}.
\]
Then \(q<T(q)<1\). A plane \(H\) has diameter \(d(q)\) if and only if, up to coordinate signs, permutation and normalization, an equation for its normal has the form \((q,t,1)\) with \(q\le t\le1\). Its possible section areas comprise **exactly the closed interval**
\[
 \boxed{B(q,T(q))\ \le\ A(H)\ \le\ \frac{(q+2)\sqrt{2q^2+1}}{(1+q)^2}.}
\]
The lower equality case consists precisely of normals with ordered absolute coordinates proportional to \((q,T(q),1)\); hence it has three distinct absolute coordinates. The upper equality case consists precisely of normals proportional to \((q,q,1)\). At the diameter endpoints, the area ranges are \(A\in[\sqrt2,2]\) for \(D=2\), and the singleton \(A=3\sqrt3/4\) for \(D=\sqrt2\). At \(D=2\), the lower endpoint comes from normals proportional to \((0,1,1)\), the upper from \((0,0,1)\); at \(D=\sqrt2\) normals are proportional to \((1,1,1)\). Every intermediate area at fixed diameter occurs.

Equivalently for each given \(D\in[\sqrt2,2]\), put \(r=D/2\) and
\[
 q=\frac{1-r^2}{r^2+\sqrt{2r^2-1}}.
\]
The formulas above specify the complete sharp area interval at that diameter, interpreting the two limiting cases separately. The nontrivial part is the **interior, asymmetric area minimizer**, in contrast to the two-equal-coordinate area maximizer.

## Assumptions and scope

The octahedron has vertices \(\pm e_1,\pm e_2,\pm e_3\). Plane diameters and areas use the induced Euclidean metric, and all planes are *central* (linear). The extremizers are classified only up to the octahedron's orthogonal symmetry group and normal sign. No probabilistic statement, affine-invariant extremum, arbitrary-polytope statement or higher-dimensional section claim is made. The known diameter formula is recalled as an ingredient, not asserted as a new result.

## Proof

**1. Normal chamber and polygon vertices.** Fix \(H=u^\perp\), and order the absolute coordinates of \(u\) as \(0\le a\le b\le c\) with \(c>0\). Signed coordinate permutations do not change \(A\) or \(D\). Set \(q=a/c\), \(t=b/c\), and scale the normal to \((q,t,1)\); thus \(0\le q\le t\le1\). For \(q,t>0\), the section is the centrally symmetric hexagon with cyclically ordered vertices
\[
 v_{12}=\frac{(t,-q,0)}{q+t},\quad
 v_{13}=\frac{(1,0,-q)}{1+q},\quad
 v_{23}=\frac{(0,1,-t)}{1+t},\quad
 -v_{12},-v_{13},-v_{23}.
\]
These are obtained by intersecting the six edges joining positive and negative coordinate vertices with \(H\). Degenerate cases follow from direct sections or continuous limits.

The oriented area vector of this centrally symmetric polygon equals
\[
 w=v_{12}\times v_{13}+v_{13}\times v_{23}+v_{12}\times v_{23}.
\]
Its Euclidean norm is \(A(H)\). Substitution and collection of terms give
\[
 w=\frac{2(qt+q+t)}{(q+t)(1+q)(1+t)}(q,t,1),
\]
so
\[
 \boxed{A(H)=B(q,t).}
\]
For the diameter, the maximum Euclidean radius is attained at a section vertex. Of the three opposite vertex pairs the largest radius comes from the most unequal normal-coordinate pair \((q,1)\), since the scalar function \(\sqrt{1+s^2}/(1+s)\) decreases on \([0,1]\). Therefore
\[
 \boxed{D(H)=\frac{2\sqrt{1+q^2}}{1+q}.}
\]
This deterministic diameter identity is also present in the previously published octahedron-section diameter law cited below.

**2. Exact constrained derivative and critical point.** Fix \(0<q<1\), so only \(t\in[q,1]\) varies when the diameter is fixed. Squaring the area gives
\[
 B(q,t)^2=\frac{4(1+q^2+t^2)(qt+q+t)^2}{(q+t)^2(1+q)^2(1+t)^2}.
\]
Direct differentiation and clearing positive denominators yields the exact identity
\[
 \frac{\partial B(q,t)^2}{\partial t}
 =-\frac{8t(qt+q+t)}{(1+q)^2(q+t)^3(1+t)^3}\,P_q(t),
\]
where
\[
 P_q(t)=-(q^2+q+1)t^2+(1-q)^2(1+q)t+q(2q^2-q+2).
\]
Its leading coefficient is strictly negative, its constant term is positive, and therefore it has exactly one positive root. Moreover
\[
 P_q(q)=3q(1-q)>0,\qquad P_q(1)=-3q^2(1-q)<0.
\]
Consequently that positive root lies strictly between \(q\) and \(1\), is exactly \(T(q)\), and \(B(q,t)\) decreases strictly up to \(T(q)\) then increases strictly thereafter. Thus the lower sharp endpoint is \(B(q,T(q))\), with its asserted unique normal-orbit equality case.

**3. Upper endpoint and rigidity.** The maximum must be one of the endpoints \(t=q\) or \(t=1\), with
\[
 B(q,q)^2=\frac{(q+2)^2(2q^2+1)}{(1+q)^4},\qquad
 B(q,1)^2=\frac{(2q+1)^2(q^2+2)}{(1+q)^4}.
\]
The exact positive gap
\[
 B(q,q)^2-B(q,1)^2=\frac{2(1-q)^3}{(1+q)^3}>0
\]
selects \(t=q\) uniquely. Strict monotonicity away from \(T(q)\) gives complete equality classification. Continuity of \(t\mapsto B(q,t)\) on the connected interval gives every intermediate area.

**4. Boundaries and inversion.** For \(q=0\) and \(0<t\le1\), the same geometric calculation gives \(B(0,t)=2\sqrt{1+t^2}/(1+t)\), strictly decreasing in \(t\in(0,1)\); the limiting \(t=0\) normal is a coordinate axis and the area is \(2\). At \(t=1\) its area is \(\sqrt2\). For \(q=1\), ordering forces \(t=1\), and the area is \(3\sqrt3/4\). The diameter is strictly decreasing as \(q\) rises from \(0\) to \(1\), with range \([\sqrt2,2]\). Solving its displayed equation for \(q\) yields the inversion formula in the finding. This proves every assertion. \(\square\)

## Verification

The accompanying `verify.py` uses exact symbolic coefficient identities (SymPy), fraction arithmetic, and a distinct geometric algorithm that enumerates all intersecting octahedron edges and computes the ordered planar polygon area without using the closed formula. The script checks derivative and endpoint identities, exact area and diameter for rational normals, strict critical-point placement, sampled sharp intervals, and numerical diameter inversion. It reports `VERIFY_OK` followed by its count of successful assertions. Run `python3 -m pip install -r requirements.txt` and then `python3 verify.py`. Finite numerical experiments do **not** prove the continuum theorem; the polygon decomposition and analytic sign argument above do.

## Relationship to prior work

Guédon, Litvak, Tatarko and Vritsiou (2026) study probabilistic bounds on diameters of random sections and provide the recent motivating setting. The more directly overlapping published octahedron-diameter result listed below already determines \(D(H)\) from the two extreme absolute normal coordinates and its complete Haar law. **Neither the area conditioned on a fixed diameter nor its sharp extremal orientations follow from that marginal law alone.** The present new assertion is the complete conditional area spectrum and its rigid asymmetric minimizer; the known diameter formula is explicitly reused.

Brazitikos and Pandis (2026) study a different *facet-barycenter* constraint for cross-polytope sections, not fixed Euclidean diameter. The log-concavity theorem of Nayar and Tkocz (2018/2020) concerns volumes along diagonal body dilations, not the present exact two-invariant feasible set. Related work on projections of the octahedron concerns areas of **orthogonal shadows** rather than central sections. A previously established inradius law for central octahedron sections concerns a different statistic and does not determine area at a fixed diameter.

Searches for equivalent fixed-radius/circumradius formulations, broader section-volume inequalities, cross-polytope area–diameter tables, and public mathematical records identified no theorem covering the displayed conditional envelopes. This search is not a proof of historical uniqueness. A relevant recent random-diameter manuscript and an additional cross-polytope section manuscript were retrievable as abstracts, but their full texts could not be obtained during comparison; this is a residual priority risk rather than evidence of absence.

## Limitations

The result is planar and specific to **central** sections of the regular octahedron. It does not determine a joint probability density under random plane orientations, establish arbitrary-section isodiametric inequalities, or generalize to higher cross-polytopes. The normal-to-diameter formula is already known. The sharp two-invariant area classification has analytic proof here but historical priority remains provisional, especially in older cross-section and polyhedral-stereology literature. Independent validation has not been performed.

## References

1. O. Guédon, A. E. Litvak, K. Tatarko, and B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131v1, first posted 2026-09-21, https://arxiv.org/abs/2609.24131 (abstract and publication metadata accessed; full text inaccessible during comparison).
2. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163v1, posted 2026-06-05, https://arxiv.org/abs/2606.07163 (abstract and freely accessible mathematical summaries checked; full primary text unavailable).
3. P. Nayar and T. Tkocz, *On a convexity property of sections of the cross-polytope*, arXiv:1810.02038, first posted 2018-10-04; Proc. Amer. Math. Soc. 148 (2020), 1271–1278, DOI:10.1090/proc/14777 (abstract and publisher bibliographic description checked).
4. *Exact Haar diameter law for central sections of the regular octahedron*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-diameter-law-for-central-sections-of-the-regular-octa--4948185eba2f (full `RESULT.md` inspected for mathematical implication comparison).
