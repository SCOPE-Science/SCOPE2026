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

# Verification of the explicit orbit construction

The verification is a pen-and-paper audit, not an independent external audit and not a computer-assisted certificate. Define \(T_0=0\), \(L_s=(T_{s-1}+1)^2\), \(R_s=(T_{s-1}+L_s+1)^2\), and \(T_s=T_{s-1}+L_s+R_s\). At each stage exactly one sequence has symbol one on the active block; all sequences have zero on the reset block. Therefore, for any fixed \(n\), the sum of the \(k\) empirical mean distances to \(0^\infty\) is at most one, yielding error at most \(1/k\) after dividing by \(k\). At the end of a dominant active block, exactly one empirical measure tends to \(\delta_{1^\infty}\) and the other \(k-1\) approach \(\delta_{0^\infty}\). The triangle inequality forces mean error at least \(1/k\) against any single prototype, so the strict one-prototype threshold is exact.

For every fixed word-window length \(h\), only \(O(hs)\) of the first \(n\) windows can cross a symbol change when \(T_{s-1}\le n<T_s\). Since \(n\ge T_{s-1}\) and \(s/T_{s-1}\to0\), the fraction tends to zero. A uniform metric tail at most \(2^{-h}\) proves \(W_1(e_n(x^{(j)}),\nu_{p_{j,n}})\to0\). During infinitely many stages for each index, the active block ends with \(p_{j,n}\to1\); resets end with \(p_{j,n}\to0\). Because consecutive empirical frequencies differ by at most \(1/(n+1)\), every intermediate limit occurs. Exact Wasserstein distance between the two extremal Dirac mixtures is the difference of weights, so the minimax radius of \(N\) prototypes is exactly \(1/(2N)\) by interval covering.

No claim of nonzero numerical precision, external code execution, or machine-checked infinite proof is made. The public documents all refer to the same finite-support, noninvariant family and the strict-error convention. The exact ordinary emergence counts **with two or more prototypes** below or at \(\varepsilon=1/k\) remain unproved and are not part of the finding.
