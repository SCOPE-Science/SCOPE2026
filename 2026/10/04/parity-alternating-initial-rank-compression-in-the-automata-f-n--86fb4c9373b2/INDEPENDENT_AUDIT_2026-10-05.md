# Independent mathematical audit

## correctness

PASS

Only a can lower rank, by at most one, and a shortest word to deficiency s ends at its s-th effective a. Immediately after an effective a, state n is missing, so separators between consecutive effective a's cannot have length zero; length two is impossible, and a length-one separator must be b. After an aba rank drop, both 1 and n are holes, so another one-letter separator would move a hole to 2 and make the next a ineffective. Hence adjacent separator lengths sum to at least four. Pairing separators gives 3s-2 for odd s and 3s-3 for even s. The proposed alternating ba/b^3a witnesses have the explicitly stated hole sets; the half-range hypothesis prevents wraparound and keeps every a effective. Fresh independent power-automaton BFS reproduced the formula for every allowed s at n=5,7,9,11,13, while the frozen verifier extends exact BFS through n=17 and witness replay through n=301. The symbolic separator/hole proof establishes all odd n.

## originality

PASS

Ananichev--Gusev--Volkov define the exact automata F_n and prove only the rank-one endpoint: for odd n>3 the reset threshold is n^2-3n+3. The relevant full PDF page was materially read and visually inspected; it gives the letter actions and Theorem 7 but no prescribed-intermediate-rank profile. Resultary searches for F_n intermediate rank/deficiency compression returned no covering theorem. The submitted parity-alternating initial half-profile therefore survives as a distinct exact classification.

## value

PASS

Intermediate rank compression is a natural refinement of reset complexity for a canonical slow-synchronization family. The exact parity-alternating law over an unbounded half-rank range identifies the local obstruction long before the known quadratic reset endpoint and gives explicit optimal words and hole geometry, making it a substantive structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
