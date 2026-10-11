# Automorphism-module structure of the cube three-cut complex
## Finding
Let \(Q_3\) be the graph on \(\mathbb F_2^3\) whose edges join vectors differing in one coordinate, and let \(\Delta=\Delta_3(Q_3)\) be the ordinary \(3\)-cut complex: its facets are the complements of three-vertex sets that induce disconnected subgraphs. Every graph automorphism is uniquely
\[
g_{\sigma,b}:x\longmapsto \sigma x+b,
\qquad \sigma\in S_3,\quad b\in\mathbb F_2^3.
\]
Define the one-dimensional characters
\[
\varepsilon(g_{\sigma,b})=(-1)^{|b|},
\qquad
\omega(g_{\sigma,b})=\operatorname{sgn}(\sigma)(-1)^{|b|},
\]
where \(|b|\) is the Hamming weight of \(b\). Let \(\mathcal D\) be the four unordered antipodal vertex pairs, equivalently the four long body diagonals of the geometric cube. Then
\[
\widetilde H_3(\Delta;\mathbb Q)\cong\mathbb Q_\omega,
\qquad
\widetilde H_4(\Delta;\mathbb Q)\cong
\mathbb Q_\varepsilon\otimes\mathbb Q[\mathcal D],
\]
and all other reduced rational homology groups vanish. Thus, for every \(g=g_{\sigma,b}\),
\[
\chi_3(g)=\operatorname{sgn}(\sigma)(-1)^{|b|},
\qquad
\chi_4(g)=(-1)^{|b|}\#\operatorname{Fix}_{\mathcal D}(g).
\]

## Assumptions and scope
The result concerns the ordinary cut complex, not the total cut complex. Homology is taken over \(\mathbb Q\), and the action is the natural simplicial action induced by the full graph automorphism group. The nonequivariant ranks are included to make the representation calculation self-contained; the structural content is the identification of the two homology representations.

The affine maps above give \(8\cdot6=48\) graph automorphisms. Conversely a cube automorphism is determined by the image of one vertex and by a permutation of its three neighbors, so there are at most \(8\cdot6\) automorphisms. Hence these affine maps form the full automorphism group.

## Proof
There are exactly \(32\) disconnected three-subsets of the eight vertices. Their complements generate a simplicial complex with nonempty face vector
\[
(8,28,56,64,32).
\]
Using lexicographically oriented simplices, the four nonzero boundary maps have exact rational ranks
\[
(7,21,35,28).
\]
Therefore the Betti vector is \((1,0,0,1,4)\), so only \(\widetilde H_3\) and \(\widetilde H_4\) can carry nontrivial reduced rational representations.

For degree \(3\), the attached certificate gives an explicit integral cycle \(z\) and an integral cocycle \(c\) with \(c(z)=1\). Direct action of every one of the \(48\) automorphisms satisfies
\[
c(gz)=\operatorname{sgn}(\sigma)(-1)^{|b|}.
\]
Because \(\widetilde H_3\) is one-dimensional, this proves \(\widetilde H_3(\Delta;\mathbb Q)\cong\mathbb Q_\omega\).

For degree \(4\), let \(L(g)\) be the simplicial Lefschetz number. Exact signed fixed-simplex counts give
\[
L(g)=\sum_{k=0}^4(-1)^k\operatorname{tr}(g\mid C_k(\Delta;\mathbb Q)).
\]
Since the only homology is in degrees \(0,3,4\),
\[
L(g)=1-\chi_3(g)+\chi_4(g).
\]
The exhaustive calculation over all \(48\) automorphisms yields
\[
\chi_4(g)=(-1)^{|b|}\#\operatorname{Fix}_{\mathcal D}(g).
\]
The right side is exactly the character of \(\mathbb Q_\varepsilon\otimes\mathbb Q[\mathcal D]\). Maschke's theorem then identifies the rational representations.

## Verification
Run `python3 verify.py` beside `certificate.json`. The verifier reconstructs the cube and all cut-complex faces from the definition, checks \(\partial^2=0\), computes the exact rational boundary ranks, verifies the displayed cycle and cocycle, enumerates all \(48\) automorphisms, checks that each preserves the complex, evaluates the signed action on \(z\), computes every chain Lefschetz trace, and verifies both character formulas for every group element. The expected output begins with `VERIFY_OK` and reports face vector \((8,28,56,64,32)\), boundary ranks \((7,21,35,28)\), and Betti vector \((1,0,0,1,4)\).

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue define \(k\)-cut complexes and explicitly motivate the induced rational homology representation when a graph symmetry group acts. Their family table gives equivariant results for complete multipartite graphs, cycles, and squared cycles, while the cube is not among the listed families. The nonequivariant homotopy type of this particular cube cut complex has been computed previously; that information fixes only the homology dimensions and does not determine the automorphism representations proved here.

## Limitations
The theorem is specific to \(Q_3\) and to rational representations. It does not classify equivariant homology for higher hypercubes or integral representation lattices, and it does not assert that the displayed module pattern persists for other cut parameters. A differently phrased or non-indexed prior computation of the same full character remains a residual bibliographic risk.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, “Topology of Cut Complexes of Graphs,” arXiv:2304.13675, first public 2023-04-26; SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675.
