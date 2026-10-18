# Exact sampling and parity classes: scientific review

## Correctness (PASS)
The explicit cyclic-edge conjugacy is a linear bijection. For every \(n\ge1\) and \(1\le j\le n\), the resulting graph splits into \(\gcd(j,n+1)\) cycles, and the first \(n+1-\gcd(j,n+1)\) edge occurrences form a forest. This proves the exact orbit-rank formula and, because the noise bits are fair and independent, the exact all-time total variation distance. Parity quotient and Burnside's lemma prove the communicating classes and their periods. The standalone checker independently passed 186840 rank tests, 1039 exact-state distribution checks, and 12 orbit-count tests; none is invoked as an infinite proof.

## Originality (PASS on inspected evidence)
Levin and Tankala's 2021 preprint, Section 5 Theorem 2, gives exact sampling for the middle site in even dimension. This follows from the current criterion, but the paper does not state the arbitrary-site gcd classification, complete finite-time distance, or cyclic parity classes. Diaconis and Graham (1992) analyze a different unipotent Jordan-block affine map, and Chung, Diaconis and Graham (1987) study integer-modulus affine recursions. Relevant exact-phrase, shift-register, controllability, and cyclic-parity searches revealed no dominating statement in the examined material. A possible equivalent statement under older binary linear-system terminology remains an acknowledged priority risk. The full text of one contextual article was not accessible, so its abstract was not used to assert whole-document noncoverage.

## Value (PASS)
Choosing where to inject randomness in a shift-register sampler changes the answer from exact \(n\)-step sampling to permanent nonmixing. This theorem determines the sharp arithmetic boundary, exact sampling time and distance at every step, and the precise nonergodic decomposition. Such a complete positive/negative structural classification addresses an intrinsic modeling choice that the closest published special-case theorem leaves open.

## Scientific boundaries
All results require a fixed injection site and independent fair binary bits. The claim does not extend to biased noise or arbitrary feedback rules. The source comparison is evidence-based rather than a certificate of first discovery; no independent audit or validation is claimed.

Self-review: passed. Independent audit: not yet performed.
