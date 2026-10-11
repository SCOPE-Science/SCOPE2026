# Shard polytopes have a canonical vertex sphere with a balanced-prefix minimum-sphere criterion
## Finding
Let
\[
\alpha=(a,b,A,B)
\]
be an arc in the sense of Padrol, Pilaud, and Ritter. Put
\[
U=\{a\}\cup A,\qquad D=B\cup\{b\},
\]
and write
\[
p=|U|,\qquad q=|D|,\qquad m=p+q=b-a+1.
\tag{1}
\]

For the standard Euclidean shard polytope
\[
\mathrm{SP}(\alpha)\subset\mathbb R^n,
\]
define
\[
c_\alpha(i)=
\begin{cases}
q/m,&i\in U,\\
-p/m,&i\in D,\\
0,&i\notin[a,b].
\end{cases}
\tag{2}
\]

Then every vertex lies on one canonical sphere:
\[
\boxed{
\|v-c_\alpha\|^2=\frac{pq}{m}
\quad
\text{for every vertex }v\text{ of }\mathrm{SP}(\alpha).
}
\tag{3}
\]

Let
\[
y_\alpha=\operatorname{proj}_{\mathrm{SP}(\alpha)}(c_\alpha)
\tag{4}
\]
be the Euclidean projection of \(c_\alpha\) onto the shard polytope. The unique minimum enclosing sphere has center \(y_\alpha\) and squared radius
\[
\boxed{
R_\alpha^2
=
\frac{pq}{m}
-
\operatorname{dist}\!\left(c_\alpha,\mathrm{SP}(\alpha)\right)^2.
}
\tag{5}
\]

Hence the canonical all-vertex sphere is itself the minimum enclosing sphere exactly when
\[
c_\alpha\in\mathrm{SP}(\alpha).
\tag{6}
\]

There is an exact word criterion for (6). For
\[
a\le j<b,
\]
put
\[
u_j=|U\cap[a,j]|,
\qquad
d_j=|D\cap[a,j]|.
\tag{7}
\]
Then
\[
\boxed{
c_\alpha\in\mathrm{SP}(\alpha)
\iff
0\le q\,u_j-p\,d_j\le m
\quad
\text{for every }a\le j<b.
}
\tag{8}
\]
Equivalently,
\[
0\le
u_j-\frac{p}{m}(j-a+1)
\le1
\quad
\text{for every }a\le j<b.
\tag{9}
\]

When (8) holds,
\[
\boxed{
R_\alpha=\sqrt{\frac{pq}{m}},
}
\tag{10}
\]
the center is \(c_\alpha\), and every vertex is a contact point.

The source also identifies
\[
\mathrm{SP}(\alpha)+\mathbf1_D
\]
with the base polytope of a series-parallel shard matroid. Restricted to the active ground set \([a,b]\), that matroid has rank \(q\), and
\[
c_\alpha+\mathbf1_D
=
\frac qm\mathbf1.
\tag{11}
\]
By the constant-coordinate characterization of uniform density, (8) is therefore equivalent to uniform density of the loopless shard matroid.

As a simple boundary case, for the monotone word
\[
U^pD^q
\]
the only potentially largest prefix discrepancy occurs after the \(p\) consecutive \(U\)'s. Thus the canonical sphere is minimum exactly when
\[
pq\le p+q,
\]
or equivalently
\[
(p-1)(q-1)\le1.
\tag{12}
\]

## Assumptions and scope
The metric is the standard Euclidean metric of the source realization.

The result applies to every ordinary arc, so \(p,q\ge1\). Coordinates outside the active interval \([a,b]\) vanish identically.

The minimum enclosing sphere is meant intrinsically in the affine hull; because the affine hull carries the metric induced from \(\mathbb R^n\), the formulas above are the same ambient Euclidean distances.

The theorem gives the exact minimum enclosing radius through the projection distance in all cases and a closed combinatorial criterion for when the canonical common sphere is already optimal. It does not give a closed word formula for the projection distance in the failing cases.

