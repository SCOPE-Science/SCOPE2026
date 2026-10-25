# A nested-copy obstruction to Scott-continuous \(E_0\) reduction

## Finding
Let \(\mathfrak K\) be a family of countable relational structures, represented by their positive atomic diagrams \(D_+(A)\subseteq\mathbb N\). Put \(X\,E_0\,Y\) exactly when the symmetric difference \(X\triangle Y\) is finite. Suppose there are three members of the learning domain, represented by copies \(A_0,B_0,A_1\), such that
\[
D_+(A_0)\subseteq D_+(B_0)\subseteq D_+(A_1),\qquad A_0\cong A_1,\qquad B_0\not\cong A_0.
\]
Then no Scott-continuous map \(\Phi\) from the positive-diagram space of \(\mathfrak K\) to \(\mathcal P(\mathbb N)\), equipped with its Scott topology, can reduce isomorphism on \(\mathfrak K\) to \(E_0\).

This applies to the family \(\widetilde{\mathcal E}=\{E_n:n\ge1\}\), where \(E_n\) has countably infinitely many equivalence classes of size \(\omega\) and countably infinitely many equivalence classes of size \(n\). For any distinct positive integers \(n,m\), copies can be nested as \(A_n\subseteq B_m\subseteq C_n\), with \(A_n\cong C_n\cong E_n\) and \(B_m\cong E_m\). Hence the family admits no Scott-continuous \(E_0\)-reduction of this form, despite being a canonical TxtEx-complete family in the positive-data learning literature.

## Assumptions and scope
The language is relational and countable; a structure is coded by its positive atomic diagram, including the designated equality/inequality facts when those are part of the coding convention. Diagram inclusion means inclusion as subsets of the fixed set of coded atomic facts. The domain of \(\Phi\) may be the positive-diagram learning domain with the subspace Scott topology. Scott continuity is used only through monotonicity: if \(X\subseteq Y\), then \(\Phi(X)\subseteq\Phi(Y)\). The target relation is the usual eventual-agreement relation on subsets of \(\mathbb N\), equivalently finite symmetric difference.

For the example, \(E_n\) has exactly countably infinitely many classes of size \(n\) and countably infinitely many classes of size \(\omega\), with no other class sizes. Thus \(E_n\not\cong E_m\) when \(n\ne m\). The result concerns Scott-continuous maps on positive diagrams; it does not rule out continuous reductions on full atomic diagrams in the Cantor topology, or reductions to other equivalence relations.

## Proof
A Scott-continuous map is monotone, so the assumed chain gives
\[
\Phi(D_+(A_0))\subseteq\Phi(D_+(B_0))\subseteq\Phi(D_+(A_1)).
\]
If \(\Phi\) reduced isomorphism to \(E_0\), then \(A_0\cong A_1\) would imply that \(\Phi(D_+(A_0))\triangle\Phi(D_+(A_1))\) is finite. Because the two endpoint images are nested, the difference \(\Phi(D_+(A_1))\setminus\Phi(D_+(A_0))\) is finite. The middle image lies between them, so
\[
\Phi(D_+(B_0))\triangle\Phi(D_+(A_0))
\subseteq \Phi(D_+(A_1))\setminus\Phi(D_+(A_0)),
\]
and is finite as well. Therefore \(\Phi(D_+(B_0))\,E_0\,\Phi(D_+(A_0))\), forcing \(B_0\cong A_0\), a contradiction.

It remains to verify the nested-copy hypothesis for \(\widetilde{\mathcal E}\). Fix \(n,m\ge1\). In a copy \(C_n\) of \(E_n\), partition its countably many infinite equivalence classes into two countably infinite collections. Use one collection as the infinite classes of a substructure \(B_m\); from each class in the other collection choose exactly \(m\) elements to form one finite class. The induced substructure is isomorphic to \(E_m\). Inside the countably many infinite classes of \(B_m\), repeat the construction using one countably infinite collection as full infinite classes and choosing exactly \(n\) elements from each class in a disjoint collection. This gives an induced substructure \(A_n\cong E_n\). Thus \(A_n\subseteq B_m\subseteq C_n\) and the positive atomic diagrams are nested. Since \(n\ne m\), the middle and endpoint types differ. The general obstruction applies.

## Verification
The proof uses only (i) monotonicity of Scott-continuous maps, (ii) the definition of \(E_0\) as finite symmetric difference, and (iii) the explicit nested-substructure construction above. In the construction, distinct source equivalence classes are placed in distinct target classes; finite classes are realized as finite subsets of target infinite classes, so both equivalence and non-equivalence among selected elements are preserved. No computation or finite experiment is used as evidence for the infinite statement.

## Relationship to prior work
The continuous-reduction framework for ordinary explanatory learning identifies learnability from full atomic diagrams with continuous reducibility to \(E_0\) in the Cantor topology. A later positive-data treatment characterizes TxtEx-learnability using positive infinitary \(\Sigma^p_2\) sentences, proves that \(\widetilde{\mathcal E}\) is TxtEx-complete, and asks for a characterization involving Scott-continuous maps and familiar Borel equivalence relations. The present result supplies a concrete obstruction to the direct analogue that uses Scott-continuous maps into \(\mathcal P(\mathbb N)\) and the same target relation \(E_0\). It is a no-go result for that specific formulation, not a full characterization of positive-data learnability.

## Limitations
The obstruction applies only when the learning domain contains the stated nested-copy chain and the target relation is finite symmetric difference on subsets of \(\mathbb N\). It does not establish that every Scott-continuous reduction to every familiar equivalence relation fails, and it does not contradict the Cantor-continuous theorem for full atomic diagrams. Literature and database searches were bounded; the result is not an independent audit or a claim of absolute priority.

## References
1. V. Cipriani, A. Marcone, and L. San Mauro, “On the learning power of Friedman-Stanley jumps,” arXiv:2501.12846, first posted 2025-01-22. https://arxiv.org/abs/2501.12846
2. N. Bazhenov, E. Fokina, D. Rossegger, A. Soskova, and S. Vatev, “Learning Families of Algebraic Structures from Text,” arXiv:2402.05744v1, first posted 2024-02-08. https://arxiv.org/abs/2402.05744
3. N. Bazhenov, V. Cipriani, and L. San Mauro, “Learning algebraic structures with the help of Borel equivalence relations,” arXiv:2110.14512, first posted 2021-10-27. https://arxiv.org/abs/2110.14512
