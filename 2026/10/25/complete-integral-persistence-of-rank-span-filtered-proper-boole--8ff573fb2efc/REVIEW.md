# Scientific review

## Correctness — PASS
The claim's domain and inclusive endpoints are explicit: all nonempty proper subsets of a ground set of size \(n\ge3\), rank-span cutoff \(0\le k\le n-2\), with a constant final tail. Kitajima's Corollary 4.19 supplies, for each filtered level, an integral homotopy type supported in precisely one degree. The newly checked chain enumeration partitions all added letters into nonempty, ordered increments, yielding exactly \(\binom ns(2^{n-s}-2)j!\operatorname{S}(s,j)\) chains of dimension \(j\) and span \(s\). The falling-factorial identity at \(-1\) collapses the Euler sum to the displayed closed expression and recurrence. Homology-support degrees at successive levels differ, forcing every nonterminal inclusion map to vanish; the final complex is a subdivided sphere. These facts prove the complete reduced integral bars. Exact matrix-rank checks independently confirm the small instances. No unproved inference from finite computation is needed.

## Originality — PASS, within the compared literature
The full published text of Kitajima's article establishes the wedge **shape** and the \(n=5\) numeric example but does not state all-parameter multiplicities or the reduced persistence barcode. The complete published rank-span-two research result yields precisely the degree-two special case of this recurrence; its other conclusions are equivariant and do not state an all-rank barcode. Hersh–Sundaram consider fixed rank selections, which are not these varying span intervals. The comparisons include the exact overlapping specialization rather than treating different titles as evidence. Exhaustive novelty is unproved; elementary implicit consequences and unindexed sources remain a genuine risk.

## Value — PASS
The rank-span filtration is used to relate topology to magnitude homology. Its core natural numerical questions are the number of sphere generators at **each** scale and their lifetimes; a general existence theorem and a single Boolean five-element example do not provide these invariants. The uniform recurrence calculates unbounded families of varying dimensions and sizes and gives the complete integral persistence without finite extrapolation. It is a natural full classification, not an arbitrarily sliced small-parameter recomputation. The result is limited in scope, and no claim of a separate equivariant theorem is made.

## Evidence and limits
- Kitajima, 2025 public poster (December 15), and arXiv:2606.15241: full available article inspected; rank-span definition, Corollary 4.19 and Example 4.21 compared.
- Hersh–Sundaram, arXiv:2604.06479: available full text's definitions and rank-selection theorems inspected for distinct scope.
- *Symmetric-group characters and contractible quotients of rank-span-two Boolean complexes*: complete published `RESULT.md` inspected; its \(k=2\) multiplicity agrees identically with the recurrence.
- Reproducible independent finite enumeration is in `verify.py`, not an infinite-family certificate.
- Risk: an equivalent all-parameter Boolean-chain Euler computation may exist outside the inspected records or be regarded as an implicit deduction of Kitajima's known structural theorem.

Self-review: passed. Independent audit: not yet performed.
