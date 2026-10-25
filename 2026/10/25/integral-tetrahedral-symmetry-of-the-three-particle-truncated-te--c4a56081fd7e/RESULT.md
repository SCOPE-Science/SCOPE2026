# Integral tetrahedral symmetry of the three-particle truncated-tetrahedron configuration space

## Finding

Let \(T\) be the graph of the truncated tetrahedron and let \(B_3(T)\) be the space of three *unordered, distinct* points on its geometric realization. The automorphism group of \(T\) is naturally \(\mathfrak S_4\). There is an isomorphism of **integral** \(\mathbb Z[\mathfrak S_4]\)-modules
\[
H_3(B_3(T);\mathbb Z)\cong \mathbb Z[\{0,1,2,3\}],
\]
the permutation lattice on the four triangular faces of \(T\). A distinguished basis comprises the four three-torus classes \(z_j\), with one independently moving point on each of the three triangles other than triangle \(j\). For all \(\sigma\in\mathfrak S_4\),
\[
\sigma_*z_j=z_{\sigma(j)}.
\]
Hence the rational character at identity, transposition, double transposition, three-cycle and four-cycle equals \((4,2,0,1,0)\); the invariant integral lattice is \(\mathbb Z(z_0+z_1+z_2+z_3)\). This invariant line **has no integral equivariant retraction** from the full module, although rationally the representation is the sum of the trivial and standard three-dimensional modules.

## Assumptions and scope

Give the graph \(T\) vertices \((u,v)\), where \(u,v\in\{0,1,2,3\}\) and \(u\ne v\). The three vertices with fixed first coordinate \(u\) form the triangle \(T_u\), and for each unordered pair \(\{u,v\}\) there is a connector edge \((u,v)-(v,u)\). Thus \(T\) has 12 vertices and 18 edges. Every graph automorphism permutes its four unique three-cycles; the connectors identify the corresponding vertices, so \(\operatorname{Aut}(T)\cong\mathfrak S_4\). The configuration space uses the ordinary topological realization of the graph, not a discrete vertex-configuration approximation and not a matching complex. The assertion is only about degree-three integral homology and its full graph automorphism action; other degrees are not classified.

## Proof

**1. A chain model.** Use the reduced Świątkowski chain model for unordered graph configurations established by An, Drummond-Cole and Knudsen. At each degree-three vertex \(v\), order the three incident edges \(e_{v,0},e_{v,1},e_{v,2}\) and use the two degree-one half-edge differences \(h_{v,i}=H_{v,i}-H_{v,0}\), \(i=1,2\). Their differential is \(\partial h_{v,i}=e_{v,i}-e_{v,0}\); edge symbols have weight one and degree zero. A degree-one difference has weight one. The model's weight-three chain modules in degrees three and two therefore have respective free integral bases of sizes
\[
\binom{12}{3}2^3=1760,\qquad \binom{12}{2}2^2\cdot18=4752.
\]
In degree three, each monomial is an oriented product of three half-edge differences at distinct vertices. The differential follows the Koszul sign rule and is precisely the sparse integer matrix constructed by the accompanying checker. There is no degree-four term at weight three, so \(H_3(B_3(T);\mathbb Z)=\ker\partial_3\).

**2. Four integral product cycles.** For each triangle \(T_u\), orient its three edges cyclically using the increasing order of its three neighbour labels. Define a degree-one, weight-one chain \(c_u\) as the sum, over the three vertices of \(T_u\), of the outgoing half-edge minus the incoming half-edge. Each such difference is expanded against the local fixed baseline. Every internal triangle edge cancels in \(\partial c_u\), so \(\partial c_u=0\). If \(j\) is the one omitted triangle, set
\[
z_j=\prod_{u\ne j}^{\text{in increasing order}}c_u.
\]
Products use distinct vertices on disjoint triangles; every such product is an integral degree-three cycle. The four supports lie in disjoint sets of monomials distinguished by their three occupied triangle labels. Every coefficient of a nonzero monomial is \(\pm1\). In particular, the four classes are linearly independent over \(\mathbb Q\), and their direct sum is a primitive rank-four sublattice of the ambient degree-three chain lattice.

