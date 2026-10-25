# Two regular embeddings of the Dyck graph and an index-four integral torus obstruction

## Finding
Let \(D\) be the 32-vertex Dyck graph, and let \(X=\operatorname{UConf}_2(|D|)\) be the space of unordered configurations of two distinct points on its geometric realization. For \(p,q\in\{6,8\}\), let \(L_{p,q}\) be the integral subgroup of \(H_2(X;\mathbb Z)\) spanned by the fundamental classes of the embedded product tori belonging to vertex-disjoint simple cycles of lengths \(p\) and \(q\). Then
\[
H_2(X;\mathbb Z)\cong\mathbb Z^{104},\qquad
H_2(X;\mathbb Z)/L_{6,6}\cong\mathbb Z^{32},
\]
\[
H_2(X;\mathbb Z)/(L_{6,6}+L_{6,8})\cong(\mathbb Z/2\mathbb Z)^2,\qquad
L_{6,6}+L_{6,8}+L_{8,8}=H_2(X;\mathbb Z).
\]
All such tori arise from exactly 16 six-cycles and 12 eight-cycles. There are 72 disjoint six–six pairs, 96 six–eight pairs, and 18 eight–eight pairs. The 192 graph automorphisms divide these pairs into five orbits: six–six orbits of sizes 24 and 48, one six–eight orbit of size 96, and eight–eight orbits of sizes 6 and 12. Either eight–eight orbit alone, when adjoined to all hexagon-involving tori, yields integral generation. Precisely two eight–eight tori are necessary and sufficient to complete such a generating collection; they may be chosen from either individual eight–eight orbit.

## Assumptions and scope
The graph has vertices \(0,1,\ldots,31\). Join each \(i\) to \(i+1\pmod{32}\) and to \(i+d_i\pmod{32}\), where the LCF list is \((-13,5,-5,13)\) repeated eight times. Retain every unordered edge only once. This is the Dyck graph's standard 32-vertex cubic presentation. The cycles are embedded *simple cycles*, and the two cycles forming a torus must be vertex-disjoint. Orientation choices affect signs of individual generators but not the asserted lattices, ranks, or quotient types. All homology groups are ordinary singular homology with integer coefficients; there are no collision-permitting sinks. The 16 hexagons and 12 octagons also reflect the graph's two classical regular-map realizations, one toroidal with hexagonal faces and one of genus three with octagonal faces.

## Proof
**1. The finite cubical model.** The unordered deleted-product cubical complex has one zero-cell \(\{u,v\}\) for each pair of different vertices, one oriented one-cell \((e,v)\) for each edge and nonincident vertex, and one oriented square \((e,f)\) for each pair of vertex-disjoint edges. For two distinct points on this loopless finite simplicial graph, this complex is homotopy equivalent to \(X\) by the standard equivariant deleted-product deformation retraction, as in Barnett–Farber. Orient each edge from its smaller to its larger vertex. Index edges lexicographically and orient squares with their first edge index smaller than their second. If \(e=(a,b)\), \(f=(c,d)\), and \(e\) precedes \(f\), then
\[
\partial_2(e,f)=(f,b)-(f,a)-(e,d)+(e,c).
\]
The zero-, one-, and two-cell counts are respectively \((496,1440,1032)\). There are no cells above dimension two. Direct signed incidence checks give \(\partial_1\partial_2=0\), and sparse Gaussian elimination over \(\mathbb F_{101}\) gives \(\operatorname{rank}(\partial_2\bmod101)=928\). This yields the upper bound \(\operatorname{rank}_{\mathbb Z}\ker\partial_2\le104\).

**2. Exhaustive short cycles and torus chains.** For each candidate least cycle vertex, a depth-first search visits only larger unused vertices, closes at lengths six or eight, and identifies the two reverse orientations. It finds exactly 16 and 12 cycles. Enumerating all unordered vertex-disjoint pairs gives 72, 96, and 18 pairs of the three listed types. Write the oriented edge chains of disjoint cycles as \(\alpha=\sum_i a_i e_i\) and \(\beta=\sum_j b_j e_j\). The corresponding torus chain is
\[
z_{\alpha,\beta}=\sum_{i\ne j}a_i b_j\operatorname{sgn}(j-i)\,(e_{\min(i,j)},e_{\max(i,j)}),
\]
where \(\operatorname{sgn}(j-i)\) is \(+1\) if \(i<j\) and \(-1\) if \(i>j\). Disjointness ensures each term is a legitimate square. A direct integer check proves \(\partial_2 z_{\alpha,\beta}=0\) for every one of the 186 tori.

