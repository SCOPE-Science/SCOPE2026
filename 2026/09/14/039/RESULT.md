# A 22-edge P6-free linear 3-graph on 13 vertices: density 22/13 refutes the disjoint 12-block picture for ex_3^lin(n,P_6^3)

## Context

Let P_k^3 denote the 3-uniform loose (linear) path with k edges: consecutive edges meet in exactly one vertex, link vertices are distinct, and non-consecutive edges are disjoint, so |V(P_k^3)| = 2k+1. Let ex_3^lin(n,P_6^3) be the maximum number of edges in an n-vertex linear 3-uniform hypergraph with no (not necessarily induced) copy of P_6^3. The target was the exact value and extremal characterization for all large n. The working conjecture was that disjoint copies of the 12-vertex 20-edge punctured Steiner triple system STS(13) (density 5/3) are extremal. This record reports the certified emergent finding that falsifies that picture.

## Definitions

- Linear: every pair of vertices lies in at most one edge.
- P_6^3: six distinct triples E_1,...,E_6 with |E_i cap E_{i+1}| = 1, all links distinct, E_i cap E_j = emptyset for |i-j| > 1, spanning 13 distinct vertices.
- MPTS(m): maximum partial triple system; MPTS(12) has 20 edges, density 5/3.

## Result

Theorem. (a) There exists a linear 3-uniform hypergraph B on vertex set {0,...,12} with 22 edges and no P_6^3:
(0,1,12),(0,2,7),(0,3,6),(0,4,11),(0,5,8),(1,2,11),(1,3,8),(1,4,7),(1,5,6),(2,3,12),(2,6,9),(2,8,10),(3,7,9),(3,10,11),(4,5,12),(4,6,10),(4,8,9),(5,7,10),(5,9,11),(6,11,12),(7,8,12),(9,10,12).
Degree sequence: twelve vertices of degree 5, one of degree 6. Hence ex_3^lin(13,P_6^3)/13 >= 22/13 = 1.6923... > 5/3, and by disjoint copies the asymptotic density is at least 22/13. No extremal family of disjoint 12-vertex 20-edge blocks can be asymptotically optimal. (b) Let A be the punctured cyclic STS(13) (12 vertices, 20 edges) and A+A' two disjoint copies (24 vertices, 40 edges, P_6-free). Among all cross triples, exactly 144 are linearly addable, and every one creates a P_6 (144/144). (c) Exact small values: ex_3^lin(9,P_6^3)=12, ex_3^lin(10,P_6^3)=13, ex_3^lin(11,P_6^3)=17, ex_3^lin(12,P_6^3)=20.

## Proof / evidence

Linearity: 22 edges cover 22*3 = 66 pairs, all distinct (of C(13,2)=78). P_6-freeness: two independent exhaustive detectors agree — DFS with pruning finds 0 loose 6-paths; independent enumeration over all P(22,6)=53,721,360 ordered 6-tuples (equivalently all C(22,6) 6-sets spanning 13 vertices) finds none; auditor re-ran both. Density corollary is arithmetic plus disjoint-union construction. Rigidity: enumerated all C(24,3)-2*C(12,3)=1584 cross triples, kept 144 using no covered pair, tested each with the P_6 detector; all create a P_6 (auditor re-executed: 144/144). Small values: witnesses stored in ilp_n{9,10,11,12}.json are linear (auditor re-verified); upper bounds: n=9 (12) and n=10 (13) follow from Schoenheim bound floor(n/3*floor((n-1)/2)); n=12 (20) equals the packing bound; n=11: 18 edges would force degree sequence ten 5s plus one 4, leaving 2 uncovered pairs at one vertex against a global deficit of 1, impossible, so 17 is optimal. For n<=12 no P_6 cut is needed since P_6 needs 13 vertices.

## Limitations

Only existence of the 22-edge example is proved; optimality ex(13)=22 is conjectured, not proved. No asymptotic upper bound matching 22/13 is proved; the true limiting density is open above 22/13. The rigidity lemma covers only the tested pair of punctured cyclic STS(13) blocks. No infinite 22/13-density family beyond disjoint copies of B is constructed.

## Reproducibility

Run `python3 output/artifacts/final_verify.py` from the record root (deterministic, ~12 s): checks linearity, DFS P_6 search, brute-force P(22,6) check, degree sequence, density comparison, and the 144/144 rigidity enumeration; prints ALL FINAL CHECKS PASSED. Data: output/artifacts/best13_22.json; witnesses ilp_n{9,10,11,12}.json.

## References

Z. Furedi, T. Jiang, R. Seiver, Exact solution of the hypergraph Turan problem for k-uniform linear paths, Combinatorica 34 (2014) (arXiv:1108.1247) — k>=4 general-host theorem, k=3 linear case conjectured. N. Bushaw, N. Kettle, Turan numbers for forests of paths in hypergraphs, SIAM J. Discrete Math. 28 (2014) — general-host forest extension. C. Tang, H. Wu, J. Zhang, The linear Turan number of the 3-graph P5, arXiv:2601.19068 (2026) — linear-host P5 bound 15n/11, no P6 content.
