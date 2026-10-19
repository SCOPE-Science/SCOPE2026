# Golden-ratio period-four cutoff and three-attractor coexistence in a triangle projection map

## Finding

Consider the farthest-perpendicular-projection map of Everett [1] on the union of the **complete supporting lines** of the isosceles triangle with vertices \(A=(0,0)\), \(B=(1,0)\), and \(C=(1/2,v)\), where \(v>1/2\). At a point lying on exactly one supporting line, orthogonally project onto whichever of the two other supporting lines is **farther away**; equal perpendicular distances make the point fixed. At a vertex, project onto the opposite supporting line. These rules agree with the geometric map in [1].

Put
\[
\varphi=\frac{1+\sqrt5}{2},\qquad
v_4=\frac{\sqrt\varphi}{2}=\sqrt{\frac{1+\sqrt5}{8}},\qquad
v_3=\sqrt{\frac34+\frac{\sqrt3}{2}}.
\]
For every \(v>1/2\), the **complete numbers of distinct primitive periodic orbits of periods three and four** (counted modulo cyclic shifts, in the entire union of three complete lines) are
\[
N_3(v)=\begin{cases}2,&1/2<v<v_3,\\0,&v\ge v_3,\end{cases}
\qquad
N_4(v)=\begin{cases}1,&1/2<v<v_4,\\0,&v\ge v_4.\end{cases}
\]
In particular, throughout \(1/2<v<v_4\), **two distinct attracting three-cycles coexist with one attracting four-cycle**. No assertion is made that these are all attractors or all periodic orbits of other periods.

The unique four-cycle, where it exists, is the explicitly symmetric rectangle
\[
(x,0)\longmapsto(1-x,h)\longmapsto(1-x,0)
\longmapsto(x,h)\longmapsto(x,0),\qquad
D=v^2+\tfrac12,\quad x=\frac1{4D},\quad h=\frac{v}{2D}.
\]
Its multiplier in side arclength under the four-step return is \(1/(16(v^2+1/4)^2)\), strictly between zero and one. At \(v=v_4\), the two points on the equal legs simultaneously become perpendicular-distance ties and are therefore fixed instead of continuing the four-cycle. The two three-cycles have respective return multipliers equal to \(- (2s^2-1)/(8s^4)\), where \(s=\sqrt{v^2+1/4}\); their absolute values are less than one whenever they exist.

## Assumptions and scope

The domain is \(X=L_{AB}\cup L_{BC}\cup L_{CA}\) with the **full infinite lines**, not merely the triangle boundary. The triangle is acute because \(v>1/2\). A primitive \(n\)-cycle consists of \(n\) distinct points with least period \(n\). Periodic-orbit counts ignore cyclic choice of the starting point. Perpendicular distances determine the branch, not distances along the supporting lines. Ties are fixed points, not set-valued branches. All results are for real, exact Euclidean orthogonal projection.

## Proof

**1. Exhaustive short itineraries.** Orthogonal projection between two nonparallel lines contracts signed line distance by the absolute cosine of the angle between them. An alternating itinerary between only two lines therefore has as its unique even-return fixed point their intersection; at such a triangle vertex the actual map instead projects onto the opposite line, so this cannot give a primitive four-cycle. For an acute triangle, a projection of any point in the interior of one triangle edge to either other supporting line is in the interior of that edge. A vertex maps into the interior of the opposite edge, and subsequent nonfixed iterates remain in interiors. Thus no nonfixed periodic orbit passes through a vertex. Every genuine four-cycle consequently has a cyclic line itinerary \(i,j,i,k\), in which \(i,j,k\) are distinct. Up to cyclic shift there is exactly one such itinerary for each choice of repeated supporting line. Every genuine three-cycle visits all three lines, in one of the two orientations. For each of these fixed itineraries, the affine return is a strict contraction; hence it has at most one periodic-point candidate on the complete lines, even before the farthest-distance test.

**2. An exhaustive four-cycle branch lemma.** Take an arbitrary acute triangle with a proposed repeated side normalized to \(A=(0,0)\), \(B=(1,0)\), \(C=(u,w)\), where \(0<u<1\) and \(w^2>u(1-u)\). Let \(a=\sqrt{(1-u)^2+w^2}\), \(b=\sqrt{u^2+w^2}\), and \(D=u^2+(1-u)^2+w^2\). The prescribed affine projections in the line order \(AB\to BC\to AB\to CA\to AB\) give the unique return-fixed candidate
\[
P=\left(\frac{u^2}{D},0\right),\quad
Q=B+\frac{1-u}{D}(C-B),\quad
R=\left(\frac{b^2}{D},0\right),\quad
S=A+\frac{u}{D}(C-A).
\]
For completeness, if \(P=(x,0)\), the first projection has \(BC\)-fraction \((1-x)(1-u)/a^2\). The second has \(AB\)-coordinate \([w^2+(1-u)^2x]/a^2\). The two last projections return \(x=u^2[w^2+(1-u)^2x]/(a^2b^2)\). Since \(a^2b^2-u^2(1-u)^2=w^2D>0\), the displayed candidate follows uniquely.

The four chosen lines really are the **farthest-distance branches**, with strict inequalities, exactly when
\[
\begin{aligned}
 bD&>u^2(a+b),\\
 (1-u)(1+b)&>D,\\
 b(a+b)&>D,\\
 u(1+a)&>D.
\end{aligned}
\tag{1}
\]
Indeed these are respectively the tests at \(P,Q,R,S\), using the perpendicular-distance formulas on a triangle side and the sine rule. Each equality produces a fixed tie point, not the proposed itinerary. Thus (1) is a necessary and sufficient exact branch test.

