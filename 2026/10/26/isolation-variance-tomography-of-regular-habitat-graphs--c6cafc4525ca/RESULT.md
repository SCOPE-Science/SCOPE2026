# Isolation-variance tomography of regular habitat graphs

## Finding
Consider a finite simple undirected \(r\)-regular habitat adjacency graph \(G\) on \(n\) vertices, with \(n\ge3\) and \(1\le r\le n-1\). Retain every vertex independently with the same probability \(p\in(0,1)\); interpret each retained isolated vertex of the induced retained graph as a surviving one-patch habitat fragment. Let \(I_p\) count these singleton fragments. The exact variance curve \(V_G(p)=\operatorname{Var}(I_p)\), together with \(n\) and \(r\), reconstructs the complete positive nonedge-codegree histogram, and therefore the triangle count of \(G\). Precisely, write \(N_s\) for the number of unordered nonadjacent vertex pairs having exactly \(s\) common neighbors, \(1\le s\le r\). Put \(q=1-p\). Then

\[
V_G(p)=npq^r-n(r+1)p^2q^{2r}+2p^2\sum_{s=1}^{r}N_s\bigl(q^{2r-s}-q^{2r}\bigr).
\]

For \(0<q<1\), define the exactly observable quotient

\[
B_G(q)=\frac{V_G(1-q)-n(1-q)q^r+n(r+1)(1-q)^2q^{2r}}{2(1-q)^3q^r}.
\]

This quotient is a polynomial of degree at most \(r-1\). If \(b_j=[q^j]B_G(q)\), with \(b_{-1}=0\), then

\[
B_G(q)=\sum_{s=1}^rN_sq^{r-s}(1+q+\cdots+q^{s-1}),\qquad N_s=b_{r-s}-b_{r-s-1}.
\]

Consequently observations of \(V_G(p)\) at **any \(r\) distinct exact known probabilities** \(p\in(0,1)\) suffice for recovery by polynomial interpolation. The number of triangles is

\[
T(G)=\frac{n\binom r2-\sum_{s=1}^r sN_s}{3}.
\]

Even without full interpolation, the cubic coefficient of the variance near zero retention determines triangles:

\[
V_G(p)=np-n(2r+1)p^2+\left[\frac{nr(7r+1)}2-6T(G)\right]p^3+O(p^4).
\]

The variance curve does **not** determine the full graph: the ten-cycle \(C_{10}\) and the disjoint union \(C_5\sqcup C_5\) have identical \(n=10\), \(r=2\), and positive nonedge-codegree histograms \((N_1,N_2)=(10,0)\), hence identical curves, but different connectivity.

## Assumptions and scope
The underlying graph is fixed, finite, simple, undirected and regular. Site retention is independent across all vertices with an identical exactly known probability \(p\); the graph need not be connected. Isolation is measured in the **induced retained subgraph**, including retained vertices of degree zero as singleton fragments. The number of sites \(n\) and regular degree \(r\) are known; probabilities are exact population probabilities, not noisy finite-sample estimates. All identities hold simultaneously for every graph and each \(p\in(0,1)\). No vertex or edge deletion is performed to the original graph, and \(r=0\) is excluded because it gives no positive codegrees.

## Proof
For each vertex \(v\), let \(X_v\) be the indicator that \(v\) survives and none of its \(r\) neighbors survive. Independent retention gives \(\mathbb E X_v=pq^r\), hence \(\mathbb E I_p=npq^r\). For two **adjacent** vertices \(u,v\), simultaneous isolation is impossible, so \(\mathbb E X_uX_v=0\). For two **nonadjacent** vertices with exactly \(s\) common neighbors, the necessary and sufficient event is that both vertices survive and all vertices in the union of their neighborhoods fail to survive. That union has size \(2r-s\), whence \(\mathbb E X_uX_v=p^2q^{2r-s}\).

Sum \(\operatorname{Var}(\sum_v X_v)\) over diagonal and unordered pairs. The diagonal term is \(npq^r-np^2q^{2r}\); each of the \(nr/2\) adjacent pairs contributes \(-2p^2q^{2r}\); each nonadjacent pair contributes twice \(p^2q^{2r-s}-p^2q^{2r}\). Nonadjacent pairs with \(s=0\) contribute zero. This yields the first displayed variance formula.

Subtract the two baseline terms and divide by \(2p^2q^r(1-q)\). Since \(p=1-q\), this division is precisely the denominator \(2(1-q)^3q^r\) displayed in the definition of \(B_G\). For each \(s\ge1\),

