# The five-vertex onset of positive degree covariance in uniform spanning trees

## Finding

Let \(G=(V,E)\) be a finite connected simple graph and let \(T\) be uniformly distributed over its spanning trees. For distinct vertices \(u,v\), write \(D_u=\deg_T(u)\). Then:

1. For every \(|V|\le4\), \(\operatorname{Cov}(D_u,D_v)\le0\).
2. At \(|V|=5\), positive covariance occurs in exactly two graph isomorphism classes. In a five-cycle \(C_5\), exactly five adjacent vertex pairs have covariance \(1/25\). In a five-cycle with one added chord, exactly two pairs have covariance \(5/121\). All remaining connected five-vertex graph isomorphism classes have nonpositive covariance for every pair.
3. For any unicyclic connected graph with unique cycle of length \(\ell\ge3\),

\[
\operatorname{Cov}(D_u,D_v)=
\begin{cases}
(\ell-4)/\ell^2, & u,v\text{ are adjacent on the cycle},\\
-4/\ell^2, & u,v\text{ are nonadjacent cycle vertices},\\
0, & \text{at least one vertex is off the cycle}.
\end{cases}
\]

Thus the sharp onset of positive vertex-degree covariance is five vertices, despite negative dependence among distinct spanning-tree edge indicators.

## Assumptions and scope

All graphs are finite, connected, loopless, without multiple edges, and undirected. The law is uniform on the entire set of spanning trees; it is not a random minimum-spanning-tree model. The covariance is over this tree law at two fixed distinct labeled vertices. The finite minimality statement quantifies over **every** connected simple graph on at most five vertices and **every** unordered vertex pair. The unicyclic formula holds for every graph order and any trees attached to the unique cycle.

## Proof

**Unicyclic identity.** A connected unicyclic graph has exactly \(\ell\) spanning trees: each is formed by deleting precisely one edge of its unique cycle. That edge \(J\) is uniform over the \(\ell\) cycle edges. For a cycle vertex \(u\), \(D_u=\deg_G(u)-I_u\), where \(I_u\) indicates that \(J\) is incident to \(u\). Hence \(\mathbb E I_u=2/\ell\). For two distinct cycle vertices, \(\mathbb E(I_uI_v)=1/\ell\) if adjacent, otherwise zero, since only adjacent vertices share an incident cycle edge. Constants disappear under covariance, giving the two displayed values. A vertex off the cycle has the same degree in every spanning tree, giving covariance zero. The sign of the adjacent expression is strictly positive exactly for \(\ell\ge5\).

**Finite global minimality and uniqueness.** The included standalone verifier enumerates all labeled simple graphs on \(n=2,3,4,5\) vertices, retaining exactly those connected. For each such graph, it enumerates all \((n-1)\)-edge subsets and retains exactly the connected ones, which are precisely its spanning trees. It calculates each two-degree covariance by the exact integer numerator

\[
N\sum_{T}D_u(T)D_v(T)
-\left(\sum_{T}D_u(T)\right)
 \left(\sum_{T}D_v(T)\right),
\]

where \(N\) is the number of spanning trees. The denominator is \(N^2>0\). This tests all unordered vertex pairs without approximation. It canonicalizes each connected graph by minimizing the adjacency-bit string over all \(n!\) label permutations. The exhaustive outputs show \(1,4,38,728\) labeled connected graphs respectively for \(n=2,3,4,5\), representing \(1,2,6,21\) isomorphism classes. None at orders two through four has a positive pair. At order five exactly two classes do: \(C_5\) and \(C_5\) with a chord; the code checks their exact canonical signatures, their spanning-tree counts \(5,11\), their numbers of positive pairs \(5,2\), and their exact positive covariances \(1/25,5/121\). There are no distinct vertex pairs at order one. Thus the exhaustive finite part is a complete, reproducible proof rather than a statistical test.

In the labeled representative with cycle edges \(01,12,23,34,40\) and chord \(02\), the two positive pairs are \(04\) and \(23\), each with \(5/121\). The unicyclic formula independently yields \(1/25\) for all five adjacent pairs in \(C_5\).

## Verification

Execute the included UTF-8 Python 3 standard-library program `verify_degree_boundary.py` from a directory containing it. It enumerates the complete finite set of graphs and trees using integer arithmetic and `fractions.Fraction`, canonicalizes graphs by all permutations, asserts the two exact witness classes, and independently tests the unicyclic formula for cycle lengths three through eleven with short pendant paths. The unicyclic theorem for arbitrary cycle length follows analytically and is not inferred from this bounded check. The replay prints `VERIFY_OK` on success.

## Relationship to prior work

Uniform spanning trees are determinantal edge processes and have classical transfer-current and matrix-tree formulas. Those results imply all individual finite spanning-tree moments in principle. The present statement isolates a *global minimum-order boundary and the full graph-isomorphism classification at that boundary*, which requires comparing all small graph types rather than evaluating one given graph. The general determinantal literature was inspected for overlap; an equivalent explicit first-order classification was not found in the inspected material, but a general formula by itself is not proof of novelty. Related studies of alternative spanning-tree sampling laws address a different distribution.

## Limitations

The minimal-graph census ends at five vertices, except for the unrestricted unicyclic theorem. The result makes no claim to classify all larger graphs with positive degree covariance or to address weighted trees or minimum-weight spanning trees. Exact finite enumeration proves its bounded classification only; its unrestricted component uses the separate analytic argument. Historical priority is not certified independently.

## References

- Kassel and Lévy, Determinantal random subgraphs, arXiv:2212.06819 (first public 2022-12-13), Section 6 and matrix-tree discussion.
- Babson et al., Models of random spanning trees, arXiv:2407.20226 (first public 2024-07-29); comparison limited to accessible abstract and descriptions.
- Burton and Pemantle, transfer-current theorem (1993), as presented in Kassel and Lévy, introduction and Section 6.
