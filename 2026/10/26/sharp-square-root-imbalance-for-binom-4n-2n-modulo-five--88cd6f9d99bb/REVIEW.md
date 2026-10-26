# Scientific review: residue imbalance of even-index central binomial coefficients

## Correctness
The exact two-state base-five transducer follows directly from Lucas's theorem and the parity of the digits of an even integer. Its two weighted transition totals are explicitly diagonalizable, proving the exact \(5^L\)-block formulas. The finite-prefix discrepancy proof uses an operator norm of at most \(\sqrt2\) for a fixed-digit transition product, the normal matrix spectral norm \(\sqrt5\), and an aligned digital partition. The sharpness argument excludes a rational rotation angle using the nonintegral rational algebraic-integer candidate \(6/5\). The standalone verifier separately checks literal binomial coefficients, independent Lucas products, block formulas, and partial sums.

## Originality
The closest direct predecessor is the three-residue restriction \(\{0,1,4\}\) attributed to Maxim Vsemirnov in Yaqubi and Mirzavaziri (2017), Theorem 4.1, motivated by Guo and Krattenthaler's 2013 Conjecture 7.1. That support claim is explicitly not claimed. Berend and Harmse (1998) give weak distribution for the full middle-binomial sequence but not the even-index subsequence. Barat and Grabner (2001), whose complete open manuscript was inspected, give broader digital and matrix techniques for two-dimensional Pascal-triangle distributions, but not the present one-dimensional signed-block identity or sharp \(\sqrt X\) constant. The exact complex-eigenvalue signed count is thus not implied by the statements inspected. Residual risk: a prior specialization of the general digital machinery may have been published elsewhere; the 1998 PDF was not accessible during the comparison, although its precise theorem statement was available through a detailed scholarly summary.

## Mathematical value
The prior restriction to three residues leaves open their relative frequencies in this natural, published counterexample family. Exact counts determine the distribution at every base-five length, global square-root cancellation strengthens this to arbitrary prefixes, and the irrational spectral phase proves the exponent cannot be improved. The result distinguishes this exceptional even-index subsequence from the residue behavior of the full middle-binomial sequence. These are quantitative and sharp mathematical facts rather than a mere restatement of Lucas's theorem or a short tabulation.

## Limits
This is not a claim about other primes, prime powers, or all values of a general diagonal binomial polynomial. No independent mathematical audit has been performed; computations are finite cross-checks only.

Self-review: passed. Independent audit: not yet performed.
