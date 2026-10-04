# Review

## Correctness
PASS. The claim is finite and fully quantified over the \(81\) ternary words of length four. The verifier constructs deletion shadows directly, enumerates every compatible \(11\)-subset and every compatible \(12\)-subset by an ordered recursion with only exact cardinality pruning, and then checks the structural core, six-cycle, orbit, and stabilizer. The replay returns six size-
\(11\) codes and zero size-
\(12\) codes. Direct shadow-union checks also show that every listed maximum has \(23\) distinct deletion outputs.

## Originality
PASS with stated residual risk. The closest inspected length-four source, arXiv:1003.4057, gives sharp results for even alphabet sizes and explicitly says its bound is not sharp when the alphabet size is odd; it does not classify ternary maxima. The full text of arXiv:1211.3128 was inspected at its numerical table: the ternary length-four row records upper bounds \(16,13,12\) and a best listed Tenengolts size \(8\), not an exact count or orbit classification. DOI:10.1002/jcd.20031 concerns existence of perfect \(T^*(3,4,v)\) codes, which is logically different because the maxima here cover only \(23\) of \(27\) deletion outputs. Targeted exact-parameter and representative searches did not locate the six-code classification. The main residual risk is an older unindexed computation; the 2011 Brock thesis was only partially inspectable through indexed snippets.

## Value
PASS. The result strengthens a size-only extremal statement into a complete classification at the smallest nonbinary odd-alphabet length-four instance: it determines every extremizer, exposes a common nine-word core and a six-cycle of allowable remainders, and proves uniqueness up to the natural channel symmetries. That structure is useful as a canonical finite benchmark for construction and search methods and is not a mere recomputation of a published table.

## Closest literature and limitations
The closest broader sources are arXiv:1003.4057 and arXiv:1211.3128; the former treats sharp even-alphabet length-four constructions and flags odd alphabets as non-sharp for its bound, while the latter gives only a fractional upper bound for the ternary case. Perfect-code existence results do not dominate this claim. The classification is finite, computer-assisted, and does not generalize automatically to other parameters. An inaccessible older thesis remains a specifically identified originality risk.

Same-model review: passed. Independent audit: not yet performed.
