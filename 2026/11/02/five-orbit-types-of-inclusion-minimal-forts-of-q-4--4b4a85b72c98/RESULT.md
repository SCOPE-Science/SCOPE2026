# Five orbit types of inclusion-minimal forts of \(Q_4\)

## Finding
Let \(Q_4\) denote the graph of all four-bit binary words, adjacent when they differ in one bit. A **fort** is a nonempty vertex subset \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is **inclusion-minimal** if no nonempty proper subset is itself a fort. There are exactly \(348\) inclusion-minimal forts, whose cardinality enumerator is
\[
28z^4+32z^6+288z^8.
\]
Under the full automorphism group of \(Q_4\), the inclusion-minimal forts form exactly **five** orbits, with representative masks and sizes:

| Representative | Selected vertices | Cardinality | Orbit size | Induced subgraph |
|---|---|---:|---:|---|
| `0x0660` | 0101, 0110, 1001, 1010 | 4 | 12 | four isolated vertices, distance profile \((2,2,2,2,4,4)\) |
| `0x0116` | 0001, 0010, 0100, 1000 | 4 | 16 | four isolated vertices, every pair at distance two |
| `0x033c` | 0010, 0011, 0100, 0101, 1000, 1001 | 6 | 32 | three disjoint edges |
| `0x1be4` | 0010, 0101, 0110, 0111, 1000, 1001, 1011, 1100 | 8 | 96 | two disjoint four-vertex paths |
| `0x19ea` | 0001, 0011, 0101, 0110, 0111, 1000, 1011, 1100 | 8 | 192 | an edge, and a four-cycle with two leaves at adjacent corners |

The vertex word in the table represents an integer \(v\) in the range \(0\le v<16\); bit \(v\) of a mask equals one exactly when vertex \(v\) is selected. The table provides canonical numeric representatives under this convention. The counts \(12+16+32+96+192=348\) give a complete orbit partition.

## Assumptions and scope
The claim concerns the single, explicitly labelled graph \(Q_4\), not arbitrary hypercubes. Graph automorphisms consist of independently complementing each coordinate followed by permuting the four coordinates. Sets are counted with labels (as subsets of the sixteen specified vertices). Inclusion-minimal is logically distinct from *minimum cardinality*: the former may have cardinality larger than four.

## Proof
**Exact fort predicate.** For each \(v\in\{0,\ldots,15\}\), let \(B_v\) be the sixteen-bit mask with bits at \(v\mathbin{\mathrm{xor}}2^j\), for \(0\le j<4\). For any subset mask \(s\), define \(f(s)=1\) precisely when \(s\ne0\) and for every \(v\notin s\), \(\operatorname{popcount}(B_v\mathbin{\&}s)\ne1\). This is exactly the graph-theoretic fort definition.

**Nonmonotone-safe minimality.** Let \(h(0)=0\) and, for every nonzero mask \(s\), define
\[
h(s)=f(s)\lor\bigvee_{v\in s}h(s\setminus\{v\}).
\]
Induction on cardinality establishes that \(h(s)=1\) if and only if \(s\) contains a nonempty fort. Therefore \(s\) is inclusion-minimal if and only if \(f(s)=1\) and all \(h(s\setminus\{v\})=0\). This criterion is valid even though the class of forts is not closed under taking subsets: merely checking whether single-vertex deletions are forts would not suffice. Every child mask is strictly smaller than its parent as an integer, so evaluating masks in ascending integer order computes the recurrence exactly.

**Exhaustive cardinality and orbit certificate.** Apply the recurrence to each mask in the complete range \(0\le s<2^{16}\). It returns exactly \(348\) minimal forts, with counts \(28,32,288\) at cardinalities \(4,6,8\) and no others. The list of all graph automorphisms is generated as follows: choose one of \(4!\) coordinate permutations and one of \(2^4\) translation words, and apply \(v\mapsto\pi(v)\mathbin{\mathrm{xor}}t\). These are \(384\) distinct automorphisms, and they are all automorphisms because an automorphism is fixed uniquely by the image of a vertex and the images of its four neighbors. Acting on each of the five displayed masks yields respective orbit sizes \(12,16,32,96,192\); all five orbits are pairwise disjoint and consist entirely of minimal forts. Their union has \(348\) members, hence exhausts the enumeration. The induced subgraphs and the pair-distance patterns distinguish the five types. All finite arithmetic, enumeration bounds, recurrence tests and group actions are reproducible with the self-contained `verify.py`.

## Verification
Running `python3 verify.py` on a standard Python version with integer `bit_count()` checks the fort predicate by two independently coded methods, then compares the dynamic-programming minimality test against exhaustive search over **every proper nonempty submask** of every fort. It enumerates all sixteen-vertex subsets, validates the complete automorphism list and its action, checks canonical representatives, computes all five orbit sizes and verifies that their disjoint union equals the complete minimal-fort set. The exact successful output is

`VERIFY_OK Q4_minimal_forts=348 sizes=4:28,6:32,8:288 aut_group=384 orbits=12,16,32,96,192 distinct_predicates_and_minimality_algorithms=agree`

The finite exhaustion is the proof of the finite claim; no finite data are extrapolated to an unbounded family. The full checker is supplied rather than only a log or output count.

## Relationship to prior work
Brimkov, Cameron and Grubbs, *On the forts and related parameters of the hypercube graph* (arXiv:2507.10826v1, publicly submitted 2025-07-14), already characterize the **minimum-cardinality** forts, including two orbit types in dimension four (their Proposition 3.9). Their Section 5 gives constructions of at least sixty **inclusion-minimal** forts in the four-cube; their conclusion explicitly reports an already-computed **total of 348** and identifies the full characterization as missing. Accordingly, neither \(348\) nor the two orbits of cardinality-four forts is claimed as new here. The new contribution is the complete five-orbit structural characterization of every inclusion-minimal fort (including the size-six and size-eight types), and the resulting entire cardinality profile. Earlier Becker–Cameron–Hanely–Ong work treats general enumeration of minimal forts but does not provide this labelled four-cube orbit partition in its inspected text.

## Limitations
This is a finite, exact classification on \(Q_4\) only. It gives no formula for dimensions larger than four, no classification of minimal zero forcing sets, and no new total count beyond the previously reported \(348\). Although the relevant accessible source was examined, exhaustive historical-priority verification, especially under alternate formulations as minimal failed-zero-forcing obstructions, has not been independently completed. Independent mathematical assessment has not been performed.

## References
1. B. Brimkov, T. R. Cameron, and O. Grubbs, *On the forts and related parameters of the hypercube graph*, arXiv:2507.10826v1 (2025-07-14), https://arxiv.org/html/2507.10826v1 ; specifically Proposition 3.9, Section 5, Conclusion.
2. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (2024), https://arxiv.org/abs/2404.05963 .
