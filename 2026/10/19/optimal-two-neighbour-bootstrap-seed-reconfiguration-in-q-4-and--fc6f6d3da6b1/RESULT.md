# Optimal two-neighbour bootstrap seed reconfiguration in \(Q_4\) and \(Q_5\)

## Finding

For two-neighbour bootstrap percolation on the binary cubes \(Q_4\) and \(Q_5\), let \(\mathcal P_d\) be the family of all minimum-cardinality percolating vertex sets. Let \(J_d\) join two sets differing by one arbitrary vertex exchange (token jumping), and let \(T_d\) join them only when the exchanged vertices are adjacent in the cube (token sliding). Both graphs are connected for each \(d\in\{4,5\}\). Their exact invariants are:

| Invariant | \(Q_4\) | \(Q_5\) |
|---|---:|---:|
| Minimum seed cardinality | 3 | 4 |
| Number of optimal seed sets | 144 | 16960 |
| Edges of \(J_d\) | 888 | 551360 |
| Radius and diameter of \(J_d\) | 4, 4 | 4, 4 |
| Edges of \(T_d\) | 384 | 120000 |
| Radius and diameter of \(T_d\) | 6, 6 | 9, 11 |

For \(T_5\) the eccentricities are distributed as
\[
\#\{S\in\mathcal P_5:\operatorname{ecc}_{T_5}(S)=9\}=960,\quad
\#\{S:\operatorname{ecc}_{T_5}(S)=10\}=11200,\quad
\#\{S:\operatorname{ecc}_{T_5}(S)=11\}=4800.
\]
The 960 central seed sets constitute one orbit under the automorphism group of \(Q_5\), represented by \(\{0,3,13,30\}\) in the binary vertex labeling. In contrast, both exchange graphs of \(Q_4\) are self-centered. The 16960 optimal sets of \(Q_5\) form 18 automorphism orbits, whereas the 144 optimal sets of \(Q_4\) form two.

## Assumptions and scope

For \(d\in\{4,5\}\), identify vertices of \(Q_d\) with integers \(0\le v<2^d\), interpreting their \(d\) binary digits as coordinates. Vertices \(u,v\) are adjacent precisely when their bitwise exclusive-or has one nonzero bit. From an initial set \(S\), define \(A_0=S\), and simultaneously update
\[
A_{t+1}=A_t\cup\{v\notin A_t:|N(v)\cap A_t|\ge 2\}.
\]
A set *percolates* if some \(A_t\) equals the full vertex set. The minimum seed cardinality is the smallest \(|S|\) for which this occurs. Distinct minimum sets \(S,S'\) are token-jumping neighbours if \(|S\triangle S'|=2\), and token-sliding neighbours if in addition the unique removed and added vertices are adjacent in \(Q_d\). Each move preserves minimum cardinality and full percolation; intermediate nonpercolating states are forbidden. Distances, radii and diameters refer to the resulting unweighted, undirected graphs.

## Proof

The following finite exhaustive certificate algorithm establishes every claimed value, without appealing to extrapolation from sampled sets.

1. **Exhaustive seed predicate and minimality.** For each \(d\), enumerate every subset of each size up to the first successful size in lexicographic order. Simulate the displayed synchronous update rule until no further vertex becomes infected. Since the infected sets grow monotonically, stabilization occurs after at most \(2^d-|S|\) strict rounds. No set of size 1 or 2 percolates on \(Q_4\), and 144 three-element sets do. No set of size 1, 2 or 3 percolates on \(Q_5\), and 16960 four-element sets do. These are exact exhaustive checks, not probabilistic estimates. The states \(\{0,3,12\}\) on \(Q_4\) and \(\{0,1,6,24\}\) on \(Q_5\) are explicit successful examples.

2. **Exact transition enumeration.** For each minimum state, replace each of its \(k\) members in turn by each excluded vertex, accepting a proposed state only if it belongs to the enumerated optimum family. This constructs all edges of \(J_d\). Retain just those exchanges for which removed and added vertices have Hamming distance one to obtain \(T_d\). The exact numbers of edges are as stated, with every adjacency represented symmetrically.

3. **Symmetry reduction without lost cases.** Translations by binary vectors and permutations of the \(d\) coordinate positions generate the full cube isometry group. Both the bootstrap predicate and both exchange rules are invariant under these operations. A generator-orbit breadth-first computation partitions the optimum family into two orbits for \(d=4\) and 18 for \(d=5\); every enumerated state is assigned exactly once. Consequently the eccentricity of any state equals that of its orbit representative. A standard breadth-first search of the full constructed exchange graph from each representative determines all graph distances and exact eccentricities. Those calculations give connectivity, all quoted radii and diameters, and the complete \(T_5\) eccentricity distribution. No all-pairs metric is inferred from a partial sampling: every isometry orbit is covered.

