# Scientific review

## Correctness — PASS

For all positive integers \(a,b,c,d\), the proof classifies every factor by transition count. The prefix/suffix characterization of minimal absence yields the ten disjoint word families, and exclusion of four or more transitions is explicit. Each extra conditional word has both proper length-one-shorter factors present under its stated exact inequalities. Summing the nine comparison regions proves the claimed \(\{1,2,4\}\) excess set. Independent brute enumeration in `verify.py` checks 4,096 positive quadruples with exponents at most eight and another 120 larger cases; all 45,328 minimal absent words from the exhaustive region matched both the full set and length polynomial. The computation is a finite check and is not relied upon for the unbounded assertion.

## Originality — PASS, with residual risk

Akagi et al., *Minimal Absent Words on Run-Length Encoded Strings* (2022; arXiv:2202.13591), provide a general enumeration classification and an output-sensitive algorithm for all run-length encoded strings. The checked methods can in principle enumerate any four-run instance, but no theorem in the examined sections states the explicit four-run ten-family closed form, complete length polynomial, or exact three-valued excess classification. Sliding-window results (arXiv:2105.08496; arXiv:1909.02804) concern general update complexity, not this parameter formula. Relevant published claim records for four-run *minimal unique* factors are not equivalent: unique factors occur once, absent factors occur zero times. Searches for binary four-run antidictionaries, synonyms, exact parameters and run-length formulas located no matching published claim. Database search absence is not evidence of uniqueness, and an unlocated specialization remains a genuine risk.

## Mathematical value — PASS

The interior-run-dependent count and forbidden excess three are a sharp structural classification across infinitely many nonisomorphic run-length-encoded strings. The explicit list and length profile give precise benchmark antidictionaries for compressed factor processing, beyond a known generic algorithm whose output must still be enumerated. This is a complete natural structured family rather than an arbitrary finite slice or a renamed textbook inequality.

## Closest results and boundaries

The 2022 run-length encoded algorithm is strictly broader as an algorithm but does not state the present explicit parameter theorem. The proof is specific to two symbols and exactly four positive runs. No claim of new generic MAW algorithms or independent audit is made.

Self-review: passed. Independent audit: not yet performed.
