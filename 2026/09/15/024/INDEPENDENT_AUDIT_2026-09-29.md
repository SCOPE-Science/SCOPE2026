# Independent Audit — 2026/09/15/024

Audit date: 2026-09-29 (UTC)
Audited tree: `5d9b95b4d702b99f3e8c4da06df7aa3f270b32d7`

## Disposition

**PASSED** — All three axes pass. The record can remain at the source path with the independent-audit evidence attached.

## Correctness

**PASS**. Independent finite checks reproduce the graph parameters: 27 vertices, degree 12, 162 edges, spectrum {12^1,0^6,(-3)^12,3^8}, and clique and independence numbers both 4. The stored 7-coloring is proper, while alpha=4 gives chi≥ceil(27/4)=7, so chi=7 exactly without relying on the reported 6-color ILP. The explicit six-dimensional rank-1 PVM construction is algebraically valid, giving chi_q≤6, and the quantum Hoffman bound from lambda_min=-3 gives chi_q≥5. The covariant no-go is also sound: summing the five character rows forces all 20 ordered character differences to attain shell kernel value -3, equivalently a 5-clique in the weight-2 graph, impossible because omega=4.

## Originality

**PASS**. Cao–Feng–Huang–Yang–Zhang already imply the general threshold interval 5≤chi_q(H(3,3,2))≤6, so that interval is not credited as new. The record adds independently certified object-specific information not supplied by that theorem: chi=7, omega=alpha=4, a concrete strict quantum/classical separation on the 27-vertex graph, and a proof excluding every translation-covariant rank-1 dimension-5 coloring. The no-go is not a parameter substitution into the general Hamming bound; it uses the character-shell identity together with the exact clique obstruction.

## Scientific value

**PASS**. The exact small-graph package gives a concrete 27-vertex instance with certified quantum advantage and meaningfully narrows the unresolved 5-versus-6 endpoint by eliminating the most natural translation-covariant rank-1 ansatz. Although the exact quantum chromatic number remains open, the combination of exact classical structure and a symmetry-class no-go is a useful finite benchmark for further SDP or representation-theoretic attacks.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://arxiv.org/abs/2510.14209 — Cao et al.: at d=(q-1)n/q, proves (q-1)(n-1)+1≤chi_Q≤(q-1)n; for q=n=3 this is exactly 5≤chi_Q≤6, and leaves the threshold gap open.
- https://doi.org/10.37236/14936 — Luo–Ning–Zhang (2026): exact results for binary distance-2 Hamming graphs; a nearby but different object.
- https://arxiv.org/abs/2412.09904 — Earlier Hamming-scheme quantum-chromatic work; does not provide the ternary H(3,3,2) exact classical/no-go package.

Independent checks:
- Enumerated all 27 ternary triples and 162 distance-2 edges; exhaustively found no 5-clique and no 5-independent set, with 4-witnesses for both.
- Verified the stored 7-coloring edge-by-edge; alpha=4 independently proves that six classical colors are impossible.
- Recomputed Krawtchouk eigenvalues 12,0,-3,3 with multiplicities 1,6,12,8 and the Hoffman lower bound 5.
- Checked the explicit six-vector basis construction for every vertex and zero same-color overlap on every edge.
- Checked the covariant character-sum identity and the reduction of a 5-character seed to a forbidden 5-clique.

Limitations:
- The exact value chi_q is still one of {5,6}; the audit does not promote the numerical optimization evidence to a proof.
- The no-go concerns translation-covariant rank-1 dimension-5 strategies only, exactly as stated.
- No inaccessible source is represented as read.