\[
\frac{q^{2r-s}-q^{2r}}{q^r(1-q)}=q^{r-s}(1+q+\cdots+q^{s-1}).
\]

Thus \(B_G\) is a polynomial. The coefficient of \(q^j\), for \(0\le j\le r-1\), is \(b_j=\sum_{s=r-j}^r N_s\), so differences of adjacent coefficients give the inversion \(N_s=b_{r-s}-b_{r-s-1}\). Since the degree bound is at most \(r-1\), exact values at any \(r\) distinct \(q\)-values uniquely determine \(B_G\) by Lagrange interpolation; each such value is computable from its matching observed variance and the known \(n,r\).

Count wedges (unordered pairs of distinct neighbors of the same vertex). Their total is \(n\binom r2\). A wedge whose endpoints are adjacent belongs to one triangle, and each triangle contributes three such wedges, hence \(3T(G)\) wedges of that kind. Nonadjacent wedge endpoints \(u,v\) contribute one wedge for each of their \(s\) common neighbors, yielding exactly \(\sum_{s\ge1}sN_s\) other wedges. This proves the triangle reconstruction formula.

Finally expand \(q^r=(1-p)^r\), \(q^{2r}=(1-p)^{2r}\), and \(q^{2r-s}-q^{2r}=sp+O(p^2)\) in the exact variance identity. The coefficient of \(p^3\) is \(n\binom r2+2nr(r+1)+2\sum_{s\ge1}sN_s\). Substituting the wedge identity simplifies this to \(nr(7r+1)/2-6T(G)\). The decagon and two separate pentagons are both triangle-free degree-two graphs with ten sites and ten nonadjacent pairs having one common neighbor, and neither has a nonadjacent pair with two common neighbors. Their variance formula is therefore identical, despite their different numbers of connected components.

## Verification
Run `python verify.py` with Python 3 standard library from the directory containing the code. The printed deterministic JSON result can be compared byte-for-byte after trimming the newline with `certificate.json`. The checker independently enumerates all \(2^n\) site-retention subsets with exact rational probabilities for nine explicit regular graphs; it compares full first and second moments to the derived formulas for three rational retention probabilities, verifies the codegree inversion and triangle wedge identity, independently expands the cubic variance coefficient, and verifies the nonisomorphic decagon/two-pentagon example. The saved certificate records 27 verified moment comparisons spanning 10,968 weighted site-subset instances and nine cubic-coefficient tests. Enumeration tests only those finite inputs; the preceding proof establishes the all-graphs theorem.

## Relationship to prior work
Landscape ecology has long used neutral binary landscapes to study patch fragmentation and the response of class-level metrics to amount and aggregation; With (1995) and Neel, McGarigal and Cushman (2004) motivate the distinction between mean landscape metrics and graph structure. Site-percolation theory on regular and pseudorandom graphs, including Diskin and Krivelevich (2023), analyzes retained components and their thresholds in forward models. The present conclusion concerns a different inverse observable: it extracts the nonadjacent common-neighbor multiplicities and an exact triangle census solely from the variance of **isolated retained sites** across retention levels. The derivation uses elementary second-moment identities and polynomial inversion and does not claim those underlying techniques are new. An equivalent identity may exist elsewhere in the broad reliability/graph-polynomial literature; this comparison is not a proof of worldwide uniqueness.

## Limitations
The method requires the known regular degree and exact probabilities at controlled retention levels; it supplies no stability bounds for empirical or noisy variance measurements. It does not reconstruct pairs with zero common neighbors directly without using the known total number of nonadjacent pairs; nor does it reconstruct the entire graph or its connectivity. Unequal survival probabilities, correlated habitat loss, edge percolation, graph changes over time and general irregular graphs are outside the theorem. An exact observable curve is not by itself a physical or biological measurement protocol. The identification is mathematical, not an independently validated ecological inference method.

## References
- With, K. A. (1995), “Critical Thresholds in Species' Responses to Landscape Structure,” *Ecology* **76**, 2446–2459. DOI: `10.2307/2265819` (original publication December 1, 1995; abstract/metadata examined).
- Neel, M. C., McGarigal, K., and Cushman, S. A. (2004), “Behavior of class-level landscape metrics across gradients of class aggregation and area,” *Landscape Ecology* **19**, 435–455. DOI: `10.1023/B:LAND.0000030521.19856.cb` (full text examined).
- Diskin, S. and Krivelevich, M. (2023), “Site percolation on pseudo-random graphs,” *Random Structures & Algorithms*. DOI: `10.1002/rsa.21141` (full text examined).
