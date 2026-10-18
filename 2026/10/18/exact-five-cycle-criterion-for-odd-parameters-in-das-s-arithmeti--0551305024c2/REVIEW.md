# Scientific review: exact five-cycles for odd parameters

## Correctness
**PASS.** For odd \(k\), every prime state other than \(2\) maps to an even composite, whereas every composite maps to a prime. Consequently every odd-length cycle contains \(2\). A five-cycle cannot have \(2\) followed immediately by a composite, because its final odd prime could not return to \(2\). The other possibility forces \(2\to k+2\to2(k+1)\to q\to k+q\to2\), with \(q=P^+(k+1)\). The necessary and sufficient conditions are precisely primality of \(k+2\), oddness of \(q\), and \(2\)-power status of \(k+q\). All five states are provably distinct, and uniqueness follows from the forced visit to \(2\). The alternative parameterization follows by divisibility of \(2^m+1\) and the largest-prime-factor condition. Exact finite calculations check the formulas but are not used as proofs of the infinite theorem.

## Originality
**PASS within inspected evidence.** The originating 2023 Das paper introduces the map and asks loop questions without the full odd-parameter five-cycle classification. The closest earlier mathematical statements treat exact periods two, three, and four (IDs `a6fb565f-372c-4ebb-9055-037c1563acd6` and `9113f264-80c9-4b61-9cc6-3b7754ef99d2`), so the original proposed period-three Fermat theorem was excluded as already covered. The separate five-cycle theorem is not a corollary of those shorter-period statements. The complete finite odd-parameter cycle census and even-parameter cycle-locator records were read in full, and neither supplies this unbounded odd-parameter characterization. Dubickas's broader framework does not fix the deterministic map's composite transition to its largest prime factor. Direct published-finding corpus and web searches by the map name, aliases, period-five language, and arithmetic criterion found no equivalent claim. Search non-detection is not a novelty proof; unindexed equivalent work remains a residual risk.

## Mathematical value
**PASS.** Exact cycle length is a central structural invariant of the originating paper's arithmetic dynamics. Unlike a finite numerical census or a routine parity observation alone, the result classifies every odd parameter admitting the next unresolved odd cycle length, proves uniqueness of each such orbit, and gives an explicit prime-divisor/smoothness parameterization in terms of \(2^m+1\). It provides a reproducible arithmetic decision criterion for a natural infinite parity class and clarifies where the odd-cycle obstruction arises.

## Closest literature and limitations
See Das (arXiv:2312.06629v1), Dubickas (*Axioms* 13 (2024), 107), the two prior period-two/three/four classifications identified in `RESULT.md`, and the two full-inspected published published-finding corpus records. No statement for even \(k\), no infinitude assertion, and no independent mathematical audit are claimed.

Self-review: passed. Independent audit: not yet performed.
