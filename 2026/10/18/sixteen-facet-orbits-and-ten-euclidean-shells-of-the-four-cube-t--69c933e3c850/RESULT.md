# Sixteen facet orbits and ten Euclidean shells of the four-cube transportation ball

## Finding
Consider the graph \(Q_4\) on the sixteen binary four-tuples, with an edge whenever two tuples differ in exactly one coordinate, and with shortest-path (Hamming) metric. The real Lipschitz-free unit ball \(B\) is a fifteen-dimensional symmetric edge polytope. Under the natural four-cube graph automorphism group \(B_4\), together with global negation of the facet normal, **its 990 facets form exactly sixteen symmetry orbits**. Their sizes and canonical representatives are given below. With the standard Euclidean inner product on the zero-sum coordinate hyperplane, **the squared Euclidean lengths of all centered facet normals take exactly ten values**:

| Squared normal length \(S\) | Number of facets | Facet distance from the origin |
|:--:|--:|:--:|
| \(4\) | 2 | \(1/2\) |
| \(23/4\) | 32 | \(2/\sqrt{23}\) |
| \(7\) | 112 | \(1/\sqrt7\) |
| \(31/4\) | 224 | \(2/\sqrt{31}\) |
| \(8\) | 204 | \(1/\sqrt8\) |
| \(39/4\) | 192 | \(2/\sqrt{39}\) |
| \(11\) | 128 | \(1/\sqrt{11}\) |
| \(47/4\) | 32 | \(2/\sqrt{47}\) |
| \(12\) | 48 | \(1/\sqrt{12}\) |
| \(16\) | 16 | \(1/4\) |

Here \(S=\sum_v f(v)^2-(\sum_v f(v))^2/16\) for an integer facet potential \(f\) with \(f(0)=0\). In the next table, each sixteen-character string has a digit in position \(v+1\), corresponding to the binary vertex whose integer label is \(v\in\{0,\ldots,15\}\). Subtracting the first digit from all sixteen gives the root-normalized potential. These are exact orbit representatives, *not* hexadecimal numerals.

| Orbit | Size | \(S\) | Height range | Representative height word |
|--:|--:|:--:|--:|:--|
| 1 | 192 | \(39/4\) | 3 | `3221211021101221` |
| 2 | 128 | \(31/4\) | 2 | `2110100110212110` |
| 3 | 128 | \(11\) | 3 | `3221211021101021` |
| 4 | 96 | \(7\) | 2 | `2110100110012110` |
| 5 | 96 | \(31/4\) | 2 | `2110100110012112` |
| 6 | 96 | \(8\) | 2 | `2110100110212112` |
| 7 | 64 | \(8\) | 3 | `3221211021121221` |
| 8 | 48 | \(12\) | 3 | `3221211021103221` |
| 9 | 32 | \(23/4\) | 2 | `2110100110010110` |
| 10 | 32 | \(47/4\) | 3 | `3221211021101001` |
| 11 | 16 | \(7\) | 2 | `2110100110010112` |
| 12 | 16 | \(8\) | 2 | `2110100112212110` |
| 13 | 16 | \(8\) | 2 | `2110102110212110` |
| 14 | 16 | \(16\) | 4 | `4332322132212110` |
| 15 | 12 | \(8\) | 2 | `2110102112010112` |
| 16 | 2 | \(4\) | 1 | `1001011001101001` |

The aggregate count of 990 facets, the smallest centered facet distance \(1/4\), and the sixteen facets touching that smallest radius are **known prior results**; this finding is the exhaustive sixteen-orbit classification and complete ten-shell distance distribution, with their relationship specified by the tables.

## Assumptions and scope
Let \(V=\{0,1\}^4\), enumerated as integers from 0 through 15 by ordinary binary expansion; \(Q_4\) has all edges \(\{v,v\oplus2^i\}\) for a coordinate \(i\in\{0,1,2,3\}\). Set \(H=\{z\in\mathbb R^{16}:\sum_{v\in V}z_v=0\}\). The Lipschitz-free unit ball, with one vertex distinguished as the base point, is identified linearly and isometrically with
\[
 B=\operatorname{conv}\{\pm(e_u-e_v):\{u,v\}\in E(Q_4)\}\subset H.
\]
Its polar is \(B^\circ=\{f\in H:|f_u-f_v|\le1\text{ for every graph edge}\}\), and facet inequalities of \(B\) have normalized form \(\langle z,f\rangle\le1\) for a polar vertex \(f\). Here \(B_4=\mathbb F_2^4\rtimes S_4\) has order \(384\) and acts on vertices by bitwise translations and coordinate permutations. The stated orbits use this group plus the independent involution \(f\mapsto-f\), modulo additive constants. The Euclidean metric in \(H\) is the inherited standard coordinate Euclidean metric, not an arbitrary Banach-space Euclidean identification.

