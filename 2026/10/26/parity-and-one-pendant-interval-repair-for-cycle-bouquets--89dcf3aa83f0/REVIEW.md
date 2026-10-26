# Scientific review: interval repair of cycle bouquets

## Correctness — PASS

The Eulerian parity obstruction is proved by incidence counting and is stated as prior work. For sufficiency, successive hub colors are paired at distance one for even petals and distance two for odd petals; the local alternating walks give valid edge colorings of every possible petal length, including the boundary cases of three and four. The construction covers all hub colors exactly once and is a proper interval coloring with palette width equal to the hub degree. In the odd case one hub pendant fills the unique missing color. Necessity of adding at least one edge comes from odd edge-count parity, and the two local deficiencies then follow from their published inequalities. The executable construction was checked on 5,800 finite inputs; those checks are not the infinite proof.

## Originality — PASS, with residual bibliographic risk

The 2013 Eulerian odd-edge obstruction covers only necessity. The 2026 local-deficiency paper describes the relevant invariants and general bounds, while a cited outerplanar weak-local bound already implies a weak-local upper estimate: that part is not presented as independently new. A 2021 cactus-spectrum algorithm and a 2025 cactus-coloring doctoral abstract are broader methodological antecedents, but the accessible comparisons did not produce a closed-form even-odd petal criterion together with a sharp one-hub-edge ordinary deficiency repair. Search terms included the rose, bouquet, flower, windmill and friendship aliases; no direct covering claim was found in the available published-finding corpus results or targeted literature. The 2021/2025 full texts were not both inspected in full, and priority remains uncertain.

## Value — PASS

This is a complete natural family classification across arbitrary cycle lengths and arbitrary numbers of petals. It couples a sharp obstruction with a uniform optimal repair localized at a distinguished vertex; the existing generic parity necessity, algorithmic decidability and weak-local estimates do not by themselves supply that repair. The constructive spectrum is optimal at the maximum-degree hub, independent of the individual lengths. The result is limited to one-vertex cycle bouquets; it is not asserted to solve cactus interval-colorability generally.

Self-review: passed. Independent audit: not yet performed.
