# Exact consecutive-prime residue-pair census to 50,000,000 with corrected Lemke Oliver–Soundararajan comparison

## Scope and definitions

Let the primes be ordered increasingly. Count a consecutive pair when its second prime is at most 50,000,000. For modulus 10, retain reduced residues 1, 3, 7, 9; for modulus 3, retain residues 1, 2. The entries below are exact finite counts. Uniform chi-square uses the equal-cell expectation. The Hardy–Littlewood comparison evaluates Conjecture 1.1 of Lemke Oliver and Soundararajan with their convention

\[
\operatorname{li}(x)=\int_2^x \frac{dt}{\log t}.
\]

At 50,000,000 this is 3001556.3815379210215....

## Exact census

There are 3,001,134 primes at most 50,000,000.

For modulus 10, the residue marginals are 750340, 750395, 750394, 750003 for residues 1, 3, 7, 9 respectively. The 3,001,130 retained consecutive pairs form

| row / column | 1 | 3 | 7 | 9 |
|---|---:|---:|---:|---:|
| 1 | 131565 | 229515 | 234815 | 154444 |
| 3 | 176570 | 123047 | 216105 | 234672 |
| 7 | 192045 | 205685 | 122881 | 229783 |
| 9 | 250160 | 192147 | 176592 | 131104 |

The uniform expectation is 187570.625 per cell and the exact recomputed chi-square is 155166.04858436657. The four diagonal entries are the four smallest entries. The most suppressed cell is (7,7), with 122881, and the most enhanced is (9,1), with 250160.

For modulus 3, the retained 3,001,131 consecutive pairs form

| row / column | 1 | 2 |
|---|---:|---:|
| 1 | 655352 | 845128 |
| 2 | 845128 | 655523 |

The uniform expectation is 750282.75 and the exact recomputed chi-square is 47958.58682709952.

## Corrected Hardy–Littlewood comparison

Using the displayed formulas of Lemke Oliver and Soundararajan at the same cutoff, the corrected leading finite predictions are:

- modulus 10: diagonal prediction 138333.309962 per residue class and symmetrised off-diagonal prediction 408037.190282 per unordered residue pair;
- modulus 3: diagonal prediction 673892.436578 per residue class and symmetrised off-diagonal prediction 1653771.508382.

For modulus 10, the observed diagonal residuals are approximately -4.89%, -11.05%, -11.17%, and -5.23%. The six symmetrised off-diagonal residuals range from approximately -0.84% to +4.61%. The collapsed 10-bin chi-square against these predictions is 6365.58, compared with 105744.04 against the corresponding collapsed uniform model.

For modulus 3, the two diagonal residuals are approximately -2.75% and -2.73%, while the symmetrised off-diagonal count is approximately +2.21% above the prediction. The four-cell chi-square against these predictions is 1815.72, compared with 47958.59 against uniformity.

These are goodness-of-fit calculations for prior conjectural formulas, not a proof of those formulas.

## Independent finite verification

A fresh odd-only Eratosthenes sieve through 50,000,000 produced exactly 3,001,134 primes with last prime 49,999,991. Packing the resulting ordered primes as little-endian unsigned 32-bit integers gives SHA-256 `76f37eb58a4ca6daf73a49a8c174ed0c05772ef59b3c95caa4df88e16f8bb22d`, matching the committed archive identifier. Independent aggregation reproduced every matrix entry, marginal, pair total, uniform chi-square, and extremal cell above.

The corrected logarithmic-integral value and Hardy–Littlewood predictions were recomputed directly from the convention and formulas in the cited paper.

## Limitations

This is a single finite cutoff and makes no claim about persistence, limiting rates, or signs beyond it. The Hardy–Littlewood formulas are prior conjectural work, and the reported fit is descriptive only.

## Reference

R. J. Lemke Oliver and K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, arXiv:1603.03720.
