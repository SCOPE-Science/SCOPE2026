# Exact Catalan–double-factorial orbit tower for \(M_3<M_4<M_6\)

## Finding

Assari, Hosseinzadeh and Macpherson construct three set-homogeneous hypergraphs on the same countable domain and identify the strict reduct chain
\[
\operatorname{Aut}(M_3)=\operatorname{Aut}(M,C,<)
<\operatorname{Aut}(M_4)=\operatorname{Aut}(M,C)
<\operatorname{Aut}(M_6)=\operatorname{Aut}(M,D),
\]
where \((M,C,<)\) is the homogeneous strongly dense ordered binary-branching \(C\)-set, \((M,C)\) its homogeneous \(C\)-reduct, and \((M,D)\) the corresponding homogeneous 3-branching \(D\)-set.

Let \(a_i(n)\) denote the number of \(\operatorname{Aut}(M_i)\)-orbits on injective ordered \(n\)-tuples. Then
\[
\boxed{a_3(n)=n!C_{n-1}=2^{n-1}(2n-3)!!},
\]
\[
\boxed{a_4(n)=(2n-3)!!},
\]
and
\[
\boxed{a_6(1)=a_6(2)=1,\qquad a_6(n)=(2n-5)!!\quad(n\ge3).}
\]
Here \(C_m=\frac1{m+1}\binom{2m}{m}\) is the Catalan number and \((-1)!!=1\). The first seven injective profiles are therefore
\[
\begin{array}{c|rrrrrrr}
n&1&2&3&4&5&6&7\\ \hline
M_3&1&2&12&120&1680&30240&665280\\
M_4&1&1&3&15&105&945&10395\\
M_6&1&1&1&3&15&105&945.
\end{array}
\]

More structurally, the two strict reduct steps have uniform orbit fibers:
\[
\boxed{a_3(n)/a_4(n)=2^{n-1}\quad(n\ge1)},
\]
\[
\boxed{a_4(n)/a_6(n)=2n-3\quad(n\ge3).}
\]
Thus the entire orbit collapse along \(M_3\to M_6\) is exactly \(2^{n-1}(2n-3)\) in arity \(n\ge3\).

If repetitions are allowed, let \(b_i(n)\) count all ordered \(n\)-tuple orbits. Equality patterns give the exact Stirling transform
\[
\boxed{b_i(n)=\sum_{k=1}^n {n\brace k}a_i(k)}.
\]
The first seven full profiles are
\[
\begin{array}{c|rrrrrrr}
n&1&2&3&4&5&6&7\\ \hline
M_3&1&3&19&207&3211&64383&1581259\\
M_4&1&2&7&41&346&3797&51157\\
M_6&1&2&5&17&86&647&6665.
\end{array}
\]

## Assumptions and scope

The result concerns the specific hypergraphs \(M_3,M_4,M_6\) from *Set-homogeneous hypergraphs*. Their automorphism groups are not inferred from the hypergraph definitions here: the cited paper proves the identifications with the homogeneous ordered \(C\)-set, homogeneous \(C\)-set and homogeneous \(D\)-set, respectively, and explicitly records the strict chain of reduct groups.

The tree descriptions used below are the standard finite realizations of binary-branching \(C\)- and \(D\)-relations. A finite binary \(C\)-structure is the leaf structure of a rooted full binary tree. In the compatible ordered expansion, the order is the left-to-right leaf order of a planar embedding. A finite binary \(D\)-structure is the leaf structure of an unrooted full binary tree, with \(D(ab;cd)\) recording disjointness of the two leaf-to-leaf paths. These correspondences are structural input; the contribution claimed here is the exact orbit profile for this 2023 hypergraph reduct chain, including the uniform fiber laws and the full-tuple Stirling transforms.

## Proof

Because the three expansion structures are homogeneous and have exactly the automorphism groups of \(M_3,M_4,M_6\), two injective ordered tuples are in the same hypergraph automorphism orbit exactly when the coordinate-preserving map between their induced expansion structures is an isomorphism. Thus the coordinates act as fixed leaf labels \(1,\ldots,n\), and it is enough to count the corresponding labeled tree types.

For \(M_4\), finite \(C\)-substructures are rooted full binary trees with the \(n\) coordinate labels on their leaves, and the tree is uniquely recoverable from its leaf \(C\)-relation. Let \(r_n\) be their number. Starting from a rooted binary tree on \(n-1\) labeled leaves, a new leaf labeled \(n\) can be inserted either by subdividing one of its \(2n-4\) edges or by creating a new root above the old root and making the new leaf the other child. These \(2n-3\) insertion positions are reversible by deleting leaf \(n\) and suppressing the resulting degree-two vertex. Hence
\[
r_n=(2n-3)r_{n-1},\qquad r_1=1,
\]
so
\[
a_4(n)=r_n=(2n-3)!!.
\]

For \(M_3\), a compatible total order is exactly a left-to-right order obtained by choosing, at every internal vertex of the rooted binary tree, which child is left and which is right. A rooted full binary tree with \(n\) leaves has exactly \(n-1\) internal vertices. With coordinate labels fixed, no nontrivial tree automorphism fixes every leaf, so the \(2^{n-1}\) choices of local left/right orientation are all distinct and all compatible orders arise this way. Therefore
\[
a_3(n)=2^{n-1}a_4(n)=2^{n-1}(2n-3)!!.
\]
Using
\[
2^{n-1}(2n-3)!!=\frac{(2n-2)!}{(n-1)!}=n!C_{n-1},
\]
we obtain the Catalan form as well. This proves simultaneously that every orbit of the \(M_4\)-reduct has exactly \(2^{n-1}\) \(M_3\)-orbits above it.

