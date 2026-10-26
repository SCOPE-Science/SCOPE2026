# Three rank-three theories of finite Grassmann adjacency graphs

## Finding

For every prime power \(q\ge 2\), every integer \(n\ge 2\), and every \(1\le k<n\), let \(\Gamma_q(n,k)\) be the simple undirected graph whose vertices are the \(k\)-dimensional linear subspaces of \(\mathbf F_q^n\). Distinct vertices \(U,V\) are adjacent exactly when \(\dim(U\cap V)=k-1\). First-order formulas use only equality and this symmetric adjacency relation; there are no constants, dimension predicates, fields, or counting quantifiers.

**Theorem.** For arbitrary prime powers \(q,s\ge2\), admissible \((n,k)\) and \((m,\ell)\),

\[
\Gamma_q(n,k)\equiv_3\Gamma_s(m,\ell)
\quad\Longleftrightarrow\quad
\min\{k,n-k,3\}=\min\{\ell,m-\ell,3\}.
\]

Thus all these graphs fall into **exactly three** equivalence classes for sentences of first-order quantifier rank at most three. Within the Grassmann family, their least-order representatives have respectively \(3\), \(35\), and \(1395\) vertices, attained by \(\Gamma_2(2,1)\), \(\Gamma_2(4,2)\), and \(\Gamma_2(6,3)\). Consequently \(1395\) is the sharp uniform representative-size bound *within this family*.

There is also a cross-family collapse to ordinary Johnson graphs: writing \(J(n,k)\) for the graph on \(k\)-subsets with adjacency at intersection size \(k-1\), the three classes are represented, even outside the Grassmann family, by \(J(3,1)\), \(J(6,2)\), and \(J(7,3)\) respectively. These have \(3\), \(15\), and \(35\) vertices. The theorem does not say that the Grassmann and Johnson graphs are isomorphic.

The first versus the other two classes is distinguishable at quantifier rank two; the latter two agree at rank two and are distinguished at rank three.

## Assumptions and scope

All underlying fields are finite (including non-prime fields), and there are no constraints relating their characteristics or orders. Quantifier rank is the maximum nesting depth, rather than the total number of quantified variable occurrences. The symbol \(\equiv_3\) denotes agreement on **all** sentences with quantifier rank at most three, permitting Boolean combinations and quantifier alternation.

By the annihilator duality, \(\Gamma_q(n,k)\cong\Gamma_q(n,n-k)\); this is an isomorphism to the graph on subspaces of the dual vector space, which is again an \(n\)-dimensional \(\mathbf F_q\)-space. Hence it suffices to prove the statement for \(1\le k\le n/2\). This also explains the effective rank \(\min(k,n-k)\) in the theorem.

## Proof

**1. A precise three-round profile criterion.** Let \(G\) be any nonempty finite vertex-transitive simple undirected graph, and write \(E\) for adjacency. For an ordered pair of distinct vertices \((a,b)\), define its third-vertex profile

\[
P_G(a,b)=\left\{(\mathbf 1_{E(a,c)},\mathbf 1_{E(b,c)}):c\notin\{a,b\}\right\}.
\]

Record as well whether \(a,b\) are adjacent. All choices \(c=a\) or \(c=b\) have predetermined atomic diagrams and do not enter \(P_G(a,b)\). For the diagonal pair \((a,a)\), record whether an adjacent third vertex exists and whether a distinct nonadjacent third vertex exists. Vertex-transitivity makes the set of pair profiles available after a fixed first vertex independent of that first vertex.

For two such graphs, equality of the sets of available labeled pair profiles, **including the diagonal profile**, is equivalent to winning the three-round Ehrenfeucht–Fraïssé game. Indeed, after the first moves, the second move can be matched with the same equality/adjacency flag and third-vertex profile; the third move can then be matched according to its equality status and its two adjacency flags. Conversely, if a labeled second-move profile is available in one graph but not the other, Spoiler chooses that pair in two rounds and uses a flag in the symmetric difference of the profiles on the third round (or the corresponding diagonal witness). This proves the criterion for all rank-three formulas, including arbitrary quantifier alternation, and not only for existential formulas.

**2. All distinct-pair profiles.** Fix a prime power \(q\ge2\), \(2\le k\le n/2\), and two distinct \(k\)-spaces \(U,V\). Write

\[
t=k-\dim(U\cap V),\qquad 1\le t\le k.\]

Choose a direct-sum decomposition

\[
\mathbf F_q^n=H\oplus A\oplus B\oplus C,
\quad U=H\oplus A,\quad V=H\oplus B,
\]