## Proof
**1. Polar vertices are unit-increment height functions.** Any molecule \((e_u-e_v)/d(u,v)\) decomposes as the mean of edge molecules along a shortest path. Hence the Lipschitz-free ball equals the symmetric edge polytope above. Since the graph is connected, its edge vectors span \(H\) and \(B\) is full-dimensional. Thus a facet is the polar of an extreme point of the bounded Lipschitz polytope. A potential \(f\in B^\circ\) is extreme if and only if its tight edges \(\{u,v\}\) satisfying \(|f_u-f_v|=1\) contain a spanning tree: if their incidence vectors do not span \(H\), a nonzero orthogonal perturbation leaves all tight inequalities unchanged and, in both sufficiently small signs, all nontight inequalities strict. Conversely a connected set of tight edges fixes every potential modulo constants and therefore makes \(f\) extreme.

For the connected bipartite graph \(Q_4\), all edges of an extreme potential must be tight. Indeed, let \(T\) be the connected spanning graph of tight edges. An arbitrary cube edge \(\{u,v\}\) joins opposite bipartition classes, so \(T\) has a path of **odd** length between \(u\) and \(v\). Every increment on that path is \(\pm1\), and their sum is an odd integer. The original Lipschitz bound makes the absolute endpoint difference at most 1; hence that difference is exactly \(\pm1\). Conversely, if all 32 edges are tight then their incidence vectors span \(H\), making \(f\) extreme. A root normalization \(f(0)=0\) therefore identifies the facets bijectively with integer height functions whose edge increments have absolute value 1.

**2. Finite, exact enumeration with an explicit exhaustive certificate.** Fix the rooted spanning tree with parent \(p(v)=v\oplus(v\mathbin{\&}(-v))\) for each nonzero integer vertex \(v\); in words, remove the least significant set bit of \(v\). Parent indices are smaller, so the fifteen tree-edge signs uniquely produce all \(2^{15}=32768\) root-normalized candidates by the recurrence \(f(v)=f(p(v))+\varepsilon_v\), where each \(\varepsilon_v\in\{-1,+1\}\). Retain a candidate precisely when the remaining seventeen non-tree edges likewise have difference of absolute value 1. Since the tree-edge sign parametrization is injective and surjective onto the tree-consistent potentials, this finite algorithm checks *every* possible facet normal and no others.

The accompanying self-contained Python 3 program `verify_q4.py` implements this full \(32768\)-case test in `candidate_heights_from_tree`, then implements **a separate backtracking construction** by Hamming-weight layers: at each new vertex \(v\), intersect the two-element height sets given by all previously assigned Hamming parents. These independently generated sets coincide and contain exactly 990 potentials. This confirms the previously published 990 total but does not reassert it as new.

**3. Exact symmetry partition.** The full graph automorphism group of a four-cube is the group of arbitrary bit translations followed by coordinate permutations: a graph automorphism is fixed by the image of 0 and the permutation of the four neighbors of that vertex, while successive unique common-neighbor constraints on cube faces fix the remaining layers. Thus there are exactly \(2^4\cdot4!=384\) graph automorphisms. Let \(m\) be such an automorphism and \(\sigma\in\{-1,+1\}\). On normalized height functions the signed action is
\[
  (m,\sigma)\cdot f(v)=\sigma\bigl(f(m(v))-f(m(0))\bigr).
\]
There are 768 such operations. For a chosen representative, the code generates its full 768-image set; remove this orbit and repeat until none remain. All orbit images satisfy the edge conditions and the output consists of the sixteen disjoint orbits and representative words in the finding table. The listed sizes sum to 990, giving an exact partition of all facets. As a separate group-theoretic checksum, the code sums the fixed-potential counts over all 768 group actions; the total is exactly \(12288=768\cdot16\), so Burnside's lemma independently recovers sixteen orbits.

