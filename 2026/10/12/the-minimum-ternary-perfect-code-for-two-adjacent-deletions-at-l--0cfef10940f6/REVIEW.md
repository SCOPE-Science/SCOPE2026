# Scientific review

**Correctness — PASS.** The exact domain is the ternary alphabet, five transmitted symbols, and one deletion of two adjacent symbols. The eight exhibited codewords have pairwise disjoint received-word sets partitioning all \(27\) ternary triples; an independent standard-library checker verifies the partition. The exhaustive lower verifier enumerates all \(243\) words and proves no seven-word covering exists using complete branching and a necessary four-shadows bound. It visits \(649\) memoized states, independently reproduced in C++ (\(735\) recursive calls). This is a finite exhaustive argument, not an extrapolation or timeout.

**Originality — PASS, with risk.** Chee–Li–Zhang (2015) give a length-five ternary perfect-code construction of nine words and describe a broader spectrum, but the inspected statements do not imply an eight-word perfect code or the exact minimum. Xie–Sun–Ge (2026) study general burst covering constructions without this sharp ternary finite result. Published published-finding corpus, original literature and own prior claims were checked for alias and broader-coverage overlap. **Risk:** the closely relevant 2015 full PDF could not be comprehensively inspected, so an uncatalogued previously known finite construction remains possible.

**Value — PASS.** The perfect burst-deletion-code spectrum has a naturally motivated first odd-alphabet case. Establishing the exact ternary length-five minimum \(8\), rather than merely an upper-bound example, closes a precise finite optimality question and improves the previously inspected nine-word construction. The claim makes no general finite-field or asymptotic assertion.

The outcome is limited to the one stated finite claim. The supplied machine-checkable source files are independent of optimization software; independent external mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
