# Four-port scattering threshold for the equilateral Shrikhande–rook quantum-graph pair

## Finding

Let \(R\) be the \(4\times4\) rook graph and \(S\) the Shrikhande graph, each with 16 vertices, degree 6 and strongly regular parameters \((16,6,2,2)\). Replace every edge by an interval of common length \(\ell>0\), equipped with the free one-dimensional Schrödinger operator \(-d^2/dx^2\) and standard Neumann–Kirchhoff matching. Attach one semi-infinite free lead to each of \(t\) **distinct** compact vertices. With the lead ordering part of the experimental configuration, let \(\mathcal S_t(G;k)\) denote the set of attainable \(t\)-channel scattering matrices, allowing any distinct contact vertices and their relabelings.

For each real positive \(k\) satisfying
\[
\sin(k\ell)\ne0,\qquad 6\cos(k\ell)\notin\{6,2,-2\},
\]
we have
\[
\mathcal S_t(R;k)=\mathcal S_t(S;k)\quad(t=1,2,3),\qquad
\mathcal S_4(R;k)\ne\mathcal S_4(S;k).
\]
The **sharp four-port witness** is a set of four mutually adjacent vertices of \(R\) (a complete row or column), whereas \(S\) has no such four-clique. This is a statement about *sets of attainable responses*, not the assertion that every four-port attachment distinguishes the two graphs. A single fixed probe frequency \(k\ell=\pi/3\) suffices.

## Assumptions and scope

The rook graph has vertex set \(\mathbb Z_4^2\); distinct \((i,j)\) and \((i',j')\) are adjacent when \(i=i'\) or \(j=j'\). The Shrikhande graph has the same vertex set, with undirected adjacency defined by differences in
\[
\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}\subset\mathbb Z_4^2.
\]
No finite-edge potentials, unequal edge lengths, repeated contact vertices, magnetic phases or exotic junction couplings are allowed. The scattering convention at a lead, with outward coordinate \(x\ge0\), is incoming amplitude \(a\) multiplying \(e^{-ikx}\) and outgoing amplitude \(b\) multiplying \(e^{ikx}\). The on-shell matrix maps \(a\) to \(b\). The excluded wavenumbers are precisely those where the derivation requires a separate singular-energy analysis; no assertion is made there.

## Proof

**1. Exact vertex reduction.** Write \(c=\cos(k\ell)\), \(s=\sin(k\ell)\), \(z=6c\), and let \(A\) be the 16-by-16 adjacency matrix. If the endpoint values of a finite edge are \(f_u,f_v\), the outward derivative at \(u\) equals \(k(f_v-cf_u)/s\). Hence the finite-edge contribution to the Kirchhoff condition is \((k/s)(Af-zf)\). Introduce \(M=zI-A\) and the vertex-to-port inclusion \(P\). At the lead endpoints, \(f_{\mathrm{ports}}=a+b\) and the sum of outward lead derivatives is \(ik(b-a)\). Kirchhoff matching gives
\[
Mf=isP(b-a)=isP(f_{\mathrm{ports}}-2a).
\]
For \(z\notin\{6,2,-2\}\), \(M\) is invertible. Define the real symmetric port resolvent
\[
G_P=(P^T M^{-1}P),
\]
where \(P\) consists of standard-basis column vectors at the selected vertices. Restricting the equation to the ports yields \((I-isG_P)f_{\mathrm{ports}}=-2isG_Pa\). Therefore
\[
\Sigma_P(k)=-(I+isG_P)(I-isG_P)^{-1}.
\]
Because \(G_P\) is real symmetric and \(s\ne0\), the denominator is invertible and \(\Sigma_P\) is unitary. Moreover the transform is injective:
\[
G_P=(is)^{-1}(\Sigma_P+I)(\Sigma_P-I)^{-1}.
\]
The latter inverse always exists under these assumptions, since \(\Sigma_P-I=-2(I-isG_P)^{-1}\).

**2. Strong regularity collapses the entire resolvent.** Both adjacency matrices obey \(A^2=4I+2J\) and \(AJ=6J\), where \(J\) is the all-ones matrix. It follows directly that their spectra are \(6\) (multiplicity 1), \(2\) (multiplicity 6) and \(-2\) (multiplicity 9), and
\[
(zI-A)^{-1}=\frac{zI+A}{z^2-4}+\frac{2J}{(z-6)(z^2-4)}.
\]
Indeed, multiplying the right-hand side by \(zI-A\) gives \(I\) using the two polynomial identities. For a port set \(T\) of size \(t\),
\[
G_T=\frac{zI_t+A[T]}{z^2-4}+\frac{2J_t}{(z-6)(z^2-4)}.
\]
The coefficient of \(A[T]\) is nonzero at every allowed energy. By the injective Cayley transform, two port configurations, with the same ordering, have identical scattering matrices if and only if their **induced labeled adjacency matrices** coincide. Up to port permutation, the attainable scattering response types are therefore in exact correspondence with attainable induced graph isomorphism types on \(t\) vertices.

