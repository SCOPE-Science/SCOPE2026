# Euclidean inradius of every lecture-hall order polytope is a weighted critical-path reciprocal
## Finding
Let \(P=([n],\preceq)\) be a nonempty naturally labeled finite poset and let
\[
s=(s_1,\ldots,s_n)\in\mathbb Z_{>0}^n.
\]
Its \(s\)-lecture hall order polytope is
\[
\mathcal O(P,s)
=
\left\{
x\in\mathbb R^n:
0\le x_i\le s_i,\quad
\frac{x_i}{s_i}\le\frac{x_j}{s_j}
\text{ whenever }i\prec j
\right\}.
\]

Adjoin a source \(\bot\) and a sink \(\top\) to the Hasse diagram of \(P\). Use arcs
\[
\bot\to i
\]
for minimal elements \(i\),
\[
i\to j
\]
for cover relations \(i\prec j\), and
\[
i\to\top
\]
for maximal elements \(i\). Assign weights
\[
w(\bot,i)=\frac1{s_i},
\qquad
w(i,j)=\sqrt{\frac1{s_i^2}+\frac1{s_j^2}},
\qquad
w(i,\top)=\frac1{s_i}.
\tag{1}
\]
Let
\[
L(P,s)
=
\max_{\gamma:\bot\leadsto\top}
\sum_{e\in\gamma}w(e).
\tag{2}
\]
Then the standard-Euclidean inradius is exactly
\[
\boxed{
r_{\mathrm{in}}\!\left(\mathcal O(P,s)\right)
=
\frac1{L(P,s)}.
}
\tag{3}
\]

Write
\[
r_*=\frac1{L(P,s)}.
\]
The complete set of centers of largest inscribed Euclidean balls is
\[
\boxed{
\begin{aligned}
\mathcal I(P,s)=\{c\in\mathbb R^n:\;&c_i\ge r_*
&&\text{for every minimal }i,\\
&s_i-c_i\ge r_*
&&\text{for every maximal }i,\\
&\frac{c_j}{s_j}-\frac{c_i}{s_i}
\ge
r_*\sqrt{\frac1{s_i^2}+\frac1{s_j^2}}
&&\text{for every cover }i\prec j
\}.
\end{aligned}
}
\tag{4}
\]

For an element \(v\in P\), let \(d_-(v)\) be the maximum weight of a directed path from \(\bot\) to \(v\), and let \(d_+(v)\) be the maximum weight of a directed path from \(v\) to \(\top\). Then
\[
\boxed{
c^-_v=s_vr_*d_-(v)
}
\tag{5}
\]
and
\[
\boxed{
c^+_v=s_v\bigl(1-r_*d_+(v)\bigr)
}
\tag{6}
\]
are both incenters.

The incenter is unique if and only if
\[
\boxed{
d_-(v)+d_+(v)=L(P,s)
\quad\text{for every }v\in P.
}
\tag{7}
\]
Equivalently, every element of \(P\) lies on at least one maximum-weight \(\bot\)-to-\(\top\) path.

The formula is algorithmic: once the Hasse diagram is available, \(L(P,s)\), \(d_-\), and \(d_+\) are obtained by two longest-path dynamic programs on a DAG.

Two specializations calibrate the theorem. If
\[
s_1=\cdots=s_n=1
\]
and the height of \(P\) is \(h\), every augmented chain with \(k\) poset elements has weight
\[
2+(k-1)\sqrt2,
\]
so
\[
r_{\mathrm{in}}
=
\frac1{2+(h-1)\sqrt2}.
\tag{8}
\]
If \(P\) itself is the chain
\[
1\prec2\prec\cdots\prec n,
\]
then \(\mathcal O(P,s)\) is the \(s\)-lecture hall simplex and
\[
\boxed{
r_{\mathrm{in}}
=
\left(
\frac1{s_1}
+
\sum_{i=1}^{n-1}
\sqrt{\frac1{s_i^2}+\frac1{s_{i+1}^2}}
+
\frac1{s_n}
\right)^{-1}.
}
\tag{9}
\]
In this chain case the incenter is unique.

## Assumptions and scope
The poset is nonempty and naturally labeled, and every \(s_i\) is a positive integer, matching the standard definition of an \(s\)-lecture hall order polytope. The metric is the ordinary Euclidean metric in the canonical \(x\)-coordinates.

