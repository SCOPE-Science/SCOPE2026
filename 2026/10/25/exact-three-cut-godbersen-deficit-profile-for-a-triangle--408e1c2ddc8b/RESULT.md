# Exact three-cut Godbersen deficit profile for a triangle

## Finding

Let \(T=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\). For cut depths \(a,b,c\ge0\) satisfying \(a+b<1\), \(a+c<1\), and \(b+c<1\), define
\[
K_{a,b,c}=T\cap\{(x,y):x+y\ge a,\ x\le1-b,\ y\le1-c\}.
\]
Set \(q=a^2+b^2+c^2\), \(s=a+b+c\), and assume \(0<q<1/2\). This range guarantees that every pair of vertex cuts is disjoint for every admissible triple with the given \(q\). The removed fraction of the triangle's area is exactly \(q\).

With planar mixed area normalized by
\[
\operatorname{area}(K+tL)=\operatorname{area}(K)+2tV_2(K,L)+t^2\operatorname{area}(L),
\]
the exact formulas are
\[
\operatorname{area}(K_{a,b,c})=\frac{1-q}{2},\qquad
V_2(K_{a,b,c},-K_{a,b,c})=1-s+ab+ac+bc.
\]
Consequently, the normalized Godbersen deficit
\[
\Delta(a,b,c)=1-\frac{V_2(K_{a,b,c},-K_{a,b,c})}{2\operatorname{area}(K_{a,b,c})}
=\frac{2s-s^2-q}{2(1-q)}
\]
has the following complete fixed-area extremal profile:
\[
\min_{a^2+b^2+c^2=q}\Delta(a,b,c)=\frac{\sqrt q}{1+\sqrt q},
\]
with equality exactly when one of \(a,b,c\) is \(\sqrt q\) and the other two are zero, and
\[
\max_{a^2+b^2+c^2=q}\Delta(a,b,c)=
\begin{cases}
\dfrac{\sqrt{3q}-2q}{1-q},&0<q\le\tfrac13,\\[4pt]
\tfrac12,&\tfrac13\le q<\tfrac12.
\end{cases}
\]
For \(q\le1/3\), the maximum is attained exactly at \(a=b=c=\sqrt{q/3}\). For \(q>1/3\), it is attained exactly when \(a+b+c=1\). The maximum therefore becomes a constant plateau of \(1/2\) after the transition at \(q=1/3\).

## Assumptions and scope

The cuts are parallel to the three sides of the reference triangle, one at each vertex. The nonnegative depths are indexed so that \(a\) cuts the origin vertex, \(b\) cuts \((1,0)\), and \(c\) cuts \((0,1)\). The inequalities \(a+b<1\), \(a+c<1\), and \(b+c<1\) ensure that the three removed corner triangles have disjoint interiors. If \(q<1/2\), then \((a+b)^2\le2q<1\), and similarly for the other pairs, so this condition holds automatically.

The result is restricted to this explicitly parameterized family and the nonoverlapping-cut regime \(0<q<1/2\). It is not a stability theorem for arbitrary convex bodies and makes no assertion about profiles after vertex cuts meet. The mixed-area convention is stated explicitly because factors of two differ between conventions.

## Proof

The reference triangle has area \(1/2\). The removed corner triangles are similar to it with linear scale factors \(a\), \(b\), and \(c\), so their areas are \(a^2/2\), \(b^2/2\), and \(c^2/2\). Their interiors are disjoint. Hence
\[
2\operatorname{area}(K_{a,b,c})=1-a^2-b^2-c^2=1-q.
\]

For polygons, the mixed-area formula is
\[
V_2(K,L)=\frac12\sum_F \ell(F)h_L(n_F),
\]
where the sum runs over edges \(F\) of \(K\), \(\ell(F)\) is edge length, \(n_F\) is the outward unit normal, and \(h_L(u)=\max_{z\in L}\langle z,u\rangle\) is the support function. The six possible edges of \(K_{a,b,c}\), their lengths, and their support values for \(-K_{a,b,c}\) are