**3. Exact upper bound and integral saturation.** The complete \(4752\)-row by \(1760\)-column differential has rank **1756** over \(\mathbb F_2\) and separately over \(\mathbb F_{32003}\). These are exact sparse Gaussian eliminations, not approximate numerical ranks. Since the rational rank is at least the rank modulo any prime, \(\dim_{\mathbb Q}\ker\partial_3\le4\). The four independent cycles force equality. An arbitrary integral cycle is consequently a rational combination of the four \(z_j\). Reading a unique degree-three monomial supported only by a given \(z_j\), where its coefficient is \(\pm1\), shows that each rational coefficient is an integer. Therefore the four cycles form an integral basis of the entire kernel. The chain-model comparison theorem identifies that kernel with the stated integral homology, without torsion or additional degree-three classes.

**4. Integral symmetry and non-splitting.** The permutation \(\sigma\in\mathfrak S_4\) acts on vertices by \((u,v)\mapsto(\sigma(u),\sigma(v))\), carrying half-edge differences to the differences of their permuted incident edges and introducing the Koszul sign when reordering factors. The exact chain calculation confirms for each of the 24 permutations and all four basis cycles that \(\sigma_*z_j=z_{\sigma(j)}\); the output coefficient is **positive one**, not merely an equality up to sign. This also follows by multiplying the three individual triangle-orientation signs and the sign of reordering the three degree-one factors. Thus the integral module is the four-point permutation lattice. An invariant vector has all four coordinates equal. Every equivariant homomorphism from this lattice to the trivial integral line is a multiple of the coordinate-sum map and hence acts on the invariant generator by a multiple of four; no such map is a retraction. Rationally averaging over four coordinates gives the usual splitting.

## Verification

The accompanying standalone `verify.py`, using only the Python standard library, constructs the graph and both complete integral chain bases. It generates each column of the differential from the local half-edge formula; verifies the four product cycles are nonzero, disjointly supported and killed by the integral differential; computes the exact ranks modulo 2 and 32003; and tests the full integral chain action of each of the 24 tetrahedral automorphisms on each of the four cycles (96 equality checks). The program outputs `TRUNCATED_TETRAHEDRON_B3_Z4_S4_PERMUTATION_VERIFIED` on success. Exact modular-rank checks are not alone an integral classification: the primitive unit-supported cycles and the rational rank sandwich complete that step.

## Relationship to prior work

The graph-configuration comparison theorem and reduced Świątkowski chains used here are due to An, Drummond-Cole and Knudsen; this work claims neither a new chain model nor an algorithm for general graph braid groups. Their study includes a case analysis of the untruncated complete tetrahedral graph, but the three-particle degree-three group and its graph symmetry for the truncated tetrahedral graph are not furnished there. Maciążek and Sawicki discuss product cycle classes and higher graph braid homology for several families, without providing this four-triangle integral symmetry calculation. Drummond-Cole's tabulations of graphs with at most nine edges do not include the 18-edge graph here. The theorem consequently gives a concrete top-degree and equivariant refinement at a natural tetrahedral graph, conditional only on the cited established chain-model comparison. A failure to locate an equivalent statement is not proof of uniqueness.

## Limitations

No other homological degree, torsion in other degrees, integral cohomology ring, graph braid fundamental group, or equivariant homotopy type is determined. The result concerns three **unordered** particles, not labeled particles, and uses the full topological configuration space. The computation is finite and complete because the relevant weight-three chain modules are explicitly exhausted; finite checks are used only to verify their exact matrix ranks and chain identities. An equivalent unindexed published calculation remains possible. Independent mathematical audit has not been performed.

## References

1. B. H. An, G. C. Drummond-Cole, B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351 (first public version 2017-08-08), especially the Comparison Theorem and reduced Świątkowski complex, https://arxiv.org/abs/1708.02351.
2. M. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, *Symmetry* **11** (2019), article 1280, doi:10.3390/sym11101280, especially product cycles.
3. G. C. Drummond-Cole, *Betti numbers of unordered configuration spaces of small graphs*, arXiv:1906.00692 (first public version 2019-06-03), https://arxiv.org/abs/1906.00692.
4. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first public version 2020-08-24), https://arxiv.org/abs/2008.10371.
