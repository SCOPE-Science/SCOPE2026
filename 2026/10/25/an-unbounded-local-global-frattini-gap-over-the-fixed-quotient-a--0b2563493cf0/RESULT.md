# An unbounded local–global Frattini gap over the fixed quotient \(A_5\)

## Finding
Let \(H=A_5\) act by conjugation on the set \(\Omega\) of its six Sylow \(5\)-subgroups. Put \(V=\mathbb F_2^{\Omega}\), and define the \(H\)-submodules
\[
 C=\mathbb F_2(1,1,1,1,1,1),\qquad
 W=\{v\in V:\sum_{\omega\in\Omega}v_\omega=0\}.
\]
For every integer \(t\ge1\), let \(G_t=V^{\oplus t}\rtimes H\), with the diagonal permutation action. The Frattini subgroup and the **local Frattini subgroup** are exactly
\[
 \Phi(G_t)=W^{\oplus t},\qquad
 \Psi(G_t)=C^{\oplus t}.
\]
In particular, \(\Phi(G_t)/\Psi(G_t)\) is elementary abelian of order \(2^{4t}\). Thus the discrepancy between the two Frattini constructions is unbounded even for split extensions with the same nonabelian simple quotient \(A_5\), and with an elementary abelian normal kernel.

## Assumptions and scope
All groups are finite. \(\Phi(K)\) denotes the intersection of maximal proper subgroups of \(K\). For each prime \(p\mid |K|\), let \(S_p\) be a Sylow \(p\)-subgroup, and let \(B_K=\bigcap_{g\in K}gBg^{-1}\) denote the core of a subgroup \(B\). The local Frattini subgroup is \(\Psi(K)=\prod_p(\Phi(S_p))_K\), following Costanzo and the earlier definition cited there. Exponents \(t\) range over all positive integers. No claim is made about minimal order or about general finite groups beyond this family.

## Proof
**The six-point \(A_5\)-module.** The six Sylow \(5\)-subgroups form a transitive \(H\)-set, with stabilizer a dihedral subgroup of order \(10\). The action is \(2\)-transitive; an ordered-pair stabilizer has order \(2\) and exchanges the other four points in two transpositions. The finite permutation enumeration in `artifacts/verify.py` checks the group, six-point action, \(2\)-transitivity, and these orbit properties directly from the even permutations on five letters.

We claim that the only \(\mathbb F_2H\)-submodules of \(V\) are \(0,C,W,V\). If a nonzero invariant subspace \(U\) contains a vector of weight \(1\), point transitivity gives all six coordinate vectors and thus \(U=V\). If it contains a weight-\(2\) vector, \(2\)-transitivity gives all pair sums, which span \(W\). For weight \(3\), choose two positions in its support and act by their nonidentity pointwise stabilizer. The third position is moved, so the sum of the two weight-\(3\) vectors is a weight-\(2\) vector; since the original vector has odd weight, \(U=V\). For weight \(4\), its complement is a two-element set: map this missing pair to another pair sharing one point, and subtract (equivalently, add in characteristic \(2\)) to obtain weight \(2\). For weight \(5\), transitivity moves the missing position and again produces weight \(2\); the odd original weight then gives \(U=V\). If the only possible nonzero weight is \(6\), \(U=C\). Every vector of \(W\) has even weight and \(W\) has codimension one, so the claimed complete submodule list follows. In particular \(W\) is the unique maximal proper \(H\)-submodule of \(V\), with \(\dim W=5\) and \(\dim C=1\).

**Global Frattini subgroup.** For any finite elementary abelian normal subgroup \(E\) of a split extension \(E\rtimes H\), the intersection of its Frattini subgroup with \(E\) is the intersection of maximal proper \(H\)-submodules of \(E\), i.e. the module radical. Indeed, if a maximal subgroup \(M\) avoids \(E\), then \(EM=E\rtimes H\), and \(M\cap E\) is a maximal \(H\)-submodule. Conversely \(B\rtimes H\) is maximal whenever \(B\) is a maximal proper \(H\)-submodule. Maximal subgroups containing \(E\) impose no further restriction on the intersection with \(E\). As the quotient of \(G_t\) by \(V^{\oplus t}\) is \(A_5\), whose Frattini subgroup is trivial, \(\Phi(G_t)\) lies inside \(V^{\oplus t}\). Since the radical of a finite direct sum is the direct sum of the radicals (or directly because the only simple quotients of \(V\) are trivial), its intersection with the kernel is \(W^{\oplus t}\). Thus \(\Phi(G_t)=W^{\oplus t}\).

