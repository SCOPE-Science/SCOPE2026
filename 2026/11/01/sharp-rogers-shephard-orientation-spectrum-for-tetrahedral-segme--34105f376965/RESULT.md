# Sharp Rogers–Shephard orientation spectrum for tetrahedral segment extrusions

## Finding

Let \(S\subset\mathbb R^3\) be any nondegenerate tetrahedron, and let \(v\ne0\) and \(t>0\). Form the Minkowski extrusion \(K=S+t[0,v]\) and define its **relative volume inflation** \(q=\operatorname{vol}_3(K)/\operatorname{vol}_3(S)-1>0\). At each fixed \(q\), with the tetrahedron fixed and the direction and segment length allowed to vary while preserving \(q\), the entire attainable Rogers–Shephard difference-body spectrum is exactly

\[
\boxed{\frac{20+8q}{1+q}\ \leq\ \frac{\operatorname{vol}_3(K-K)}{\operatorname{vol}_3(K)}\ \leq\ \frac{20+12q}{1+q}.}
\]

Both bounds are attained for every \(q>0\), and every value between them is attained. In terms of the usual three-dimensional mixed volume, equivalently the complete attainable normalized Godbersen spectrum is

\[
\boxed{\frac{3+q}{1+q}\ \leq\ \frac{V_3(K,K,-K)}{\operatorname{vol}_3(K)}\ \leq\ \frac{3+5q/3}{1+q}.}
\]

The lower equality in both displayed inequalities holds precisely when the extrusion direction joins the midpoints of two opposite edges of the tetrahedron (up to nonzero scalar). The upper equality holds precisely when, among the four nonzero or zero directional derivatives of the tetrahedron's barycentric coordinates, at most one is positive or at most one is negative; zero derivatives are permitted. In particular, every direction parallel to a tetrahedron edge attains the upper endpoint. The equality configurations and the full interval are invariant under nonsingular affine maps.

More explicitly, in affine coordinates where \(S=\operatorname{conv}\{0,e_1,e_2,e_3\}\), set

\[
w_0=-(v_1+v_2+v_3),\qquad w_i=v_i\ (1\le i\le3),\qquad
T=\frac12\sum_{i=0}^3|w_i|,\qquad H=\sum_{i=1}^3|w_0+w_i|.
\]

Then \(q=3tT\), \(T\le H\le 2T\), and the **exact direction-resolved identity** is

\[
\boxed{\frac{\operatorname{vol}_3(K-K)}{\operatorname{vol}_3(K)}=\frac{20+4q(1+H/T)}{1+q}.}
\]

Thus the sharp directional variation of the normalized Godbersen deficit \(3-V_3(K,K,-K)/\operatorname{vol}_3(K)\) is the interval

\[
\left[\frac{4q}{3(1+q)},\ \frac{2q}{1+q}\right].
\]

## Assumptions and scope

All bodies are full-dimensional compact convex subsets of \(\mathbb R^3\). The volume is three-dimensional Lebesgue measure. A segment \([0,v]\) contains \(sv\) for \(0\le s\le1\). The difference body is \(K-K=K+(-K)\), while \(V_3\) is the symmetric, Minkowski-multilinear mixed volume normalized by \(V_3(K,K,K)=\operatorname{vol}_3(K)\). The tetrahedron and nonzero extrusion direction are arbitrary, and \(t\) ranges over positive reals. The volume inflation \(q\), rather than Euclidean segment length, is the natural affine-invariant fixed parameter. Tetrahedral barycentric derivatives sum to zero and do not depend on the choice of affine coordinates. The original unextruded tetrahedron \(t=0\) recovers the classical ratio \(20\) and the normalized Godbersen value \(3\), independent of direction.

## Proof

**Affine reduction.** Ratios of volumes and the normalized mixed volume are preserved by invertible affine maps. Send the four vertices to \(0,e_1,e_2,e_3\). Along a displacement by \(v\), the derivatives of the four barycentric coordinates are exactly \(w_0=-\sum_{i=1}^3v_i\) and \(w_i=v_i\).

**The two-sided simplex.** For \(a,b>0\), let \(B_{a,b}=aS+b(-S)\). Writing \(x_i^+=\max(x_i,0)\) and \(x_i^-=\max(-x_i,0)\), there is an exact description

\[
B_{a,b}=\left\{x:\sum_{i=1}^3x_i^+\le a,\ \sum_{i=1}^3x_i^-\le b\right\}.
\]

In the orthant with exactly \(j\) positive coordinates its volume is \(a^j b^{3-j}/(j!(3-j)!)\). Summing the eight orthants gives

\[
\operatorname{vol}_3(B_{a,b})=\frac{a^3+9a^2b+9ab^2+b^3}{6}.
\]

**All directional projections.** For each nonempty \(J\subset\{1,2,3\}\), let \(j=|J|\). The supporting facet of \(B_{a,b}\) with outer normal \(\mathbf1_J/\sqrt j\) consists of a positive \((j-1)\)-simplex with coordinate sum \(a\), crossed with a negative \((3-j)\)-simplex of coordinate sum at most \(b\). Its Euclidean area is

\[
\frac{\sqrt j\,a^{j-1}b^{3-j}}{(j-1)!(3-j)!}.
\]

The opposite-normal facet has the same expression with \(a,b\) swapped. All fourteen facet normals are accounted for, including the two complete-index facets. Cauchy's elementary facet projection formula therefore yields, for the volume increase per unit segment length parameter,

\[
\begin{aligned}
G_v(a,b)&=\operatorname{vol}_2(P_{v^\perp}B_{a,b})\,\|v\|_2\\
&=\frac12\sum_{\emptyset\ne J\subset\{1,2,3\}}
\frac{a^{j-1}b^{3-j}+b^{j-1}a^{3-j}}{(j-1)!(3-j)!}
\left|\sum_{i\in J}v_i\right|\\
&=\frac T2(a^2+b^2)+Hab.
\end{aligned}
\]

