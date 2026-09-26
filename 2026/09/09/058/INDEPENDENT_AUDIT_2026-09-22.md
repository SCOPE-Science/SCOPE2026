# Independent audit — 2026/09/09/058

## Correctness — PASS for the certified core

For the raw partition, u0,v1,x0,y0,x1,y1 form one background component while v0 is isolated. Every one of the 32 states of the five w-incident edges leaves v0 outside that component, so f=-1 identically. For the symmetrized partition, the two blocks are {u0,v1,x0,y0,x1,y1} and {u1,v0}; the w edges touch only x/y and cannot join the second block, so both cross indicators are one and both same-layer indicators zero: g=-1. Independently, these are realizable in a series-parallel base graph: take the theta graph with three x–y paths x–y, x–w–y, and x–u–z–v–y. With w edges omitted, open u0x0, x0y0, post x, x1y1, y1v1 for the first block, and u1z1, post z, z0v0 for the second, closing all other background edges. This has positive probability for 0<p<1. The grid-screening counts 233/877 and 1107/4140 were not independently certified as exact counts of all negative polynomials; they are not needed for the -1 theorem.

## Originality — PASS, specific conditional no-go

The checked open work of Denart proves cactus and listed block cases, while Gladkov–Pak–Zimin disprove the unrestricted conjecture. Neither supplies this degree-2 conditioning identity for a series-parallel theta example in the material checked. The result is an elementary obstruction to one proposed proof technique, not a counterexample to the averaged series-parallel conjecture.

## Scientific value — PASS, modest

A positive-probability realizable -1 conditional partition rules out the universal pointwise induction and its layer-symmetrized form, steering a proof toward cancellations among boundary states. It leaves the sign of the unconditional probability difference entirely open.

## Sources

- Original RESULT.md and METADATA.json; independent partition and theta-graph state construction above.
- Denart, https://arxiv.org/abs/2506.09264 .
- Gladkov–Pak–Zimin, https://arxiv.org/abs/2410.02545 .
- Linusson, https://arxiv.org/abs/0811.0949 .
