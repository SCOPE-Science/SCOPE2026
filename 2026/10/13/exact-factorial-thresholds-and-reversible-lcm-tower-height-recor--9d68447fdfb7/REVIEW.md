# Review of exact factorial thresholds and reversible lcm tower-height records

## Correctness
PASS. The least-height lemma is reconstructed by induction. Legendre's formula and the dominance of the \(2\)-adic factorial valuation yield exact first hits with no finite truncation. The lcm valuation formula gives a full interval on which \(h\) is constant, and a separate argument certifies the drop at its double: an odd-height obstruction proves the upper bound while explicit primes for \(k=3,4\) and Bertrand's postulate for every \(k\ge5\) prove the matching lower bound. The standalone verifier checks small and moderately large boundary instances. The only external number-theoretic theorem required is the classical Bertrand postulate.

## Originality
PASS, subject to a normal literature-coverage risk. The directly relevant De Koninck–Verreault paper defines \(h\) and identifies the least height-\(k\) integer but addresses density, means and runs, not factorial/lcm first indices or record reversal. Their companion factorial-arithmetic-function paper covers other functions. OEIS A288636 uses a different gcd-of-exponents height (with coincident minimum tower thresholds). Searches for exact, equivalent, and broader formulations in primary literature, sequence tables and published research records gave no statement implying the complete factorial/lcm theorem; the closest same-object facts supply an ingredient, not the combined conclusions. Existing small thresholds are not represented as novel by themselves.

## Value
PASS. The standard factorial and initial-lcm sequences are natural contrasting tests of a nonmonotone recursive arithmetic invariant. The theorem gives exact all-level hitting laws and a striking unbounded family of full-length lcm record intervals followed by immediate decreases, requiring an odd-prime exponent witness and a genuine prime-in-interval argument. This is a structural behavior not reducible to finite numerical examples. Later return times and full trajectories remain open.

## Limitations and closest prior literature
The shortest unrestricted integer of tower height \(k\) was already known to be \(E_k\), and the proof uses that input explicitly. No conclusion is asserted about every subsequent factorial or lcm height, and an unindexed equivalent result is an originality risk. Sources: De Koninck–Verreault, *On the tower factorization of integers*, arXiv:2308.09149v1 (especially Sections 1, 6, 7); De Koninck–Verreault, *Arithmetic functions at factorial arguments*, arXiv:2308.09761; OEIS A288636.

Self-review: passed. Independent audit: not yet performed.
