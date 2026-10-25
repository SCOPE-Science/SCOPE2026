# Thirteen five-spheres and duality-odd symmetry of the Heawood 2-independence complex

## Finding
Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane. A face of its \(2\)-independence complex \(K=\operatorname{Ind}_2(H)\) is a subset of the fourteen graph vertices whose induced connected components have at most two vertices. Then the **integral homotopy type** is
\[
K\simeq\bigvee^{13}S^5.
\]
The complete rational character of the natural full automorphism group of order \(336\) on \(\widetilde H_5(K;\mathbb Q)\) is explicitly determined below. In particular, with \(G=\operatorname{GL}_3(\mathbb F_2)\) the incidence-preserving subgroup and \(W\) its six-dimensional augmentation representation on the seven Fano points,
\[
\widetilde H_5(K;\mathbb Q)\big|_G\cong \mathbf 1\oplus 2W.
\]
The unique \(G\)-invariant line is negated by point–line duality. Thus no nonzero rational fifth-homology class is invariant under every graph automorphism.

## Assumptions and scope
Write the seven points and the seven line covectors as the nonzero elements of \(\mathbb F_2^3\). A point \(p\) and a line covector \(a\) are adjacent exactly when \(a\cdot p=0\) in \(\mathbb F_2\). Order both lists lexicographically and number the point vertices \(0\) through \(6\) and line vertices \(7\) through \(13\). This defines a simple cubic graph with exactly \(21\) edges and girth \(6\). For any simple graph, induced components of order at most two are equivalent to induced maximum degree at most one, so this is also its degree-one-independent vertex-set complex. The empty set is present as the empty simplex.

An invertible binary matrix \(A\) acts on points by \(p\mapsto Ap\) and on line covectors by \(a\mapsto(A^{-1})^{\mathsf T}a\). Symmetry of the incidence equation also gives the involution \(D\) swapping the point and line vertex labeled by the same binary triple. The matrices constitute \(G\), of order \(168\), and adjoining \(D\) gives the full automorphism group of order \(336\): every graph automorphism preserves or exchanges the connected graph's two bipartite parts, and every incidence-preserving point permutation preserves the Fano addition rule \(\{p,q,p+q\}\), hence is linear. The line permutation is then uniquely forced.

## Proof
**Finite acyclic matching.** Enumerate all \(2^{14}-1\) nonempty subsets, retaining a subset exactly when each selected vertex has at most one selected graph neighbor. The number of faces in dimensions \(0\) through \(6\) is
\[
(14,91,322,651,728,392,58),
\]
so there are \(2256\) nonempty faces. The complex is nonpure: it has \(70\) maximal five-simplices and \(58\) maximal six-simplices.

Starting with all nonempty faces unpaired, successively use pivot vertices \(0,1,\ldots,13\). At pivot \(v\), pair each still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) if this extension is also still unmatched; remove both from later stages. This gives \(1121\) pairs. The unmatched faces are the vertex with binary mask \(1\) and exactly thirteen five-simplices with binary masks
\[
1008,3300,5460,6712,8064,9826,10600,12160,12504,14208,15232,15744,16000.
\]
Here bit \(v\) of a mask records whether vertex \(v\) belongs to the simplex. Reverse each matched covering relation in the nonempty face-poset Hasse diagram and direct every other covering relation from a face to its facet. There are exactly \(10150\) such incidences. Complete topological sorting visits all \(2256\) vertices of this directed graph, so the matching is acyclic, without relying on an unverified matching rule. Forman's discrete Morse theorem now gives a CW complex with one \(0\)-cell and thirteen \(5\)-cells and no other cells. All attaching maps land at the single point, proving the displayed **integral** homotopy equivalence.

**Automorphism character.** Every graph automorphism permutes the complex's faces and acts on oriented simplicial chains. If a face \(\sigma\) is fixed setwise by a permutation \(g\), let \(c_g(\sigma)\) be the number of cycles of the restricted vertex permutation on that face, taking \(c_g(\varnothing)=0\). On a nonempty fixed face, its oriented Lefschetz contribution is \((-1)^{c_g(\sigma)+1}\). Because reduced homology occurs only in odd degree five, the Hopf trace formula yields
\[
\operatorname{tr}\bigl(g\mid\widetilde H_5(K;\mathbb Q)\bigr)
=\sum_{\substack{\sigma\in K\\g\sigma=\sigma}}(-1)^{c_g(\sigma)}.
\]
Exact enumeration of all \(168\) invertible matrices and all \(168\) duality-coset elements gives the following complete trace-by-order data:

