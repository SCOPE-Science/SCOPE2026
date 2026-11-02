# Self-review

## Correctness
PASS. For a fixed cycle, the \(k\) prescribed images are forced and the remaining \(n-k\) independent sources have exactly \(n-1\) possible destinations each. The conditional zero-indegree factorial-moment probability includes separate factors for prospective empty vertices (which cannot map to themselves) and other free vertices. The exact formula is valid at the endpoints \(t=0\), \(t=n-k\), and \(k=n\). Summing the marked-cycle expectations yields (1); the explicit positive \(k=2\) and negative \(k=3\) numerators plus strict decreasing \(g_n(k)\) prove every finite sign. The special \(k=3\) cancellation is checked before asymptotic expansion. The packaged checker verified 40,314 exact assertions, including exhaustive enumeration through seven vertices.

## Originality
PASS at best-knowledge, qualified. Flajolet–Odlyzko's inspected Section 5.1 names fixed-point-free functional digraphs and gives unmarked generating functions; the inspected material does not give the marked mixed cycle/source moments or three-regime sign law. Hansen–Jaworski's 2006 introduction discusses independent-choice self-maps with diagonal bias but its focus is component and cyclic-point distributions, not the joint statistics here. Prior local-structure studies remain a material historical priority risk, particularly Harris (1960) and Berg–Jaworski (1992), whose complete texts could not be read. Search nonmatches are not proof of novelty. Earlier general methods may facilitate an alternative derivation but have not been identified as a published stronger statement implying this claim verbatim.

## Mathematical value
PASS. Feedback cycles of length two, three and at least four represent natural distinct circuit types in a loopless functional digraph. The proven reversal of the sign at length two and singular cancellation of the leading \(1/n\) term specifically at length three provide a non-obvious dependence hierarchy not captured by ordinary marginal cycle counts or expected number of sources. Conditional factorial moments also give the complete finite-source law under a planted directed cycle. The comparison with unrestricted mappings shows why the loopless hypothesis matters.

## Closest literature and limitations
The classical fixed-point-free mapping model is explicit in Flajolet–Odlyzko (1990), Section 5.1, and the general independent-choice model is described in Hansen–Jaworski (2006). The results were compared at statement and implication level; claims about cyclic *vertices* or fixed points do not automatically yield statements about individual cycle lengths. The historical local-statistics articles by Harris (1960) and Berg–Jaworski (1992) could not be evaluated at full-text level; this prevents certification of absolute priority. No conclusion is asserted for dependent mappings or for growing cycle lengths in the asymptotics.

Self-review: passed. Independent audit: not yet performed.
