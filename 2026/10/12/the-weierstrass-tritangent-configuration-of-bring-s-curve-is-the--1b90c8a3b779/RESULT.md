# The Weierstrass tritangent configuration of Bring's curve is the clique geometry of \(A_{5,3}\)
## Finding
Let \(B\) be Bring's curve in the canonical \(\mathbf P^4\)-model. Braden and Disney-Hogg label its sixty Weierstrass points by ordered injective triples \(W_{ijk}\), where \(i,j,k\in\{1,2,3,4,5\}\) are pairwise distinct and the coordinates in positions \(i,j,k\) are the three roots \(\alpha,\beta,\gamma\) of
\[
f(T)=T^3+2T^2+3T+4.
\]
Among the one hundred twenty tritangent planes, consider the sixty planes whose three contacts are all Weierstrass points. These sixty points and sixty planes form a \((60_3)\) incidence configuration with three parallel classes of twenty planes. Its point-collinearity graph is exactly the arrangement graph \(A_{5,3}\), and its type-preserving incidence automorphism group is
\[
\operatorname{Aut}_{\mathrm{tp}}(\mathcal C)\cong S_5\times S_3.
\]
The factor \(S_5\) is the geometric automorphism group of Bring's curve. The second factor permutes the three root positions and the three twenty-plane classes. Since \(f\) is irreducible and \(\operatorname{disc}(f)=-200\), this second factor is naturally \(\operatorname{Gal}(f/\mathbb Q)\cong S_3\).

## Assumptions and scope
All statements are over characteristic zero. The configuration \(\mathcal C\) uses only the sixty class-(i) tritangents of Proposition 5.6 in Braden--Disney-Hogg, namely those with three Weierstrass contacts. The phrase "type-preserving" means that automorphisms send Weierstrass points to Weierstrass points and tritangent blocks to tritangent blocks. No statement is made about possible point-block dualities of the Levi graph. No statement is made about the remaining sixty class-(ii) tritangents, and the extra \(S_3\) is not asserted to act by holomorphic automorphisms of \(B\).

## Proof
Braden--Disney-Hogg give the sixty Weierstrass points as \(W_{ijk}\), with \(i,j,k\) pairwise distinct, and state that changing the labeling of \(\alpha,\beta,\gamma\) changes this labeling of the Weierstrass points. Their class-(i) tritangents occur in the three forms \(\Pi^{(1)}_{\alpha jk}\), \(\Pi^{(1)}_{i\beta k}\), and \(\Pi^{(1)}_{ij\gamma}\). Their contact divisor formula gives
\[
T^{(1)}_{\alpha jk}=\sum_{i\ne j,k} W_{ijk},
\]
and the two other families are obtained by cycling the distinguished root position. Define
\[
A_{jk}=\{W_{ijk}:i\notin\{j,k\}\},\quad
B_{ik}=\{W_{ijk}:j\notin\{i,k\}\},\quad
C_{ij}=\{W_{ijk}:k\notin\{i,j\}\}.
\]
Each family has \(5\cdot4=20\) blocks, each block has three points, and each point lies on exactly one block in each family. Thus every family partitions the sixty points and the full structure is a \((60_3)\) configuration.

There is no additional incidence between a Weierstrass point and a class-(i) tritangent beyond these contacts. Indeed, a tritangent plane cuts the canonical genus-four curve in a divisor of degree six, and its three tangencies already contribute the complete divisor \(2P+2Q+2R\). Therefore a Weierstrass point lying on such a plane must be one of its three contact points.

Identify \(W_{ijk}\) with the ordered injective triple \((i,j,k)\). Two points share a block exactly when they agree in two coordinate positions, equivalently when the ordered triples differ in exactly one coordinate. This is the defining adjacency relation of the arrangement graph \(A_{5,3}\). Exact enumeration also shows that the sixty blocks above are precisely all maximal cliques of \(A_{5,3}\), each of size three, so the incidence structure is intrinsically recoverable from its point graph.