The last identity uses the fact that the three two-index sums have absolute values \(|w_0+w_i|\). The segment extrusion identity

\[
\operatorname{vol}_3(C+s[0,v])=\operatorname{vol}_3(C)+s\|v\|_2\operatorname{vol}_2(P_{v^\perp}C)
\]

holds for every convex body \(C\) and \(s\ge0\) by slicing parallel to \(v\). Hence the preceding formula extends continuously to \(a=0\) or \(b=0\), and

\[
\operatorname{vol}_3(S+t[0,v])=\frac16+\frac{tT}{2}=\frac{1+3tT}{6}.
\]

Since \(K-K=(S-S)+t[-v,v]\), and \([-v,v]\) is a translate of \(2[0,v]\), the central formula is

\[
\operatorname{vol}_3(K-K)=\frac{10}{3}+2tG_v(1,1)
=\frac{10}{3}+2t(T+H).
\]

Dividing the last two displayed volume identities proves the direction-resolved ratio with \(q=3tT\). Reflection invariance of mixed volume in dimension three gives

\[
\operatorname{vol}_3(K-K)=2\operatorname{vol}_3(K)+6V_3(K,K,-K),
\]

which yields the normalized Godbersen formula as well.

**Sharp range of direction anisotropy.** Consider the zero-sum quadruple \(w_0,w_1,w_2,w_3\). The quantity \(H\) is invariant under permutations: its three summands correspond to the three partitions of four indices into two pairs, and complementary pairs have opposite sums. If the nonzero coordinates have a \(3+1\) sign split (possibly with zeros), direct addition of their pair sums gives \(H=2T\). If there are two strictly positive coordinates \(a,b\) and two strictly negative coordinates \(-c,-d\), where \(a+b=c+d=T\), permutation invariance gives

\[
H=T+|a-c|+|a-d|.
\]

For \(a,c,d\in(0,T)\) with \(c+d=T\), convexity of \(x\mapsto|x-c|+|x-d|\) on \([0,T]\) shows \(0\le |a-c|+|a-d|<T\). Its minimum is zero precisely when \(a=c=d=T/2\), also forcing \(b=T/2\). Thus \(T\le H\le2T\), the lower equality holds precisely for two positive and two negative entries of equal absolute magnitude, and the upper equality precisely for the stated one-versus-rest sign configurations, allowing zeros.

The lower equality velocities \((s,s,-s,-s)\), up to permutation and scaling, are exactly the directions joining midpoints of opposite tetrahedral edges. To see the entire interval is realized, use the continuous zero-sum family

\[
(w_0,w_1,w_2,w_3)=(1,1,-u,-(2-u)),\qquad0\le u\le1.
\]

It has \(T=2\) and \(H/T=2-u\), so after setting \(t=q/(3T)\), every value between the bounds is attained for every fixed \(q>0\). Both sharp bounds and both equality classifications follow.

## Verification

The included `verify.py` independently constructs the convex hull of the eight translated/untranslated tetrahedron vertices, the hull of all differences of those vertices, and for general \(a,b>0\) the hull of \(aS+b(-S)+s[0,v]\). It compares their three-dimensional polytope volumes with the exact formulas, separately checking rational algebra and endpoint orientations. Execute `python verify.py` after installing `requirements.txt`. The checked run passed 486 comparisons on exact-rational sample parameters and independent numerical convex hull volumes. The proof above, not these finitely many computations, supplies the universal quantifiers and equality analysis.

## Relationship to prior work

The Rogers–Shephard inequality, and the later resolved Godbersen inequalities, give the universal upper bounds \(\operatorname{vol}_3(K-K)/\operatorname{vol}_3(K)\le20\) and \(V_3(K,K,-K)/\operatorname{vol}_3(K)\le3\), with simplex equality. The October 2026 works of Fryš–Kotrbatý–Mouamine–Wang and Friedland–Putterman–Szusterman characterize equality for every full-dimensional convex body and prove higher-order statements. The present calculation gives a different kind of information: the **complete two-sided, direction-sensitive spectrum at an exact positive relative volume increase**, for the canonical tetrahedral segment-extrusion family. It does not strengthen their universal inequality or reprove their equality classification. Brandenberg–González Merino–Grundbacher study strong stability near simplices in Banach–Mazur and Minkowski asymmetry parameters; their abstract does not specify this exact directional fixed-volume spectrum.

## Limitations

The theorem is specific to three-dimensional tetrahedra plus one segment; it does not classify arbitrary Minkowski perturbations, sums with several nonparallel segments, or higher-dimensional simplices. Fixed relative volume increase is not a general Banach–Mazur distance constraint. The historical-priority search does not rule out older convex-geometric or polyhedral formulas in unindexed sources. No independent mathematical audit has been performed.

## References

1. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik **8** (1957), 220–233.
2. F. Fryš, J. Kotrbatý, M. A. Mouamine, and S. Wang, *Higher-Order Godbersen Inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v2, originally posted 2026-10-05, https://arxiv.org/abs/2610.06806 .
3. O. Friedland, E. Putterman, and M. Szusterman, *The equality case in Godbersen's inequality and its generalizations*, arXiv:2610.04527v2, originally posted 2026-10-03, https://arxiv.org/abs/2610.04527 .
4. R. Brandenberg, B. González Merino, and F. Grundbacher, *Tight Stability Estimates Near the Simplex and Improved Bounds for the Diameter of the Banach-Mazur Compactum in Fixed Dimensions*, arXiv:2607.27041v1, 2026-07-29, https://arxiv.org/abs/2607.27041 .
