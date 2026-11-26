# Independent mathematical audit

## correctness

PASS

For H even, equal large counts and unit discrepancy L mod 2 attain the total-load parity lower bound. For H odd and L<r−1, any partition has an odd large-count difference and discrepancy at least r−L, attained by putting all L units with the large-poor agent. For H odd and L≥r−1 the parity-compatible compensation is r or r−1, again attaining the parity bound. This proves the prefixwise MMS formula including zero counts. On a unit arrival the even-H case is equalization and the odd-H compensation delta changes by exactly one, with the sign specifying the receiving agent. On a large arrival, the parity switches; the recipient of the new large good transfers q=(delta−(L mod 2))/2 old units. The two agents' unit-count difference changes by 2q in the required direction in either parity case. For r=2,3, q is 0 or 1; whenever it is 1 the recipient has a unit available and its old position is matched to the new large good while all other old items remain in place for that agent. Thus the injections hold from the empty allocation onward. The rule is deterministic with fixed tie-breaking and uses a constant number of counter/list operations per arrival. For r≥4 the fixed five-good word has MMS 2 at prefix four and MMS 4 at prefix five, forcing cardinalities (2,2) then (1,4) up to labels, which fails an injection regardless of foresight. The EFX argument moves one strictly positive good from the envied bundle and obtains two parts strictly above the allegedly envying agent's value, contrary to its MMS guarantee. Identical valuations make every complete allocation Pareto optimal.

## originality

PASS

The substantive distinct content is the exact item-level all-prefix rule for ratios 2 and 3 and its combination with the sharp obstruction into a complete feasibility classification. The strongest static two-size result and the exact bundle-level result do not supply the compatibility of successive allocations under item injections. The negative mechanism has an especially close precursor in Huang–Teh B.12 and the EFX consequence is already in C.2; neither is credited as an independent novelty. This is a best-of-current-knowledge statement for the bounded domain.

## value

PASS

The restriction to a common valuation and just two sizes isolates when the smallest form of recourse suffices for optimal prefix fairness. The transition invariant yields an implementable one-displacement guarantee for every arrival word, whereas the forbidden ratios require no adaptive adversary and cannot be saved by advance knowledge. Static optimal partitions alone do not answer that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
