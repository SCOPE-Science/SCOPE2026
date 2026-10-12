# Minimum determining sets in subgroup-intersection graphs of \(C_p^3\)

## Finding

Let \(p\) be a prime and let \(\Gamma_p\) be the graph whose vertices are the nontrivial proper subgroups of \(C_p^3\), with two vertices adjacent exactly when their intersection is nontrivial. The full graph automorphism action is \(\operatorname{PGL}(3,p)\) on the projective points and lines. Its determining number is \(3\) for \(p=2\) and \(4\) for odd \(p\). For \(p=2\), the minimum determining sets are exactly the triples of noncollinear point vertices and, dually, the triples of nonconcurrent plane vertices; there are \(56\) in total. For odd \(p\), the minimum determining sets are exactly: four point vertices with no three collinear; four plane vertices with no three concurrent; three noncollinear point vertices together with a plane vertex containing none of them; and the dual configurations of one point with three nonconcurrent planes containing no common incident point. Their total number is \(\frac{5}{12}p^3(p^3-1)(p^2-1)\).

The automorphism-group identification is structural background for the determining-set theorem: the new content asserted here is the sharp determining number, the complete classification of every minimum determining set, and the exact count of those sets.

## Assumptions and scope

Let \(p\) be prime and identify
\[
C_p^3\cong V=\mathbf F_p^3.
\]
Every nontrivial proper subgroup is therefore either a one-dimensional or a two-dimensional subspace. Write
\[
t=p^2+p+1.
\]
There are \(t\) subgroups of each dimension.

A determining set of a graph is a vertex set whose pointwise stabilizer in the full graph automorphism group is trivial.

Call one-dimensional vertices *points* and two-dimensional vertices *planes*. In projective language the latter are the lines of \(\operatorname{PG}(2,p)\).

## Proof

Two distinct point vertices intersect trivially, so the point vertices form an independent set. Two distinct plane vertices in a three-dimensional vector space intersect in dimension one, so the plane vertices form a clique. A point is adjacent to a plane exactly when it is contained in that plane.

Hence a point vertex has degree
\[
p+1,
\]
whereas a plane vertex has degree
\[
(t-1)+(p+1)=(p+1)^2.
\]
The two degrees are distinct. Every graph automorphism therefore preserves the two vertex types and their incidence relation. The fundamental theorem of projective geometry then gives
\[
\operatorname{Aut}(\Gamma_p)\cong\operatorname{PGL}(3,p),
\tag{1}
\]
because the prime field has no nontrivial field automorphisms. Equivalently, the natural map
\[
\operatorname{GL}(3,p)\longrightarrow\operatorname{Aut}(\Gamma_p)
\]
is onto and has kernel the nonzero scalar matrices. Thus
\[
|\operatorname{Aut}(\Gamma_p)|
=
p^3(p^3-1)(p^2-1).
\tag{2}
\]

We now determine the pointwise bases of this action.

For any two distinct projective points, let \(A\) be their joining line. A nontrivial elation with axis \(A\) fixes every point of \(A\). Dually, two fixed projective lines never form a base. For a point-line pair, if the point lies on the line then an elation with that line as axis fixes the pair; if the point does not lie on the line, a nontrivial projectivity preserving the line and the complementary point fixes the pair. Thus no two graph vertices form a determining set.

More generally, any configuration consisting of two points and one line has nontrivial pointwise stabilizer. Let \(A\) be the line through the two points and let \(R\) be the intersection of \(A\) with the fixed line. A nontrivial elation having axis \(A\) and center \(R\) fixes the two points and the fixed line. The dual statement holds for one point and two lines.

Consider three point vertices. If they are collinear, an elation with their common line as axis fixes them pointwise. If they are noncollinear, choose them as the coordinate points. Their pointwise stabilizer in \(\operatorname{PGL}(3,p)\) is the diagonal torus
\[
\{\operatorname{diag}(a,b,c):a,b,c\in\mathbf F_p^\times\}/\mathbf F_p^\times,
\]
of order
\[
(p-1)^2.
\tag{3}
\]
For \(p=2\), (3) is trivial. Thus three noncollinear points form a determining set, and the preceding paragraph shows that no smaller or mixed triple does. By duality, three nonconcurrent plane vertices also form a minimum determining set. This proves
\[
\operatorname{Det}(\Gamma_2)=3.
\tag{4}
\]

There are
\[
\binom{7}{3}-7=28
\]
noncollinear triples in the Fano plane and the same number of nonconcurrent triples of lines. Hence \(\Gamma_2\) has exactly
\[
56
\tag{5}
\]
minimum determining sets.

Assume now that \(p\) is odd. Equation (3) is nontrivial, so no three points form a base; the preceding mixed and dual arguments show that no three graph vertices of any type form a base. Four points in general position form a projective frame, so
\[
\operatorname{Det}(\Gamma_p)=4
\qquad (p\text{ odd}).
\tag{6}
\]

It remains to classify the four-vertex bases.

Four points form a base exactly when no three are collinear. Indeed, such a set is a projective frame. If three lie on a line \(A\), then either all four lie on \(A\), in which case an elation with axis \(A\) survives, or the fourth point is outside \(A\), in which case a nontrivial homology with axis \(A\) and that fourth point as center survives because \(p>2\). The dual statement classifies four-plane bases.

For three points and one plane, collinear points again leave a nontrivial elation. Suppose the three points are noncollinear and choose them as the coordinate points. Their stabilizer is the diagonal torus (3). Write the plane as
\[
\alpha x+\beta y+\gamma z=0.
\]
The diagonal torus fixes this plane only scalarly exactly when
\[
\alpha\beta\gamma\ne0,
\]
which is equivalent to the plane containing none of the three point vertices. Thus this is precisely the third class in the statement; duality gives the fourth.

