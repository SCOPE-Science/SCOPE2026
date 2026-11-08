---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read the complete RESULT.md, proof and check_determinantal.py in frozen tree. Reconstructed the additive-character proof: generating characters exist from the unique socle, the unit sum c_r(a)=q^r 1_{a=0}-q^{r-1}1_{a in pi^{r-1}}, and pairwise Fourier orthogonality yield the exact j-sum q^{k+2j} c_{k-j}(det(M/pi^j)). The endpoint j=d+2v-k+1 contributes -q^{2k-1} and lower terms cancel, giving precisely zero, negative, or positive frequency cases. Primitive rank-one determinant-zero lifts number (q-1)(q+1)^2 q^{3(r-1)}; valuation stratum summation yields the stated rank q^{4(k-floor(k/2))}+B_q sum_{j<floor(k/2)}q^{3k-2-2j}. Independent exhaustive modular character-sum calculations verified every Fourier frequency in Z/2, Z/4, Z/8, Z/3, Z/9; rank counts 16,160,1408,81,2673 respectively and exact predicted eigenvalue sets. No inference from these examples to all rings; analytic proof supplies universal assertion.

## originality

PASS

Specialized spectrum is distinguished from generic Frobenius-ring Fourier orthogonality, higher-dimensional rank partitions, invertible-matrix Gauss sums, and field-level determinant rank-one associations. Xu–Kan–Han (2025) rank-weight Fourier partitions are a related general formalism but inspected definitions/claims do not state this det-equals-zero convolution spectrum over every chain length; older local zeta treatments remain a possible equivalent specialization.

## value

PASS

Determinant-zero in a nonfield chain ring is substantially different from the singular/nonunit determinant set. Exact spectral support, surprising field invertibility versus exponential rank collapse in ring length, and uniformity across nonisomorphic chain rings give a natural sharp invariant with possible use in local additive matrix harmonic analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