where \(\dim H=k-t\), \(\dim A=\dim B=t\), and \(\dim C=n-k-t\). Choose ordered bases \(a_1,\ldots,a_t\) of \(A\) and \(b_1,\ldots,b_t\) of \(B\). We show exactly which of the four Boolean adjacency flags occur for a third, distinct \(k\)-space \(W\).

* **Nonadjacent to both, for every \(t\).** Since \(n\ge2k\), the complement \(C\) has a subspace \(C'\) of dimension \(k-t\). Define

  \[
  W=\langle a_i+b_i:1\le i\le t\rangle\oplus C'.
  \]

  Then \(\dim W=k\) and \(W\cap U=W\cap V=\{0\}\). Since \(k\ge2\), \(W\) is adjacent to neither \(U\) nor \(V\). Thus flag \((0,0)\) occurs for every distinct pair.

* **Adjacent to the first but not the second, for \(t\ge2\).** Set

  \[
  W=H\oplus\langle a_2,\ldots,a_t,a_1+b_1\rangle.
  \]

  Its intersections with \(U\) and \(V\) have dimensions \(k-1\) and \(k-t\), respectively. The second dimension is at most \(k-2\). Hence flag \((1,0)\) occurs; interchanging the two selected spaces gives \((0,1)\).

* **Adjacent to the first but not the second, for \(t=1\).** Write \(H=\langle h_1,\ldots,h_{k-1}\rangle\). Now \(\dim C=n-k-1\ge k-1\ge1\); choose \(0\ne c\in C\) and put

  \[
  W=\langle a_1,h_2,\ldots,h_{k-1},c\rangle.
  \]

  Its intersections with \(U,V\) have dimensions \(k-1,k-2\). This again gives \((1,0)\) and symmetrically \((0,1)\).

* **Adjacent to both, for \(t=1\).** Put \(W=H\oplus\langle a_1+b_1\rangle\). The two intersection dimensions are each \(k-1\), and \(W\) is distinct from both selected spaces. Thus flag \((1,1)\) occurs.

* **Adjacent to both, for \(t=2\).** Put \(W=H\oplus\langle a_1,b_1\rangle\). Again both intersections have dimension \(k-1\), giving \((1,1)\).

* **Adjacent to both is impossible for \(t\ge3\).** If such a \(W\) existed, then

  \[
  \dim(U\cap V)\ge\dim(U\cap W)+\dim(V\cap W)-\dim W\ge k-2,
  \]

  contradicting \(\dim(U\cap V)=k-t\le k-3\).

These constructions require only the existence of nonzero elements and independent subspaces; they work over **every** finite field, including characteristic two. Each constructed third space is distinct from both previously chosen spaces. We obtain the complete table:

| Pair separation | Adjacent pair? | Possible flags \((E(U,W),E(V,W))\) |
|---|---|---|
| \(t=1\) | Yes | \((0,0),(0,1),(1,0),(1,1)\) |
| \(t=2\) | No | \((0,0),(0,1),(1,0),(1,1)\) |
| \(3\le t\le k\) | No | \((0,0),(0,1),(1,0)\) |

Every \(t\in\{1,\ldots,k\}\) occurs because \(n\ge2k\). In the diagonal case \(U=V\), a distinct neighbor exists (replace one one-dimensional direction) and a distinct nonneighbor exists by choosing a disjoint \(k\)-space; both are available for all \(k\ge2\). Therefore the complete rank-three profile depends only on whether \(k=2\) or \(k\ge3\).

**3. The complete-graph case and exact separation.** For \(k=1\), every two distinct one-dimensional subspaces have zero intersection and hence are adjacent. The graph is complete on \((q^n-1)/(q-1)\ge3\) vertices, so all these graphs have one rank-three theory. The rank-two sentence

\[
\exists x\,\exists y\;(x\ne y\wedge\neg E(x,y))
\]

separates every \(k\ge2\) graph from the complete-graph class. Among the noncomplete graphs, the rank-three sentence

\[
\exists x\,\exists y\;\bigl[x\ne y\wedge\neg E(x,y)
\wedge\forall z\;\neg(E(x,z)\wedge E(y,z))\bigr]
\]

holds exactly when \(k\ge3\): take a pair with \(t=3\); for \(k=2\) every nonadjacent pair has \(t=2\) and a common neighbor. The two noncomplete classes have the same rank-two theory: in either, for every vertex there are distinct neighbors and nonneighbors, and every edge and nonedge exists. This proves the exact three-class classification and the rank threshold assertions.

**4. Cross-family comparison and optimal representatives.** For ordinary Johnson graphs, the three-round pair-extension calculation on \(J(3,1)\), \(J(6,2)\), and \(J(7,3)\) yields exactly the three profiles above. It can be checked directly by enumerating all \(3\), \(15\), or \(35\) subset-vertices, respectively, and is independently reproduced by the accompanying checker. The profile criterion therefore proves the asserted cross-family equivalences without assuming that induced subgraphs preserve first-order theory.

The Grassmann graph has the Gaussian-binomial number of vertices

\[
|V(\Gamma_q(n,k))|={n\brack k}_q
=\prod_{i=0}^{k-1}\frac{q^{n-i}-1}{q^{k-i}-1}.
\]

This number is increasing in \(n\) for fixed \(k\), and its central values \({2k\brack k}_q\) increase with \(k\): embed a \(k\)-space into a \((k+1)\)-space in two extra ambient dimensions. Gaussian-binomial polynomials have nonnegative coefficients in \(q\), so each nontrivial value increases with \(q\ge2\). Thus the least graph order in each of the effective ranks \(1\), \(2\), and at least \(3\) occurs at \((q,n,k)=(2,2,1),(2,4,2),(2,6,3)\). Their respective Gaussian-binomial values are \(3,35,1395\). The last class requires effective rank at least three, so no smaller Grassmann representative exists. This proves sharpness.

## Verification

The standalone `verify_grassmann.py` enumerates finite-field subspaces through reduced-row-echelon matrices, checks Gaussian-binomial vertex counts, and independently derives the actual adjacency flags for each distance-orbit representative. It completed for the eight sample parameter triples with field orders \(2\), \(3\), and \(4\), including \(1395\), \(11811\), and \(33880\)-vertex cases. It also computes the Johnson comparison profiles from subsets. Output is in `verification_output.txt`.

The separate `verify_logic.py` computes a full rank-three first-order type recursively from atomic graphs, with no reliance on the pair-profile reduction. It confirms the complete-graph comparison and \(\Gamma_2(4,2)\equiv_3 J(6,2)\), and distinguishes the Johnson representatives of the two noncomplete theories. Output is in `direct_output.txt`.

These computations check finite cases and two independent implementations, but **do not certify every prime power or parameter**. Universal validity is furnished by the exact subspace constructions and the three-round profile argument in the proof.

## Relationship to prior work

Pankov's 2010 preprint on isometric embeddings of Johnson graphs in Grassmann graphs (arXiv:1003.3329, sections 1–3 and the embedding theorems) establishes the relevant adjacency and duality context, along with a classification of **isometric embeddings**. It does not establish logical equivalence across finite fields, quantifier-rank-three classification, or the stated representative bound; an isometric induced embedding alone cannot establish elementary equivalence.

Pikhurko and Verbitsky's 2010 survey (arXiv:1003.4865, sections 1–3) supplies the broader Ehrenfeucht–Fraïssé and logical-depth framework, rather than this Grassmann-family classification. Naimi and Shaw's 2010 preprint (arXiv:1008.0595, sections 1–5) studies which graphs occur as induced subgraphs of Johnson graphs; those existence questions do not imply the present rank-three equivalence theorem. An existing rank-three profile result for finite strongly regular graphs can account for the **diameter-two Grassmann subfamily** (effective rank two), but does not handle the diameter-at-least-three subfamily or its equivalence across all finite fields. An existing rank-three classification of ordinary Johnson graphs supplies comparison representatives, not a theorem about all Grassmann graphs.

The additional logical statement here is the uniform **finite-field Grassmann classification**, in particular the entire effective-rank-at-least-three class and its sharp representative bound. This is not claimed as a classification of arbitrary distance-regular graphs.

## Limitations

The theorem is only about the pure adjacency/equality language and quantifier rank at most three; field elements, dimension predicates, counting quantifiers, and higher ranks may separate cases classified together here. The sharp bound \(1395\) is for representatives **within the Grassmann family**. The smaller Johnson representatives are outside that family except for the complete-graph case. The field-uniform result is proved, but independent human verification has not been carried out. Searches of accessible literature and research records cannot exclude all unindexed or inaccessible equivalent prior results.

## References

1. Mark Pankov, *Isometric embeddings of Johnson graphs in Grassmann graphs*, arXiv:1003.3329, first public version March 17, 2010. https://arxiv.org/abs/1003.3329
2. Oleg Pikhurko and Oleg Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first public version March 25, 2010. https://arxiv.org/abs/1003.4865
3. Ramin Naimi and Jeffrey Shaw, *Induced Subgraphs of Johnson Graphs*, arXiv:1008.0595, first public version August 3, 2010. https://arxiv.org/abs/1008.0595