The obvious actions of \(S_5\) on the five symbols and \(S_3\) on the three coordinate positions commute and give \(120\cdot6=720\) distinct graph automorphisms. Exhaustive graph-automorphism enumeration gives exactly \(720\) automorphisms. Since the blocks are precisely the maximal cliques, this proves
\[
\operatorname{Aut}_{\mathrm{tp}}(\mathcal C)\cong S_5\times S_3.
\]
Finally, \(f(T)\) has no rational root and is therefore irreducible. Its discriminant is \(-200\), which is not a square in \(\mathbb Q\). The Galois group of an irreducible cubic with nonsquare discriminant is \(S_3\). Galois permutation of \(\alpha,\beta,\gamma\) is exactly the coordinate-position action just described, so the non-geometric factor has the claimed arithmetic interpretation.

## Verification
The accompanying `verify.py` constructs all sixty injective triples and all sixty fibre blocks, checks the three parallel classes and the \((60_3)\) incidence counts, verifies that collinearity is Hamming distance one, identifies all sixty maximal cliques with the tritangent blocks, and exhaustively enumerates the graph automorphisms. It independently constructs the \(S_5\times S_3\) subgroup and verifies that it already has order \(720\). It also verifies irreducibility, discriminant \(-200\), and Galois group order six for \(f\). A fresh execution of the embedded artifact returned:

`VERIFY_OK points=60 blocks=60 incidence=60_3 point_graph=A(5,3) maximal_cliques=60 aut_type_preserving=720=S5xS3 cubic_disc=-200 cubic_galois=S3`

## Relationship to prior work
Braden--Disney-Hogg, following Edge for the tritangents, provide the geometric ingredients: the sixty Weierstrass points, the sixty all-Weierstrass tritangents, the three twenty-element odd-theta orbits, and the contact-divisor formula. They do not identify the resulting point-tritangent incidence structure with an arrangement graph or determine its type-preserving incidence automorphism group. Their full text contains no occurrence of "arrangement graph". The associated public computation notebook reproduces the odd-theta orbit partition but does not analyze this incidence structure.

Arrangement graphs are independently standard objects: \(A_{n,k}\) has ordered injective \(k\)-tuples as vertices and adjacency by changing one coordinate. General literature determines their symmetry properties. Accordingly, no originality is claimed for the abstract graph \(A_{5,3}\) or for its abstract automorphism group. The contribution here is the exact identification of the natural Bring-curve incidence configuration with the clique geometry of \(A_{5,3}\), together with the interpretation of the extra \(S_3\) as the Galois permutation group of the cubic that labels the three root positions.

Edge's 1981 paper is an important residual comparison because its abstract states that all tritangent equations and contact coordinates are found. Its full text was not available for inspection here, so an equivalent classical incidence description under different terminology cannot be ruled out solely from the accessible abstract.

## Limitations
This result concerns only the sixty class-(i) tritangents. It does not classify incidences involving the other sixty tritangents, does not determine type-swapping automorphisms of the one hundred twenty-vertex Levi graph, and does not assert that the extra \(S_3\) consists of complex projective automorphisms of Bring's curve. The abstract arrangement-graph symmetry is known in graph theory; novelty is restricted to the curve-specific incidence identification and arithmetic interpretation described above.

## References
1. H. W. Braden and L. Disney-Hogg, *Bring's curve: old and new*, arXiv:2208.13692; European Journal of Mathematics 10 (2024), article 3, DOI 10.1007/s40879-023-00706-0. First public version: 2022-08-29.
2. W. L. Edge, *Tritangent Planes of Bring's Curve*, Journal of the London Mathematical Society s2-23 (1981), 215--222, DOI 10.1112/jlms/s2-23.2.215.
3. F.-G. Yin and Y.-Q. Feng, *The symmetry property of \((n,k)\)-arrangement graph*, Journal of Graph Theory 98 (2021), DOI 10.1002/jgt.22690.
