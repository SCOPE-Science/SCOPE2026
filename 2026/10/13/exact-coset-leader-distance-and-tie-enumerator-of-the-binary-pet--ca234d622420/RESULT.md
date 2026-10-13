# Exact coset-leader distance and tie enumerator of the binary Petersen cycle code

## Finding
Let \(\Gamma\) be the Petersen graph with vertices the ten two-element subsets of \(\{0,1,2,3,4\}\), adjacent when disjoint. Fix the binary vertex–edge incidence matrix \(H\), and let \(C=\ker(H)\subseteq\mathbb F_2^{15}\). For each even-weight vertex syndrome \(t\in\mathbb F_2^{10}\), let \(d(t)\) be the minimum Hamming weight of an edge vector \(e\) satisfying \(He=t\), and let \(m(t)\) be the number of such minimum-weight edge vectors.

The **joint coset-leader distance and multiplicity enumerator** is exactly
\[
\begin{aligned}
F_C(u,v)&=\sum_{t:\,\sum t_i=0}u^{d(t)}v^{m(t)}\\
&=v+15uv+105u^2v\\
&\quad+u^3(195v+70v^2)\\
&\quad+u^4(45v^2+65v^3+15v^4)+u^5v^6.
\end{aligned}
\]
Thus the distance distribution over the \(512\) cosets is \((1,15,105,265,125,1)\), and the covering radius is \(5\). Exactly one coset has distance \(5\); it is the syndrome consisting of all ten vertices, and has precisely six nearest error supports, which are exactly the six perfect matchings of the Petersen graph. The corresponding numbers of ambient received words at each distance from \(C\) are \((64,960,6720,16960,8000,64)\).

## Assumptions and scope
All vector spaces and incidence arithmetic are over \(\mathbb F_2\). Vertex coordinates are indexed by the ten unordered pairs of \(\{0,1,2,3,4\}\) in lexicographic order. The fifteen edges are indexed by the lexicographically ordered pairs of disjoint vertices. An integer syndrome mask encodes membership of vertex index \(i\) by bit \(2^i\). A minimum error support is an edge subset, not an ordered recovery sequence. This is the single specified length-\(15\) code; no analogous formula for arbitrary graphs is claimed.

The graph is connected, with ten vertices and fifteen edges; hence the incidence matrix has rank \(9\), its kernel has dimension \(6\), and the code has parameters \([15,6,5]_2\), because the graph's girth is \(5\). Each of the \(512\) even vertex subsets is a realizable syndrome, since the binary boundary map of a connected graph surjects onto the even subspace.

## Proof
**Syndrome–coset identification.** Each edge vector \(e\) has vertex syndrome \(He\), the set of vertices of odd degree in its support. Two received words have the same syndrome exactly when they differ by a word of \(C\). Consequently, \(d(t)\) is the weight of a coset leader and \(m(t)\) counts the nearest codewords to any received word in the associated coset. In graph terms the leaders are the minimum-cardinality \(t\)-joins.

**Finite exact recurrence and independent check.** For each of the \(2^{15}=32768\) edge masks, calculate its syndrome via the recurrence \(s(0)=0\) and \(s(e)=s(e\setminus\{j\})\oplus h_j\), where \(j\) is the least-indexed chosen edge and \(h_j\) is its two-endpoint syndrome. Update the smallest observed weight and the number attaining it for each vertex mask. This is a complete enumeration, not sampling. An independent breadth-first search on the \(512\)-vertex even-syndrome Cayley graph, using the fifteen edge-syndrome vectors as generators, obtains minimum distances and counts \(P(t)\) of shortest ordered paths. No shortest path repeats a generator, because two copies cancel in characteristic two and their removal would shorten the walk. Hence each distinct minimum edge support yields precisely \(d(t)!\) shortest ordered paths; the independent count checks \(P(t)=d(t)!m(t)\) for all \(512\) syndromes.

**Orbit certificate.** The \(120\) permutations of the five underlying symbols preserve adjacency in \(\Gamma\), and therefore preserve each pair \((d(t),m(t))\). They partition the \(512\) even vertex masks into the following \(18\) orbits. For each row the displayed representative is a decimal vertex-bit mask; each orbit size is obtained by applying all \(120\) permutations and discarding duplicates.