| Edge | Length | \(h_{-K}(n_F)\) |
|---|---:|---:|
| \(y=0\) | \(1-a-b\) | \(1-c\) |
| \(x=1-b\) | \(b\) | \(0\) |
| \(x+y=1\) | \(\sqrt2(1-b-c)\) | \(-a/\sqrt2\) |
| \(y=1-c\) | \(c\) | \(0\) |
| \(x=0\) | \(1-a-c\) | \(1-b\) |
| \(x+y=a\) | \(\sqrt2a\) | \(1/\sqrt2\) |

Substitution gives
\[
\begin{aligned}
2V_2(K,-K)={}&(1-a-b)(1-c)-a(1-b-c)\\
&+(1-a-c)(1-b)+a,
\end{aligned}
\]
which expands to \(2(1-a-b-c+ab+ac+bc)\). This proves the mixed-area formula. Since
\[
ab+ac+bc=\frac{s^2-q}{2},
\]
substitution into the normalized deficit yields
\[
\Delta=\frac{s-s^2/2-q/2}{1-q}=\frac{2s-s^2-q}{2(1-q)}.
\]

At fixed \(q\), nonnegative triples with \(a^2+b^2+c^2=q\) have \(\sqrt q\le s\le\sqrt{3q}\), with the lower endpoint attained exactly by a one-cut profile and the upper endpoint exactly by equal cuts. Every intermediate value of \(s\) occurs by continuity on the positive-octant part of the sphere. As a function of \(s\), the deficit is concave and
\[
\frac{d\Delta}{ds}=\frac{1-s}{1-q}.
\]
Thus its maximum occurs at \(s=\sqrt{3q}\) when \(q\le1/3\), and at \(s=1\) when \(q>1/3\); the latter level is feasible for every \(q\in(1/3,1/2)\). The endpoint deficits satisfy
\[
\Delta(\sqrt{3q})-\Delta(\sqrt q)=\frac{(\sqrt3-1)\sqrt q-q}{1-q}>0,
\]
because \(q<1/2<(\sqrt3-1)^2\). Therefore the minimum is always at the one-cut endpoint. Evaluating the endpoint and the stationary level \(s=1\) gives the stated formulas and equality cases.

## Verification

The area formula follows from disjoint similar corner triangles. The mixed-area identity was independently reconstructed from the six edge lengths and the support-function values in the table; no numerical fit is used. The optimization reduces exactly to the scalar variable \(s\) at fixed \(q\), with the derivative, endpoint comparison, and feasibility range given above. The regime restriction \(q<1/2\) is used to guarantee pairwise disjoint cuts and the stated six-edge description.

## Relationship to prior work

Fryš, Kotrbatý, Mouamine, and Wang prove the general Godbersen mixed-volume inequality and characterize its equality cases by simplices; they also prove a higher-order extension. Those results provide the governing deficit but do not state this fixed-area profile for a triangle cut at all three vertices. A close published-finding corpus record gives the exact Godbersen profile for a simplex truncated at one vertex; it covers the one-cut boundary case, not the interior three-cut family. Another published-finding corpus record gives a reflected mixed-area formula for convex quadrilaterals; it does not cover the generic hexagons in this family. The present claim is only the exact multi-cut family formula and its fixed-area extremizer classification, not a new proof of the general Godbersen inequality.

## Limitations

The parameter range excludes intersecting cuts, and the theorem does not classify the family after two cut lines meet. The calculation is two-dimensional and does not extend the formula to higher-dimensional simplices. The closest published-finding corpus records were available as search-result summaries, but their direct record pages were not accessible for full-text inspection; broader unpublished or poorly indexed multi-cut formulas therefore remain a residual originality risk.

## References

1. F. Fryš, J. Kotrbatý, M. A. Mouamine, and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1 (first public date 2026-10-05), especially Theorems 1.2, 1.4, 1.5, and 1.8.
2. published-finding corpus record `2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949`, *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*.
3. published-finding corpus record `2026/10/11/SCOPE-the-maximal-triangle-formula-for-reflected-mixed-area-of-convex--ad85c8e58a4d`, *The maximal-triangle formula for reflected mixed area of convex quadrilaterals*.
