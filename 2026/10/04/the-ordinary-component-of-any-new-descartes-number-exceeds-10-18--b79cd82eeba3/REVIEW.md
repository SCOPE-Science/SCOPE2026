# Same-model scientific review

## Correctness
PASS. From \(\sigma(q)(p+1)=2pq\) with odd \(p,q\), 2-adic valuation forces \(\sigma(q)\) odd, hence \(q\) is a square. This converts the complete range \(q\le10^{18}\) into the finite root range \(m\le10^9\). The packaged segmented sieve factors every odd root, computes \(\sigma(m^2)\) exactly, and applies the defining divisibility test. Its only nontrivial hit is \((q,p)=(9018009,22021)\), Descartes' example.

## Originality
PASS. Tóth's peer-reviewed bound is \(q>10^{12}\). The closest located public extension is a 2023 Mathematics Stack Exchange computation through \(10^{16}\), which uses the same square observation but stops two orders of magnitude earlier. Current database entries and broader spoof-factorization literature do not state a \(10^{18}\) exclusion. Residual risk remains for an unindexed computation.

## Value
PASS. The ordinary-component cutoff is the central finite invariant in Tóth's theorem. Extending it from \(10^{12}\) to \(10^{18}\) is a million-fold improvement of the peer-reviewed bound, and the proof exposes a simple square-root reduction that makes the certificate inexpensive and reproducible.

## Closest literature and limitations
The primary source is László Tóth, “On the Density of Spoof Odd Perfect Numbers,” arXiv:2101.09718 / *Computational Methods in Science and Technology* 27 (2021), 25–28. The closest located public computation reports \(10^{16}\) on Mathematics Stack Exchange in 2023. The result here is finite and positive-Descartes-specific; it does not prove uniqueness and does not address signed or multiperfect spoof generalizations.

Same-model review: passed. Independent audit: not yet performed.
