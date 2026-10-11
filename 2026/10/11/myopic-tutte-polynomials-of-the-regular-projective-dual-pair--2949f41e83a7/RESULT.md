# Myopic Tutte polynomials of the regular projective dual pair
## Finding
Let \(H\subset\mathbb{RP}^2\) be the regular hemi-icosahedral cellular embedding obtained from the icosahedral graph by identifying antipodal vertices, and let \(H^\ast\) be the cellular dual obtained from the dodecahedral graph by the same antipodal quotient. The underlying graphs are \(K_6\) and the Petersen graph, respectively. Their myopic Tutte polynomials are
\[
\psi_H(x,y)=x^5+10x^4+10x^3y+45x^3+15x^2y^2+75x^2y+110x^2+30xy^3+105xy^2+201xy+134x+6y^5+40y^4+110y^3+180y^2+164y+60,
\]
and
\[
\psi_{H^\ast}(x,y)=x^9+6x^8+21x^7+56x^6+6x^5y+120x^5+30x^4y+210x^4+90x^3y+290x^3+15x^2y^2+165x^2y+300x^2+45xy^2+205xy+200x+10y^3+60y^2+110y+60.
\]

## Assumptions and scope
The myopic Tutte polynomial is the invariant introduced by Boyle and Spyropoulos for graphs embedded in \(\mathbb{RP}^2\). For a connected embedded graph \(G\), their state-sum formula is
\[
\psi_G(x,y)=\sum_{A\subseteq E(G),\ A\text{ local}}(x-1)^{b_0(A)-1}(y-1)^{b_1(A)}.
\]
Here a spanning subgraph is local when its induced map to \(H_1(\mathbb{RP}^2;\mathbb F_2)\) is zero. The finding concerns exactly the two antipodal quotient embeddings described above; it is not a formula for arbitrary embeddings of the same abstract graphs.

## Proof
Choose one lift of each quotient vertex in the antipodal double cover \(S^2\to\mathbb{RP}^2\). Each quotient edge then receives a sheet-change label \(\lambda(e)\in\mathbb F_2\). For a spanning subgraph \(A\), the image of a cycle in \(H_1(\mathbb{RP}^2;\mathbb F_2)\) is the sum of its edge labels. Hence \(A\) is local exactly when \(\lambda|_A\) is a graph coboundary: there is a vertex potential \(p\colon V(A)\to\mathbb F_2\) satisfying \(p(u)+p(v)=\lambda(uv)\) on every edge of \(A\).

For the hemi-icosahedral quotient, the fifteen labeled edges, after numbering the six quotient vertices \(0,\ldots,5\), are
\[
(01,0),(02,1),(03,1),(04,0),(05,0),(12,0),(13,1),(14,0),(15,1),(23,1),(24,1),(25,1),(34,0),(35,1),(45,1).
\]
They contain every unordered pair of the six vertices, so the quotient graph is \(K_6\). For the hemi-dodecahedral quotient, with vertices \(0,\ldots,9\), the fifteen labeled edges are
\[
(01,0),(05,1),(09,1),(12,0),(18,0),(23,0),(26,0),(34,0),(39,1),(45,0),(48,1),(56,0),(67,0),(78,0),(79,0).
\]
These are the quotient edges obtained from antipodal pairs of the dodecahedral graph; this quotient is the regular hemi-dodecahedral map.

For each edge subset \(A\), solve the coboundary equations by propagation on each connected component. If inconsistent, discard \(A\). Otherwise compute
\[
b_1(A)=|A|-|V|+b_0(A)
\]
and add the corresponding state-sum monomial. Exact enumeration of all \(2^{15}=32768\) subsets gives \(7204\) local subsets for \(H\) and \(25564\) for \(H^\ast\); expanding the state sums gives the displayed polynomials.

## Verification
The accompanying `verify.py` independently enumerates every edge subset using integer arithmetic only. It reproduces both coefficient dictionaries, checks \(\psi_H(1,1)=1296\) and \(\psi_{H^\ast}(1,1)=2000\), the spanning-tree counts of \(K_6\) and the Petersen graph, and verifies the Boyle--Spyropoulos cellular-duality identity
\[
T_H(x,y)=\psi_H(x,y)+(y-1)\psi_{H^\ast}(y,x)
\]
against a separately enumerated ordinary Tutte polynomial of \(K_6\). The maximum \(y\)-degrees are \(5\) and \(3\), respectively, providing an additional consistency check with the projective-rank relation in the same source.

## Relationship to prior work
Boyle and Spyropoulos introduce the myopic Tutte polynomial, prove the state-sum formula used here, and prove that it recovers the generalized Krushkal polynomial. Their paper contains small illustrative examples but does not compute either the hemi-icosahedral \(K_6\) embedding or its hemi-dodecahedral dual. Earlier topological Tutte-polynomial literature develops the Krushkal, Las Vergnas, and related invariants for embedded graphs, including nonorientable surfaces, but the exact coefficient pair above was not located in the checked literature.

The two maps form a canonical regular dual pair on \(\mathbb{RP}^2\). Because the invariant retains embedding information that the ordinary Tutte polynomial forgets, the explicit pair is a natural exact benchmark for computations of the newly introduced invariant and, through the recovery theorem, for the corresponding generalized Krushkal data.

## Limitations
The computation is specific to the regular antipodal quotient embeddings. It does not classify myopic Tutte polynomials for all embeddings of \(K_6\) or the Petersen graph. Exhaustive state-sum enumeration proves the formulas for these finite graphs, but literature search cannot rule out an unindexed older computation phrased solely in an equivalent topological Tutte invariant.

## References
1. Keegan Boyle and Dean Spyropoulos, *Myopic Tutte polynomials and Khovanov homology in \(\mathbb{RP}^3\)*, arXiv:2609.40122v1, 2026. In particular Proposition 3.3 and Corollary 3.13.
2. Joanna A. Ellis-Monaghan and Iain Moffatt, *The Las Vergnas polynomial for embedded graphs*, European Journal of Combinatorics 50 (2015), 97--114.
