# Catalan edge enumerator and gap-free edge spectrum of the set-homogeneous hypergraph \(M_3\)

## Finding

Let \(M_3=(M,E)\) be the countably infinite set-homogeneous but nonhomogeneous \(3\)-hypergraph constructed by Assari--Hosseinzadeh--Macpherson from the unique strongly dense \(2\)-regular ordered \(C\)-set \((M,C,\le)\). For \(n\ge1\), let \(p_{n,e}\) be the number of isomorphism types of \(n\)-vertex induced subhypergraphs of \(M_3\) with exactly \(e\) hyperedges, and put
\[
P_n(q)=\sum_{e=0}^{\binom n3}p_{n,e}q^e.
\]
Then
\[
\boxed{P_1(q)=1,\qquad
P_n(q)=\sum_{i=1}^{n-1}q^{i\binom{n-i}{2}}P_i(q)P_{n-i}(q)\quad(n\ge2).}
\]

Three consequences are immediate and useful.

First,
\[
\boxed{P_n(1)=C_{n-1}},
\]
so the age profile of \(M_3\) is the Catalan sequence \(1,1,2,5,14,42,132,\ldots\). Second,
\[
\boxed{P_n(q)=q^{\binom n3}P_n(q^{-1})},
\]
so the distribution by edge count is palindromic. Third, if
\[
S_n=\{e:p_{n,e}>0\},
\]
then
\[
\boxed{S_5=\{0,1,2,3,4,6,7,8,9,10\}}
\]
and
\[
\boxed{S_n=\{0,1,\ldots,\binom n3\}\quad\text{for every }n\ge6.}
\]
Thus five vertices have a single forbidden edge count, namely \(5\), whereas from six vertices onward every possible number of hyperedges occurs among finite induced substructures of \(M_3\).

The first nontrivial polynomials are
\[
P_3(q)=1+q,
\]
\[
P_4(q)=1+q+q^2+q^3+q^4,
\]
and
\[
P_5(q)=1+q+q^2+2q^3+2q^4+2q^6+2q^7+q^8+q^9+q^{10}.
\]
The \(P_4\) row agrees with the source paper's explicit statement that its five four-vertex configurations carry \(0,1,2,3,4\) edges respectively.

The same tree description gives the injective ordered-tuple orbit count
\[
\boxed{a_n=n!C_{n-1}=\frac{(2n-2)!}{(n-1)!}},
\]
beginning \(1,2,12,120,1680,30240,665280,\ldots\). This orbit formula is included as a corollary; the retained new content of this finding is the hypergraph age edge-enumerator, its palindromy, and the exact edge-count spectrum.

## Assumptions and scope

The primary source proves that there is a unique countably infinite strongly dense \(2\)-regular ordered \(C\)-set \((M,C,\le)\), that it is homogeneous, and that its associated hypergraph \(M_3\) is set-homogeneous but not homogeneous. It also proves
\[
\operatorname{Aut}(M_3)=\operatorname{Aut}(M,C,\le).
\]
For distinct \(x<y<z\), the source's definition of \(E\) simplifies to
\[
E(x,y,z)\iff C(x;y,z).
\]
The source further recalls the standard semilinear-tree representation of a \(C\)-relation: points of the \(C\)-set are maximal chains, and \(C(x;y,z)\) says that \(y,z\) agree farther up the semilinear tree than \(x\) does with them.

The claim concerns isomorphism types occurring in the age of this specific \(M_3\). It does not claim that Catalan enumeration of plane full binary trees is new. Older oligomorphic-group literature may already contain the unrefined Catalan subset profile of the underlying ordered \(C\)-set under another notation such as \(\partial PT_3\); the new assertion retained here is the edge-refined recursion and its consequences for \(M_3\).

## Proof

Take a finite subset \(A\subset M\), and list its points in the inherited order. In the semilinear-tree representation of the \(2\)-regular \(C\)-set, suppress all nodes that do not branch on the selected maximal chains. The resulting finite hierarchy is a rooted full binary tree whose leaves are the points of \(A\). Compatibility of \(C\) with \(\le\) makes the two cones at every branching node consecutive intervals in the leaf order, so this is a plane full binary tree. Conversely, binary branching and strong density let every finite plane full binary tree occur by recursively choosing points in the two cones. Thus finite induced \((C,\le)\)-types on \(n\) points are exactly plane full binary trees on \(n\) leaves.

Because \((M,C,\le)\) is homogeneous, two finite subsets lie in the same \(\operatorname{Aut}(M,C,\le)\)-orbit exactly when their plane trees are isomorphic. Because this automorphism group equals \(\operatorname{Aut}(M_3)\), the same is true for \(M_3\)-subset orbits. Finally, set-homogeneity of \(M_3\) identifies subset orbits with isomorphism types of induced hypergraphs. Hence plane full binary trees on \(n\) leaves index the isomorphism types counted by \(P_n\), one tree type per hypergraph type.

Now split such a tree at its root. Suppose its left subtree has \(i\) leaves and its right subtree has \(j=n-i\) leaves. Hyperedges lying wholly in one side contribute the exponents from \(P_i\) and \(P_j\). Consider a cross triple. If it has one leaf on the left and two on the right, then in increasing leaf order it is \(x<y<z\) with \(y,z\) in the same root cone and \(x\) in the other cone, so \(C(x;y,z)\) holds and the triple is an edge. There are
\[
i\binom j2
\]
such triples. If the triple has two leaves on the left and one on the right, then the two left leaves cluster and \(C(x;y,z)\) fails, so it is a nonedge. Therefore the root split contributes the factor
\[
q^{i\binom j2},
\]
and summing over all \(i=1,\ldots,n-1\) proves the displayed recurrence.

