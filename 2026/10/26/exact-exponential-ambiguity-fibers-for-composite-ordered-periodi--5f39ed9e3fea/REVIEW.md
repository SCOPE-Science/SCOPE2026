# Mathematical assessment: complete ordered-cycle signature fibers

**Final claim.** For each factorization \(n=mr\), with \(m,r\ge2\), the full time-by-point left-right signature of the canonical consecutive-block cycle has exactly \(r^{m-1}\) single-cycle preimages. It is not a general upper bound over all signatures. This yields exactly \(2^{n/2-1}\) alternatives in an explicit family at every even period.

## Correctness — PASS
The common-signature construction is proved for all parameters: after a full traversal of the \(m\) blocks the internal coordinate advances by exactly one \(r\)-residue, so every constructed map is one \(mr\)-cycle. Nonmultiples of \(m\) compare disjoint ordered blocks and multiples of \(m\) compare the same canonical cyclic rotation, independent of block shifts.

The difficult step is exhaustive uniqueness **within the signature fiber**. For an arbitrary matching \(n\)-cycle, its \(m\)th power has exactly \(m\) cycles of length \(r\). The observed strict right/left profile of that power has exactly \(m\) descending points, occurring at the endpoints of the consecutive blocks. Every cycle contains a descending maximum, so these endpoints are exactly the maxima of those \(m\) cycles. Successively removing cycles in increasing order of maxima forces each cycle support to equal the corresponding consecutive block. Strict ascent at all but the final point of a block then forces the internal cyclic shift by one. Commutation with the \(m\)th power identifies the interblock bijections as cyclic translations; the observed first-step signs force successive block order, and the power identity forces total shift one. No unproved group-classification or unbounded computation is needed.

The standalone finite checker exhausts **all** single \(n\)-cycles for \(n=4,6,8,9,10\) against eight specific signatures, and tests all shifts for sixteen small factorizations. It is confirmatory evidence, not a proof of universal quantifiers. Boundary cases \(m=2\) and \(r=2\) are included; neither parameter may equal one in the theorem.

## Originality — PASS under accessible comparisons
Fuhrmann–Gröger–Passeggi, arXiv:2610.07435v1, Section 2, supplies the precise signature notion and establishes uniqueness for *prime* cycle lengths, explicitly observing nonuniqueness for composites with a four-point illustration. That does not determine the exact ambiguity cardinality for each factorization or recover every cycle in a fiber. The inspected public note *Quadratic-time reconstruction of prime cycles from left-right orbit signatures* improves prime reconstruction time but keeps the prime assumption; it gives neither our composite family nor a complete converse. Standard excedance-set enumerations address a single permutation, rather than simultaneous sign data for all its powers.

Searches for all-power excedance-set equality, ordered orbit-signature collisions, composite cycle fibers, and larger permutation-classification statements revealed no direct prior exact-fiber theorem. Literature coverage is not exhaustive; a specialized all-powers permutation-enumeration result may imply the classification, so independent priority review is still warranted. The absence of an indexed hit is not itself treated as proof of novelty.

## Mathematical value — PASS
This is a quantitatively sharp instance of the inverse problem that drives the motivating paper's prime-cycle rigidity lemma. For every factorization the theorem determines an entire naturally defined ambiguity fiber, not just two indistinguishable examples. The reverse classification is a structural rigidity statement for the hidden return permutation. The even-period specialization shows exponential information loss despite observing all non-return times for all orbit points, a relevant boundary for reconstruction and identifiability.

## Scope and limitations
The result is finite-orbit rigidity/ambiguity with time-indexed left-right comparisons, not equality of global continuous-map period spectra. It gives one exact fiber per factorization, not the global maximum across fibers. No claim is made that a finite checker establishes the universal statement or that historical priority is independently certified.

Self-review: passed. Independent audit: not yet performed.