| Symmetry subset | Element order | Number | Fifth-homology trace |
| --- | ---: | ---: | ---: |
| Incidence-preserving | \(1\) | \(1\) | \(13\) |
| Incidence-preserving | \(2\) | \(21\) | \(5\) |
| Incidence-preserving | \(3\) | \(56\) | \(1\) |
| Incidence-preserving | \(4\) | \(42\) | \(1\) |
| Incidence-preserving | \(7\) | \(48\) | \(-1\) |
| Incidence-exchanging | \(2\) | \(28\) | \(-1\) |
| Incidence-exchanging | \(6\) | \(56\) | \(-1\) |
| Incidence-exchanging | \(8\) | \(84\) | \(-1\) |

For each \(g\in G\), the computed trace satisfies \(\chi(g)=1+2(f(g)-1)\), where \(f(g)\) is its number of fixed Fano points. Since \(G\) acts doubly transitively on those seven points, its permutation representation splits over \(\mathbb Q\) as a trivial line plus the irreducible six-dimensional augmentation module \(W\). Equality of rational characters establishes \(\mathbf1\oplus2W\).

Averaging \(\chi\) over the \(168\) incidence-preserving elements gives a one-dimensional invariant space. The trace sum over the other \(168\) elements is \(-168\), so duality acts by \(-1\) on that invariant line. In particular, averaging over the full group gives zero invariants.

## Verification
Run `python3 verify.py` with Python's standard library. The complete standalone script reconstructs the Fano graph and all faces; records the matching and every reversed Hasse incidence; tests acyclicity by topological sort; checks simplicial boundary ranks over \(\mathbb F_2\); reconstructs all \(336\) automorphisms; and obtains each Lefschetz trace twice, from cycle counts and independently from inversion parity on oriented faces. It prints `VERIFY_OK` on success. The independent mod-two chain calculation has boundary ranks \((13,78,244,407,321,58)\) in degrees \(1\) to \(6\), and Betti vector \((1,0,0,0,0,13,0)\). Those field ranks are corroboration; the acyclic Morse reduction proves the full integral homotopy claim.

## Relationship to prior work
Zaker's 2015 work studies degree-bounded independent vertex sets and their numerical maxima, not the homotopy of their simplicial complexes. Deshpande and Singh's 2020 higher-independence classifications treat complete multipartite graphs, fully whiskered graphs, cycles, and perfect rooted trees. Abdelmalek and coauthors' later theorems concern chordal graphs, trees, and caterpillars. The cubic girth-six Heawood graph is in none of those stated classes. A recorded calculation of the Petersen \(2\)-independence complex gives \(S^3\) but no graph-family theorem covering this different graph. The known **ordinary** Heawood independence complex is \(\bigvee^6S^3\); its faces forbid every edge, whereas the present complex permits induced disjoint edges, so its topology and symmetry character cannot be inferred by substituting parameters. Likewise the Heawood two-matching complex uses graph **edges** as simplicial vertices and does not encode these graph-vertex subsets. The comparison is about statements and their implications, not merely titles.

## Limitations
This is an exact finite classification for \(\operatorname{Ind}_2\) of the Heawood graph and the stated automorphism representation; no formula is claimed for all cubic graphs, all incidence graphs, or other values of the higher-independence parameter. A lack of a located equivalent theorem is not proof that none exists; differently indexed or unpublished calculations may remain. All mathematical checks described here are reproducible computations and deductions, not an independent external scientific audit.

## References
1. M. Zaker, *Lower bounds for independence and k-independence number of graphs using the concept of degenerate degrees*, arXiv:1507.07194v1 (first public 2015-07-26), especially Section 3 on degree-one-independent vertex sets.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (first public 2020-01-15), definitions and homotopy-classification results.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1 (first public 2021-06-21).
4. *The 2-independence complex of the Petersen graph is a 3-sphere*, indexed mathematical result `156dc9567f6a`; *The Heawood independence complex is a wedge of six 3-spheres*, indexed mathematical result `dbd95019d1e2`; *The Heawood two-matching complex is a wedge of six 10-spheres*, indexed mathematical result `5bc5713358d6`. These concern distinct complexes as explained above.