For \(M_6\), finite \(D\)-substructures are unrooted full binary trees with labeled leaves. For \(n\ge3\), let \(u_n\) be their number. An unrooted full binary tree on \(n-1\) labeled leaves has \(2n-5\) edges. Subdivide any one of those edges and attach a new leaf labeled \(n\); deleting leaf \(n\) reverses the construction. Thus
\[
u_n=(2n-5)u_{n-1},\qquad u_3=1,
\]
and hence
\[
a_6(n)=u_n=(2n-5)!!\qquad(n\ge3).
\]
The group is 3-transitive, so the exceptional arities \(1,2\) each have one injective orbit as stated.

There is also a direct explanation of the second uniform fiber. Forgetting the root of a rooted labeled full binary tree means suppressing its degree-two root, yielding an unrooted labeled binary tree. Conversely, a root can be inserted into any edge of an unrooted binary tree. Such a tree with \(n\) leaves has exactly \(2n-3\) edges. Since all leaves are coordinate-labeled, distinct root edges give distinct rooted labeled types. Hence every \(M_6\) orbit has exactly \(2n-3\) \(M_4\) orbits above it, proving
\[
a_4(n)=(2n-3)a_6(n)\qquad(n\ge3).
\]

Finally, for a possibly noninjective ordered \(n\)-tuple, its equality pattern is a partition of the coordinate set into \(k\) nonempty blocks. There are \({n\brace k}\) such patterns. Ordering the blocks by their least coordinate turns the distinct tuple values into an injective ordered \(k\)-tuple, and automorphisms preserve the equality pattern. Summing independently over all equality partitions gives
\[
b_i(n)=\sum_{k=1}^n {n\brace k}a_i(k).
\]

## Verification

The bundled verifier constructs the relevant finite labeled tree species directly rather than merely evaluating the closed formulas.

For rooted non-plane binary trees it recursively enumerates unordered bipartitions of the leaf labels and recovers counts \(1,1,3,15,105,945,10395\) through seven leaves. For plane rooted trees it recursively enumerates ordered root splits through six leaves and checks that forgetting left/right choices has the uniform fiber size \(2^{n-1}\). To test the root-forgetting step independently, it suppresses the root of every generated rooted labeled tree, canonically identifies the resulting unrooted tree by its set of leaf-edge splits, and checks through seven leaves that there are \((2n-5)!!\) classes and every class has exactly \(2n-3\) rooted preimages.

It then checks all three displayed injective sequences, both collapse identities, and the three Stirling-transformed full-tuple sequences through arity seven. The replay ends with `VERIFY_OK`.

## Relationship to prior work

Assari--Hosseinzadeh--Macpherson supply the decisive model-theoretic identifications. They prove \(\operatorname{Aut}(M_3)=\operatorname{Aut}(M,C,<)\), \(\operatorname{Aut}(M_4)=\operatorname{Aut}(M,C)\), \(\operatorname{Aut}(M_6)=\operatorname{Aut}(M,D)\), and explicitly place them in the strict reduct chain used here. Their paper also recalls that these treelike homogeneous groups are oligomorphic and have long been studied through orbit growth, but it does not state the displayed tuple profiles or the two uniform collapse laws.

Bodirsky--Jonsson--Van Pham identify the finite substructures of the homogeneous binary-branching \(C\)-relation with leaf structures of finite rooted binary trees and note that the underlying tree is determined by the leaf relation. Almazaydeh--Macpherson likewise recall the correspondence between finite \(D\)-sets and leaves of finite unrooted graph-theoretic trees. Those correspondences make the enumerative reduction canonical.

The individual labeled binary-tree counts are classical. The originality claim is therefore not for the double-factorial or Catalan formulas as combinatorial sequences. It is for their exact simultaneous realization as the injective orbit tower of the specific \(M_3<M_4<M_6\) hypergraph reduct chain, the constant-size fibers \(2^{n-1}\) and \(2n-3\), and the resulting full ordered-tuple profiles. Targeted searches using the hypergraph names, the three automorphism groups, \(C\)- and \(D\)-relation terminology, Catalan/double-factorial formulas, and the collapse factors did not locate a covering statement.

## Limitations

The proof uses the published identifications of the hypergraph automorphism groups with their homogeneous treelike expansions; it does not reprove those definability results. The finite tree correspondences and their classical counts are not new.

The originality assessment has a real folklore risk. The automorphism groups of homogeneous \(C\)- and \(D\)-relations are classical oligomorphic groups, and older permutation-group literature studies their orbit growth. An equivalent individual profile could therefore have appeared in older work under tree or Jordan-group terminology even though the targeted searches and the directly inspected sources did not expose the integrated \(M_3<M_4<M_6\) orbit tower or its exact fiber laws.

## References

1. Amir Assari, Narges Hosseinzadeh, Dugald Macpherson, “Set-homogeneous hypergraphs,” *Journal of the London Mathematical Society* 108 (2023), 1852–1885. arXiv:2202.09613. DOI: 10.1112/jlms.12796.
2. Manuel Bodirsky, Peter Jonsson, Trung Van Pham, “The Complexity of Phylogeny Constraint Satisfaction,” *LIPIcs STACS 2016* 47, 20:1–20:13. arXiv:1503.07310. DOI: 10.4230/LIPIcs.STACS.2016.20.
3. Asma Ibrahim Almazaydeh, Dugald Macpherson, “Jordan permutation groups and limits of D-relations,” *Journal of Group Theory* 25 (2022), 447–508. arXiv:2009.04711. DOI: 10.1515/jgth-2020-0083.
