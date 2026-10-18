# Mathematical review

## Correctness — PASS

The quotient by squares for a product of \(r\) odd primes is exactly \((\mathbb F_2)^r\). Prime bases give Legendre-bit columns, and composite bases cannot add a new column-space direction. The combined conductor modulus \(M_t\) has precisely uniform Legendre sign patterns by quadratic reciprocity and the Chinese remainder theorem. In the range \(r\log(r+2)\le C\log\log X\), its size is at most a fixed power of \(\log X\), so Siegel--Walfisz controls the entire sign-vector law in total variation even after sampling \(r\) rows. The standard full-rank count then proves the stated formula and growing-rank limit. The proof does not infer an infinite result from the finite tests.

## Originality — PASS, subject to the stated risk

Bellotti (arXiv:2610.10177v1, full accessible HTML) studies the full least-generator cutoff and bounds its mean and almost-all size, not the explicit quadratic-quotient cutoff law across prime products. Fulman--Goldstein (arXiv:1211.0504, full readable preprint text) already supplies finite-field random-matrix rank distributions; that input is credited rather than reclaimed. Separate quadratic reciprocity and Siegel--Walfisz statements control characters in progressions, but no inspected source states the resulting growing-rank arithmetic coupling or this cutoff distribution. Searches for Legendre-symbol rank matrices, small-prime generators modulo squares, and squarefree-product character generation revealed no decisive covering theorem. **Residual risk:** the result may be implicit in an earlier unlocated synthesis of classical tools; absence from a search is not proof of uniqueness.

## Mathematical value — PASS

The first positive-prime cutoff removing all quadratic characters is a necessary and computable component of Bellotti's least-generator problem, not an arbitrary invariant. A complete law, including a sharp nontrivial \(0.288788\ldots\) minimum-rank fraction, a geometric-overshoot tail, and uniform validity while the number of prime factors grows, provides a precise benchmark for later study of higher-order character obstructions. No claim is made about the final \(G(n)\) distribution.

## Checks and limitations

The package contains `verify.py`, which completes 130 exact/finite checks and four prime-sample illustrations. Direct source inspection and published-record searches did not identify a stronger result that implies the complete arithmetic statement. The proof relies on classical prime number theory for the uniform arithmetic step. Independent expert validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
