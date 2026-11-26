# Independent mathematical audit

## correctness

PASS

For each unselected edge uv the odd line-graph adjacency is the parity of deg_A(u)+deg_A(v). Thus the support size is |δ(S)|+|A\δ(S)| for the even-cardinality set S of odd selected degrees. A nonempty proper cut of size at most four has a forest shore by cyclic connectivity, and a cubic forest shore of s vertices and c components has s+2c crossing edges. The only eligible proper cut is consequently an even 4-cut isolating one adjacent pair. Its four crossing ends on the far shore are distinct by girth. If S is the far shore, at most four crossing edges and one noncrossing edge make at most six of its vertices odd, whereas it has at least eight (the radius-two cubic Moore bound gives 1+3+6 vertices). If S is the pair, either its joined edge is selected alone or two crossing edges must be closed by an outside edge, forming a prohibited 4-cycle with the pair's edge. If S is empty, selected edges form disjoint cycles and weight at most five forces one pentagon. If S is all vertices, weight at least |V(H)|/2 forces order ten and all selected degrees one for equality. All three surviving types have weight five. Independent XOR support enumeration reproduced 15+12+6, 21, and 30+12 in the examples (python3 /workspace/branches/reproduce.py 2); an independent cut census confirmed the examples' relevant small cuts. The local-complementation identity gives degree four, and X-parts distinguish all stabilizer products even if some support sets coincide. For the fullerene application, Euler's formula gives twelve pentagonal faces and order at least twenty. Using Došlić's standard cyclic 5-edge-connectivity theorem, a shortest cycle of length ≤4 would be chordless, and its cut to the complement would have size ≤4 with both shores cyclic (a complement forest would require more than four edges). A nonfacial 5-cycle would have both interior and exterior nonempty with positive attachment numbers summing to five; each interior/exterior shore would have to be a forest, since the other shore includes the cycle. The forest cut formula would require at least three attachments on each side, impossible. Thus the fullerenes satisfy the needed girth and all five-cycles are facial; no embedded code-distance claim is needed.

## originality

PASS

The supported distinct claim is the complete deterministic extremizer classification for this cubic line-graph family, hence its exact graph-state stabilizer multiplicity; not the optimization parameter, local-complementation correspondence, or fullerene cut theorem. The strongest inspected alternate formulations concern different predicates or do not classify the equality witnesses. This is a bounded best-of-knowledge assessment, not proof of historical priority.

## value

PASS

The graph-state interpretation motivates the multiplicity of minimum-weight elements, not merely their weight. A uniform classification pinpoints three distinct mechanisms and exactly where the perfect-matching mechanism can occur, and for all fullerenes explains the constant twelve additional elements beyond generators. This is structural equality information not supplied by a numerical check of three examples or by the ordinary degree bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
