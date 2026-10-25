## Correctness

PASS. The repeated-state lower bound forces a cycle length divisible by \(p\); transition-compatible bipartiteness forces it to be even. The explicit cycle of length \(\operatorname{lcm}(p,2)\) recognizes exactly \(L_{p,r}\), giving matching bounds. The unrestricted minimum \(p\), allowing a self-loop when \(p=1\), is proved separately.

## Originality

PASS, with bounded residual risk. The primary bipartite-cactus paper proves existence but explicitly leaves tight state-complexity bounds open. The inspected unary state-complexity literature does not impose this transition-compatible graph constraint. published-finding corpus searches found no direct match; they are not exhaustive uniqueness proofs.

## Value

PASS. The result gives an exact boundary case for the primary paper’s stated state-complexity direction and quantifies the structural penalty on the canonical family \(L_{p,r}\): factor two for odd \(p\), none for even \(p\).

## Closest literature and limitations

Grobler, Koziel, and Siebertz, “Every Regular Language Has a Bipartite Cactus Automaton” (2026), establishes the representation theorem and identifies state complexity as an open direction. Czerwiński et al. (2023) and Pighizzini–Shallit (2002) provide unary automata and periodicity context but do not cover the same graph-constrained minimum in the inspected sections. A related 2022 paper on undirected state graphs was not separately inspected; this remains a residual originality risk. The result is limited to one residue class over a unary alphabet.

Self-review: passed. Independent audit: not yet performed.
