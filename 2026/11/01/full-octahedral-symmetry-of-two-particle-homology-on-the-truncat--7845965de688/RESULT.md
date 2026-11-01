# Full octahedral symmetry of two-particle homology on the truncated octahedron

## Finding

Let \(T\) be the graph on the 24 signed coordinate permutations of \((0,1,2)\), with two vertices adjacent precisely when their squared Euclidean distance is \(2\). This is the graph of the truncated octahedron, equivalently the three-dimensional permutohedron. Put \(X=\operatorname{UConf}_2(|T|)\), the space of unordered pairs of distinct points on its geometric realization. Its full automorphism group \(G\) consists of the 48 signed coordinate permutations and is isomorphic to \(S_4\times C_2\).

Write \(V_{(4)},V_{(1,1,1,1)},V_{(3,1)},V_{(2,1,1)},V_{(2,2)}\) for the five irreducible rational \(S_4\)-modules, of dimensions \(1,1,3,3,2\), respectively. A superscript \(+\) or \(-\) specifies the character of the central inversion \(C_2\), so \(V_\lambda^\pm=V_\lambda\boxtimes\varepsilon_\pm\). The complete positive-degree rational homology representations are

\[
\begin{aligned}
H_1(X;\mathbb Q)\cong{}& V_{(1,1,1,1)}^+\oplus 2V_{(1,1,1,1)}^-\oplus 2V_{(2,1,1)}^+\oplus V_{(2,1,1)}^-\oplus V_{(2,2)}^-,\\
H_2(X;\mathbb Q)\cong{}&V_{(4)}^+\oplus2V_{(4)}^-\oplus V_{(1,1,1,1)}^+\oplus3V_{(3,1)}^+\oplus6V_{(3,1)}^-\\
&\quad\oplus3V_{(2,1,1)}^+\oplus3V_{(2,1,1)}^-\oplus2V_{(2,2)}^+\oplus V_{(2,2)}^-.
\end{aligned}
\]

Thus the rational Betti vector is \((1,14,55)\); higher homology vanishes. The 55 embedded tori associated to unordered pairs of disjoint faces form an integral basis of \(H_2(X;\mathbb Z)\), by the classical planar ordered-configuration theorem and the transfer argument below. That general face-torus basis theorem is **prior work**, not a newly claimed theorem.

The full character is specified by the following ten classes. The \(S_4\) label is the cycle type on the four opposite-vertex pairs of the cube \(\{\pm1\}^3\), while \(\varepsilon\) is the product of the three coordinate sign changes. The columns give class size and traces on the two positive-degree homology groups.

| \(S_4\) cycle type | \(\varepsilon\) | Size | \(\operatorname{tr} H_1\) | \(\operatorname{tr} H_2\) |
| --- | ---: | ---: | ---: | ---: |
| \(1^4\) | \(+\) | 1 | 14 | 55 |
| \(1^4\) | \(-\) | 1 | 0 | -7 |
| \(2,1,1\) | \(+\) | 6 | -6 | 5 |
| \(2,1,1\) | \(-\) | 6 | 0 | -5 |
| \(2,2\) | \(+\) | 3 | 2 | -5 |
| \(2,2\) | \(-\) | 3 | -4 | 5 |
| \(3,1\) | \(+\) | 8 | 2 | 1 |
| \(3,1\) | \(-\) | 8 | 0 | -1 |
| \(4\) | \(+\) | 6 | 0 | -1 |
| \(4\) | \(-\) | 6 | 2 | 1 |

There is also a geometric description of the unique full-group invariant. The 55 unordered disjoint facet pairs break into **five** orbits: two square–square orbits of sizes 3 and 12; two hexagon–hexagon orbits of sizes 4 and 12; and a square–hexagon orbit of size 24. Every same-type orbit has a stabilizer interchanging its two faces, hence acts by a minus sign on the associated torus and supplies no invariant vector. The 24 mixed square–hexagon pairs have no such interchange. Orient every facet by the outward-normal convention, and always take the square cycle as the first torus factor. Their **24-term integral orbit sum**

\[
\Omega=\sum_{\substack{F\text{ square},\ H\text{ hexagon}\\V(F)\cap V(H)=\varnothing}}[T_{F,H}]
\]

is a primitive generator of \(H_2(X;\mathbb Z)^G\cong\mathbb Z\). Thus the one surviving rational quotient two-class has an explicit geometric invariant lift.

Let \(G^{\mathrm{rot}}\) denote the 24-element subgroup of signed permutation matrices of determinant \(+1\), and let \(\iota\) be central inversion. Rational homology of the respective ordinary topological quotients has Betti vectors

\[
\begin{aligned}
(\beta_0,\beta_1,\beta_2)(X/G)&=(1,0,1),\\
(\beta_0,\beta_1,\beta_2)(X/G^{\mathrm{rot}})&=(1,2,1),\\
(\beta_0,\beta_1,\beta_2)(X/\langle\iota\rangle)&=(1,7,24).
\end{aligned}
\]

