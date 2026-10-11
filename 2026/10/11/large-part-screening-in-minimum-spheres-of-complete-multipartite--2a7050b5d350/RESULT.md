# Large-part screening in minimum spheres of complete multipartite stable-set polytopes
## Finding
Let
\[
k\ge3,\qquad a_1,\ldots,a_k\in\mathbb Z_{>0},
\]
and let \(G=K_{a_1,\ldots,a_k}\) be the complete multipartite graph with disjoint independent vertex classes \(V_i\) of sizes \(a_i\). Every stable set of \(G\) is a subset of one vertex class. Hence the stable-set polytope in the usual indicator-vector realization is
\[
P=\operatorname{STAB}(G)
=\operatorname{conv}\{\mathbf1_S:S\subseteq V_i\text{ for some }i\}
\subset\mathbb R^N,
\qquad N=\sum_i a_i.
\tag{1}
\]

There is a unique \(h\) in the interval
\[
0<h<\max_i a_i
\]
satisfying
\[
\boxed{\sum_{i=1}^k\left(1-\frac{h}{a_i}\right)_+=2,}
\qquad
(z)_+=\max\{0,z\}.
\tag{2}
\]
Set
\[
p_i=\frac12\left(1-\frac{h}{a_i}\right)_+,
\qquad
B=\sum_{i=1}^k a_i p_i^2.
\tag{3}
\]
The **unique minimum enclosing Euclidean ball** of \(P\) is
\[
\boxed{
\mathbb B\left(c,\sqrt{B+h}\right),
\qquad c=\sum_i p_i\mathbf1_{V_i},
\qquad R^2=B+h.
}
\tag{4}
\]
The contact vertices of this sphere are **exactly**
\[
\boxed{\{\mathbf1_{V_i}:a_i\ge h\}.}
\tag{5}
\]
In particular, the empty stable set and all proper subsets of a vertex class are strictly inside the sphere.

Define the active index set and its elementary statistics by
\[
I=\{i:a_i>h\},\quad m=|I|,\quad
A_I=\sum_{i\in I}a_i,\quad
H_I=\sum_{i\in I}\frac1{a_i}.
\tag{6}
\]
Then \(m\ge3\) and
\[
\boxed{
h=\frac{m-2}{H_I},
\qquad
R^2=\frac14\left(A_I-\frac{(m-2)^2}{H_I}\right).
}
\tag{7}
\]
All values in (2)--(7), except the radius without squaring, are rational.

**Screening principle.** If a new vertex class of size \(b\le h\) is added, with all cross-class edges as required in a complete multipartite graph, the unique enclosing radius and all existing center coordinates are unchanged, and the new center coordinates are zero. If \(b<h\), its full-class vertex is strictly inside the sphere. If \(b=h\), its full-class vertex is on the sphere but has zero coefficient in the center's convex-combination certificate. This remains true for any finite number of added classes, each of size at most \(h\).

For example, for all \(s\ge0\), the polytopes of
\[
K_{\underbrace{10,10,10}_{\text{three large classes}},\underbrace{1,\ldots,1}_{s\text{ singleton classes}}}
\]
share the exact squared enclosing radius
\[
\boxed{R^2=\frac{20}{3}.}
\tag{8}
\]
Their unique centers equal \(1/3\) on the thirty coordinates belonging to the three size-ten classes and zero on each additional singleton coordinate. Thus the ambient dimension can grow arbitrarily while the Euclidean minimum enclosing radius remains fixed.

## Assumptions and scope
The stable-set polytope is the convex hull of all stable-set indicators in the standard coordinate space \(\mathbb R^N\), with its unweighted Euclidean metric. The formula does **not** concern the fractional stable-set relaxation or a signed, unconditional, or Hansen polytope associated with the same graph. The graph has at least three nonempty parts; the excluded two-part case behaves differently, since the ordinary coordinate-cube sphere can contact many non-full stable-set vertices.

The source *Unconditional reflexive polytopes* provides the stable-set and perfect-graph polytope framework, and the companion literature on \(2\)-level stable-set polytopes develops related combinatorial structure. The new calculation addresses an intrinsic Euclidean metric invariant of the **unsymmetrized** stable-set polytope.

## Proof
For each index \(i\), put
\[
v_i=\mathbf1_{V_i}\in\mathbb R^N.
\tag{9}
\]
The \(v_i\) have disjoint supports, with
\[
\langle v_i,v_j\rangle=0\quad(i\ne j),
\qquad \|v_i\|^2=a_i.
\tag{10}
\]
The function
\[
F(h)=\sum_i\left(1-\frac{h}{a_i}\right)_+
\]
is continuous and strictly decreasing wherever it is positive. Since \(F(0)=k>2\) and \(F(\max_i a_i)=0\), equation (2) has a unique solution in the stated open interval. Thus the coefficients (3) satisfy
\[
0\le p_i<\frac12,\qquad \sum_i p_i=1.
\tag{11}
\]
Their support is \(I\). Since each positive term in \(F(h)\) is strictly less than one and their sum is two, \(m=|I|\ge3\).

Take the proposed center \(c\) from (4), and let \(S\subseteq V_i\) be a stable set of cardinality \(s\). Disjointness of the vertex classes gives the exact identity
\[
\|\mathbf1_S-c\|^2
=\sum_j a_jp_j^2+s(1-2p_i)
=B+s(1-2p_i).
\tag{12}
\]
For every index \(i\),
\[
a_i(1-2p_i)
=\min\{a_i,h\}\le h.
\tag{13}
\]
Since \(0\le s\le a_i\) and \(1-2p_i>0\), equations (12)--(13) yield
\[
\|\mathbf1_S-c\|^2\le B+h=R^2.
\tag{14}
\]
Equality is possible exactly when \(s=a_i\) and \(a_i\ge h\). This proves both containment of all vertices in the proposed ball, hence containment of the whole convex polytope, and the complete contact classification (5).