## Proof
The source proves that the vertices of \(\mathrm{SP}(\alpha)\) are exactly the characteristic vectors of \(\alpha\)-alternating matchings. Such a matching has the form
\[
a_1<b_1<\cdots<a_k<b_k
\]
with every \(a_i\in U\) and every \(b_i\in D\). Its characteristic vector has \(k\) coordinates equal to \(1\) on \(U\), \(k\) coordinates equal to \(-1\) on \(D\), and all remaining coordinates zero.

Fix such a vertex \(v\). On the selected \(U\)-coordinates,
\[
v_i-c_\alpha(i)=1-\frac qm=\frac pm,
\]
while on unselected \(U\)-coordinates it equals \(-q/m\). On selected \(D\)-coordinates,
\[
v_i-c_\alpha(i)=-1+\frac pm=-\frac qm,
\]
while on unselected \(D\)-coordinates it equals \(p/m\). Therefore
\[
\begin{aligned}
\|v-c_\alpha\|^2
&=
k\frac{p^2}{m^2}
+
(p-k)\frac{q^2}{m^2}
+
k\frac{q^2}{m^2}
+
(q-k)\frac{p^2}{m^2}\\
&=
\frac{pq(p+q)}{m^2}
=
\frac{pq}{m}.
\end{aligned}
\tag{13}
\]
This proves (3).

We next record the geometric lemma that converts a common vertex sphere into the exact minimum enclosing sphere.

Let
\[
P=\operatorname{conv}\{z_1,\ldots,z_N\}
\]
and suppose
\[
\|z_i-c\|=R_0
\]
for every \(i\). Let
\[
y=\operatorname{proj}_P(c)
\]
and put
\[
d=y-c.
\]
The projection inequality says
\[
\langle d,z-y\rangle\ge0
\qquad
(z\in P).
\tag{14}
\]
Thus, for every vertex,
\[
\langle d,z_i-c\rangle\ge\|d\|^2.
\]
Consequently
\[
\|z_i-y\|^2
=
R_0^2+\|d\|^2
-
2\langle d,z_i-c\rangle
\le
R_0^2-\|d\|^2.
\tag{15}
\]

The exposed face
\[
F=
\{z\in P:\langle d,z-c\rangle=\|d\|^2\}
\]
contains \(y\). Write \(y\) as a convex combination of vertices of \(F\):
\[
y=\sum_i\lambda_i z_i,
\qquad
\lambda_i\ge0,
\qquad
\sum_i\lambda_i=1.
\]
For those vertices, equality holds in (15). For any alternative center \(x\),
\[
\sum_i\lambda_i\|z_i-x\|^2
=
R_0^2-\|d\|^2+\|x-y\|^2.
\tag{16}
\]
Therefore every enclosing ball centered at \(x\) has squared radius at least the right side of (16). The center \(y\) attains the lower bound, and equality forces \(x=y\). Hence
\[
R_{\min}^2=R_0^2-\operatorname{dist}(c,P)^2,
\]
with unique center \(y\).

Applying this lemma with (3) gives (5). It also proves that the canonical sphere is minimum if and only if its center already belongs to the polytope.

It remains to characterize that membership.

The source's facet description gives:
- coordinates outside \([a,b]\) vanish;
- coordinates indexed by \(U\) are nonnegative;
- coordinates indexed by \(D\) are nonpositive;
- prefix sums are at most \(1\) at every arc fall and at least \(0\) at every arc rise.

The same source observes that these inequalities force every prefix sum of every point of the shard polytope to lie between \(0\) and \(1\).

For the point \(c_\alpha\), the prefix sum through \(j\) is
\[
\sum_{i=a}^{j}c_\alpha(i)
=
\frac{q\,u_j-p\,d_j}{m}.
\tag{17}
\]
Thus membership implies (8).

