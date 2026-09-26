# Independent Audit — 2026-09-22 campaign

**Record:** `2026/09/08/082`
**Audited source tree:** `69d96faba5eded5bcd0208a16ecaa3016ddc43bf`

## Correctness — PASS

A fresh odd-only Eratosthenes sieve to 50,000,000 produced exactly 3,001,134 primes, ending at 49,999,991. Independent aggregation of consecutive-prime residues reproduced every committed entry of the modulo-10 matrix and modulo-3 matrix. Their totals are 3,001,130 and 3,001,131 after the stated exclusions. Direct recomputation gives uniform chi-square 155166.0486 and 47958.5868, respectively, and confirms the stated diagonal suppression and extremal cells.

The Hardy–Littlewood comparison is correctly presented as a numerical comparison to prior conjectural formulae, not as a proof of those formulae.

## Originality — PASS, narrowly scoped

Lemke Oliver and Soundararajan (arXiv:1603.03720) established the consecutive-prime residue-bias phenomenon and its Hardy–Littlewood explanation. Holt (arXiv:2405.03540) describes the well-known mod-10 experiment as using the first 100 million primes. I did not identify a checked source publishing these exact x<=50,000,000 T10/T3 matrices and residual statistics.

The originality finding is limited to this exact finite cutoff dataset and quantified comparison, not the underlying bias phenomenon or theory.

## Scientific value — PASS

The record supplies a fully specified, independently reproducible transition-matrix benchmark for a recognized analytic-number-theory phenomenon. Its value is finite and computational rather than a new asymptotic theorem.

## Overall verdict

**PASS.** Correctness, narrow finite-scope originality, and benchmark scientific value are supported.
