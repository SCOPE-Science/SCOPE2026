# Scientific review

## Correctness — PASS

The object is a binary most-significant-digit-first automaton with outputs correct on every word, including leading zeroes and the empty word. The proof reconstructs exact residuals from the finite carry-offset set, proves a one-to-one correspondence between distinct residual functions and indexed Thue–Morse fingerprints, and counts pure-dyadic fingerprints by isolated run-parity vectors. For successor-dyadic shifts, floor/ceiling maps identify even fingerprints with pure-dyadic fingerprints and odd fingerprints with predecessor successor-dyadic fingerprints. The parity classes are disjoint because Thue–Morse contains no constant triple. The resulting recurrence has base six and solves to \(2F_{k+4}\). Each step is algebraic and covers every positive integer \(k\). Exact checker results corroborate the general proof; they do not replace it.

## Originality — PASS within examined evidence

The 2025/2026 paper of Moradi, Rampersad, and Shallit states only upper/lower bounds and asks for exact shift-state counts. Biswas (2026) treats pure dyadic shifts \(2^r\); his inspected full textual proof does not address the successor class \(2^k+1\). The OEIS table A382296 already contains small successor-shift values, but has no inspected infinite successor-dyadic identity or parity-residual proof. Targeted indexed-record searches and primary-paper comparisons did not reveal a covering statement. Residual risk: a differently formulated or unindexed general state-complexity formula could imply the claim.

## Value — PASS

This gives a complete exact infinite-family solution for shifts immediately above powers of two, a mathematically natural first extension beyond the previously solved dyadic case and a subfamily of a stated general open problem. The equivalence \(N(2^k+1)=N(2^{k+1})\) and disjoint even/odd residual decomposition characterize a non-obvious structural relationship between neighboring shift classes. The result is not merely a recomputation of known numerical entries: it proves their infinite Fibonacci law and gives an explicit mechanism.

## Closest literature and limits

Moradi–Rampersad–Shallit, arXiv:2512.10017, Section 4.2 and Open Problem 2; Biswas, *State Complexity of Thue-Morse Shifts by Powers of Two* (2026); OEIS A382296. Exact values for individual small shifts are already public. This result does not resolve arbitrary shifts. Independent scientific audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
