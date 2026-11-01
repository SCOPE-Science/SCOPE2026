# Projective-plane summands in the open-neighborhood complexes of the Shrikhande and rook graphs

## Finding
Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph. For a finite loopless graph \(G\), define the **open** Lovász neighborhood complex \(\mathcal N(G)\) to contain a nonempty vertex set \(\sigma\) precisely when there exists a vertex \(c\notin\sigma\) adjacent to every vertex of \(\sigma\). Then
\[
\boxed{\mathcal N(S)\cong\mathcal N(R)\simeq\mathbb{RP}^{2}\vee\bigvee^{55}S^{2}.}
\]
Here the first symbol is an isomorphism of abstract simplicial complexes, whereas the second is a nonequivariant homotopy equivalence. In particular, in either case
\[
\pi_1\cong\mathbb Z/2,\qquad
\widetilde H_1(-;\mathbb Z)\cong\mathbb Z/2,\qquad
\widetilde H_2(-;\mathbb Z)\cong\mathbb Z^{55},
\]
with all other reduced integral homology zero. Each original neighborhood complex is pure five-dimensional and not shellable.

## Assumptions and scope
Use the common vertex set \((\mathbb Z/4\mathbb Z)^2\), labeled by \(4i+j\) for \(0\le i,j<4\). In \(S\), two vertices are adjacent when their coordinate difference is one of
\[
(1,0),\ (-1,0),\ (0,1),\ (0,-1),\ (1,1),\ (-1,-1)\pmod4.
\]
In \(R\), distinct vertices are adjacent exactly when their first or second coordinates coincide. These are the two nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\), a classical graph classification; the classification itself is not proved here. The claim concerns **open** rather than closed neighborhoods; adding the center to each neighborhood changes the complex. No larger strongly regular family or equivariant homology decomposition is asserted.

## Proof
**1. Exact simplicial identification.** Index vertices and neighborhood centers from \(0\) to \(15\). The permutations
\[
\begin{aligned}
\rho={}&(0,8,2,10,7,3,5,1,14,6,12,4,9,13,11,15),\\
\pi={}&(11,1,9,3,2,4,0,6,5,15,7,13,12,10,14,8)
\end{aligned}
\]
are written as images of \(0,1,\ldots,15\). Directly checking the six neighbors of every center proves
\[
\pi(N_S(c))=N_R(\rho(c))\qquad(0\le c<16).
\]
Thus the two families of facet sets agree after relabeling by \(\pi\), and \(\pi\) induces an isomorphism of their full simplicial complexes. An isomorphism between their canonical bipartite incidence coverings is known independently; the explicit face bijection is used here to verify that the same computation applies to both complexes, not claimed as a new graph-theoretic rigidity principle.

**2. Complete finite face posets.** For either graph every open neighborhood has six vertices. Enumerating all subsets of those sixteen neighborhoods, with independent checking over every one of the \(2^{16}\) vertex masks, gives exactly \(808\) nonempty simplices and the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,320,240,96,16).
\]
Every maximal face is an entire six-vertex neighborhood, hence the complex is pure of dimension five. All pairs of distinct graph vertices have two common neighbors, giving the complete \(1\)-skeleton as a further check.

**3. An exhaustive acyclic matching.** Represent a simplex by its sixteen-bit mask. Temporarily include the empty face and, for pivots \(v=0,1,\ldots,15\), traverse currently unmatched masks by increasing cardinality and then increasing mask value. Pair \(\sigma\) with \(\sigma\cup\{v\}\) if \(v\notin\sigma\) and both faces are still unmatched. Omit the pair between the empty face and the vertex \(0\), so the latter remains as an ordinary critical zero-cell. This determines \(375\) nonempty matching pairs in each complex. Exactly one zero-cell, one one-cell, and fifty-six two-cells remain critical, with no other critical cells.

To establish acyclicity without relying on a heuristic greedy rule, form **all \(2736\) codimension-one incidences** among nonempty faces. Orient each incidence downward except for a matched incidence, oriented upward. A complete topological sort removes all \(808\) faces for each graph, proving that the directed face-poset graph is acyclic. Forman's finite discrete-Morse theorem therefore gives a homotopy-equivalent CW complex containing one cell in dimension zero, one in dimension one, and fifty-six in dimension two.

**4. Exact attaching degrees.** Orient each simplex by increasing vertex labels. For a codimension-one face \(\tau=\sigma\setminus\{v\}\), its incidence sign is \((-1)^t\), where \(t\) is the number of elements of \(\tau\) smaller than \(v\). The signed Morse boundary can be computed by recursively eliminating the lower simplex in each matched pair: if \((\alpha,\beta)\) is a pair and the incidence of \(\alpha\) in \(\partial\beta\) is \(u\in\{\pm1\}\), replace \(\alpha\) by \(-u(\partial\beta-u\alpha)\), recursively projecting the remaining faces onto critical cells. Acyclicity makes this a finite recursive computation. This is integral elementary chain cancellation, not a calculation merely modulo a prime.

