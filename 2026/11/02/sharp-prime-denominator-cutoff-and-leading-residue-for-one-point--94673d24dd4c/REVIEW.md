# Scientific review

## Correctness — PASS
The claim follows from the Faber--Pandharipande generating identity and an exact partition-denominator argument. Each partition term has valuation bounded by \(E\); all partitions with length above \(m\) have valuation at most \(E-1\), and the only term of valuation \(E\) at length \(m\) is the partition with \(r\) singleton parts and \(q\) parts of size \(s\). Wilson's theorem fixes the residue, while the monic integral rising-factorial basis and the shift of variable preserve the maximal degree. The finite standard-library checker passed 206 parameter pairs. The proof covers every quantified genus and prime, independent of this finite calculation.

## Originality — PASS, with priority risk
The nearest primary work is Holmes, arXiv:2610.30274v1, §3.1 and Proposition 3.7; it computes the genus-wise least common denominator, exhibits an extremal partition and obtains existence of an extremal coefficient. The added result identifies the **exact largest** one-point Hodge index realizing the full prime denominator and its residue. The length-above-cutoff exclusion is not a separately stated assertion in Holmes, but extends the same valuation estimate; the close mathematical dependence is expressly acknowledged. The Faber--Pandharipande trigonometric generating identity predates both results. Adelberg's Nørlund arithmetic was checked at abstract level, and an equivalent coefficient-degree result in that literature cannot be excluded. Semantic research-record and accessible local-history queries yielded no matching claim; search absence does not prove priority.

## Mathematical value — PASS
The global least common denominator alone does not say which individual tautological intersection classes realize it. This theorem determines the smallest Hodge Chern-class index among all one-point linear Hodge integrals that still exhibits maximal \(p\)-adic complexity, uniformly for every odd prime \(p\ge5\) in range, and gives the nonzero residue needed to rule out cancellation. It is a precise natural boundary for geometric intersections, not an arbitrary chosen coefficient or finite numerical improvement. The literature dependence limits its independent scope.

## Sources and limitations
The primary 2026 full text, especially Lemmas 3.1--3.5 and Proposition 3.7, was compared at the level of statements and implications. Faber--Pandharipande and Adelberg metadata/abstracts were checked; their full texts were not used to claim noncoverage. The theorem is only for the one-point linear family, primes at least five, and genus at least two. Historical priority and independent mathematical validation remain unresolved.

Self-review: passed. Independent audit: not yet performed.
