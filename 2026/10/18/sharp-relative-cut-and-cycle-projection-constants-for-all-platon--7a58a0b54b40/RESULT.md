# Sharp relative cut and cycle projection constants for all Platonic graphs

## Finding

Let \(G\) be the one-skeleton of one of the five convex regular polyhedra, give \(\mathbb R^{E(G)}\) its usual real \(\ell_1\) norm or \(\ell_\infty\) norm, and let \(B(G)\) and \(Z(G)\) be its cut and cycle subspaces. Define the **relative projection constant** of \(Y\subseteq\mathbb R^{E(G)}\) to be
\[
\lambda_p(Y;G)=\inf\{\|P\|_{\ell_p(E)\to\ell_p(E)}:P^2=P,\ \operatorname{range}(P)=Y\},\qquad p\in\{1,\infty\}.
\]
The following table determines these constants over **all real linear projections**, not just graph-invariant or orthogonal projections.

| Graph \(G\) | \(|V(G)|\) | \(|E(G)|\) | \(\lambda_1(B;G)=\lambda_\infty(B;G)\) | \(\lambda_1(Z;G)=\lambda_\infty(Z;G)\) |
|---|---:|---:|---:|---:|
| Tetrahedral | \(4\) | \(6\) | \(3/2\) | \(3/2\) |
| Cubical | \(8\) | \(12\) | \(2\) | \(11/6\) |
| Octahedral | \(6\) | \(12\) | \(11/6\) | \(2\) |
| Dodecahedral | \(20\) | \(30\) | \(38/15\) | \(34/15\) |
| Icosahedral | \(12\) | \(30\) | \(34/15\) | \(38/15\) |

For each of these five graphs the Euclidean-orthogonal projections \(Q_G\) onto \(B(G)\) and \(C_G=I-Q_G\) onto \(Z(G)\) attain the indicated minima simultaneously for both endpoint norms. These are the **unique graph-automorphism-invariant projections** onto the respective subspaces (uniqueness among arbitrary, not necessarily invariant, minimizers is **not** asserted). The dodecahedron–icosahedron pair is the non-Hamming, non-complete finite case in this classification and exhibits the strict exchange of the two rational constants under planar duality.

## Assumptions and scope

All graphs are finite, simple, connected, with unit edges and a fixed arbitrary orientation. Write \(D\in\mathbb R^{V\times E}\) for the oriented vertex-edge incidence matrix. The cycle space is \(Z=\ker D\), while the cut space is \(B=\operatorname{im}D^{\mathsf T}=Z^\perp\) in the ordinary Euclidean inner product. For any choice of a deleted vertex row \(\widetilde D\), let
\[
Q=\widetilde D^{\mathsf T}(\widetilde D\widetilde D^{\mathsf T})^{-1}\widetilde D,
\qquad C=I-Q.
\]
The \(\ell_1\) and \(\ell_\infty\) norms are coordinate norms in the oriented edge basis, not the quotiented transportation-cost norm. Changing all or some edge orientations conjugates these matrices by diagonal signs and does not change the constants.

## Proof

**1. Global minimality from disjoint cut and cycle characters.** Let \(\Gamma=\operatorname{Aut}(G)\), acting on oriented edge coordinates by signed permutations. This representation is isometric for \(\ell_1\), \(\ell_\infty\), and Euclidean norms and preserves \(B\) and \(Z\). For \(g\in\Gamma\), define
\[
\chi_B(g)=\#\{v:g(v)=v\}-1,
\quad\chi_E(g)=\#\{e:g\text{ fixes the oriented }e\}-\#\{e:g\text{ reverses }e\},
\quad\chi_Z(g)=\chi_E(g)-\chi_B(g).
\]
The first identity follows by identifying \(B\) with the vertex permutation representation modulo constants. The second counts the trace of the signed edge permutation; the third uses \(\mathbb R^E=B\oplus Z\). The complete group enumeration, derived by extending every compatible partial vertex permutation, yields the following **joint character multiplicities** \((\chi_B,\chi_Z):m\):

| Graph | \(|\Gamma|\) | \((\chi_B,\chi_Z):m\) | \(\sum_g\chi_B(g)\chi_Z(g)\) |
|---|---:|---|---:|
| Tetrahedral | \(24\) | \((-1,-1):3;\ (-1,1):6;\ (0,0):8;\ (1,-1):6;\ (3,3):1\) | \(0\) |
| Cubical | \(48\) | \((-1,-3):3;\ (-1,-1):6;\ (-1,1):24;\ (1,-1):8;\ (3,-1):6;\ (7,5):1\) | \(0\) |
| Dodecahedral | \(120\) | \((-1,-1):15;\ (-1,1):69;\ (1,-1):20;\ (3,-3):15;\ (19,11):1\) | \(0\) |

Here the finite group calculation is an exact exhaustive one, with its complete enumeration algorithm embedded in `CHECKER.py`. The character inner product \(|\Gamma|^{-1}\sum_g\chi_B(g)\chi_Z(g)\) therefore vanishes. Character orthogonality implies \(\operatorname{Hom}_\Gamma(B,Z)=\{0\}\) and \(\operatorname{Hom}_\Gamma(Z,B)=\{0\}\), both over the real field. Every projection onto \(Z\) has the form \(C+TQ\) with \(T:B\to Z\); it is invariant precisely when \(T\) intertwines the representations. Hence \(C\) is the unique invariant projection onto \(Z\). The same reasoning makes \(Q\) the unique invariant projection onto \(B\).

