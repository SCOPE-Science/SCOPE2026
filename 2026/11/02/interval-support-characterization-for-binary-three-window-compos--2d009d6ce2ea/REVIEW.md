# Self-review

## Correctness — PASS

The proof explicitly separates necessary and sufficient conditions. The necessary condition follows from the exact sliding-window recurrence for weight changes; sufficiency is demonstrated for all ten nonempty interval supports using short base words and reversible three-step endpoint gadgets. Positive-composition counting establishes the exact cubic formula, the \(m^2-1\) forbidden formal profiles, and the maximal zero-error code size. For every width \(h\ge4\), the all-positive single-duplicate weight-two profile forces disjoint constant length-\(h\) factors, leaving exactly one additional bit; this allows only four other duplicate levels. The executable checker verifies finite cases independently; it is not invoked as an infinite proof.

## Originality — PASS

Marcovich–Yaakobi (arXiv:1912.11108) study literal fixed-length reads; Gupta–Mahdavifar (arXiv:2201.09955) use all substring lengths; Sporring–Darkner (doi:10.3390/e24030433) retain the **order** of overlapping local histograms. None of their inspected definitions and results provides the iff for the unordered count-vector of length-three binary reads. Published exact binary length-two multispectrum results are narrower in the read-width dimension, not directly covering this claim. OEIS A188554 contains **precisely the same cubic numerical sequence** for another combinatorial object; the number sequence is not a novelty claim. The new statement is the nontrivial overlapping-window realization bridge and sharp failure at width four. A not-yet-located equivalent specialization remains a risk, particularly in work on sliding-histogram reconstruction; direct access to one publisher page was intermittently limited, although substantive indexed sections including formal definitions and conclusions were available.

## Value — PASS

The complete characterization converts an observation-space feasibility problem into a one-line support test. Its constructive converse gives an explicit optimal codebook of \(rac{m^3+11m+12}{6}\) words under the deterministic binary three-composition-read channel, for every \(m\ge1\). The quadratic excluded-profile formula and proof that width three is the **largest** width with unrestricted interval sufficiency identify a useful structural boundary. This is more than a numerical rediscovery or an arbitrary small case.

## Scientific limitations

Only binary, noiseless, unordered contiguous triple-composition reads are classified. The proof does not classify all width-four or wider multispectra, nor noisy reconstruction; it does not claim novelty of the OEIS polynomial. The proof and standalone checks remain without independent external validation.

Self-review: passed. Independent audit: not yet performed.