In particular, the full symmetry quotient retains exactly one nonzero positive-degree rational class, whereas removing orientation-reversing symmetries restores two independent first-homology classes.

## Assumptions and scope

The graph is finite and simple, with vertices \(v=(v_1,v_2,v_3)\) the distinct signed permutations of \((0,1,2)\). There are exactly 24 vertices and 36 edges. Its convex hull has six square facets \(v_i=\pm2\) and eight hexagonal facets \(\pm v_1\pm v_2\pm v_3=3\). Every vertex has degree three. Faces are identified with their induced boundary cycles, and a pair of faces is called disjoint when their vertex sets are disjoint. The configuration space uses distinct **points of the geometric graph**, not just pairs of graph vertices or sink-allowed collisions. The homology representation statements use \(\mathbb Q\), and the explicit basis statement in degree two uses \(\mathbb Z\). The automorphism action is induced by its action on the geometric graph. Primary MSC2020: 55R80.

## Proof

**Finite cellular model.** The two-point deleted-product deformation retraction gives an equivariant two-dimensional cubical model. Its oriented cells are unordered pairs of vertices, a vertex and a disjoint oriented edge, and two disjoint oriented edges. With vertex indices increasing along each edge and an order on edges, the chain groups have ranks \(276,792,558\). For edges \(e=(a,b)\), \(f=(c,d)\), the square boundary is
\[
\partial(e\times f)=(b,f)-(a,f)-(d,e)+(c,e),
\]
with the convention that an interchange of the two edge factors reverses orientation. The complex is connected, and \(\chi(X)=276-792+558=42\).

**Degree-two basis and rank.** The fourteen facet boundaries consist of six four-cycles and eight six-cycles. Exactly 55 of their unordered pairs are vertex-disjoint. For each such pair \(\{F,H\}\), the product of the oriented boundary circles gives an embedded torus in \(X\) and an explicit integral cellular two-cycle \(z_{F,H}\). Its square coefficients are products of the oriented edge coefficients, multiplied by \(-1\) when necessary to put edge factors in the chosen order. Direct integer boundary substitution shows \(\partial z_{F,H}=0\). Modulo two the 55 cycle columns have rank 55. A separate bitset elimination on the complete \(558\)-column second-boundary matrix has rank 503 over \(\mathbb F_2\). Therefore the rational boundary rank is at least 503 and at most \(558-55=503\); it is exactly 503, and the displayed tori form a rational basis of \(H_2(X;\mathbb Q)\). The Euler characteristic and connectivity now give \(\beta_1=14\).

For the integral refinement, Barnett–Farber's Theorem 6.1 gives an **integral basis** of ordered two-particle degree-two homology consisting of the 110 ordered tori on disjoint oriented facial pairs. Exchanging the two particle labels sends \([T_{F,H}]\) to \(-[T_{H,F}]\). For the two-sheeted covering from ordered to unordered configurations, transfer sends the unordered torus class to \([T_{F,H}]-[T_{H,F}]\). These 55 differences form a basis of the invariant lattice upstairs. Transfer is injective downstairs because the unordered degree-two cellular homology is the kernel of an integer boundary matrix, hence torsion-free, and covering projection composed with transfer is multiplication by two. Since the 55 displayed classes map onto the entire invariant lattice, they form the asserted integral basis downstairs. This uses the existing general theorem rather than claiming a new integral-basis principle.

**Symmetry and traces.** Every signed coordinate permutation preserves \(T\); all 48 are distinct. There are no further graph automorphisms: the six square facets are exactly the graph's four-cycles, and every vertex lies on exactly one square. Contracting each of those six squares, retaining the twelve edges between squares, gives the octahedral graph \(K_{2,2,2}\). Any graph automorphism permutes these six unique squares and induces an automorphism of \(K_{2,2,2}\); this map is injective because each original vertex is uniquely specified by its square and the different square joined by its one nonsquare edge. Since \(\operatorname{Aut}(K_{2,2,2})\cong (C_2)^3
times S_3\) has order 48, and the explicit 48 signed coordinate permutations act faithfully, they are all the graph automorphisms. A signed orthogonal matrix of determinant \(\delta\) takes the outward-oriented boundary of every face to \(\delta\) times the outward-oriented boundary of its image. Thus the degree-two torus basis is permuted with coefficient \(+1\) if the two images preserve the order of faces, and \(-1\) if they exchange it: the two factors each contribute \(\delta\), whose product is one, while interchanging one-dimensional factors contributes the Koszul sign \(-1\). Accordingly
\[
\operatorname{tr}(g\mid H_2)=\#\{\{F,H\}:gF=F,\ gH=H\}-\#\{\{F,H\}:gF=H,\ gH=F\},
\]
where all pairs counted are disjoint facet pairs.