**3. Repeated base and exclusion of both repeated legs.** For the isosceles triangle, \(u=1/2\), \(a=b=s=\sqrt{v^2+1/4}\), and \(D=v^2+1/2=s^2+1/4\). The first and third strict inequalities in (1) hold automatically for \(v>1/2\). The other two coincide and reduce to
\[
2D<1+s
\ \Longleftrightarrow\ 
4s^2-2s-1<0
\ \Longleftrightarrow\ 
s<\frac{1+\sqrt5}{4}=\frac\varphi2
\ \Longleftrightarrow\ \frac12<v<v_4.
\]
The base candidate then becomes exactly the four points in the Finding section, and all four have distinct locations in the triangle edges. At the upper endpoint both leg points are ties, so the upper inequality is strict.

To exclude a four-cycle with a repeated **leg**, renormalize that leg to unit length. Its third vertex then has normalized perpendicular-foot coordinate \(u'=1/(2s^2)\), height \(w'=v/s^2\), and the new opposite side length in the notation of the branch lemma is \(a'=1\). Its branch denominator is
\[
D'=(u')^2+(1-u')^2+(w')^2=1+\frac1{4s^4}.
\]
The fourth necessary strict test in (1) would say
\[
1+\frac1{4s^4}=D'<u'(1+a')=\frac1{s^2},
\]
which after multiplication by \(s^4>0\) is \((s^2-1/2)^2<0\), impossible. Reflection excludes the other repeated leg. Step 1 now proves the exact four-cycle census, including the absence of any exterior four-cycles on the complete lines.

**4. Three-cycle classification and coexistence.** Set \(m=1/(1+2s^2)\). In one cyclic orientation the unique affine three-step return candidate is
\[
(m,0)\longmapsto(1-m/2,mv)
\longmapsto(m,2mv)\longmapsto(m,0).
\]
Direct orthogonality verifies every displayed projection; uniqueness follows from strict contraction of the prescribed affine return. The farthest-distance test at the base point is \(m<1/2\), equivalent to \(s^2>1/2\). The test at the point on \(BC\) is \(m<1/(1+s)\), equivalent to \(s>1/2\). The final test at the point on \(CA\) is
\[
2m>\frac{1-2m}{s}
\ \Longleftrightarrow\ 
2s^2-2s-1<0
\ \Longleftrightarrow\ 
s<\frac{1+\sqrt3}{2}.
\]
For \(v>1/2\), the first two tests always pass, so this orientation exists precisely for \(v<v_3\). Reflection across the symmetry axis gives the other orientation and a distinct orbit; Step 1 excludes all others. The corresponding three-return derivative is \(-\cos^2(\angle A)\cos(\angle C)=-(2s^2-1)/(8s^4)\). The four-return derivative is \(\cos^4(\angle A)=1/(16s^4)\). Both are strictly contracting on the relevant branch neighborhoods, giving genuine local attraction of each cycle. As \(v_4<v_3\), the claimed three-attractor coexistence and the complete short-period census follow. \(\square\)

## Verification

An independent exact-rational implementation in `verify_cycles.py` constructs the three supporting lines, computes projections and squared perpendicular distances using rational arithmetic, enumerates all admissible length-three and length-four line itineraries, solves their affine return equations, and checks each candidate against the **actual farthest-branch rule**. Twelve rational triangle heights, including points on either side of the golden-ratio cutoff and the three-cycle cutoff, reproduce the theorem's respective counts. The full exact-rational verifier is included. These finite checks support the analytical, all-real-parameter proof above; they do not establish it by enumeration.

## Relationship to prior work

Everett's 2024 originating paper [1] defines this farthest-projection map, proves qualitative convergence statements, and plots isosceles-triangle periodic-orbit bifurcations. It does not state the exact golden-ratio four-cycle cutoff, the exhaustive three-line period-four itinerary reduction, or the simultaneous coexistence of two primitive three-cycles with a four-cycle. A published mathematical finding [2] gives an exact **period-three** orientation classification, including the isosceles three-cycle interval; that previously known classification is used here for comparison and independently reconstructed in Step 4, **not claimed as the novelty**. The distinct contribution is the exhaustive period-four theorem, exact sharp cutoff, and coexistence window. A separate previously recorded equilateral-triangle basin calculation concerns a different shape outside this window and does not imply the new cutoff. No conclusion about priority beyond the inspected sources is claimed.

## Limitations

This theorem makes no claim about periodic points of periods one, two, or at least five, nor about global attraction, basin measures, or what happens for nonacute or nonisosceles triangles. Near the cutoff, ties are **fixed** under the stated single-valued rule; other tie conventions can change boundary behavior. The originality comparison is conditional on accessible published material: the full hosted content of reference [2] could not be inspected through the available source, although its indexed claim was compared. Independent mathematical validation has not been performed.

## References

[1] Samuel Everett, *A Piecewise Contractive Map on Triangles*, arXiv:2408.16019v1 (first public version 2024-08-26), especially Definition 2.1 and Sections 3–4. https://arxiv.org/html/2408.16019v1

[2] *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published research record, 2026-10-11, identifier `2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`. Available indexed description establishes only its three-cycle scope.