For **any** projection \(P\) onto either invariant subspace, the average \(|\Gamma|^{-1}\sum_{g\in\Gamma}gPg^{-1}\) is still a projection onto that subspace and has norm at most \(\|P\|\) for each endpoint norm. It must equal the orthogonal projection by uniqueness. Thus \(Q,C\) globally minimize their respective norms, separately for \(p=1\) and \(p=\infty\). This argument invokes only the explicitly verified character sums and standard finite-group character orthogonality, not an unproved assumption of irreducibility.

**2. Exact norm extraction.** The same complete enumeration proves that each graph's automorphism group acts transitively on its edges. Consequently all columns of \(Q\) have the same \(\ell_1\) norm; since \(Q\) and \(C\) are symmetric, their row and column absolute sums agree. For a reference edge \(e=\{a,b\}\) oriented from \(a\) to \(b\), solve
\[
L\phi=\mathbf1_a-\mathbf1_b,\qquad L=DD^{\mathsf T}.
\]
The edge-current column of \(Q\) is \(i_f=\phi(f_-)-\phi(f_+)\). Setting \(s=\sum_f|i_f|\) and \(r=i_e>0\), the corresponding column of \(C\) gives the exact identities
\[
\|Q\|_{1\to1}=s,\qquad \|C\|_{1\to1}=1+s-2r.
\]
The numerical certificates for the three primal graphs are exact rationals:

| Graph | \(s\) | \(r\) | \(1+s-2r\) |
|---|---:|---:|---:|
| Tetrahedral | \(3/2\) | \(1/2\) | \(3/2\) |
| Cubical | \(2\) | \(7/12\) | \(11/6\) |
| Dodecahedral | \(38/15\) | \(19/30\) | \(34/15\) |

For a self-contained dodecahedral certificate, present its vertices as \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+2}\), all indices modulo \(10\). For a unit source from \(u_0\) to \(u_1\), the following potential, with the additive constant fixed by the stated values, satisfies all \(20\) Laplacian equations exactly:
\[
(\phi(u_0),\ldots,\phi(u_9))=
\tfrac1{60}(19,-19,-8,-5,-2,-1,1,2,5,8),
\]
\[
(\phi(v_0),\ldots,\phi(v_9))=
\tfrac1{60}(8,-8,0,-5,0,-2,2,0,5,0).
\]
In particular \(\phi(u_0)-\phi(u_1)=19/30\). For the \(10\) outer-ring edges, \(10\) spokes and \(10\) inner-ring edges, respectively, the absolute current sums are \(19/15\), \(11/15\), \(8/15\). Their sum is \(38/15\); then \(1+38/15-2(19/30)=34/15\). Every edge has the same norm by the proved transitivity, not by an unverified numerical observation.

**3. Planar duality.** On a fixed sphere embedding, primal edge coordinates correspond to dual edge coordinates up to orientation signs. The signed edge map carries the primal cut space isometrically onto the dual cycle space and the primal cycle space onto the dual cut space: primal vertex-star relations become dual facial boundaries and conversely. Thus the projection minima interchange for a planar dual pair. The cube and octahedron are dual, as are the dodecahedron and icosahedron; the tetrahedron is self-dual. Hence the three direct rational calculations and duality give every entry of the displayed table. The duality also transports uniqueness of graph-automorphism-invariant projections, since the dual automorphism action is the corresponding edge action for these polyhedra.

## Verification

`CHECKER.py` is a standalone Python 3 standard-library exact-arithmetic verification script. It defines the tetrahedral, cubical and dodecahedral edge lists; enumerates **all** adjacency-preserving vertex permutations by backtracking over every feasible image; verifies all their signed-edge characters and vanishing character inner products; checks edge transitivity; solves rational grounded Laplacian systems; checks Kirchhoff equations at all vertices; and reproduces the current sums and the displayed five-graph duality table. No floating-point calculations, external graph libraries, or unproved numerical solvers are used. Run with `python3 CHECKER.py`. This certificate is finite and is not presented as an infinite-class proof.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (arXiv:2305.12582, posted 2023-05-21), Sections 1.4–1.5 and Theorem 5, give the general averaging and representation-disjointness criterion for minimal cycle projections. The present result **uses** those established methods rather than claiming they are new; its specific contribution is the complete finite Platonic classification, the exact dodecahedral/icosahedral constants, and the concrete character and electrical-current certificates. The inspected paper's family calculations concern discrete tori and Hamming graphs, not this five-solid table. Their earlier Laakso/diamond work concerns different graph families. Published graph-metric \(\ell_1\)-embedding distortion values for the dodecahedral graph are not projection constants for its cut or cycle spaces and do not imply this table.

## Limitations

The theorem treats only the five Platonic graphs over real scalar fields and the **relative** projection problem in the standard unweighted edge-coordinate \(\ell_1\) and \(\ell_\infty\) spaces. It does not classify all minimizers, all Archimedean graphs, arbitrary edge weights, or arbitrary regular graphs. Full mathematical correctness of the finite certificate depends on the transparent exact backtracking/linear-algebra algorithm; it has been checked directly but not independently audited. A bibliographic search and inspection of the closest primary article found no covering computation, but absence of a search match is not proof of publication priority. The result is not claimed to be an independent derivation of the general invariant-projection theorem.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first publicly posted 2023-05-21), especially Sections 1.1, 1.4–1.5 and 2.1; https://arxiv.org/abs/2305.12582.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949; https://arxiv.org/abs/2007.07949. Background on the different recursive-graph projection problem.
