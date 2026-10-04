# Same-model review

## Correctness
PASS. The identity \(C_h=2(I-hQ/2)^{-1}-I\) is exact. The resolvent is a nonnegative stochastic matrix because \(I-hQ/2\) is a nonsingular \(M\)-matrix and fixes \(\mathbf 1\). Hence only diagonal entries can violate positivity. Reversibility symmetrizes the generator and expresses each diagonal resolvent entry as a positive mixture of strictly decreasing scalar resolvents, proving a unique crossing and the spectral bounds. The finite-state resolvent limit gives the unconditional classification. Exact-rational replay verifies the matrix identities and the two closed families.

## Originality
PASS with explicit residual risk. General Runge–Kutta positivity, the trapezoidal rule's problem-class positivity radius \(2\), and the Cayley identity \(I+C(A)=2(I+A)^{-1}\) are all prior work and are excluded from the novelty claim. Targeted searches of the current research ledger, published-finding corpus, and primary literature under Crank–Nicolson, trapezoidal, Cayley, Markov-generator, reversible-chain, return-resolvent, and \(1/2\)-diagonal aliases did not locate the fixed-generator theorem: exact reduction to return diagonals together with the reversible single-threshold spectral law, unconditional classification, and closed chain-family thresholds. The principal residual risk is specialized stochastic-matrix literature using different terminology.

## Value
PASS. Crank–Nicolson is a standard second-order, \(A\)-stable integrator, but a negative entry in a Markov transition approximation is a direct probabilistic failure. The result gives a generator-specific exact diagnostic rather than a generic sufficient step restriction, explains the failure through resolvent return probabilities, identifies the only nontrivial irreducible chain with unconditional positivity, and supplies sharp spectral bounds and closed thresholds useful for step selection and regression tests.

Same-model review: passed. Independent audit: not yet performed.
