# Semitotal domination polynomial and all minimal sets of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and deleted perfect matching
\[
M=\{a_i b_i:1\le i\le n\}.
\]

Its semitotal-domination polynomial, in which the coefficient of \(z^k\) counts semitotal dominating sets of cardinality \(k\), is
\[
\mathcal S_n(z)
=
2z^n+
\bigl((1+z)^n-1-nz\bigr)^2
+2nz^2\bigl((1+z)^{n-1}-1\bigr).
\tag{1}
\]

The inclusion-minimal semitotal dominating sets are exactly the following three types:

1. the two partite classes \(A\) and \(B\);
2. the triples
\[
\{a_i,b_i,b_j\},\qquad \{a_i,a_j,b_i\},\qquad i\ne j;
\]
3. the four-vertex sets
\[
\{a_i,a_j,b_k,b_\ell\}
\]
with \(i,j,k,\ell\) pairwise distinct.

Hence the polynomial enumerating inclusion-minimal semitotal dominating sets by size is
\[
\mathcal M_n(z)
=
2z^n+2n(n-1)z^3+
\binom n2\binom{n-2}{2}z^4.
\tag{2}
\]
The last term is zero for \(n=3\).

In particular,
\[
\gamma_{t2}(\operatorname{Cr}_n)=3,
\qquad
\Gamma_{t2}(\operatorname{Cr}_n)=n.
\]
The equality for the upper semitotal domination number is already implied by the published regular-graph bounds; the new content here is the complete feasible-set polynomial and the exact classification of all inclusion-minimal sets.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. A set \(S\subseteq V(G)\) is semitotal dominating when it is dominating and every vertex of \(S\) has another vertex of \(S\) at distance at most \(2\). It is inclusion-minimal when no proper subset is semitotal dominating.

The claim concerns connected crown graphs \(\operatorname{Cr}_n\) with \(n\ge3\).

## Proof
Write
\[
p=|S\cap A|,\qquad q=|S\cap B|.
\]
The only pairs of crown vertices at distance \(3\) are the deleted matched pairs \(a_i,b_i\). Therefore every set of at least three vertices automatically satisfies the semitotal witness condition: for any selected vertex, at most one other selected vertex can be at distance \(3\), so another selected vertex lies at distance at most \(2\).

It remains to characterize domination. If \(p=q=0\), domination fails. If \(q=0\), domination forces every vertex of \(A\) into \(S\), so \(S=A\); symmetrically, \(S=B\) is the only case with \(p=0\). If \(p,q\ge2\), every unselected vertex sees a selected vertex in the opposite part, so domination is automatic.

Suppose \(p=1\), say \(S\cap A=\{a_i\}\), and \(q\ge2\). Every unselected \(A\)-vertex is dominated because at least two \(B\)-vertices are selected. On the \(B\)-side, the only vertex not adjacent to \(a_i\) is \(b_i\), so domination holds exactly when
\[
b_i\in S.
\]
The case \(q=1\), \(p\ge2\) is symmetric. Finally, a two-vertex dominating set must be a deleted matched pair \(\{a_i,b_i\}\), but its two vertices are at distance \(3\), so it is not semitotal dominating. This proves the complete set classification.

For enumeration, the two one-sided sets contribute \(2z^n\). Sets with \(p,q\ge2\) contribute
\[
\left(\sum_{p=2}^{n}\binom np z^p\right)^2
=
\bigl((1+z)^n-1-nz\bigr)^2.
\]
For \(p=1\), choose the unique \(a_i\), force \(b_i\), and then choose a nonempty subset of the remaining \(n-1\) vertices of \(B\). This contributes
\[
nz^2\bigl((1+z)^{n-1}-1\bigr),
\]
and symmetry doubles it. Equation (1) follows.

We next classify inclusion-minimal sets. Both \(A\) and \(B\) are minimal because deleting any vertex leaves an undominated vertex in the same part. In the case \(p=1\), minimality forces \(q=2\), producing precisely \(\{a_i,b_i,b_j\}\) with \(i\ne j\); the symmetric triples give the second family.

If \(p,q\ge2\), minimality forces \(p=q=2\), since otherwise deleting a vertex from a side of size at least three leaves at least two selected vertices on both sides. Write the selected index sets as
\[
I=\{i,j\},\qquad J=\{k,\ell\}.
\]
Deleting \(a_i\) leaves one selected \(A\)-vertex \(a_j\); the resulting set remains dominating exactly when \(b_j\) is selected. Thus minimality requires \(j\notin J\), and similarly \(i\notin J\). Hence
\[
I\cap J=\varnothing.
\]
Conversely, if the two index pairs are disjoint, deleting any selected vertex creates the one-versus-two configuration in which the matched opposite of the remaining singleton is absent, so domination fails. These and only these four-vertex sets are minimal.

There are \(2n(n-1)\) minimal triples and
\[
\binom n2\binom{n-2}{2}
\]
minimal four-vertex sets, proving (2). The smallest minimal size is \(3\), and the largest is \(n\).

## Verification
The included checker constructs \(\operatorname{Cr}_n\) for \(3\le n\le7\), computes all-pairs distances by breadth-first search, and tests every vertex subset directly against the semitotal domination definition. It independently compares the result with the structural classification, every coefficient of (1), and every coefficient of (2).

Across the five tested graphs it checks \(21{,}824\) vertex subsets. The direct test and both formulas agree in every case.

## Relationship to prior work
Upper semitotal domination was explicitly studied in 2017. That work proves that a \(k\)-regular graph with \(k\ge3\) has upper semitotal domination number at most half its order, while the corresponding bound for triangle-free \(2\)-regular graphs also gives the six-cycle value. Applied to the \((n-1)\)-regular crown graph of order \(2n\), these bounds already imply the upper estimate \(\Gamma_{t2}(\operatorname{Cr}_n)\le n\); the partite class \(A\) or \(B\) gives equality. Accordingly, the scalar upper value is not claimed as new.

A 2019 full-text treatment characterizes semitotal dominating sets in joins, coronas, and lexicographic products. Its stated graph-operation results do not specialize to crowns, and a targeted full-text search found no crown occurrence. The same source records the standard semitotal domination definition and MSC class \(05C69\).

Targeted literature and database searches under crown graph, deleted-perfect-matching, \(K_{n,n}-M\), semitotal-domination polynomial, and minimal semitotal dominating sets did not locate equation (1), equation (2), or the three-family minimal-set classification.

## Limitations
The upper semitotal domination number \(\Gamma_{t2}(\operatorname{Cr}_n)=n\) is a consequence of earlier general regular-graph bounds and is included only as a consistency consequence of the complete classification.

The result concerns semitotal domination, not secure semitotal domination, total domination, or restrained domination. The exhaustive verification through \(n=7\) is corroborative only; the arbitrary-\(n\) theorem follows from the structural proof.

A differently phrased or non-indexed all-set classification may exist. The 2017 upper-semitotal source was available through publisher metadata, abstract, and theorem summary rather than full article text; this is retained as an access-related originality risk, but it cannot cover the new all-set formulas merely through its general scalar bounds.

## References
1. M. A. Henning, “Edge Weighting Functions on Semitotal Dominating Sets,” Graphs and Combinatorics 33 (2017), 403–417, DOI 10.1007/s00373-017-1769-4.
2. I. S. Aniversario, S. R. Canoy Jr., F. P. Jamil, “On Semitotal Domination in Graphs,” European Journal of Pure and Applied Mathematics 12 (2019), 1410–1425, DOI 10.29020/nybg.ejpam.v12i4.3501.
