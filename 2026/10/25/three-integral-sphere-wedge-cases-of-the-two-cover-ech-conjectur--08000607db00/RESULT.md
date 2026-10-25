# Three integral sphere-wedge cases of the two-cover Čech conjecture

## Finding
Let \(\mathrm{Cov}_{m,2}\) be the simplicial complex of all finite edge sets of \(K_m\) admitting a vertex cover of cardinality at most two, with the edge set of \(K_m\) as its simplicial vertices. For exactly \(m\in\{8,9,10\}\), its integral homotopy types are
\[
\begin{aligned}
\mathrm{Cov}_{8,2}&\simeq\bigvee^{35}S^3\vee\bigvee^{70}S^4,\\
\mathrm{Cov}_{9,2}&\simeq\bigvee^{70}S^3\vee\bigvee^{126}S^4,\\
\mathrm{Cov}_{10,2}&\simeq\bigvee^{126}S^3\vee\bigvee^{210}S^4.
\end{aligned}
\]
In particular these three complexes are simply connected, all their integral reduced homology is free and occurs in degrees three and four, and their stated multiplicities equal \(\binom{m-1}{4}\) and \(\binom m4\), respectively. These are the first three orders beyond the computed range in the motivating article; no claim is made for larger orders.

## Assumptions and scope
The underlying graph is a complete simple undirected graph on the labeled set \([m]=\{1,\ldots,m\}\). A face is a nonempty set of its graph edges for which some pair \(\{i,j\}\) meets every selected edge. Consequently the maximal face associated with \(\{i,j\}\) contains precisely all graph edges incident to at least one of the two vertices. There are exactly \(\binom m2\) such (not necessarily distinct in small orders) generating facets, and a simplicial complex is their downward closure.

Equivalently, the vertices are weight-two Boolean vectors with the symmetric-difference distance. The inclusive Čech nerve formed by intrinsic radius-\(r/2\) closed balls with \(4\le r<8\) has exactly this face relation: a center at distance at most two from each selected weight-two vector is exactly a two-element vertex cover. This is the convention and comparison in Biswas, Section 1 and Section 5.

## Proof
Order the \(\binom m2\) simplicial vertices lexicographically as graph edges \((0,1),(0,2),\ldots\), using zero-based labels for the algorithms only. Encode a nonempty face as the bit mask of its edges. Generate **all** faces by taking the downward closure of every two-star generating facet. There is no sampling or truncation.

Construct a partial matching on the nonempty face poset by sweeping the graph-edge bits in ascending order. At bit \(b\), match each still-unmatched face \(L\) not containing \(b\) to the still-unmatched face \(L\cup\{b\}\), if the latter is a face. Remove both from later sweeps. Each pair is an incident face-poset pair of consecutive dimensions, and the matching is injective by removal.

Reverse exactly the matched covering arrows in the directed Hasse graph; leave all other covering arrows downward. The attached program `verify_acyclic.cpp` enumerates every covering arrow, constructs indegrees for these orientations, and runs a complete topological sort. For \(m=8,9,10\) respectively, it processes all \(202140\), \(1099623\), \(5673835\) nonempty faces, across respectively \(1372896\), \(8460504\), \(48937095\) Hasse incidences. Thus the discrete-Morse matching is acyclic in each case. Its unmatched cells, counted by simplicial dimension, are exactly \((c_0,c_3,c_4)=(1,35,70),(1,70,126),(1,126,210)\), with no other critical cells.

The program `verify_morse_boundary.py` independently regenerates the face sets and matching and evaluates the **signed integral** critical-four-cell to critical-three-cell Morse boundary. Each boundary coefficient is computed via the oriented simplicial boundary and recursive elimination along matched pairs, with every incidence sign given by its position in the ordered edge mask. There are, respectively, \(70\), \(126\), \(210\) complete critical-four-cell columns and every integer coefficient is exactly zero. These are entire integer matrices, not reductions modulo a prime.

Forman's discrete Morse theorem now gives a CW model with one zero-cell, the stated three- and four-cells, and nothing else. Its three-skeleton is the wedge of the stated three-spheres. The homotopy classes of maps \(S^3\to\bigvee S^3\) are fully determined by their degrees on the three-sphere summands: by the Hurewicz theorem, \(\pi_3(\bigvee S^3)\cong H_3(\bigvee S^3;\mathbb Z)\). The zero signed Morse boundary therefore makes every four-cell attaching map null-homotopic. Their attachments split off four-spheres, giving the claimed integral homotopy equivalences.

## Verification
The complete verification source consists of `verify_acyclic.cpp`, `verify_morse_boundary.py`, and `verification_output.txt`. To reproduce with a standard C++17 compiler and Python 3 standard library, execute `g++ -O3 -std=c++17 verify_acyclic.cpp -o verify_acyclic`; then for each \(m\in\{8,9,10\}\), run `./verify_acyclic m` and `python3 verify_morse_boundary.py m`, replacing the final argument by the actual integer. The output log records all six exact runs. The C++ checker independently regenerates the same complexes and checks every Hasse edge; the Python verifier evaluates all integral Morse coefficients. As a smaller control, the matching was also tested on the four previously tabulated orders \(m=4,5,6,7\) and its critical-cell vectors reproduce their known sphere multiplicities; these controls are not counted as new results.

## Relationship to prior work
Biswas (2026), *Čech complexes for finite sets*, Section 5, presents homotopy calculations through \(m=7\) for this two-subset Čech family and Conjecture 5.2 proposing a general decomposition that yields the sphere counts; it also proposes an analogous extension in Conjecture 5.3 for the three-subset family. The present finite result establishes the two-subset homotopy formula for the first three previously uncomputed orders by a different, complete discrete-Morse proof, without proving the conjectured general induction. Jonsson (2005) treats the bounded-covering-number graph complex and establishes general homology-rank relationships and connectivity, not these three integral homotopy decompositions. A recent rational fourth-homology representation calculation applies to all orders, but knowledge of a rational representation does not determine the integral homotopy types proved here.

## Limitations
This is a three-order finite theorem, not a theorem for arbitrary \(m\). An integer boundary matrix equal to zero proves the splitting only after the verified absence of critical cells in dimensions one and two; both ingredients are supplied here. Computational verification requires sufficient RAM to store approximately 5.7 million faces at \(m=10\). The matching construction and all coefficients are specified and rerunnable, but no independent human audit or uniqueness claim is made. The literature comparison is subject to incompletely accessible later sources.

## References
Biswas, Anamitro. *Čech complexes for finite sets*. arXiv:2609.32786v1, September 26, 2026. Section 1 and Section 5; especially Table 5.1 and Conjecture 5.2. https://arxiv.org/pdf/2609.32786v1

Jonsson, Jakob. *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*. SIAM Journal on Discrete Mathematics, DOI 10.1137/S0895480104443680 (2005). Its homological results are background, not asserted here as new.

Forman, Robin. *Morse theory for cell complexes*. Advances in Mathematics 134 (1998), 90–145. The acyclic-matching theorem yields the cell model used above.
