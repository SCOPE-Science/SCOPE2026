# The surjective-homomorphism order inside K4-stable graph logics

## Finding
Let \(G=(G_0\sqcup G_1,E_G)\) and \(H=(H_0\sqcup H_1,E_H)\) be finite connected simple bipartite graphs with at least one edge and with their two color classes fixed. Associate to each such graph the finite transitive frame \(F_G^*\) and stable modal formula \(\Gamma_G=\gamma(F_G^*,\varnothing)\) defined below, and put \(L_G=\mathsf K4+\Gamma_G\). Then
\[
L_G\subseteq L_H\quad\Longleftrightarrow\quad
\text{there is a surjective graph homomorphism }h:G\to H\text{ with }h[G_i]\subseteq H_i\ (i=0,1).
\]
Consequently, the preorder of finite connected two-colored bipartite graphs under color-preserving surjective graph homomorphisms embeds faithfully, modulo color-preserving isomorphism, into the inclusion order on K4-stable modal logics.

In particular, for \(n\ge3\), let \(L_n=L_{C_{2n}}\), with the alternating two-coloring of the cycle. Then
\[
L_3\supsetneq L_4\supsetneq L_5\supsetneq\cdots,
\qquad \bigcap_{n\ge3}L_n=\mathsf K4.
\]
Each \(L_n\) is finitely axiomatized and K4-stable. By Takahashi's 2026 hardness theorem, finite-frame validity for each is coNP-complete; consequently, if \(\mathrm P\ne\mathrm{NP}\), every \(L_n\) is non-elementary. The conditional non-elementarity and coNP-completeness are prior results, not new contributions.

## Assumptions and scope
The color classes are ordered: a homomorphism must map the first class into the first and the second into the second. Graphs are finite, simple, undirected, connected, and have at least two vertices. A surjective graph homomorphism preserves adjacency, not necessarily nonadjacency. The inclusion order compares complete normal modal logics, not merely finite-frame truth values.

For \(G=(G_0\sqcup G_1,E_G)\), define \(F_G^*\) on \(V(G)\sqcup\{r,a,b,c\}\) with accessibility relation consisting **exactly** of the loops \((v,v)\) for \(v\in V(G)\), arrows \((r,x)\) for every world \(x\), arrows \((a,v)\) for all \(v\in V(G)\), \((a,c)\), arrows \((b,v)\) for \(v\in G_1\), arrows \((v,c)\) for \(v\in G_0\), and arrows \((u,v)\) whenever \(u\in G_0\), \(v\in G_1\), and \(\{u,v\}\in E_G\). The root \(r\) and the graph vertices are reflexive; \(a,b,c\) are irreflexive. This is Takahashi's four-marker construction, with a fixed orientation of the graph colors. It is transitive and has a reflexive root.

We use the established stable-formula property for a finite rooted K4-frame \(F\): a finite transitive frame \(X\) refutes \(\gamma(F,\varnothing)\) exactly when \(F\) is a surjective relation-preserving image of a rooted upset of \(X\). A relation-preserving (stable) map is not required to reflect edges. We also use the established finite model property for K4-stable logics.

## Proof
**1. Rigid recovery of the bipartite graph.** Suppose \(F_H^*\) is the stable image of a rooted upset \(U\subseteq F_G^*\), via an onto relation-preserving map \(f\). Because a reflexive point cannot map to an irreflexive one, all three target marker worlds \(a_H,b_H,c_H\) have preimages among the only three irreflexive source worlds \(a_G,b_G,c_G\). Thus all source markers lie in \(U\), mapped bijectively to the target markers. A rooted upset containing both \(a_G\) and \(b_G\) must contain \(r_G\), the only world reaching both; as \(r_G\) accesses all worlds, \(U=F_G^*\).

Both \(a_G\) and \(b_G\) have successors because \(G_1\ne\varnothing\); \(c_G\) is a dead end. The only dead-end target marker is \(c_H\), so \(f(c_G)=c_H\). Since \(a_G\) sees \(c_G\) but \(b_H\) does not see \(c_H\), the other markers must map \(f(a_G)=a_H\) and \(f(b_G)=b_H\). As \(r_G\) sees \(a_G\) and is reflexive, while no target graph vertex sees \(a_H\), necessarily \(f(r_G)=r_H\).

Every graph vertex \(v\) is reflexive and satisfies \(a_G Rv\); its image must therefore be a reflexive successor of \(a_H\), hence a vertex of \(H\). If \(v\in G_0\), then \(vRc_G\), hence \(f(v)Rc_H\), forcing \(f(v)\in H_0\). If \(v\in G_1\), then \(b_G Rv\), hence \(b_H Rf(v)\), forcing \(f(v)\in H_1\). Surjectivity forces \(f[V(G)]=V(H)\). Finally, for every edge \(\{u,v\}\in E_G\) with \(u\in G_0\) and \(v\in G_1\), preservation of \(uRv\) yields \(\{f(u),f(v)\}\in E_H\). Therefore \(h=f|_{V(G)}\) is a surjective color-preserving graph homomorphism.

Conversely, any surjective color-preserving graph homomorphism \(h:G\twoheadrightarrow H\) extends to a surjective stable map \(F_G^*\twoheadrightarrow F_H^*\) by setting \(r_G\mapsto r_H\), \(a_G\mapsto a_H\), \(b_G\mapsto b_H\), and \(c_G\mapsto c_H\). The listed relations show edge preservation case by case. We have proved
\[
F_H^*\text{ is a stable image of a rooted upset of }F_G^*
\iff G\twoheadrightarrow H\text{ by a color-preserving homomorphism}.\tag{1}
\]