For each automorphism \(g\), the rational Hopf trace formula on the finite complex gives
\[
\operatorname{tr}(g\mid H_1)=1+\operatorname{tr}(g\mid H_2)-\operatorname{tr}(g\mid C_0)+\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_2).
\]
Each cellular trace is counted by fixed cells with orientation sign. Enumeration of the 55 disjoint face pairs under all 48 symmetries also gives exactly five orbits of sizes \(3,12,4,12,24\). In each of the first four the pair stabilizer exchanges the two faces; the mixed 24-element orbit cannot interchange its differently shaped faces. These facts prove the asserted invariant integral orbit sum and show that the full-group invariant sublattice in degree two has rank one. Exhaustive application to all 48 coordinate symmetries yields the ten-row table. The permutation on the four body diagonals and the coordinate-sign product together identify the group with \(S_4\times C_2\). Inner products of both row characters with the ten rational irreducible characters give precisely the two displayed decompositions, with nonnegative integer multiplicities and total dimensions 14 and 55.

**Quotients.** For a finite group acting cellularly on a finite complex, rational homology of its ordinary quotient is the invariant part of rational homology. Averaging the verified characters over the full 48 elements, the determinant-\(+1\) subgroup and the two-element central inversion subgroup gives invariant dimensions \((0,1)\), \((2,1)\), and \((7,24)\) in degrees one and two respectively. Each quotient is connected. This proves all stated quotient Betti vectors.

## Verification

The standalone standard-library Python program `verification/verify.py` rebuilds the graph and the fourteen convex facets from their coordinate definitions, constructs all 276 vertices, 792 edges and 558 squares of the deleted-product complex, checks \(\partial_1\partial_2=0\), checks that each of 55 integral facial tori is closed, and obtains mod-two ranks 503 and 55. It enumerates all 48 signed coordinate symmetries, verifies commutation with both boundary maps for every cellular basis generator, checks each map on each facial torus chain, enumerates the five disjoint-face-pair orbits and all their interchange stabilizers, calculates the ten homology characters by independent cellular and facial methods, and computes the rational irreducible multiplicities by exact character inner products. Running `python3 verification/verify.py` from the extracted package reproduces `verification/output.json` byte-for-byte (apart from terminal handling of the final newline). The checker relies on no downloaded datasets or third-party Python modules.

## Relationship to prior work

Barnett and Farber (first public preprint March 12, 2009), especially their Lemma 1.1 and Theorem 6.1, establish the deleted-product model and integral basis of **ordered** two-particle second homology for planar graphs; the facet-torus basis construction here is a specialization and is explicitly not claimed as new. The first-homology ranks also follow from their general planar calculation. What is determined here is the **specific full 48-element rational homology representation**, its ten character values and irreducible constituents in both degrees, and its three natural symmetry-quotient invariants. Those do not appear as statements or tabulated values in the inspected general theorem; producing them requires the explicit coordinate- and orientation-sensitive symmetry action and complete character calculation. Kurlin's early graph-braid presentation method is methodological rather than an octahedral-module computation; An–Maciażek's planar braid-group quotient theorem addresses fundamental-group presentations, not these homology characters. Earlier calculations on the cuboctahedral and dodecahedral graphs treat different graph configuration spaces. The published graph-metric Rips filtration on the same truncated-octahedral graph uses a different simplicial construction and does not imply the configuration-space representation.

## Limitations

The new contribution is the exact rational equivariant classification **for this one canonical graph**, not a general face-torus-basis theorem; general nonequivariant ranks and face-torus generation have historical antecedents. The calculation does not determine the integral \(G\)-lattice structure of \(H_1\), integral torsion in \(H_1\), cohomology rings, quotient fundamental groups or quotient homotopy types. Computed finite-chain ranks are not substitutes for general infinite-family assertions. The full-text availability of some separate published computational records was limited; an equivalent unindexed octahedral-specific calculation is a residual priority risk. This result has not undergone independent mathematical validation.

## References

1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, Algebraic & Geometric Topology **9** (2009), 593–624; first public preprint March 12, 2009, https://arxiv.org/abs/0903.2180, especially Lemma 1.1 and Theorem 6.1.
2. V. Kurlin, *Computing braid groups of graphs with applications to robot motion planning*, Homology Homotopy and Applications **14** (2012), 159–180; first public preprint August 7, 2009, https://arxiv.org/abs/0908.1067.
3. B. H. An and T. Maciażek, *Geometric Presentations of Braid Groups for Particles on a Graph*, Communications in Mathematical Physics **384** (2021), 1109–1140, https://doi.org/10.1007/s00220-021-04095-x, particularly Theorem 1.
4. E. W. Weisstein, *Truncated Octahedral Graph*, MathWorld, https://mathworld.wolfram.com/TruncatedOctahedralGraph.html (graph identification and automorphism order only).
5. Published result records concerning the cuboctahedral two-particle configuration space and the truncated-octahedral graph-metric Vietoris–Rips filtration, respectively: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-full-symmetry-modules-of-the-cuboctahedral-two-particle-configur--5d6ece5c784b and https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-truncated--3b8391bcadb8 (indexed summaries compared; underlying full files not read).
