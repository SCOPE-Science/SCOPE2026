# Independent audit — 2026-09-30

## Final claim
Subtract-a-cube Sprague–Grundy and outcome periodicity

## Correctness — PASS
Fresh dynamic programming from the move set {1,8,27,64,125} reproduces the outcome cycle [1,1,0,1,0,1,0] from 263 and SG cycle [2,0,1,0,1,0,1] from 264, the last mismatch witnesses at 262/263, the complete [0,200] SG histogram (71,71,34,19,6), and the six SG=4 positions through 200. Direct checks verify the required 125-consecutive-equality windows; the max-move recurrence then proves the periodic tails.

## Originality — PASS
Best-of-knowledge originality passes after comparing statements and implications, not merely titles.

### Equivalent formulations
Searches: Resultary semantic search for subtract-a-cube Sprague Grundy period 7 263 264; targeted web search for subtract-a-cube Sprague-Grundy
Evidence: Resultary's exact-topic hit is this record; the closest returned published SCOPE item is a census of primitive three-move games with max<=10, a different family.
Reasoning: Outcome P-positions, SG zeroes, and cube-difference-free cold positions were searched as equivalent descriptions of the same game.

### Broader coverage
Searches: Eppstein arXiv:1804.06515; general subtraction-game search; Resultary subtraction-game records
Evidence: Eppstein develops general algorithms and applies them to subtract-a-square, not this five-move cube set or its numerical eventual period. General subtraction-game eventual periodicity/algorithms do not determine this game's least period and preperiod without the finite certificate.
Reasoning: The checked broader theory supplies methodology, not the claimed exact invariant.

### Exact database or table
Searches: Targeted web/OEIS searches for subtract a cube Grundy and losing positions; Resultary exact-topic search
Evidence: No independent checked table with period 7 from 263/264 or the [0,200] cold census was located.
Reasoning: This supports best-of-knowledge originality only; absence of search results is not treated as proof.

### Claim versus prior implication
Searches: Eppstein 2018 subtraction-game algorithms; standard finite-subtraction recurrence
Evidence: The recurrence proves a periodic tail once a length-max(S) equality window is verified, but prior general results do not specify where that window first occurs for this S.
Reasoning: The numeric least-onset and census require the exact computation/certificate supplied here.

### Source inspections
- **Faster Evaluation of Subtraction Games** (arXiv:1804.06515): General algorithmic background with an explicit subtract-a-square application; it does not state the subtract-a-cube values audited here. Material read: Abstract and application description. Evidence: The abstract describes fast algorithms and experimental square-subtraction results.

Checked sources: Eppstein, arXiv:1804.06515; Resultary published-record search; targeted web/OEIS searches
Residual risks: Best-of-knowledge originality may miss an unindexed recreational-game table. The claim concerns the fixed move set relevant through heap 200, not the infinite set of all cubes as heap size grows.

## Scientific value — PASS
Perfect-cube subtraction is a canonical analogue of the well-studied subtract-a-square game. Its exact least periodic tail, cold census, and maximal nimbers are natural invariants that a future study of polynomial subtraction sets can use as a benchmark.

## Limitations
- The fixed set is exactly the cube moves applicable through heap 200; larger heaps would introduce additional cube moves if the game were redefined with all cubes.
- Literature coverage is targeted rather than exhaustive.

## Conclusion
The final claim passes correctness, originality, and scientific-value review on the evidence stated above.