4. **Independent enumeration.** A separately written implementation begins with each seed as a zero-dimensional coordinate subcube, repeatedly merges two internally spanned subcubes whose graph distance is at most two, and accepts exactly when the full cube is obtained. This projection-merger characterization is a standard two-neighbour cube closure principle (see Kang–Missethan–Schmid, Lemmas 2.6–2.10). The implementation enumerates states without using the synchronous update method, constructs adjacency directly and uses all coordinate permutations and translations rather than generator-based orbit search. It independently reproduces every count and eccentricity. For each dimension, the sorted lists of accepted seeds have identical SHA-256 digests between both implementations. Thus even a discrepancy that conserved the total seed count would be detected.

A concrete \(T_5\) path of length 11 is the successive sequence
\[
\begin{aligned}
&\{0,1,6,26\},\{0,1,6,24\},\{0,1,6,25\},\{0,1,6,29\},\\
&\{0,1,7,29\},\{0,1,15,29\},\{0,1,11,29\},\{0,3,11,29\},\\
&\{0,11,19,29\},\{4,11,19,29\},\{11,12,19,29\},\{11,19,28,29\}.
\end{aligned}
\]
Every neighbouring pair differs by sliding one seed along a cube edge. The complete breadth-first distance layers from the first state place the final state at distance 11, proving this path is shortest. Together with the orbit-by-orbit upper-bound search, this certifies the diameter.

## Verification

Both standalone reproducibility programs and their exact recorded console outputs are included. From the root of the extracted package run `python3 code/verify_direct.py` and `python3 code/verify_boxes.py`; the former has only the bundled `code/seed_direct.py` dependency, and neither requires third-party packages. Compare their output with `evidence/direct-output.txt` and `evidence/boxes-output.txt`. The shared SHA-256 of the lexicographic seed encoding (each set as comma-separated integers followed by a newline) is `98038473d31775e85da42f0cba78cc0d8515c900edcc89fdd7fffffe07f6b99c` for \(Q_4\) and `359127dfbab8d1227813648543501eece0f7a72a546b826ff26e81f65ea2ce10` for \(Q_5\). The output prints all orbit representatives and their exact distance-layer sizes. These are finite exhaustive calculations only.

## Relationship to prior work

The 2009 paper of Balogh, Bollobás and Morris analyzes two-neighbour bootstrap percolation on high-dimensional grids and random critical thresholds. Morrison and Noel (first public preprint 2015) study minimum cardinalities, weak saturation and asymptotic extremal bounds in hypercubes. Kang, Missethan and Schmid (2024) develop the framework of internally spanning coordinate projections and sequentially spanning seed sets and analyze random threshold behaviour of Hamming graphs. These works supply the natural process and useful closure language, but their central assertions concern probabilistic thresholds or minimum seed sizes, not adjacency between *all* optimum seeds under single-seed jumps and slides, exact graph distances, or the center/periphery transition computed here. An existing count of seed sets alone cannot imply the edge sets or metric of these exchange graphs. Earlier two-neighbour bootstrap literature is acknowledged; no new minimum-cardinality formula in general dimension is claimed.

## Limitations

Only the two finite dimensions \(d=4,5\) and the strict threshold-two rule are covered. The result does not establish connectivity, radii or diameters in any higher dimension, and does not concern random infection, non-minimum seeds or moves through nonpercolating intermediate states. A computationally exhaustive finite proof remains dependent on the correctness of the fully specified enumerators and standard integer/Python semantics. Unindexed or inaccessible work containing equivalent finite reconfiguration results cannot be excluded absolutely.

## References

- J. Balogh, B. Bollobás and R. Morris, *Bootstrap percolation in high dimensions*, arXiv:0907.3097 (first submitted 17 July 2009), https://arxiv.org/abs/0907.3097 .
- N. Morrison and J. A. Noel, *Extremal Bounds for Bootstrap Percolation in the Hypercube*, arXiv:1506.04686 (first submitted 15 June 2015), https://arxiv.org/abs/1506.04686 .
- M. Kang, M. Missethan and D. Schmid, *Bootstrap percolation on the high-dimensional Hamming graph*, arXiv:2406.13341 (first submitted 19 June 2024), https://arxiv.org/abs/2406.13341 .
- J. Balogh and B. Bollobás, *Bootstrap percolation on the hypercube*, Probability Theory and Related Fields 134 (2006), 624–648, https://doi.org/10.1007/s00440-005-0451-6 . This earlier background source was available bibliographically and in abstract; its full text was not independently inspected here.
