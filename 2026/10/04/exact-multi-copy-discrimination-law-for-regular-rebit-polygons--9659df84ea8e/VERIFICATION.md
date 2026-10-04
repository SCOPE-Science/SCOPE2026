---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification
The proof is analytic. The following checks were performed on the packaged statement.

1. The weighted Gram entry was expanded as a binomial Fourier sum, and cyclic characters were checked to coincide exactly when their binomial indices agree modulo \(N\). This gives the claimed spectrum without a rank or nonsingularity assumption.
2. The pure-GU success formula \(P=N^{-1}(\operatorname{tr}\sqrt G)^2\) was applied to the weighted Gram convention \(G_{ab}=N^{-1}\langle\psi_a|\psi_b\rangle^k\); the normalization \(\operatorname{tr}G=1\) agrees with \(\sum_r p_r=1\).
3. In the non-aliasing regime \(N>k\), each occupied residue contains one binomial index, reproducing the published \(N^{-1}2^{-k}(\sum_j\sqrt{\binom{k}{j}})^2\) formula.
4. The root-of-unity filter isolates the conjugate modes of modulus \(\cos(\pi/N)\). For \(N\ge4\), all remaining nonconstant modes have modulus at most \(|\cos(2\pi/N)|\le\cos(\pi/N)^3\); for \(N=3\) there are no further modes. This supports the stated remainder after the square-root expansion.
5. The projective-circle argument uses distinct lines modulo angle \(\pi\); equality in the minimum-gap bound forces all \(N\) gaps to be \(\pi/N\), so the exponent equality case is genuinely rigid.
6. `artifacts/verify.py` was executed from the extracted package. It checks representative Gram eigenvector equations directly against the residue sums and checks convergence of the normalized error toward the predicted coefficient \(1/2\).

The checker does not certify the universal theorem by enumeration, and no claim is made about finite-copy global optimality outside the regular polygon.