**Local Frattini subgroup.** A Sylow \(2\)-subgroup of \(H\) is \(P\cong C_2\times C_2\). For \(S=V^{\oplus t}\rtimes P\), the Burnside basis formula \(\Phi(S)=S'S^2\) gives
\[
\Phi(S)=[V^{\oplus t},P]=[V,P]^{\oplus t},
\]
because both \(V\) and \(P\) have exponent \(2\), and \((vp)^2=v+p(v)\) in additive notation. Each of the five conjugate Sylow \(2\)-subgroups of \(H\) acts on \(\Omega\) with three orbits of size two. These five perfect matchings of the six points are pairwise edge-disjoint and collectively partition the fifteen edges of the complete graph on \(\Omega\); an explicit exact list is reproduced by the verifier. For a matching \(\{\{i,j\},\{k,l\},\{m,n\}\}\), the subspace \([V,P]\) is spanned by the three pair sums \(e_i+e_j,e_k+e_l,e_m+e_n\). It therefore consists precisely of vectors having equal coordinates at the ends of each matched edge. The intersection of these five three-dimensional subspaces is \(C\), since every pair of coordinates is matched in exactly one of the matchings. Consequently,
\[
 (\Phi(S))_{G_t}=\left(\bigcap_{h\in H}[V,P]^h\right)^{\oplus t}=C^{\oplus t}.
\]
Every Sylow \(3\)-subgroup and Sylow \(5\)-subgroup of \(G_t\) is cyclic of prime order and has trivial Frattini subgroup. There are no other prime divisors of \(|G_t|\). Hence \(\Psi(G_t)=C^{\oplus t}\). The dimensions of the two subgroups are \(5t\) and \(t\), proving the asserted quotient order.

## Verification
Run `python3 artifacts/verify.py`. It uses only the Python standard library, constructs \(A_5\) as the sixty even permutations of five points, constructs the six Sylow \(5\)-subgroups and their conjugation permutation action, checks the group order and \(2\)-transitivity, exhaustively enumerates all binary subspaces of the six-dimensional permutation module in reduced-row-echelon form and checks the four invariant subspaces, constructs all five Sylow \(2\)-subgroup orbit matchings, checks that their fifteen edges partition the complete graph, and calculates the intersection of the five commutator subspaces. The successful terminal marker is `VERIFY_OK`. The arbitrary-\(t\) statement follows from the direct-sum identities proved above, not from extrapolating a finite experiment.

## Relationship to prior work
Costanzo, *On the local Frattini subgroup of a finite group* (arXiv:2610.16821v1), defines \(\Psi\), proves \(\Psi\le\Phi\), and develops sufficient conditions for containment of a Frattini normal \(p\)-subgroup in \(\Psi\). His results do not state this split affine \(A_5\) family or compute its gap. Semmen, *The Group Theory Behind Modular Towers* (2006), Example 5.6, identifies the same six-point permutation module modulo its fixed line as the first universal \(2\)-Frattini module for \(A_5\) and describes its simple factors. That known module structure is an essential precedent; it does not state a local Frattini calculation for the split semidirect products considered here. The new comparison is the explicit equality \(\Psi(G_t)=C^{\oplus t}\) versus \(\Phi(G_t)=W^{\oplus t}\), based on the Sylow orbit-matchings.

## Limitations
No minimality of the order of \(G_1\) (\(3840\)) is claimed. The result does not classify all groups with \(\Psi\ne\Phi\); it establishes an explicit family with unbounded quotient index and a fixed simple complement. Prior unpublished or unindexed treatments of this exact affine family cannot be excluded by bounded literature searches. The full original papers by Rose (1980) and Kaplan–Lev–Mann–Solomon (2017) were not directly read; their relevance to general Frattini conditions was checked through Costanzo's exposition, and the possibility of an earlier equivalent application remains a priority risk.

## References
1. David G. Costanzo, *On the local Frattini subgroup of a finite group*, arXiv:2610.16821v1 (12 October 2026), especially Sections 1, 3, 4; https://arxiv.org/html/2610.16821v1.
2. Darren Semmen, *The Group Theory Behind Modular Towers*, Séminaires & Congrès 13 (2006), 343–366, Example 5.6; https://studylib.net/doc/10698619/the-group-theory-behind-modular-towers-by-darren-semmen.
3. Gil Kaplan, Arieh Lev, Avinoam Mann, Ron Solomon, *Adequate field extensions and Frattini closed groups*, Communications in Algebra 45 (2017), 4622–4630 (cited by Costanzo; full text not directly inspected).
4. John S. Rose, *Frattini normal subgroups of finite groups*, J. Reine Angew. Math. 316 (1980), 83–98 (cited by Costanzo; full text not directly inspected).