**3. Integral completeness.** Form the \(1032\times186\) integer matrix \(T\) of the signed torus chains in lexicographically indexed square coordinates. The verifier selects 104 square-coordinate rows by exact Gaussian elimination over \(\mathbb F_2\). For the resulting \(104\times186\) matrix \(T_0\), exact column Hermite normal form gives \(\operatorname{HNF}(T_0)=I_{104}\). In particular, the 186 cycle columns have rational rank at least 104. Since they lie in \(\ker\partial_2\), the modular rank bound in step 1 forces \(\operatorname{rank}_{\mathbb Z}\ker\partial_2=104\). The projection \(\pi:\ker\partial_2\to\mathbb Z^{104}\) onto the selected square coordinates is surjective, because its image contains the columns of \(T_0\). It is also injective: its domain is a free abelian group of rank 104 and its image has rank 104. Hence \(\pi\) is an isomorphism. Since the torus columns already project onto the entire target, they generate \(\ker\partial_2=H_2(X;\mathbb Z)\) integrally. This argument does not assume that modular rank alone proves integral saturation.

**4. Exact filtration quotients.** Restrict \(T_0\) to its 72 six–six columns. Its integer Smith normal form has 72 unit diagonal entries and no nonunit invariant factors. Because \(\pi\) is an integral isomorphism, the quotient is \(\mathbb Z^{32}\). Restrict instead to the 168 columns with at least one hexagon. Their column Hermite normal form is square with absolute determinant \(4\), and its Smith normal form has 102 unit entries and exactly two entries equal to \(2\). Thus the remaining integral quotient is \((\mathbb Z/2\mathbb Z)^2\), although these 168 tori already span rationally. Restoring all 18 eight–eight columns gives Hermite normal form \(I_{104}\), hence zero quotient.

**5. Automorphism-orbit completions.** Exhaustive graph isomorphism enumeration yields 192 automorphisms. Transporting the 186 unordered cycle pairs gives the orbit sizes and length types in the statement. The six- and twelve-element orbits consist entirely of eight–eight tori. For each one separately, adjoining its columns to the 168 hexagon-involving columns yields column Hermite normal form \(I_{104}\). Thus either orbit maps onto the two-dimensional quotient \((\mathbb Z/2\mathbb Z)^2\). A cyclic subgroup cannot generate this quotient, so at least two added classes are required; since the image of each individual orbit spans the quotient, two classes from either orbit suffice.

## Verification
Run `python verify_dyck.py` with the dependency versions in `requirements.txt` (or compatible releases). The program reconstructs the graph from the displayed LCF list, all short cycles, the entire signed cubical boundary and the torus chains; verifies \(\partial_1\partial_2=0\); computes the modular rank; and performs exact Hermite/Smith integer computations. It also enumerates all 192 automorphisms and checks both orbit completion assertions. On successful execution it prints `VERIFY_OK_DYCK_SHORT_CYCLE_TORUS_LATTICES`, the dimension and orbit counts, both Smith factors, and the deterministic indices of the 104 projected square coordinates. All required computations are bounded finite exhaustive procedures, not extrapolations from samples.

## Relationship to prior work
Barnett–Farber's 2009 paper supplies the deleted-product model and intersection framework, principally studying ordered two-point configurations and planar graphs. Farber–Hanbury (2010) studies ordered spaces of mature graphs and homology through intersection forms, without the Dyck graph's cycle-length-constrained integral torus lattices. An–Knudsen (2022; preprint 2020) develops geometric generation of second homology for planar graph braid groups and explicitly gives a nonplanar obstruction to general extension of their planar statement. Those statements do not identify the present 32-vertex nonplanar graph's particular index-four filtration or either completing orbit. The two regular-map presentations motivate the selected six- and eight-cycle lengths. The exact numbers and integral indices above are established by the included finite certificates rather than asserted on the basis of general theorems.

## Limitations
The result concerns only two unordered points on this fixed graph and only product tori formed by vertex-disjoint cycles of lengths six and eight. It does not classify all longer-cycle tori, higher-particle configuration spaces, the full cohomology ring, or the complete homotopy type. The modular rank calculation is used solely as an upper bound; the integer HNF/SNF steps are essential to the integral claims. No independent mathematical audit or exhaustive survey of unpublished literature is asserted.

## References
1. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180 (first posted 2009-03-12), Algebraic & Geometric Topology 9 (2009), 593–624. https://arxiv.org/abs/0903.2180
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (2010), Algebraic & Geometric Topology 10 (2010), 2203–2227. https://arxiv.org/abs/1005.2300
3. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020), Journal of Topology 15 (2022), 666–691. https://arxiv.org/abs/2008.10371
4. E. W. Weisstein, *Dyck Graph*, MathWorld (LCF representation and toroidal embedding). https://mathworld.wolfram.com/DyckGraph.html
5. A. E. Brouwer, *Dyck graph* (32 vertices, 192 automorphisms, relation to the Shrikhande graph). https://aeb.win.tue.nl/graphs/Dyck.html
