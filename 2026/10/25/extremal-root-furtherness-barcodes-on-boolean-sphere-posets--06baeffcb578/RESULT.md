# Extremal-root furtherness barcodes on Boolean sphere posets
## Finding
For every integer \(n\ge3\), let \(P_n\) be the finite poset of nonempty proper subsets of \([n]\), ordered by inclusion and equipped with its Alexandrov topology. For \(x,y\in P_n\) set
\[
U_y=\{z\in P_n:z\subseteq y\},\qquad \Psi_x(y)=|U_y\setminus U_x|.
\]
For each real \(t\ge0\), let \(F_x(t)\) be the order complex of the full subposet on those \(y\) with \(\Psi_x(y)\le t\). This is the rooted furtherness filtration, with inclusive thresholds. Over **every coefficient field**, the complete ordinary persistent-homology barcode is as follows.

**Atom root:** For \(x=\{1\}\), there is exactly one essential degree-zero interval \([0,\infty)\). For each integer \(1\le j\le n-2\), there are exactly \(\binom{n-1}{j}\) intervals in degree \(j-1\), all equal to
\[
[2^j-1,\,2^{j+1}-2).
\]
There is exactly one essential interval \([2^{n-1}-1,\infty)\) in degree \(n-2\). There are no other positive-length intervals.

**Coatom root:** For \(x=[n]\setminus\{1\}\), there is exactly one essential degree-zero interval \([0,\infty)\). For each integer \(0\le k\le n-3\), there are exactly \(\binom{n-2}{k}\) intervals in degree \(k\), all equal to
\[
[2^k,\,2^{k+1}).
\]
There is exactly one essential interval \([2^{n-2},\infty)\) in degree \(n-2\), and no others. These formulas include degree-zero transient intervals in addition to the unique essential component.

Thus, for this canonical finite-space sphere, rooted furtherness creates an all-degree sequence of binomially many short-lived homology classes at exponentially separated thresholds. The natural atom and coatom roots have different full barcodes, even though the unfiltered order complex is the same sphere \(S^{n-2}\).

## Assumptions and scope
The Alexandrov opens are downward-closed subsets. Each open set \(U_y\) includes every nonempty subset of \(y\), including \(y\) itself. The furtherness weight is the literal cardinality of the set difference, rather than a Hamming metric or graph distance. Homology is ordinary homology of the geometric realization of the order complex (equivalently, the homology of the finite-space filtration by the finite-space/order-complex weak equivalence). In every displayed interval the birth endpoint is included and a finite death endpoint excluded. All statements hold for all integers \(n\ge3\), any coefficient field, and all real filtration parameters \(t\ge0\). The two roots represent the two extremal rank types under relabeling.

A useful exact model is the following. Write \(Y=[n]\setminus\{1\}\), and let \(\Delta(W)\) denote the full simplex on vertex set \(W\). A simplicial complex is determined by its nonempty face poset, and order complexes of face posets are its barycentric subdivisions. Therefore all the following simplicial identifications are natural in the filtration parameter, not merely stagewise homotopy equivalences.

## Proof
**1. Weights and the atom filtration.** For any nonempty proper \(B\subset[n]\), counting nonempty subsets gives the general identity
\[
\Psi_x(B)=2^{|B|}-2^{|B\cap x|}.
\]
For \(x=\{1\}\), this becomes \(2^{|B|}-2\) when \(1\in B\), and \(2^{|B|}-1\) otherwise. These are exactly the possible filtration weights. For every \(1\le j\le n-1\), just after the threshold \(t=2^j-2\) and before \(2^j-1\), the permitted nonempty subsets form the face poset of
\[
A_j=\{1\}*\operatorname{skel}_{j-2}\Delta(Y),
\]
where \(\operatorname{skel}_{-1}\Delta(Y)=\{\varnothing\}\). This is a cone. All faces without \(1\) in \(A_j\) are included in its base, so the equality is literal.

At \(t=2^j-1\), for \(1\le j\le n-2\), all nonempty subsets of cardinality at most \(j\), and no larger ones, are present. The resulting simplicial complex is \(\operatorname{skel}_{j-1}\Delta([n])\). At \(j=n-1\), all proper nonempty subsets are present and the simplicial complex is the boundary \(\partial\Delta([n])\), a sphere \(S^{n-2}\). Every positive-degree homology class at a skeleton stage is killed upon entering the next cone stage; the same holds for reduced degree-zero classes. Thus all nonessential bar lengths and endpoints follow from the homology ranks of these skeletons. The final sphere contributes the essential degree-\(n-2\) class.

**2. Skeleton homology with integral control.** For a simplex on \(N\ge2\) vertices, its \(r\)-skeleton with \(0\le r\le N-2\) is homotopy equivalent to
\[
\bigvee^{\binom{N-1}{r+1}} S^r.
\]
For \(r=0\), this means \(N\) discrete points, equivalently a wedge of \(N-1\) copies of \(S^0\), and homology is reduced in degree zero. To see this directly, fix one vertex \(v\). Pair every nonempty face \(\sigma\) not containing \(v\) of size at most \(r\) with \(\sigma\cup\{v\}\). Every matched pair is a free elementary-collapse pair in a suitable decreasing-dimensional order; equivalently, the associated element matching is acyclic, since removing \(v\) cannot occur along an unmatched upward move. One critical vertex remains, together with the \(\binom{N-1}{r+1}\) faces of size \(r+1\) not containing \(v\). The resulting CW complex has a single zero-cell and cells only in dimension \(r\), giving the displayed wedge; the \(r=0\) case is immediate. This provides integer, field-independent homotopy information. With \(N=n\) and \(r=j-1\), the transient multiplicity is \(\binom{n-1}{j}\), exactly as asserted.

