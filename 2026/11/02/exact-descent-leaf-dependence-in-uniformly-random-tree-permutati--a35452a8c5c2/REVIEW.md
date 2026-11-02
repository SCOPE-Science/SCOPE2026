# Scientific review

**Correctness (PASS).** The two insertion operations have an explicit last-comparison update; they give \(D=1+N_{01}\). Acan–Hitczenko's published leaf/run lemma gives \(L=n-1-(N_{01}+N_{10})\). The telescoping identity, independent transition-bit recoding, exact binomial conditional law, moment computation and CLT are proved in RESULT.md. The embedded standard-library checker passed 16,499 exact assertions, independently brute-classifying 126 tree permutations. No finite computation is treated as a proof for all sizes.

**Originality (PASS, with historical-priority risk).** The nearest paper Acan–Hitczenko (2014) already gives the binary code and leaf statistic, but not the joint relation to adjacent descents. Janson (2022) studies ordinary permutation-pattern occurrences, not the adjacent-descent/leaf joint law. Selig–Zhu (first public March 28, 2023) covers one-CNAT permutation classes and a different descent-preserving tableau bijection, not the stated law. The conditional mixture and asymptotically perfect negative correlation are therefore not identified as covered in the inspected sources or semantic research-record results. A major residual risk is that they may be derivable or previously recorded as consequences of the older code; independent historical verification is needed.

**Value (PASS).** The theorem identifies an exact near-conservation law coupling a permutation-local statistic with a nonlocal graph statistic, gives its entire finite-sample conditional distribution and resolves its asymptotic dependence with correlation tending to minus one. In random permutation graph models this is a structural cross-statistic statement, not merely a new formula for a previously tabulated marginal.

**Limits.** Uniform tree permutations only; no transfer to forests or weighted codes. The 2014 encoding is not new, and neither novelty nor proof has independent certification.

Self-review: passed. Independent audit: not yet performed.