Conversely, if (8) holds, then every prefix sum in (17) lies in \([0,1]\). The coordinate sign conditions and the zero coordinates outside \([a,b]\) are automatic from (2), and the total active coordinate sum is
\[
p\frac qm-q\frac pm=0.
\]
In particular all the source rise and fall inequalities hold, so the complete H-description places \(c_\alpha\) in \(\mathrm{SP}(\alpha)\). This proves (8).

Finally, the source proves that translating by \(\mathbf1_D\) gives a matroid base polytope. On the active interval every translated vertex has exactly \(q\) ones, so the loopless shard matroid has rank \(q\). Equation (11) follows immediately. The theorem of Devriendt and Mulas says that a matroid is uniformly dense exactly when its base polytope contains the constant-coordinate point. This gives the stated matroidal equivalence.

For the monotone word \(U^pD^q\), prefix sums increase throughout the \(U\)-run and then decrease. The lower bound in (8) is automatic, while the largest numerator is \(pq\). Hence (12).

## Verification
The proof is symbolic for every arc.

The source-dependent inputs were checked in the primary full text: the alternating-matching vertex description, the complete H-description, the all-prefix consequence, the exact dimension and facet statement, and the translation of shard polytopes to base polytopes of series-parallel shard matroids.

The accompanying `verify.py` exhaustively checks every \(U/D\) arc word of length
\[
2\le m\le10
\]
that begins with \(U\) and ends with \(D\). It enumerates all alternating-matching vertices, checks the exact common-sphere identity with rational arithmetic, checks the balanced-prefix condition, and checks its equivalence with the source rise/fall facet conditions for the canonical center. It also verifies the translated rank-\(q\) vertex weight and the monotone-word criterion. The finite computation is corroborative only.

## Relationship to prior work
Padrol, Pilaud, and Ritter introduce shard polytopes as Minkowski-indecomposable building blocks for quotientopes. Their paper gives the alternating-matching vertices, the facet inequalities, and the series-parallel matroid interpretation. It does not state a Euclidean minimum enclosing sphere or a balanced-prefix radius criterion.

Devriendt and Mulas prove that a matroid is uniformly dense exactly when its base polytope contains the appropriate constant-coordinate point. That theorem supplies the matroidal interpretation of (8), but it does not identify the shard-polytope common sphere, its Euclidean radius, or the exact minimum-enclosing projection formula.

A previously checked same-object metric result computes the Euclidean diameter of shard polytopes from run data. Diameter does not determine a minimum enclosing center or radius, and its run statistic does not imply the prefix discrepancy criterion (8).

The distinction is visible even within one fixed \((p,q)\): all shard vertices always lie on the canonical sphere (3), but depending on the order of \(U\)'s and \(D\)'s the center can lie inside or outside the shard polytope. Thus the minimum-sphere question detects a balance property invisible to the common radius alone.

Targeted published-result searches under “shard polytope”, “minimum enclosing sphere”, “circumradius”, “uniform density”, “matroid base polytope”, and “balanced prefix” did not locate a theorem implying (3)--(12).

## Limitations
When (8) fails, formula (5) is exact but still contains the projection distance to the shard polytope. No closed run-length formula for that projection is claimed.

The theorem concerns the standard shard-polytope realization and is not invariant under arbitrary affine transformations.

The uniform-density equivalence uses the loopless shard matroid on the active interval; the loops that the source adds outside \([a,b]\) only record the ambient embedding and are deleted before applying the constant-coordinate characterization.

The common-sphere projection lemma is general convex geometry. The shard-specific content is the exact center and radius (2)--(3), the balanced-prefix membership criterion (8), and the identification with uniform density of the associated series-parallel matroid.

## References
1. Arnau Padrol, Vincent Pilaud, and Julian Ritter, *Shard polytopes*, arXiv:2007.01008, first public version 2020-07-02; *International Mathematics Research Notices* 2023(9), 7686--7796, DOI 10.1093/imrn/rnac042.
2. Karel Devriendt and Raffaella Mulas, *Uniform density in matroids, matrices and graphs*, arXiv:2306.15267, first public version 2023-06-27.
