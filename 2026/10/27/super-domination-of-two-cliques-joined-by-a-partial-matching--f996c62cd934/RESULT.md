# Super domination of two cliques joined by a partial matching

## Finding
Let \(J_{n,t}\) consist of two disjoint labeled complete graphs with vertices \(A_1,\ldots,A_n\) and \(B_1,\ldots,B_n\), supplemented by exactly the cross edges \(A_iB_i\) for \(1\le i\le t\). For all integers \(n\ge3\) and \(0\le t\le n\), every super dominating set is characterized as follows.

Put \(X=V(J_{n,t})\setminus D\). Then \(D\) is super dominating **if and only if** precisely one of the following (disjoint) conditions applies:

1. \(X=\varnothing\);
2. \(X\) lies wholly in one clique, and either \(|X|=1\) or every vertex of \(X\) is incident to one of the added matching edges;
3. \(X\) consists of exactly one vertex in each clique.

The ordinary set-counting polynomial, in which \(z\) records \(|D|\), is
\[
\boxed{\mathcal S_{n,t}(z)=2z^{2n-t}(1+z)^t-z^{2n}+2(n-t)z^{2n-1}+n^2z^{2n-2}.}
\]
The polynomial of **inclusion-minimal** super dominating sets is
\[
\boxed{\mathcal I_{n,t}(z)=n^2z^{2n-2}+2\mathbf{1}_{\{t\ge2\}}z^{2n-t}.}
\]
At \(t=2\), both summands have the same exponent and their coefficients add.

In particular, the minimum and maximum sizes of inclusion-minimal super dominating sets satisfy
\[
\boxed{\gamma_{\mathrm{sp}}(J_{n,t})=2n-\max\{2,t\},\qquad
\Gamma_{\mathrm{sp}}(J_{n,t})=2n-2.}
\]
Here \(\Gamma_{\mathrm{sp}}\) denotes the maximum cardinality among inclusion-minimal super dominating sets, not the maximum possible cardinality of an arbitrary super dominating set. All inclusion-minimal solutions have one cardinality if and only if \(t\le2\). For \(t\ge3\), the two possible cardinalities are \(2n-t\) and \(2n-2\), whose difference \(t-2\) becomes unbounded on the connected graphs with \(t=n\). For \(t\ge3\) there are exactly two minimum sets; for \(t=2\) there are \(n^2+2\), and for \(t\le1\) there are \(n^2\).

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled. An index \(i\le t\) is called *matched*; for \(i>t\) there is no cross edge at that index. A set \(D\subseteq V(G)\) is *super dominating* when each \(u\notin D\) has a selected witness \(v\in D\) with open-neighborhood condition \(N(v)\cap(V(G)\setminus D)=\{u\}\). The empty omitted set is permitted. Inclusion-minimal means no proper super dominating subset. The parameter range \(n\ge3\) matters for the two-sided omission case. The graph is connected precisely when \(t\ge1\); \(t=n\) is the complete prism \(K_n\square K_2\), whereas \(t=0\) is the disjoint union of two complete graphs.

## Proof
**1. Necessity and sufficiency of the omission classification.** Let \(a=|X\cap A|\) and \(b=|X\cap B|\). Suppose \(a\ge2\) and \(b\ge1\). Every selected vertex in clique \(A\) is adjacent to at least two omitted vertices of \(A\), so it cannot be a private witness for any omitted vertex of \(A\). A selected vertex \(B_i\) can be adjacent to an omitted \(A_j\) only if \(i=j\le t\). But that same \(B_i\) is adjacent to every omitted vertex in clique \(B\), because \(B_i\) itself is selected. As \(b\ge1\), it too cannot witness any omitted \(A_j\). Hence no omitted vertex of \(A\) can be witnessed, contradiction. By symmetry, \(b\ge2\) and \(a\ge1\) are impossible. Therefore, if both cliques contain omissions, necessarily \(a=b=1\).

Conversely, suppose \(X=\{A_i,B_j\}\). Since \(n\ge3\), choose an index \(h\) different from both \(i\) and \(j\). The selected vertex \(A_h\) is adjacent to omitted \(A_i\) but not to omitted \(B_j\), so it witnesses \(A_i\). Likewise selected \(B_h\) witnesses \(B_j\). Thus every two-sided omitted pair works, irrespective of matching indices.

It remains to consider \(X\subseteq A\); the \(B\) case is symmetric. If \(|X|=1\), any other selected vertex of clique \(A\) witnesses the sole omission. If \(|X|\ge2\), every selected \(A\) vertex has at least two omitted neighbors. Each omitted \(A_i\) consequently requires selected \(B_i\) as private witness, which exists exactly when \(i\le t\). Since \(X\cap B=\varnothing\), such a \(B_i\) sees precisely the single omitted vertex \(A_i\); hence the condition is necessary and sufficient. If \(X=\varnothing\), the super domination condition is vacuous. This completes the classification.