Finally consider two points and two planes. Let \(A\) be the line through the two point vertices and let \(R\) be the intersection point of the two plane vertices. If \(R\in A\), a nontrivial elation with axis \(A\) and center \(R\) fixes all four vertices. If \(R\notin A\), a nontrivial homology with axis \(A\) and center \(R\) exists because \(p>2\) and again fixes all four. Hence no two-plus-two configuration is a base. This completes the classification.

For the count, let
\[
g=|\operatorname{PGL}(3,p)|=p^3(p^3-1)(p^2-1).
\]
The group acts sharply transitively on ordered projective frames, so there are
\[
\frac{g}{24}
\]
four-point frames and the same number of four-line frames.

The pointwise stabilizer of an ordered noncollinear triple has order \((p-1)^2\), so the number of unordered triangles is
\[
\frac{g}{6(p-1)^2}.
\]
For a fixed triangle, inclusion-exclusion shows that exactly
\[
t-3p=(p-1)^2
\]
projective lines avoid all three vertices. Therefore the number of three-point-plus-one-line minimum bases is
\[
\frac{g}{6},
\]
and the dual class has the same size. Summing the four classes gives
\[
2\frac{g}{24}+2\frac{g}{6}
=
\frac{5g}{12}
=
\frac{5}{12}p^3(p^3-1)(p^2-1).
\tag{7}
\]

## Verification

The accompanying `verify.py` was read from its actual packaged path before replay.

For \(p=2\) and \(p=3\), it constructs all projective points and lines directly over \(\mathbf F_p\), builds the subgroup-intersection graph from incidence, enumerates every element of \(\operatorname{PGL}(3,p)\), verifies the graph action and group orders, and computes pointwise stabilizers with exact bit masks.

For \(p=2\), all two-vertex subsets fail and exactly \(56\) three-vertex subsets are bases, split as \(28\) point triples and \(28\) line triples.

For \(p=3\), all three-vertex subsets fail and exactly \(2340\) four-vertex subsets are bases. Their type counts are \(234\) four-point frames, \(936\) three-point-plus-one-line bases, \(936\) dual bases, \(234\) four-line frames, and no two-plus-two bases.

The counting identities are additionally checked for \(p=5,7,11\).

Exact replay output:

```text
p=2: |PGL|=168, minimum determining sets=56, type counts={3: 28, 0: 28}
p=3: |PGL|=5616, minimum determining sets=2340, type counts={4: 234, 3: 936, 1: 936, 0: 234}
odd-prime counting identities checked for p=3,5,7,11
VERIFY_OK
```

The finite calculations corroborate the proof. The arbitrary-prime statement rests on the projective stabilizer arguments and the explicit classification above.

## Relationship to prior work

Kayacan and Yaraneri study isomorphism of intersection graphs of finite abelian groups; this establishes the same subgroup-intersection object as an algebraically meaningful invariant. Kayacan later treats \(C_p^3\) explicitly in the \(K_{3,3}\)-free classification, observing that its \(p^2+p+1\) maximal subgroups are two-dimensional subspaces and pairwise intersect nontrivially.

Shahsavari and Khosravi prove in general that group automorphisms induce automorphisms of subgroup-intersection graphs, with kernel the power automorphisms. Their theorem supplies an injection from the appropriate quotient of \(\operatorname{Aut}(G)\) into the graph automorphism group but does not determine the pointwise bases considered here.

A prior public comparison on elementary-abelian join graphs, opaque identifier `8185c52da7d2`, proves \(\operatorname{PGL}(d,p)\) projective rigidity for the join graph. In rank three its point-plane cross edges are the complement of the incidence cross edges used here, so its automorphism theorem already implies the structural identification (1). Accordingly, (1) is treated as prior background rather than as the originality claim. That comparison contains no determining-set, base-size, minimum-base-classification, or minimum-base-count statement.

The determining-set invariant is standard in graph symmetry, following Boutin. The result here specializes it to the subgroup-intersection geometry and classifies every optimal mixed point-plane base rather than only giving a numerical base size.

## Limitations

The theorem is specific to rank three. In higher rank the subgroup-intersection graph contains intermediate dimensions and the simple point-line projective-plane classification of minimum bases no longer applies directly.

The field is prime because the group is \(C_p^3\). Over a nonprime finite field, semilinear field automorphisms enlarge the natural projective action.

The automorphism-group identity itself is implication-covered by the prior join-graph comparison described above; originality is claimed only for the determining-number theorem, complete minimum-set classification, and exact count.

No distinguishing-number formula is asserted.

## References

1. S. Kayacan and E. Yaraneri, “Abelian Groups With Isomorphic Intersection Graphs,” arXiv:1310.5343, first submitted 20 October 2013; *Acta Mathematica Hungarica* 146 (2015), 107–127.
2. S. Kayacan, “\(K_{3,3}\)-free Intersection Graphs of Finite Groups,” arXiv:1512.05113, first submitted 16 December 2015; *Communications in Algebra* 45 (2017), 2466–2477. The published classification lists primary MSC 20D99.
3. H. Shahsavari and B. Khosravi, “On the intersection graph of a finite group,” *Czechoslovak Mathematical Journal* 67 (2017), 1145–1153. DOI: 10.21136/CMJ.2017.0446-16.
4. D. L. Boutin, “Identifying Graph Automorphisms Using Determining Sets,” *Electronic Journal of Combinatorics* 13 (2006), R78. DOI: 10.37236/1104.
