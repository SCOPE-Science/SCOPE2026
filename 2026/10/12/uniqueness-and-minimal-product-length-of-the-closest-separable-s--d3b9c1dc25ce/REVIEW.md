# Scientific self-review: interior one-zero Dicke edge

## Correctness
The original RESULT.md proof used the false inequality
\[\prod_j(1+|x_j|^2)\ge(1+\tfrac1n\sum_j|x_j|^2)^n.\]
It has been replaced by a complete correct proof. If \(u=n^{-1}\sum_j r_j\) is the mean probability of local zero outcomes of a product state, the Dicke zero overlap is at most \((1-u)^n\) by arithmetic-geometric mean, and the Dicke one-zero overlap is at most \(nu(1-u)^{n-1}\) by triangle, Cauchy--Schwarz and Maclaurin's inequality. The witness expectation thus has a uniquely maximizing common local modulus \(u=p\), and equality forces common phase. Vector-state logarithmic Jensen and weighted arithmetic-geometric mean establish global relative-entropy optimality; saturation and Fourier-moment annihilation force every minimizing density operator to equal the original phase-twirled candidate. Rank \(n+1\) and an \((n+1)\)-point roots-of-unity ensemble give the exact minimum number of pure-product terms. All statements hold for integers \(n\ge2\) and \(0<s<1\), not by extrapolation from finite numerical checks.

## Originality
Wei's 2008 symmetric-state theorem proves the optimum value and constructs the phase average and supplies the classical Dicke overlap bound. Those are not claimed new. The equality-orbit rigidity, uniqueness for this rank-two mixed state and exact minimum pure-product length are the additional findings. Friedland--Gour full-rank uniqueness does not imply the rank-deficient case. Possible unindexed equivalent proofs remain a bibliographic limitation.

## Mathematical value and scope
Uniqueness of a closest separable optimizer in a rank-deficient entangled family is a nonautomatic structural problem. The exact minimum pure-product ensemble length is a natural preparation invariant. The result does not address endpoints, more general mixtures, or uniqueness of the phase ensemble itself.

## Verification and integrity
The earlier reversed arithmetic-geometric mean step must not be used; only the fully corrected RESULT.md supplies the final proof. The accompanying finite verifier checks formulas and roots of unity but does not prove the universal quantifiers. No formal-machine proof or external expert attestation is claimed.