**2. All-set enumeration.** Omitted sets lying inside either clique and contained wholly in the \(t\) matched vertices contribute \(2(1+w)^t-1\) to the omitted-size polynomial; the subtraction avoids counting the empty omission twice. The singleton omissions at the \(n-t\) unmatched indices in each clique contribute \(2(n-t)w\), and the omitted pairs meeting both cliques contribute \(n^2w^2\). The three parts are disjoint. Replacing each omitted-size monomial \(w^r\) with \(z^{2n-r}\) gives \(\mathcal S_{n,t}(z)\) as displayed.

**3. Inclusion minimality.** Because super domination is monotone under adding selected vertices, \(D\) is inclusion-minimal exactly when its omitted set \(X\) is inclusion-maximal within the preceding admissible family. Every two-sided omitted pair is maximal: adding a third omitted vertex creates at least two omissions on one side while leaving one on the other. If \(t\ge2\), the full \(t\)-vertex matched subset on either one side is also maximal: further omissions on that side introduce an unmatched index, whereas an omission on the opposite side violates the two-sided rule. Conversely, every other admissible omission set extends to one of these: a singleton extends to a two-sided pair; a proper subset of the matched vertices with size at least two extends within its own clique. Thus these and only these are the maximal omitted sets. There are \(n^2\) two-sided pairs and, if \(t\ge2\), two matched-side sets. Their selected-set sizes yield \(\mathcal I_{n,t}(z)\).

**4. Extremal consequences.** The largest possible omitted set is of cardinality \(\max\{2,t\}\); the largest omitted size among maximal omitted sets and the smallest are \(\max\{2,t\}\) and \(2\). The extremal formulas, cardinality classification, minimum multiplicities, and growing gap follow directly. The families overlap in cardinality only when \(t=2\), and not in the actual sets.

## Verification
A supplied standalone Python program named `verify_superdom.py` constructs adjacency from the defining edge rule and applies the original witness condition to **every** vertex subset for each \(3\le n\le7\) and each \(0\le t\le n\), a total of 167,424 subsets across 30 parameter pairs. It compares the definitional predicate to the proposed classification, the polynomial coefficient dictionary, and inclusion-minimal counts. It reports no discrepancies. Run with `python verify_superdom.py` using a standard Python 3 installation. The finite checks independently implement the definition but do not replace the all-parameter proof above.

## Relationship to prior work
Klein, Rodríguez-Velázquez, and Yi established the foundational super domination condition and general Cartesian-product results; notably, their Theorem 22 gives \(\gamma_{\mathrm{sp}}(G\square K_2)=|V(G)|\). In the case \(t=n\), that **already implies the scalar minimum** \(n\), so that special-case equality is not claimed as new. Ghanbari, Jäger, and Lehtilä developed super domination for graph operations and enumerated minimum sets in other graph classes. Their inspected classification and enumeration results do not state the exact all-set enumerator, the matched-subset characterization, or the inclusion-minimal two-size transition for this family.

The general super-domination-polynomial framework of Kaidash is relevant background. Only its accessible abstract and bibliographic description were inspected; the full chapter was not available in this examination, and a potential overlap with some of its unnamed examples cannot be excluded. The main new assertion assessed here is the all-set characterization and two-parameter enumeration, with the maximality gap as a structural consequence—not a claim to have introduced the polynomial notion.

## Limitations
The theorem is stated only for \(n\ge3\). The proof depends on a third index in the mixed omission case and does not claim an analogous formula at \(n=2\). The polynomial counts labeled vertex subsets, not isomorphism classes. The coefficient values for the connected complete-prism endpoint overlap existing scalar super-domination results but the all-set polynomial is not implied by those scalar values. Literature priority is subject to additional checking, especially the inaccessible full text of Kaidash's broad polynomial chapter and any unindexed formulas. No independent mathematical audit has been carried out.

## References
1. D. J. Klein, J. A. Rodríguez-Velázquez, E. Yi, *On the super domination number of graphs*, arXiv:1705.00928, first posted 2017-05-02. https://arxiv.org/abs/1705.00928
2. N. Ghanbari, G. Jäger, T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795, first posted 2022-09-05. https://arxiv.org/abs/2209.01795
3. P. A. Kaidash, *Super Domination Polynomial of a Graph*, in *Mathematical Optimization Theory and Operations Research: Recent Trends*, 2024, DOI:10.1007/978-3-031-73365-9_6. Abstract accessible; full text not inspected. https://doi.org/10.1007/978-3-031-73365-9_6