**3. The coatom filtration.** Take \(x=Y\). If \(1\notin B\), then \(B\subseteq Y\) and the weight is zero. If \(B=\{1\}\cup S\), for \(S\subseteq Y\) of cardinality \(k\), its weight is \(2^k\). Therefore, for each \(0\le k\le n-2\) and \(2^k\le t<2^{k+1}\), the allowed simplicial complex is
\[
C_k=\Delta(Y)\cup\bigl(\{1\}*\operatorname{skel}_{k-1}\Delta(Y)\bigr).
\]
The upper bound \(k\le n-2\) is forced by excluding the full subset \([n]\). The two terms are contractible, and their intersection is the \((k-1)\)-skeleton of \(\Delta(Y)\). For \(k\ge1\), the intersection is nonempty and the homotopy pushout of these inclusions is its suspension. Thus
\[
C_k\simeq\bigvee^{\binom{n-2}{k}}S^k.
\]
For \(k=0\), the terms are disjoint (the second term is the isolated vertex \(1\)), so \(C_0\simeq S^0\), agreeing with \(\binom{n-2}{0}=1\). At \(k=n-2\), the common intersection is the full boundary \(\partial\Delta(Y)\), and \(C_{n-2}=\partial\Delta([n])\simeq S^{n-2}\). Every preceding nonzero reduced homology group dies when the next filtration threshold introduces a space whose nonzero reduced homology is in a strictly higher degree. Thus the stated coatom intervals are exact; the unique connected-component class survives throughout.

**4. Persistent maps and coefficient independence.** The order-complex functor on face posets realizes barycentric subdivision, naturally under every subcomplex inclusion in both filtrations. Therefore the described thresholds identify the genuine persistent chain complexes and their inclusion-induced homology maps. At a given positive-length interval's birth and strictly before its death, the homology group in that degree is precisely the stated free vector space; at its death threshold that degree's homology is zero (apart from the one persistent degree-zero component), so each bar has exactly the claimed death. No hidden crossing of bars of the same homological degree is possible because all intermediate nontrivial stages have disjoint homological degrees and the intervening atom stages are contractible. The elementary-collapse and cone arguments work over the integers, implying the formulas over any field.

## Verification
The included standalone `verify.py` computes persistent homology by exact binary-column reduction on the full proper-face poset (filtered according to the literal furtherness count) for both root types and every \(3\le n\le8\). It compares every interval endpoint, homological degree, and multiplicity with the formulas. A separate implementation constructs the order complex **directly from its chains**, without passing to the original simplex face complex, for every \(3\le n\le5\). Both calculations produce the predicted barcodes and terminate with `VERIFY_OK` and `DIRECT_ORDER_VERIFY_OK`. These finite tests provide independent implementation checks; they do not substitute for the all-\(n\) proof.

For example, at \(n=5\), the atom root has \(4\) reduced degree-zero intervals \([1,2)\), \(6\) degree-one intervals \([3,6)\), \(4\) degree-two intervals \([7,14)\), and one essential degree-three interval born at \(15\), in addition to its essential degree-zero interval. The coatom root has one extra degree-zero interval \([1,2)\), \(3\) degree-one intervals \([2,4)\), \(3\) degree-two intervals \([4,8)\), and one essential degree-three interval born at \(8\).

## Relationship to prior work
Badra and Singh introduced furtherness for finite topological spaces in March 2026 and established the cardinality identity underlying the weights here. Their October 2026 paper introduced the associated persistence diagrams and studied degree-zero features and their stabilization. The present result instead determines **every degree** and **every exact birth/death multiplicity** for two natural extremal root orbits on the canonical finite Boolean-sphere model.

Earlier studies of rank-selected Boolean-lattice order complexes analyze fixed collections of allowed subset ranks, rather than the root-weighted, successively changing allowed faces and their persistent inclusion maps. A published classification of punctured Boolean-sphere posets addresses the different question of removing one poset element and comparing finite-space contractibility with weak contractibility. A published rank-span-two Boolean complex calculation studies local chain rank differences and its symmetric-group character; it does not give either rooted furtherness barcode. Those prior statements do not imply the formulas without a new calculation of the weighted filtrations.

## Limitations
The result concerns only atom and coatom roots, not the full classification of intermediate-rank roots. Ordinary persistent homology of order-complex realizations is studied; no independent claim about finite-space homotopy equivalence of different filtration stages is made. The argument is exact for all \(n\ge3\) and all coefficient fields, while the independent computations cover only \(n\le8\) (and direct order complexes \(n\le5\)). Bibliographic priority cannot be guaranteed against inaccessible, unpublished, or unindexed equivalent work; no such covering result was identified in the inspected sources.

## References
1. A. Badra and V. Singh, “Persistence diagrams of finite topological spaces,” arXiv:2610.16386v1 (first public version October 12, 2026), https://arxiv.org/abs/2610.16386 .
2. A. Badra and V. Singh, “Furtherness in finite topological spaces,” arXiv:2603.18580v1 (first public version March 19, 2026), https://arxiv.org/abs/2603.18580 .
3. P. Hersh and S. Sundaram, “Stability and ribbon bases for the rank-selected homology of geometric lattices,” arXiv:2604.06479v1 (first public version April 7, 2026), https://arxiv.org/abs/2604.06479 .
4. “A rank dichotomy for punctured Boolean sphere posets” (2026), published comparison concerning finite-space contractibility after one-point deletion.
5. “Symmetric-group characters and contractible quotients of rank-span-two Boolean complexes” (2026), published comparison concerning a different rank-span filtration.