| Syndrome mask | Orbit size | Minimum error weight | Number of leaders |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 0 | 1 |
| 20 | 15 | 1 | 1 |
| 3 | 30 | 2 | 1 |
| 15 | 5 | 4 | 3 |
| 184 | 10 | 3 | 1 |
| 54 | 15 | 2 | 1 |
| 58 | 60 | 2 | 1 |
| 23 | 60 | 3 | 1 |
| 29 | 60 | 3 | 2 |
| 183 | 5 | 3 | 1 |
| 126 | 10 | 3 | 2 |
| 207 | 15 | 4 | 4 |
| 187 | 60 | 3 | 1 |
| 221 | 60 | 3 | 1 |
| 63 | 60 | 4 | 3 |
| 495 | 15 | 4 | 2 |
| 255 | 30 | 4 | 2 |
| 1023 | 1 | 5 | 6 |

The orbit sizes add to \(512\). Summing the orbit sizes grouped by the final two columns gives exactly the polynomial in the finding. In particular, only the mask \(1023\) has distance \(5\). A five-edge subset has boundary all ten vertices exactly when all vertices have degree one; thus the six leaders for this syndrome are the six perfect matchings.

Every coset has \(|C|=64\) ambient words and all its members have the same minimum distance to \(C\). Multiplying the coset distance counts by \(64\) gives the ambient distance spectrum. This proves every asserted equality.

## Verification
Run the dependency-free Python program `python3 verify.py`. It reconstructs \(\Gamma\), checks \(|V|=10\) and \(|E|=15\), enumerates all \(32768\) edge subsets, checks the classical \(64\)-word code weight distribution, runs an independent shortest-path algorithm on the syndrome Cayley graph, verifies all \(120\) vertex permutations and all \(18\) orbit representatives, and compares the full bivariate frequency table against the statement. The success marker is `VERIFY_OK`. The code has no numerical tolerances, external data, or probabilistic stages.

## Relationship to prior work
Del Valle and Praeger, *Constructing linear codes from digraphs and groups*, first posted July 30, 2026, Section 6.2, give a highly symmetric Petersen graph code with parameters \([15,6,5]_2\), describing its graph-code construction rather than its nearest-coset multiplicity profile. The underlying cycle code is substantially older; the Error Correction Zoo documents its incidence-matrix description, and Brouwer's Petersen graph notes give the ordinary codeword weight distribution. The exact joint distance-and-tie coset enumerator is distinct from that ordinary weight distribution.

Solé and Zaslavsky (1993) relate covering radii of *graph cycle codes* to minimum \(T\)-joins and establish covering-radius results for several graph classes; this prior work must be credited for the general correspondence and cannot be excluded as prior art for the covering-radius number alone. The present finite finding is specifically the complete joint coset-leader multiplicity spectrum, its \(18\) symmetry orbits, and the equality-case counts, none of which is asserted to follow merely from a covering radius. The older full text was unavailable for line-by-line comparison, a residual originality risk.

## Limitations
This is an exhaustive, exact, finite combinatorial result for one ten-vertex graph, not a general theorem for other graph codes. A published unindexed coset census or a theorem implying all nearest-leader multiplicities would subsume the claimed originality; the 1993 primary full text could not be inspected beyond its bibliographic abstract and searchable preview. The mathematical census itself is completely reproducible from the supplied finite algorithm.

## References
1. Coen del Valle and Cheryl E. Praeger, *Constructing linear codes from digraphs and groups*, arXiv:2607.28016v1 (first posted 2026-07-30), especially Section 6.2. https://arxiv.org/pdf/2607.28016
2. Patrick Solé and Thomas Zaslavsky, *The covering radius of the cycle code of a graph*, Discrete Applied Mathematics 45 (1993), 63–70, doi:10.1016/0166-218X(93)90140-J.
3. *Petersen cycle code*, Error Correction Zoo, https://errorcorrectionzoo.org/c/petersen.
4. A. E. Brouwer, *The Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html.