**3. Equality through three contacts.** On 1 or 2 vertices both graphs attain all graph types. On 3 vertices there are precisely four simple graph types: no edge, one edge, a path of two edges, and a triangle. Both graphs attain a triangle because every adjacent pair has exactly 2 common neighbors, and attain a two-edge path because every nonadjacent pair has exactly 2 common neighbors. For an adjacent pair, its open neighborhood union outside the pair has size \(2(6-1)-2=8\); hence among the remaining 14 vertices at least 6 are adjacent to neither endpoint, producing the one-edge triple. For a nonadjacent pair, the union of their neighborhoods has size \(6+6-2=10\); among the remaining 14 vertices at least 4 are adjacent to neither, producing an independent triple. Thus \(\mathcal S_t(R;k)=\mathcal S_t(S;k)\) for \(1\le t\le3\), including channel-order permutations.

**4. Sharp four-contact separation.** Each rook row is a four-clique, whereas the six neighbors of any Shrikhande vertex induce a 6-cycle: this is checked directly by differences of the six specified generating vectors. A four-clique in the Shrikhande graph would force a triangle in the neighborhood of one of its vertices, impossible. Therefore a rook four-clique produces a scattering matrix which no Shrikhande four-port configuration can produce (even after port relabeling), by step 2.

For an explicit single-energy witness, let \(k\ell=\pi/3\), so \(z=3\) and \(s=\sqrt3/2\). The resolvent becomes
\[
G_T=\frac35I_t+\frac15A[T]-\frac{2}{15}J_t.
\]
For the rook four-clique, \(G_T=\tfrac25I_4+\tfrac1{15}J_4\), whose off-diagonal entries all equal \(\tfrac1{15}\). Any four Shrikhande contacts contain a nonedge, giving an off-diagonal entry \(-\tfrac2{15}\). The Cayley transform makes their scattering matrices unequal. This completes necessity, sufficiency and the sharpness claim.

## Verification

The included standard-library `verify.py` constructs both graphs from their generators, verifies the exact strongly regular adjacency identity, exhaustively canonicalizes all induced configurations of 1 through 4 vertices, and confirms that only the rook graph realizes a four-clique (eight labeled four-cliques). It computes the full rational inverse of \(3I-A\) by Gauss–Jordan elimination and compares every entry with the derived resolvent identity, and numerically checks unitarity for representative scattering matrices at \(k\ell=\pi/3\). Run `python3 verify.py`; the expected final line begins `VERIFY_OK`. The finite checks substantiate the exact algebraic proof; the universal wavenumber statement is proved symbolically, not inferred from sampled energies.

## Relationship to prior work

Mugnolo and Pivovarchik, arXiv:2211.05465 (2022), establish the premise of distinguishing cospectral equilateral metric graphs by scattering, concentrating on one lead and graphs of up to six vertices, trees of at most nine vertices and fuzzy-ball examples; their explicit results do not identify this 16-vertex strongly regular pair's minimum channel threshold. Lawrie, Gnutzmann and Tanner, arXiv:2309.11251 (2023), provide general scattering Green-function machinery rather than the rook–Shrikhande discrimination threshold. Kurasov and collaborators, arXiv:2505.16621 (2025), construct general isoscattering graph families with M-functions; their examples and theorems do not assert the sharp four-contact threshold for this pair. Band, Sawicki and Smilansky, arXiv:1007.0222 (2010), study symmetry-generated isoscattering quantum graphs. The graph pair and its differing clique geometry are classical inputs, not claimed as new. The new claim is the physically normalized scattering-response classification with a sharp minimum number of terminals.

## Limitations

Only identical positive finite-edge lengths, the free edge Laplacian and Neumann–Kirchhoff conditions are covered. The theorem excludes \(\sin(k\ell)=0\) and the discrete adjacency spectral values; it does not classify embedded eigenmodes or limiting scattering matrices there. A generic-frequency distinction of the *sets of attainable responses* need not identify an unknown graph under an arbitrarily selected four-contact layout. Similar arithmetically symmetric graphs or differently indexed multi-terminal scattering studies could contain equivalent formulations; a negative bibliographic search is not mathematical proof of publication priority.

## References

- D. Mugnolo and V. Pivovarchik, *Distinguishing co-spectral quantum graphs by scattering*, arXiv:2211.05465, first public 2022-11-10, https://arxiv.org/abs/2211.05465.
- T. Lawrie, S. Gnutzmann and G. Tanner, *Closed form expressions for the Green's function of a quantum graph—a scattering approach*, arXiv:2309.11251, first public 2023-09-20, https://arxiv.org/abs/2309.11251.
- P. Kurasov et al., *Families of isospectral and isoscattering quantum graphs*, arXiv:2505.16621 (2025), https://arxiv.org/abs/2505.16621.
- R. Band, A. Sawicki and U. Smilansky, *Scattering from isospectral quantum graphs*, arXiv:1007.0222, https://arxiv.org/abs/1007.0222.
- M. Ingremeau, *Scattering resonances of large weakly open quantum graphs*, arXiv:2012.08369, https://arxiv.org/abs/2012.08369 (quantum-graph scattering classifies under primary MSC 81Q35, among its primary codes).
