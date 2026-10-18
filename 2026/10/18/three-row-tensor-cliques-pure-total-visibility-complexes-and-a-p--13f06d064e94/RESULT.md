# Three-row tensor cliques: pure total-visibility complexes and a Poisson window

## Finding
For each integer \(n\ge3\), let \(G_n=K_3\times K_n\) be the **direct (tensor/categorical)** product of complete graphs: its vertex set is \(\{1,2,3\}\times[n]\), and distinct \((i,a),(j,b)\) are adjacent exactly when \(i\ne j\) and \(a\ne b\). A set \(X\subseteq V(G_n)\) is *total mutually visible* if, for **every** pair of vertices \(u,v\) of \(G_n\), some shortest \(u,v\)-path has no internal vertex in \(X\). This differs from ordinary mutual visibility, which tests only pairs in \(X\).

Define the three row-complement supports
\[
A_i=\{a\in[n]:(i,a)\notin X\},\qquad i=1,2,3.
\]
Then \(X\) is total mutually visible **if and only if** each \(A_i\) has at least two elements and any two among the \(A_i\) have union of size at least three. Equivalently, each \(A_i\) has size at least two and the two-element sets among \(A_1,A_2,A_3\) are pairwise different.

Write \(Q=\binom n2\) and
\[
B_n(z)=\sum_{k=3}^{n}\binom nk z^{n-k}.
\]
Let \(T_n(z)=\sum_{X\text{ total mutually visible}}z^{|X|}\), including \(X=\varnothing\). The **complete** enumerator, not only its leading term, is
\[
\boxed{T_n(z)=B_n(z)^3+3Qz^{n-2}B_n(z)^2+3Q(Q-1)z^{2n-4}B_n(z)+Q(Q-1)(Q-2)z^{3n-6}.}
\]
Every inclusion-maximal total-mutual-visibility set is maximum, and all are exactly the configurations in which the three \(A_i\) are **pairwise distinct two-subsets** of \([n]\). Thus the simplicial complex of total-mutual-visibility sets is pure, with facets of cardinality \(3n-6\) (dimension \(3n-7\)), and
\[
\boxed{\mu_{\rm t}(G_n)=3n-6,\qquad \#\{\text{facets}\}=Q(Q-1)(Q-2).}
\]
Finally, select each vertex of \(G_n\) independently with probability \(p_n=1-\lambda/n\), for any fixed \(\lambda\ge0\) and sufficiently large \(n\). Then
\[
\boxed{\lim_{n\to\infty}\Pr(X_{p_n}\text{ is total mutually visible})=\bigl[1-(1+\lambda)e^{-\lambda}\bigr]^3.}
\]
In particular, the transition occurs when the **omission** probability has order \(1/n\).

## Assumptions and scope
Graphs are finite, simple, unweighted and undirected. The result holds for **every integer \(n\ge3\)**; no probabilistic independence is assumed for the deterministic statements. The random limit uses independent Bernoulli vertex selection with parameter \(p_n\). The polynomial is the *total*-visibility polynomial, not the ordinary mutual-visibility polynomial. All path distances are taken in the original graph, before any vertices are marked or omitted.

## Proof
**1. Diameter two and witness geometry.** Vertices in different rows and different columns are adjacent. If two distinct vertices occupy the same row, say \((i,a),(i,b)\) with \(a\ne b\), a common neighbor is exactly a vertex \((j,c)\) with \(j\ne i\) and \(c\notin\{a,b\}\). Such a vertex exists because \(n\ge3\). If they occupy the same column, say \((i,a),(j,a)\) with \(i\ne j\), their common neighbors are precisely the \((k,c)\) with \(k\) the remaining third row and \(c\ne a\). Such vertices also exist. Hence every nonadjacent pair has distance two. Adjacent pairs are automatically visible; for nonadjacent pairs visibility is equivalent to having at least one common neighbor outside \(X\).

**2. Necessary-and-sufficient row conditions.** For a fixed column \(a\), apply the condition to \((i,a),(j,a)\). Its only possible unselected common neighbors are in row \(k\), with column in \(A_k\setminus\{a\}\). Requiring this for all columns \(a\) is exactly \(|A_k|\ge2\). As the missing row \(k\) can be arbitrary, this forces and is forced by \(|A_i|\ge2\) for all three rows. Likewise, apply the condition to \((i,a),(i,b)\) with \(a\ne b\). The unselected common neighbors are in the two other rows \(j,k\), in columns from \((A_j\cup A_k)\setminus\{a,b\}\). This is nonempty for every distinct pair \(a,b\) precisely when \(|A_j\cup A_k|\ge3\): if the union has size at most two, a two-element choice \(\{a,b\}\) containing it is possible because \(n\ge3\). Thus the two stated conditions are necessary and sufficient.

Since \(|A_i|\ge2\), the union condition can fail only if two row supports are **equal two-element sets**. This proves the equivalent formulation.

**3. Exact enumeration.** Each row support of size exactly two contributes \(Qz^{n-2}\). A support of size at least three contributes \(B_n(z)\). If zero, one, two, or three rows have size exactly two, respectively, their pairwise-distinct choices number \(1,Q,Q(Q-1),Q(Q-1)(Q-2)\), and their locations among the three labeled rows number \(1,3,3,1\). Multiplying by the choices of larger row supports gives the displayed polynomial. The cases are disjoint and exhaustive.

**4. All maximal sets.** If some \(|A_i|\ge4\), removing any one element of \(A_i\) leaves size at least three, so the conditions remain true; this *adds* a vertex to \(X\). If some \(|A_i|=3\), its three distinct two-element subsets include one not equal to either of the at most two other two-element row supports. Replacing \(A_i\) by that two-element subset likewise enlarges \(X\) while preserving the condition. Therefore an inclusion-maximal \(X\) must have all three \(|A_i|=2\), and the pairwise-distinctness condition is then necessary. Conversely, every such triple is feasible and cannot be enlarged, because adding any vertex makes its row complement a singleton. Its size is exactly \(3n-6\), and its count is \(Q(Q-1)(Q-2)\). This proves both maximality/purity and the extremal formulas, including the boundary \(n=3\).

**5. Random critical window.** Let \(q_n=\lambda/n\), the probability that a vertex is **not** selected. The omitted count in each row is an independent \({\rm Bin}(n,q_n)\) random variable. The probability that every count is at least two equals
\[
\left[1-(1-q_n)^n-nq_n(1-q_n)^{n-1}\right]^3
\longrightarrow\left[1-(1+\lambda)e^{-\lambda}\right]^3.
\]
The only additional failure is equality between two two-element row complements. For a fixed pair of rows, its probability is exactly \(\binom n2q_n^4(1-q_n)^{2n-4}\), which is \(O(n^{-2})\) at fixed \(\lambda\). A union bound over three row pairs proves that this failure has vanishing probability, giving the limit. More generally, if \(n(1-p_n)\to0\) then the valid-set probability tends to zero; if \(n(1-p_n)\to\infty\), row omissions are at least two with probability tending to one, and the forbidden equal-two-support events vanish. This confirms the \(1/n\) scale.

## Verification
The standalone C++17 program `check_total_visibility_K3Kn.cpp` reconstructs adjacency from the definition and computes every common-neighbor witness for all nonadjacent vertex pairs independently of the row-support classification. It checks every vertex subset, every polynomial coefficient and all inclusion-maximal sets for \(n=3,4,5,6\). This is \(512+4096+32768+262144=299520\) tested subsets. The attached `verification_output.txt` is the actual successful output from compilation and execution of this source. Independently of code, the five proof steps establish the infinite family and the random limit.

To rerun with a C++17 compiler:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic check_total_visibility_K3Kn.cpp -o check_total_visibility_K3Kn
./check_total_visibility_K3Kn
```

## Relationship to prior work
Kuziak and Rodríguez-Velázquez (arXiv:2306.15818, first posted 27 June 2023) developed total mutual visibility and studied lexicographic and Cartesian products, not this direct-product all-size count. Cicerone, Di Stefano, Klavžar and Yero (arXiv:2401.02373, first posted 4 January 2024), **Theorem 2.2**, proved \(\mu_{\rm t}(K_m\times K_n)=mn-4\) for \(m,n\ge5\); the condition excludes the three-row factor, and the theorem gives only the maximum cardinality, not the full polynomial or the maximal-set characterization. Their product is the same direct/tensor adjacency as used here. Bujtás, Klavžar and Tian (arXiv:2412.03066) developed general visibility polynomials and generic characterizations, but did not state this full product-family enumerator or its random law. Tonny and Shikhi (arXiv:2507.01851) considered **ordinary** mutual-visibility polynomials, including joins, not the **total** visibility polynomial of direct products. These distinctions are about definitions, quantifiers and parameter ranges, not merely differences in wording.

## Limitations
No claim is made about the ordinary, outer or dual visibility polynomials, about tensor products with factors of size two, or about the complete polynomial for general \(K_m\times K_n\) when \(m\ge4\). The probabilistic result concerns independent selection only. Bibliographic priority is assessed against the accessible primary material and mathematical-record searches; unindexed equivalents remain possible. The computational tests cover only the stated finite range and do not substitute for the proof. Independent scientific validation has not been performed.

## References
1. D. Kuziak and J. A. Rodríguez-Velázquez, *Total mutual-visibility in graphs with emphasis on lexicographic and Cartesian products*, arXiv:2306.15818 (first public version 2023-06-27), https://arxiv.org/abs/2306.15818.
2. S. Cicerone, G. Di Stefano, S. Klavžar and I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, arXiv:2401.02373 (first public version 2024-01-04); European Journal of Combinatorics 120 (2024), 103995. https://arxiv.org/abs/2401.02373.
3. C. Bujtás, S. Klavžar and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066 (first public version 2024-12-04), https://arxiv.org/abs/2412.03066.
4. K. B. Tonny and M. Shikhi, *On the visibility polynomial of graphs*, arXiv:2507.01851 (first public version 2025-07-02), https://arxiv.org/abs/2507.01851.
