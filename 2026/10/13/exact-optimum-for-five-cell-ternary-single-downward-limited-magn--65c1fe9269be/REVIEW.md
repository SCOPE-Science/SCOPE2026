# Scientific review: five-cell ternary limited-magnitude codes

## Correctness — PASS
The channel has exactly 243 possible transmitted words, with disjoint radius-one directed error balls exactly characterizing zero-error codes. Receiver-preimage packing constraints form a provably equivalent 243-variable 243-constraint integer optimization. A separate construction of all 1890 confusability edges yields an independent exact maximum-independent-set model. Both solvers reported optimal status, primal value 45, and dual bound 45. A third standard-library program checked every output of each of the 45 listed codewords. The upper-bound proof is computational, relies on correct mixed-integer solver execution, and is not an independent formal proof certificate.

## Originality — PASS, with bibliographic risk
The closest explicit primary result is the 2014 paper of Fazeli, Vardy and Yaakobi, Section V.A, Table V, giving an upper bound of 55 for the same parameters; it derives fractional bounds and does not determine the exact unrestricted integer packing number. Buzaglo and Etzion study the perfect-lattice construction setting rather than the unrestricted finite maximum. Published coding constructions by Cassuto and colleagues and by Kløve, Bose and Elarief are highly relevant, but only available abstracts or bibliographic data were inspected for some of them. An earlier unindexed tabulation cannot be excluded. The finite packing optimum is therefore compared to verified statements rather than asserted globally unique.

## Value — PASS
An exact unrestricted cardinality is a natural finite-capacity benchmark for a physical one-coordinate downward-error channel, and this parameter reduces the strongest inspected fractional upper bound from 55 to 45, a reduction of ten codewords. The explicit code gives a usable optimal design, while the separate upper-bound computation establishes that non-linear alternatives cannot do better under the specified error model. This is an exact finite design fact, not an asymptotic theorem or a new decoder for arbitrary lengths.

Self-review: passed. Independent audit: not yet performed.
