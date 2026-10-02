# Independent mathematical audit — 2026-09-30

## Record

Exact consecutive-prime residue-pair census to 5e7 with quantified Lemke Oliver-Soundararajan comparison

## Disposition

repaired

## Correctness: PASS

The final repaired claim was reconstructed from the stated consecutive-prime definition. A fresh odd-only Eratosthenes sieve through 50,000,000 independently produced 3,001,134 primes, last prime 49,999,991, and the little-endian uint32 prime-list SHA-256 76f37eb58a4ca6daf73a49a8c174ed0c05772ef59b3c95caa4df88e16f8bb22d. Independent aggregation reproduced the complete mod-10 and mod-3 transition matrices and the uniform chi-square values exactly. The published logarithmic-integral value in the source package was incorrect: Lemke Oliver–Soundararajan define li as the integral from 2 to x, which at 50,000,000 is 3001556.381537921..., not 3001562.6973931813. Re-evaluating their displayed Conjecture 1.1 with the correct convention gives diagonal/symmetrised predictions 138333.30996 and 408037.19028 for modulus 10, and 673892.43658 and 1653771.50838 for modulus 3. The repaired RESULT and stats file use those values; the collapsed chi-square values remain 6365.6 and 1815.7 when rounded to one decimal.

## Originality: PASS

Best-of-knowledge comparison found prior residue-transition data and the general conjectural asymptotics, but not this exact cutoff matrix. Lemke Oliver–Soundararajan tabulate mod-3 pairs among the first million primes, mod-10 pairs among the first hundred million primes, and later comparisons at much larger cutoffs; their general formulas do not imply the exact finite 50,000,000 matrix. Resultary returned this record as the exact SCOPE hit. The repaired claim explicitly treats the Hardy–Littlewood formulas as prior work and claims originality only for the exact finite benchmark and its evaluated comparison.

## Scientific value: PASS

An exact, byte-replayable transition matrix at a natural intermediate cutoff supplies a reproducible finite benchmark for a well-studied bias phenomenon and quantifies how much of the uniform discrepancy is captured by the established conjectural secondary terms. This is a motivated finite invariant rather than an arbitrary slice.

## Limitations and residual risks

- The original package's logarithmic-integral numerical value was wrong; the accepted finding is the repaired version with the corrected convention and derived predictions.
- The exact census is finite and makes no persistence or asymptotic theorem claim.
- The Hardy–Littlewood comparison is conjectural prior work applied to the finite data.

## Sources inspected

- Lemke Oliver and Soundararajan, `Unexpected biases in the distribution of consecutive primes`, arXiv:1603.03720.
- The assigned package's RESULT.md, counts.json, stats.json, and verify.py.

This file records a mathematical audit of the scientific claim. It is not an expert attestation or a statement about any separate verification channel.