The result is not an affine-invariant restatement of the ordinary order-polytope formula. Although the diagonal map
\[
y_i=\frac{x_i}{s_i}
\]
identifies \(\mathcal O(P,s)\) affinely with the ordinary order polytope, that nonorthogonal scaling changes Euclidean facet-normal lengths. The cover relation \(i\prec j\) therefore contributes the genuinely weight-dependent quantity in (1).

A path from \(\bot\) to \(\top\) is precisely a saturated maximal chain of \(P\), together with its two boundary arcs. “Maximum-weight chain” refers to the weights in (1), not necessarily to maximum cardinality.

## Proof
The diagonal change of coordinates
\[
x_i=s_i y_i
\]
takes \(\mathcal O(P,s)\) to the ordinary order polytope. The irredundant facet types therefore correspond to the ordinary order-polytope facets:
\[
x_i\ge0
\quad(i\text{ minimal}),
\tag{10}
\]
\[
x_i\le s_i
\quad(i\text{ maximal}),
\tag{11}
\]
and
\[
\frac{x_i}{s_i}\le\frac{x_j}{s_j}
\quad(i\prec j\text{ a cover}).
\tag{12}
\]

For (10) and (11), the Euclidean facet normal has norm \(1\). For (12), an unnormalized normal is
\[
s_j e_i-s_i e_j,
\]
whose norm is
\[
\sqrt{s_i^2+s_j^2}.
\]
Hence a Euclidean ball of radius \(r\) centered at \(c\) is contained in the polytope if and only if
\[
c_i\ge r
\]
for minimal \(i\),
\[
s_i-c_i\ge r
\]
for maximal \(i\), and
\[
s_i c_j-s_j c_i
\ge
r\sqrt{s_i^2+s_j^2}
\]
for every cover \(i\prec j\). Dividing the last inequality by \(s_is_j\) gives
\[
\frac{c_j}{s_j}-\frac{c_i}{s_i}
\ge
r\sqrt{\frac1{s_i^2}+\frac1{s_j^2}}.
\tag{13}
\]
Thus (4) is exactly the radius-\(r_*\) feasibility system once optimality is proved.

Put
\[
y_i=\frac{c_i}{s_i}.
\]
For any augmented path
\[
\gamma:
\bot\to v_1\to\cdots\to v_k\to\top,
\]
the corresponding ball-containment inequalities give
\[
y_{v_1}\ge r\,w(\bot,v_1),
\]
\[
y_{v_{a+1}}-y_{v_a}\ge r\,w(v_a,v_{a+1}),
\]
and
\[
1-y_{v_k}\ge r\,w(v_k,\top).
\]
Summing telescopically yields
\[
1\ge r\sum_{e\in\gamma}w(e).
\]
Choosing a maximum-weight path gives
\[
r\le\frac1{L(P,s)}.
\tag{14}
\]

It remains to attain this bound. Define \(d_-(v)\) as above and set
\[
y^-_v=r_*d_-(v).
\]
For a minimal \(v\),
\[
d_-(v)=w(\bot,v),
\]
so the lower boundary inequality holds. For a cover \(u\prec v\), longest-path optimality gives
\[
d_-(v)\ge d_-(u)+w(u,v),
\]
so the cover inequality holds. If \(v\) is maximal, appending \(v\to\top\) to a longest path ending at \(v\) gives a complete path, and therefore
\[
d_-(v)+w(v,\top)\le L(P,s).
\]
Multiplication by \(r_*=1/L(P,s)\) gives the upper boundary inequality. Thus
\[
c^-_v=s_vy^-_v
\]
is the center of a feasible ball of radius \(r_*\). Together with (14), this proves (3).

The same argument in reverse gives
\[
y^+_v=1-r_*d_+(v)
\]
and proves that \(c^+\) in (6) is an incenter.

More generally, every feasible radius-\(r_*\) center satisfies all inequalities in (4), and those inequalities are sufficient because they are exactly the facet-distance conditions. This proves the complete incenter description.