The key to global optimality is that \(c\) is itself a convex combination of its contacts:
\[
c=\sum_i p_i v_i,
\qquad \sum_i p_i=1,
\tag{15}
\]
and every \(v_i\) with \(p_i>0\) satisfies \(\|v_i-c\|^2=R^2\), because \(a_i>h\). For an arbitrary competing center \(y\in\mathbb R^N\), the exact variance identity gives
\[
\begin{aligned}
\sum_i p_i\|v_i-y\|^2
&=\sum_i p_i\|v_i-c\|^2+\|y-c\|^2\\
&=R^2+\|y-c\|^2.
\end{aligned}
\tag{16}
\]
At least one stable-set vertex therefore has distance squared at least the right-hand side. Every enclosing sphere has squared radius at least \(R^2\), with strict inequality if \(y\ne c\). This proves **global optimality and uniqueness** without any unproved symmetry assumption.

It remains to derive the exact active-set expressions. On \(I\), equation (2) reads
\[
\sum_{i\in I}\left(1-\frac{h}{a_i}\right)
=m-hH_I=2,
\]
so
\[
h=\frac{m-2}{H_I}.
\tag{17}
\]
For \(i\in I\), \(p_i=(1-h/a_i)/2\); for other indices, \(p_i=0\). Therefore
\[
\begin{aligned}
B+h
&=\frac14\sum_{i\in I}a_i\left(1-\frac{h}{a_i}\right)^2+h\\
&=\frac14\left(A_I-2mh+h^2H_I\right)+h\\
&=\frac14\left(A_I-\frac{(m-2)^2}{H_I}\right),
\end{aligned}
\]
which proves (7) and rationality.

Finally, append a new class of size \(b\le h\). Its summand in the left side of (2), evaluated at the old \(h\), is zero. Hence the old value still solves the new defining equation and is unique by the same monotonicity argument. Its new coefficient is \(p_{\mathrm{new}}=0\), while all old coefficients stay unchanged. Consequently both \(B\) and \(R^2\) remain unchanged, and (5) gives the stated strict or weak contact behavior. Repeating the argument handles any finite number of new classes.

For (8), the three size-ten classes give \(h=10/3\) and three coefficients \(p_i=1/3\); singleton classes have zero coefficients. Then \(B=30/9=10/3\), hence \(R^2=20/3\).

## Verification
The proof holds symbolically for every \(k\ge3\) and all positive integer part sizes. It uses the complete vertex description of the stable-set polytope, an exact one-dimensional monotone equation, a direct vertex-distance calculation, and the contact-barycenter identity (16). No numerical optimization is needed for the infinite-parameter theorem.

The included `verify.py` computes \(h\), every coefficient, center, and squared radius with exact rational arithmetic, checks the active-set and contact formulas, and enumerates all stable-set vertices across a bounded but complete set of integer part-size profiles. It also tests the arbitrary-size plateau example and the exact-threshold weak-contact case. Finite replay is corroborative only.

## Relationship to prior work
Kohl, Olsen, and Sanyal define stable-set polytopes, explain their connection to perfect graphs and anti-blocking polytopes, and study signed unconditional extensions, reflexivity, Gale duality, and Gröbner structures. Their inspected full text does not state a Euclidean minimum-enclosing-sphere formula or a part-size screening phenomenon for complete multipartite stable-set polytopes.

Aprile, Cevallos, and Faenza study \(2\)-level polytopes associated with combinatorial optimization. Their full-text treatment of perfect-graph stable-set polytopes gives facet/vertex and counting relationships rather than minimum-sphere geometry. The present result is distinct from such combinatorial statements and from general enclosing-ball algorithms: it identifies an exact graph-specific center, all contact vertices, rational squared radius, and a stable rank-screening law under adjoining entire vertex classes.

The criterion (2) is not an abstract symmetry statement alone. It quantitatively selects which entire graph classes participate in the supporting contact certificate, and it proves that sufficiently small classes become **irrelevant to the Euclidean outer radius** even though they change the graph, polytope, and ambient dimension.

## Limitations
The statement applies to standard \(0\)/\(1\) stable-set polytopes of complete multipartite graphs with at least three nonempty parts. An arbitrary affine transformation, weighted Euclidean metric, or a different graph class need not preserve the formula. Fractional stable-set relaxations generally have additional vertices and are not covered.

The proof reduces to elementary Euclidean point-set geometry once the full-class vertex structure is identified. Equivalent observations might exist under descriptions such as free sums of anchored coordinate cubes, convex hulls of mutually orthogonal cube sections, or graph stable-set polytopes without the term “minimum enclosing ball”; this remains an originality risk.

## References
1. Florian Kohl, McCabe Olsen, and Raman Sanyal, *Unconditional reflexive polytopes*, arXiv:1906.01469, first public version 2019-06-03; *Discrete & Computational Geometry* 64 (2020), 427--452, DOI 10.1007/s00454-020-00199-8.
2. Manuel Aprile, Alfonso Cevallos, and Yuri Faenza, *On 2-level polytopes arising in combinatorial settings*, arXiv:1702.03187, first public version 2017-02-10; *SIAM Journal on Discrete Mathematics* 32 (2018), 1857--1886, DOI 10.1137/17M1116684.
3. Jack Elzinga and Donald Hearn, *The minimum sphere covering a convex polyhedron*, *Naval Research Logistics Quarterly* 21 (1974), 715--718, DOI 10.1002/nav.3800210414.
