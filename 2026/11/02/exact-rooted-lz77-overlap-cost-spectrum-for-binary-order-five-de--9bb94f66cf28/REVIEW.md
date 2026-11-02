# Scientific review

## Correctness — PASS

The switch-map proof gives an exhaustive one-to-one characterization of all cyclic order-five binary de Bruijn words by \(16\) choices, accepted precisely on a single \(32\)-state orbit. The two explicitly defined greedy phrase lengths are computed by both exhaustive previous-source comparisons and a separate suffix-LCP dynamic program, with exact equality of boundaries on each of \(65{,}536\) linear traversals. A second Euler-tour construction reproduces all \(2{,}048\) normalized cycles. The exact \(24\)-cell distribution, seven gain frequencies and eight cycle-range classes match independent arithmetic totals and all embedded checker assertions. The proof does not extend the result beyond order five.

## Originality — PASS, qualified

Relevant algorithms and the LZ/novLZ definitions were compared against Goto–Bannai (arXiv:1211.3642), Kärkkäinen–Kempa–Puglisi (arXiv:1212.2952), and Kosolobov–Shur (arXiv:1708.03558). The latter's all-string inequality \(z\le\widehat z\) already implies nonnegative gap, but its general bounds give none of the new exact frequencies for a fixed de Bruijn order and root. Andreasen's 2001 discussion of concatenated de Bruijn sequences establishes a relationship to compression, not the complete isolated-cycle joint table. Comparison with accessible related research records and earlier rooted LZ78 results found no implication of this LZ77 census. Residual risk: an unindexed exact table or another source with an implicit complete enumeration might predate the result. Absence from a semantic database is not proof of priority.

## Value — PASS

The largest uniformly manageable de Bruijn family at order five gives a natural controlled compression benchmark: all inputs have identical cyclic five-factor coverage, while rooted greedy parse counts and the penalty for disallowing overlapping references vary substantially. A complete *joint* distribution distinguishes which overlap-cost outcomes coexist and supplies exact worst and per-cycle guaranteed gains. It cannot be read off an LZ78 census, general parsability bounds, or individual demonstrations; the result makes a finite but structurally motivated comparative classification available with self-contained verification.

## Scientific limitations

Results concern exactly one non-wrapping linear traversal of binary order-five cycles, pair-reference LZ77 and novLZ, and phrase counts only. They neither determine bit-level compressed lengths nor classify arbitrary de Bruijn orders. Independently verified historical priority and independent mathematical audit are outstanding.

Self-review: passed. Independent audit: not yet performed.