For uniqueness, summing lower path inequalities from \(\bot\) to \(v\) gives
\[
\frac{c_v}{s_v}\ge r_*d_-(v),
\tag{15}
\]
while summing from \(v\) to \(\top\) gives
\[
\frac{c_v}{s_v}\le1-r_*d_+(v).
\tag{16}
\]
If
\[
d_-(v)+d_+(v)=L(P,s),
\]
then the two bounds coincide. If this holds for every \(v\), every coordinate of every incenter is fixed, so the incenter is unique.

Conversely, if the equality fails at some \(v\), then
\[
d_-(v)+d_+(v)<L(P,s),
\]
and (5)--(6) give
\[
c^-_v<c^+_v.
\]
Since both vectors are incenters, uniqueness fails. This proves (7).

Finally, the equivalence in (7) with membership in a maximum-weight augmented chain follows because concatenating a longest prefix ending at \(v\) with a longest suffix starting at \(v\) gives a complete path of weight
\[
d_-(v)+d_+(v).
\]

## Verification
The proof is symbolic and applies to every finite naturally labeled poset and every positive integer sequence \(s\). No finite experiment is used as an infinite proof.

The nonstandard metric step was checked directly: the cover halfspace has normal
\[
s_j e_i-s_i e_j
\]
and its normalized Euclidean slack is exactly the cover-edge quantity in (1). The sharpness construction was checked in both forward and reverse dynamic-programming forms, so it also verifies the uniqueness criterion.

The accompanying `verify.py` reconstructs several small Hasse DAGs with unequal \(s\)-weights. It independently enumerates maximal saturated chains, compares their weights with dynamic programming, verifies the two explicit incenter constructions against every facet-distance constraint, and checks the ordinary-order and chain specializations. These finite computations are corroborative only.

## Relationship to prior work
Olsen's survey develops the polyhedral geometry of lecture hall partitions and highlights lecture hall order polytopes as a central recent generalization. It records that for naturally labeled \(P\),
\[
\mathcal O(P,s)
\]
is defined by the normalized order inequalities together with the coordinate bounds, and that chains recover the \(s\)-lecture hall simplices. The inspected full text focuses on Ehrhart theory, Gorenstein and level properties, integer decomposition, triangulations, and related lattice geometry; it does not state an inradius or Chebyshev-center theorem.

Brändén and Solus subsequently prove the integer decomposition property for all \(s\)-lecture hall order polytopes and again record that these polytopes simultaneously generalize ordinary order polytopes and \(s\)-lecture hall simplices. Their inspected full text likewise contains no inradius, radius, or Chebyshev-center statement.

The ordinary order-polytope case
\[
s=(1,\ldots,1)
\]
is already known in the comparison record. It is a strict specialization of (3). It does not determine the weighted theorem by Euclidean invariance: diagonal scaling by unequal \(s_i\) is not orthogonal and changes each cover-facet normal by a different factor. The present formula replaces cardinality height by a weighted longest-path invariant whose edge weights couple adjacent lecture-hall parameters.

Targeted searches used “lecture hall order polytope”, “\(s\)-lecture hall order polytope”, “inradius”, “Chebyshev center”, “largest inscribed ball”, “weighted longest chain”, and the lecture-hall-simplex specialization. No inspected source or returned published-result statement supplied (3)--(7).

## Limitations
The theorem concerns the canonical Euclidean realization. Other norms, or Euclidean metrics after an additional nonorthogonal affine transformation, require different normal weights.

The result assumes the standard weak-order version for naturally labeled posets. Partially open variants arising from non-natural labelings are outside the claim.

The metric optimization becomes a longest-path problem once the facet structure is known. Accordingly, the value lies in the exact weighted formula, complete center classification, and natural lecture-hall specialization rather than in a new facet theorem.

The originality comparison cannot exclude an equivalent observation hidden in unindexed optimization or weighted-order-polytope literature under different terminology. In particular, a very general theorem about Chebyshev centers of difference-constraint polytopes could subsume the dynamic-programming argument even though no such covering statement was located.

## References
1. McCabe Olsen, *Polyhedral Geometry for Lecture Hall Partitions*, arXiv:1808.06131, first public version 2018-08-18; in *Algebraic and Geometric Combinatorics on Lattice Polytopes*, 2019, DOI 10.1142/9789811200489_0021.
2. Petter Brändén and Liam Solus, *Some Algebraic Properties of Lecture Hall Polytopes*, arXiv:1911.12459, first public version 2019-11-27.
3. Richard P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry 1 (1986), 9--23.
