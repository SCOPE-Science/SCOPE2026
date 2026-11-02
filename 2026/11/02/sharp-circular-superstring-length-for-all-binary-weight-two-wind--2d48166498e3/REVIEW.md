# Scientific review

## Correctness — PASS
The proof uses the literal full-window de Bruijn graph, verifies that required edges are disjoint balanced rotation circuits, and constructs a connected Eulerian augmentation of exactly \(k-1\) edges. For the lower bound, subtracting one required edge per word leaves an integral circulation. The Fine–Wilf overlap step is valid because any two added circuits have total length at most \(k-2\), strictly less than the shared vertex factor length \(k-1\). Periodic circuits shorter than \(k-1\) meeting the adjacent-pair necklace cannot meet another required orbit. The connectedness contradiction proves the lower bound for all \(k\ge4\). Boundary \(k=3\) is treated separately. Independently checked literal Eulerian constructions up to \(k=19\) and exhaustive all-shorter-word tests up to \(k=6\).

## Originality — PASS, with residual risk
Ruskey–Sawada–Williams (2012) and Sawada–Williams (2021) construct shorthand cycles; they explicitly distinguish shorthand from full length-\(k\) weight-two windows, so their statements do not imply the claimed minimal length. Blanca–Godbole give an asymptotic subset-cover result. Nellore–Ward treat near-balanced factor frequencies rather than an exact specified-weight covering requirement. Related 2026 bounded-weight results do not explicitly assert this sharp fixed-weight full-window optimum in available material. Searches of published mathematical records and relevant previous findings found no equivalent claim. The possibility of a disguised older covering-cycle construction remains, particularly in work not available in complete text.

## Value — PASS
The quantity is a natural exact shortest circular superstring invariant for all words of one fixed composition, not an arbitrary finite or parameter-selected slice. The result gives an all-length sharp formula and an optimal constructive Eulerian route, resolving the extra cost imposed by disconnected weight-two necklaces. It distinguishes three often conflated concepts: exact full-window universal cycles, shorthand fixed-content cycles, and full-window covers allowing extra factors.

## Limitations
No uniqueness of optimal covers or results for other fixed weights are claimed. Finite computation is only corroborative. Independent assessment is not yet performed.

Self-review: passed. Independent audit: not yet performed.
