# Sharp two-piece equal-area fatness of an equilateral triangle

## Finding

Let \(T\) be any nondegenerate equilateral triangle and let \(T=K_1\cup K_2\) be a partition into two closed convex bodies of equal positive area and disjoint interiors. Write \(r(K)\) for the radius of a largest Euclidean disk contained in \(K\), and \(R(K)\) for the radius of a smallest Euclidean disk containing \(K\). Then

\[
\min_{i=1,2}\frac{r(K_i)}{R(K_i)}\le\frac{\sqrt3-1}{2}.
\]

Equality holds if and only if the common cutting segment is a median of \(T\). Hence the maximum possible worst-piece fatness is exactly \((\sqrt3-1)/2\); precisely three geometric cuts realize it, one per median.

## Assumptions and scope

The parts are compact, full-dimensional, Euclidean convex subsets of the same given equilateral triangle, whose intersection consists of the shared boundary cut. Disconnected or curved interfaces cannot arise: the interiors of two convex sets are disjoint, so a separating line exists; since their union is convex, the common interface is the chord of the triangle on that line. The statement allows cuts through an original vertex. The ratio uses smallest *enclosing* Euclidean disks, not an arbitrary circumscribed circle and not the circumcircle of a quadrilateral. Scaling the original triangle preserves the objective.

## Proof

Normalize the side length to \(1\), and put \(A=(0,\sqrt3/2)\), \(B=(-1/2,0)\), and \(C=(1/2,0)\). Every nontrivial chord joins two sides of \(T\); relabel the original vertices so these are \(AB\) and \(AC\). Write its endpoints as

\[
P=A+t(B-A),\qquad Q=A+u(C-A),\qquad 0<t,u\le1.
\]

The apex triangle \(APQ\) occupies fraction \(tu\) of \(T\), hence equal areas force \(tu=1/2\). Reflect across the altitude through \(A\) if necessary to obtain \(t\ge u\). Thus

\[
\frac1{\sqrt2}\le t\le1,\qquad u=\frac1{2t}.
\]

Focus on the *other* piece \(K=\operatorname{conv}\{B,C,P,Q\}\), a triangle at the endpoint \(t=1\) and a quadrilateral otherwise. It contains \(BC\), so its smallest enclosing disk must have \(R(K)\ge1/2\).

Let \(m=\sqrt3(t-u)/(t+u)\ge0\) be the slope of the cut line \(PQ\); write the line as \(y=mx+b\). The piece \(K\) is above \(BC\), to the left of the line \(AC\), and below \(PQ\). If a disk of radius \(r\) and center \((x,y)\) is contained in \(K\), the unit-normal offsets of these three supporting lines give

\[
 y\ge r,\qquad \sqrt3x+y\le \frac{\sqrt3}{2}-2r,\qquad y-mx\le b-r\sqrt{1+m^2}.
\]

The first two inequalities yield \(x\le1/2-\sqrt3r\). As \(m\ge0\), substituting into the third gives

\[
 r\bigl(1+\sqrt3m+\sqrt{1+m^2}\bigr)\le b+m/2.
\]

Let \(L=|P-Q|=\sqrt{t^2+u^2-tu}\). Directly from the coordinates,

\[
 b+\frac m2=\frac{\sqrt3(t-1/2)}{t+u},\qquad
 \sqrt{1+m^2}=\frac{2L}{t+u},
\]

so the preceding bound is

\[
 r(K)\le \frac{\sqrt3(t-1/2)}{2(2t-u+L)}. \tag{1}
\]

Set \(h=\sqrt3/2\) and \(c=(3+\sqrt3)/2\). The equal-area relation implies the *exact identity*

\[
 L^2-h^2t^2=\frac14\left(t-\frac1t\right)^2\ge0,
\]

so \(L\ge ht\), and equality requires \(t=1\) on the permitted parameter interval. Moreover,

\[
 (2+h)t-\frac1{2t}-c(2t-1)
 =\frac{(1-t)((1+h)t-1/2)}{t}\ge0.
\]

(The second factor is strictly positive because \(t\ge1/\sqrt2\).) Combining these inequalities yields

\[
 2t-u+L\ge c(2t-1),
\]

with strict inequality whenever \(t<1\). Since \(t>1/2\), (1) becomes

\[
 r(K)\le\frac{\sqrt3}{4c}=\frac{\sqrt3-1}{4},
\]

again strictly for \(t<1\). Consequently

\[
\min_i\frac{r(K_i)}{R(K_i)}\le\frac{r(K)}{R(K)}
\le2r(K)\le\frac{\sqrt3-1}{2},
\]

with strict inequality for every nonmedian chord.

When \(t=1\), the chord joins \(B\) to the midpoint of \(AC\), hence is a median. Both pieces are congruent right triangles of side lengths \(1,\;1/2,\;\sqrt3/2\). Each has smallest enclosing disk radius \(1/2\) (the hypotenuse is a diameter), and inradius \((\sqrt3-1)/4\). The ratio therefore attains \((\sqrt3-1)/2\). The symmetry of the equilateral triangle gives exactly three maximizing cuts. This proves both sharpness and uniqueness.

## Verification

The proof is analytic and covers the entire continuous family, including the symmetric chord \(t=u=1/\sqrt2\) and the vertex-endpoint chord \(t=1\). The supplementary script `verify.py` checks, in exact symbolic arithmetic, the two critical identities and the endpoint value, and samples the strict intermediate bounds. The numeric samples are only sanity checks, not the source of the theorem.

To reproduce in a Python environment containing SymPy, run `python verify.py` from the extracted package directory. The expected line is `EQUAL_AREA_TRIANGLE_IDENTITIES_OK`.

## Relationship to prior work

Pach and Tardos (arXiv:2609.20702v1, publicly available 2026-09-17) prove the existence of equal-area dyadic decompositions into quantitatively fat convex pieces and introduce a roundness measure. They do not establish this sharp two-piece equilateral benchmark in the examined abstract and introductory statements. Damian and O'Rourke (arXiv:cs/0304023) study the minimizing worst-piece inverse fatness of partitions of regular polygons with an *unrestricted number* of pieces: their equilateral-triangle optimum approaches \(3/2\) only with an increasing number of pieces. That asymptotic optimum does not determine a fixed two-piece equal-area optimum. The present claim uses the standard inradius-to-smallest-enclosing-disk ratio, fixes exactly two pieces and equal area, and establishes uniqueness of the optimizing cut.

## Limitations

The finding concerns only equilateral triangles and partitions into *exactly two* convex equal-area pieces. It does not give a universal dyadic constant for all planar convex bodies, nor does it optimize partitions into three or more parts. The core recent source was inspected in its abstract and opening pages rather than exhaustively through every section; unindexed or unavailable literature could contain an equivalent special case. The mathematical proof is self-contained; the novelty assessment is limited by literature access. Independent external audit has not been carried out.

## References

1. J. Pach and G. Tardos, *Cutting a convex body into fat parts and approximating Euclidean distance by graph distances*, arXiv:2609.20702v1, first submitted 2026-09-17, https://arxiv.org/abs/2609.20702.
2. M. Damian and J. O'Rourke, *Partitioning Regular Polygons into Circular Pieces I: Convex Partitions*, arXiv:cs/0304023, originally 2003, https://arxiv.org/abs/cs/0304023.
3. J. O'Rourke, *Most Circular Partition of a Square*, Open Problems Project, Problem 59, 2004, https://topp.openproblem.net/p59; cites the preceding paper and distinguishes unrestricted-number circular partitions.