**4. Complete Euclidean shell spectrum.** Under the coordinate quotient by constants, the unique centered representative of \(f\) is \(f^\circ_v=f(v)-\frac1{16}\sum_wf(w)\). Its squared Euclidean length is the rational number
\[
  S(f)=\sum_{v\in V} f(v)^2-\frac{1}{16}\left(\sum_{v\in V}f(v)\right)^2.
\]
The facet is the hyperplane \(\langle z,f^\circ\rangle=1\), so its distance from the origin is \(S(f)^{-1/2}\). The program evaluates this expression with exact rational arithmetic for every one of the completely enumerated 990 potentials. It produces precisely the ten norm values and multiplicities in the first table, and it checks that every potential in a displayed orbit has its displayed squared norm. Its maximum, \(16\), and the resulting inradius \(1/4\), are also consequences of existing general results for hypercubes. The ten-level **full distribution**, in contrast, is the new assertion.

## Verification
Run `python3 verify_q4.py` with standard Python 3, no third-party packages or input files. The executable exhausts 32768 spanning-tree assignments, checks 32 graph edges, independently enumerates every admissible Hamming-layer extension, constructs all 384 graph automorphisms and 768 signed transformations, checks orbit disjointness and exact representative words, computes all shell multiplicities using `fractions.Fraction`, and verifies the independent Burnside identity. It reports `ALL EXACT CHECKS PASSED` with the enumerated tables; the complete finite-domain proof relies on the demonstrably exhaustive parametrization, not on sampling or a timeout. Standard integer and rational arithmetic avoids floating-point classification errors. The script is an exact finite checker, not an independent external audit.

## Relationship to prior work
Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces* (arXiv:2102.01219, first public 2021-02-01; primary MSC 46B20), establishes foundational extremal structure for Lipschitz-free Banach balls. It treats **vertices of the primal ball**, whereas the present theorem classifies **facets of a specific finite-dimensional ball**; the assertions do not imply one another. Higashitani, Jochemko and Michałek (arXiv:1807.07678, Theorem 3.1) give the general connected-tight-edge facet characterization; this is credited, not new. D'Alì, Delucchi and Michałek (arXiv:1910.05193, Lemma 4.5) establish the special bipartite all-tight-edge condition, likewise prior.

Çelik, Jamneshan, Montúfar, Sturmfels and Venturello, *Wasserstein Distance to Independence Models* (arXiv:2003.06725, Proposition 10 and the following enumeration), **explicitly report the total 990 normalized Lipschitz vertices of the four-cube**, and identify equivalence to graph homomorphisms into the infinite path. A 2011 treatment (arXiv:1111.6055) also contains the same 990 numerical total. Neither inspected source gives the sixteen graph-symmetry-plus-negation orbits or ten exact Euclidean facet-distance shells. Chen, Davis and Korchevskaia (arXiv:2107.12315) study general facet subgraphs, not this evaluated orbit-and-shell classification.

*Sharp Euclidean inballs and high-dimensional center freedom in hypercube symmetric edge polytopes*, a separately available mathematical result, proves the inradius and count of origin-touching facets for all hypercubes. Those consequences are **excluded from the claim of originality** here. A published treatment of fan-graph facet-distance spectra is on a different graph and does not imply the hypercube shell values. The novelty claim is only the simultaneous complete 16-orbit / 10-shell refinement at the canonical first four-dimensional Hamming cube.

## Limitations
The classification is for the graph-metric real Lipschitz-free ball of \(Q_4\) alone, not arbitrary hypercubes \(Q_d\) and not its complete face lattice. It uses the stated natural automorphism-plus-sign group, not a classification under all possibly additional abstract combinatorial symmetries. Numerical values depend on the specified Euclidean coordinate realization. It neither changes the known total of 990 facets nor the known inradius/contact count. Bibliographic overlap with unindexed classifications cannot be ruled out; independent external scientific review is not claimed.

## References
1. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219, first posted 2021-02-01; primary MSC 46B20. https://arxiv.org/abs/2102.01219
2. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first posted 2018-07-20. https://arxiv.org/abs/1807.07678
3. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first posted 2019-10-11. https://arxiv.org/abs/1910.05193
4. T. Ö. Çelik, A. Jamneshan, G. Montúfar, B. Sturmfels, L. Venturello, *Wasserstein Distance to Independence Models*, arXiv:2003.06725, first posted 2020-03-15. https://arxiv.org/abs/2003.06725
5. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first posted 2021-07-26. https://arxiv.org/abs/2107.12315
6. Y. X. Zhang, *Adinkras for Mathematicians*, arXiv:1111.6055, first posted 2011. https://arxiv.org/abs/1111.6055
7. *Sharp Euclidean inballs and high-dimensional center freedom in hypercube symmetric edge polytopes*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-euclidean-inballs-and-high-dimensional-center-freedom-in-h--c4dd39cda462