The unique critical one-cell has zero cellular boundary. For the rook graph, of the fifty-six critical two-cells, thirty-eight have boundary coefficient zero, nine have coefficient \(+2\), and nine have coefficient \(-2\) on that one-cell. For the Shrikhande graph, the corresponding counts are thirty-nine, thirteen, and four. Hence in both cases the greatest common divisor of the fifty-six integral attaching degrees is exactly \(2\).

The CW one-skeleton is \(S^1\). Its fifty-six two-cell attaching maps are classified by their integer degrees. A Nielsen basis transformation of the attaching wedge \(\bigvee^{56}S^1\) realizes integral elementary column operations on the vector of degrees, reducing it to \((2,0,\ldots,0)\) without changing the homotopy type of the mapping cone. A degree-two two-cell attached to \(S^1\) is \(\mathbb{RP}^2\); the other fifty-five two-cells attach trivially and yield the displayed sphere wedge. This proves the claimed **homotopy equivalence**, not just the homology groups.

**5. Shellability.** A pure shellable five-dimensional complex has reduced integral homology concentrated in degree five. The exhibited nonzero first and second homology therefore exclude shellability for either complex.

## Verification
The accompanying standard-library program `verify_neighborhood.py` reconstructs the two adjacency matrices, verifies every degree and common-neighbor count, tests both explicit permutations on all neighborhood facets, enumerates and independently checks all face masks, constructs the nonempty Morse matchings, verifies acyclicity across every Hasse incidence, and computes the signed Morse boundary recursively. It additionally computes simplicial Betti numbers directly over \(\mathbb F_2\) and \(\mathbb F_3\), independently of Morse cancellation. The Betti vectors in degrees zero through five are \((1,1,56,0,0,0)\) and \((1,0,55,0,0,0)\) for either graph, in agreement with the integral homotopy type and its unique two-torsion summand. The exact integers \(0,\pm2\), rather than these field calculations, certify the integral attachment. Running `python3 verify_neighborhood.py` produces the full record in `verification_output.txt` and ends with `OPEN_NEIGHBORHOOD_RP2_PLUS_55_S2_OK`.

## Relationship to prior work
Shukla's 2018–2019 neighborhood-complex classification treats graphs of maximum degree at most three and certain four-regular circulants; these degree-six graphs fall outside its theorems [1]. Matsushita's general theorem identifies the fundamental group of an open neighborhood complex with a graph-theoretic even fundamental group, but does not calculate either graph's group or its remaining homotopy type [2]. The known isomorphism between the canonical bipartite double covers of the two graphs [3] already predicts that their open neighborhood complexes are isomorphic: the equality between the two cases is **not** presented as novel independently of the homotopy calculation.

A published open-rook-graph result determines a cofiber and integral homology above degree two but explicitly leaves the low-degree groups and complete homotopy type undetermined [4]. The known scale-two graph Čech computations use **closed** neighborhoods, giving a distinct complex, and the published Shrikhande/rook independence-complex comparison also uses a different face condition [5,6]. These results do not imply the projective-plane summand or the precise fifty-five additional spheres. The new content is the exact *open* neighborhood homotopy classification with its integral attaching degree, not the classical graph parameters, covering isomorphism, or results for other complexes.

## Limitations
This is an exact finite result for two sixteen-vertex graphs, not a uniform theorem for other parameters. The calculation is reproducible but relies on the explicitly supplied complete finite acyclic matching and signed boundary algorithm; an unexecuted transcript or field-rank computation alone would not prove the integral homotopy assertion. No group-equivariant wedge decomposition is claimed. A covering theorem or equivalent calculation not identified in the inspected literature may exist; the novelty comparison is not an independent certification.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1, first public 2018-02-13; *Electron. J. Combin.* **26** (2019), #P2.4. https://arxiv.org/abs/1802.04526

[2] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, 2012; *J. Math. Sci. Univ. Tokyo* **24** (2017), 321–353. https://arxiv.org/html/1210.2803v4

[3] *Cores of cubelike graphs*, *European J. Combin.* **87** (2020), article 103092; discussion of the isomorphic bipartite double covers of the Shrikhande and rook graphs. https://doi.org/10.1016/j.ejc.2020.103092

[4] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, publicly indexed mathematical research record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45

[5] *Scale-two Čech homotopy distinguishes the Shrikhande and rook graphs*, publicly indexed mathematical research record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-scale-two-ech-homotopy-distinguishes-the-shrikhande-and-rook-gra--5b6e4436155e

[6] *Independence complexes of the Shrikhande and four-by-four rook graphs have different sphere-wedge homotopy types*, publicly indexed mathematical research record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187

[7] R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* **134** (1998), 90–145, for the discrete-Morse reduction theorem.