**2. Logical inclusion.** If the map in (1) exists, any finite transitive frame refuting \(\Gamma_G\) has a rooted upset mapping stably onto \(F_G^*\); composing with \(F_G^*\twoheadrightarrow F_H^*\) shows that frame refutes \(\Gamma_H\). Therefore every finite \(L_H\)-frame validates \(\Gamma_G\). As \(L_H\) is K4-stable and has the finite model property, \(\Gamma_G\in L_H\), so \(L_G\subseteq L_H\).

Conversely, if \(L_G\subseteq L_H\), the transitive frame \(F_G^*\) refutes \(\Gamma_G\) through its identity map, hence cannot validate \(\Gamma_H\). The stable-formula characterization gives a stable image of a rooted upset onto \(F_H^*\); (1) recovers a surjective color-preserving graph homomorphism. This proves the biconditional. Mutual surjective color-preserving homomorphisms between finite graphs imply equal vertex counts and edge counts; both maps are then bijective and preserve every edge in both directions, so the graphs are color-preservingly isomorphic. This establishes faithful embedding on isomorphism classes.

**3. Cyclic hierarchy.** For integers \(m\ge n\ge3\), traverse \(C_{2n}\) once in \(2n\) steps and then insert \(m-n\) immediate two-step backtracks at the starting vertex. The resulting closed walk of length \(2m\) defines a surjective adjacency- and color-preserving map \(C_{2m}\twoheadrightarrow C_{2n}\). If \(m<n\), a surjection is impossible by cardinality. By the biconditional, \(L_m\subsetneq L_n\) for \(m>n\). For incomparability elsewhere in the order, the six-vertex path and six-vertex star, colored according to their unique bipartitions, have respective color-class sizes \((3,3)\) and \((1,5)\). Neither can surject color-preservingly onto the other, so their associated modal logics are incomparable.

**4. Infimum.** Certainly \(\mathsf K4\subseteq\bigcap_{n\ge3}L_n\). Let \(\varphi\notin\mathsf K4\). By the finite model property of \(\mathsf K4\), choose a finite transitive frame \(X\), with a valuation refuting \(\varphi\). For all sufficiently large \(n\), \(|F_{C_{2n}}^*|=2n+4>|X|\); hence no rooted upset of \(X\) surjects onto \(F_{C_{2n}}^*\). Thus \(X\models\Gamma_{C_{2n}}\) as a frame, but \(X\not\models\varphi\). Therefore \(\varphi\notin L_n\) for all such \(n\), establishing the claimed intersection.

## Verification
The accompanying self-contained Python program `verify.py` constructs each frame from its defining edges, verifies transitivity, and compares the existence of surjective color-preserving graph homomorphisms with the existence of arbitrary surjective stable frame maps for all 529 ordered pairs drawn from the 23 labeled connected bipartite graphs on two through four vertices. It does not assume marker identities in the frame-map enumeration. It additionally checks 21 explicit cyclic folding witnesses and the six-vertex path/star incomparability. The output is `VERIFY_OK_FULL`. These finite checks test the argument but do not replace its general proof.

## Relationship to prior work
Takahashi, *Non-elementary modal logics, assuming P \(\ne\) NP* (arXiv:2609.10872v1, 9 September 2026), introduces the four-marker frame construction, uses stable images to reduce surjective graph coloring to finite-frame logic validity (Lemma 3.4 and Claim 3.5), and proves coNP-completeness and conditional non-elementarity for infinitely many cycle-based axioms (Theorem 3.7). That work explicitly establishes pairwise distinct logics by size. The present theorem identifies the **entire inclusion order** for all fixed-colored connected bipartite graph inputs, and its cyclic corollary identifies an exact strictly descending chain and its infimum. These are not asserted as independently proved complexity or non-elementarity claims.

Bezhanishvili, Bezhanishvili and Ilin, *Stable modal logics* (2016 open preprint, 2018 journal), establish general stable-image and K4-stability machinery, including the finite model property and stable canonical formulas. The general connection between stable images and logical implication is therefore inherited; the graph-to-logic order equivalence, color rigidity, and specified cyclic infimum are the asserted contribution.

## Limitations
The theorem concerns colored connected bipartite graphs with nonempty classes, the fixed four-marker frame construction, and K4-stable logics defined by its single stable formula. It does not classify arbitrary stable logics, provide an unconditional non-elementarity theorem, or prove new complexity hardness. Prior work provides a large part of the semantic machinery; an equivalent order-embedding specialization in terminology not retrieved remains a literature risk. The finite verifier covers only its stated sizes.

## References
- T. Takahashi, *Non-elementary modal logics, assuming P \(\ne\) NP*, arXiv:2609.10872v1 (first version, 2026-09-09), Sections 2–3, especially Proposition 3.1, Claim 3.5 and Theorem 3.7. https://arxiv.org/pdf/2609.10872
- G. Bezhanishvili, N. Bezhanishvili and J. Ilin, *Stable modal logics*, University of Amsterdam preprint PP-2016-11 (2016), especially Section 5 and Theorem 6.7. https://eprints.illc.uva.nl/id/eprint/547/1/PP-2016-11.text.pdf ; published in *Review of Symbolic Logic* 11 (2018), 436–469, DOI 10.1017/S1755020317000375.
- T. Takahashi, *Stable canonical rules and formulas for pre-transitive logics via definable filtration*, *Journal of Logic and Computation* (2026), DOI 10.1093/logcom/exag023, preliminaries and Section 5. https://doi.org/10.1093/logcom/exag023