Setting \(q=1\) gives
\[
P_n(1)=\sum_{i=1}^{n-1}P_i(1)P_{n-i}(1),\qquad P_1(1)=1,
\]
which is the Catalan recurrence, hence \(P_n(1)=C_{n-1}\).

For palindromy, reflect a plane tree left-to-right. On every three chosen leaves, compatibility of the binary \(C\)-relation says that exactly one of the two extreme leaves is separated from the other pair. Reversing left and right therefore toggles whether that triple satisfies the \(M_3\) edge rule. Reflection sends an \(e\)-edge type to a \(\binom n3-e\)-edge type, proving
\[
P_n(q)=q^{\binom n3}P_n(q^{-1}).
\]
This is also consistent with the source's observation that reversing the order produces the complement and that \(M_3\) is isomorphic to its complement.

It remains to prove the edge-count spectrum. Directly from the recurrence,
\[
S_5=\{0,1,2,3,4,6,7,8,9,10\}.
\]
For \(n=6\), the root splits \(5+1\) and \(1+5\) produce all values except \(5\) and \(15\), while the splits \(4+2\) and \(2+4\) produce \(5\) and \(15\), respectively. Hence
\[
S_6=\{0,1,\ldots,20\}.
\]
Assume now \(n\ge7\) and inductively that
\[
S_{n-1}=\{0,\ldots,\binom{n-1}{3}\}.
\]
The root split \((n-1)+1\) contributes the whole interval
\[
[0,\binom{n-1}{3}],
\]
while the split \(1+(n-1)\) contributes
\[
[\binom{n-1}{2},\binom n3].
\]
For \(n\ge7\), these intervals overlap because
\[
\binom{n-1}{3}\ge \binom{n-1}{2}-1.
\]
Their union is therefore every integer from \(0\) to \(\binom n3\), completing the induction.

Palindromy implies that the uniform average number of edges over the \(C_{n-1}\) isomorphism types is exactly \(\frac12\binom n3\). Finally, since the global order is preserved by every automorphism, the setwise stabilizer of a finite subset fixes its inherited increasing enumeration pointwise. Each subset orbit therefore yields \(n!\) injective ordered-tuple orbits, giving \(a_n=n!C_{n-1}\).

## Verification

The bundled checker generates plane full binary trees recursively rather than using Catalan numbers as its generator. For each tree it labels leaves in-order, computes the \(C\)-relation by longest common prefixes of root-to-leaf paths, and evaluates the \(M_3\) edge rule on every triple. It independently computes edge counts from the root-split formula and checks equality for every tree through ten leaves.

It also computes the polynomial recurrence independently and compares it coefficient-for-coefficient with direct tree enumeration through ten leaves. It verifies Catalan totals, palindromy, the five-vertex missing midpoint, and the complete edge-count spectrum for \(6\le n\le10\). As a separate finite isomorphism check, it canonically relabels every generated \(3\)-hypergraph under all vertex permutations through six vertices and confirms that the number of distinct unlabelled hypergraphs is exactly \(C_{n-1}\). The script returns `VERIFY_OK`.

## Relationship to prior work

Assari--Hosseinzadeh--Macpherson provide all structural ingredients used here: the strongly dense ordered \(2\)-regular \(C\)-set, its homogeneity, the definition of \(M_3\), equality of the two automorphism groups, set-homogeneity, the five four-vertex configurations, and self-complementarity after order reversal. They do not state the polynomial recurrence above, a Catalan formula for the age of \(M_3\), the palindromic edge enumerator, or the exact all-edge-count spectrum from six vertices onward.

The source itself points to older oligomorphic-permutation-group literature for the treelike structures and notes that their subset-orbit profiles have at most exponential growth. The pure Catalan count of plane full binary trees is classical. Accordingly, novelty is not claimed for Catalan enumeration in isolation; it is claimed for the edge-refined age interpretation of \(M_3\), especially the recurrence and the single five-vertex gap followed by a gap-free spectrum.

Targeted published-finding corpus searches covered the names \(M_3\), set-homogeneous hypergraphs, ordered \(C\)-sets, \(\partial PT_3\), Catalan age/profile terminology, edge enumerators, edge-count spectra, and rooted-binary-tree formulations. Targeted web searches additionally used the exact polynomial fragments, the first Catalan profile values, and rooted-triple language. No covering statement was located.

## Limitations

The bridge from finite ordered \(C\)-sets to plane full binary trees is a standard treelike interpretation rather than a theorem stated verbatim in the primary paper. The paper supplies the semilinear representation, binary regularity, compatible order, strong density, and homogeneity from which the bridge follows. Because the Catalan profile of related oligomorphic tree groups may be classical under old notation, residual folklore risk remains for the unrefined count. The finite checker verifies the combinatorial consequences but does not replace the infinite homogeneity and set-homogeneity arguments from the source.

## References

1. Amir Assari, Narges Hosseinzadeh, and Dugald Macpherson, *Set-homogeneous hypergraphs*, arXiv:2202.09613, first submitted 19 February 2022; Journal of the London Mathematical Society 108 (2023), 1852--1885, DOI 10.1112/jlms.12796.
2. Peter J. Cameron, *Oligomorphic Permutation Groups*, London Mathematical Society Lecture Note Series 152, Cambridge University Press, 1990, DOI 10.1017/CBO9780511549809.
3. OEIS A000108, Catalan numbers, used only as a classical enumeration cross-check.
