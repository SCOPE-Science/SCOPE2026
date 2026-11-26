---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Pass for repairs/3/RESULT.md. The frozen odd-cycle sentence could be read as saying that the common determinant is independent of tau; that assertion is false. On C3 the determinant is 2(1-x)^2(1+x^2)/9 with x=exp(-3 tau). The replacement states the fixed-tau equality for all positive tau and retains the exact formula. It also specifies the Gram weighting versus Fisher information and clarifies which two-dimensional directions are being compared. Independently, the invertible temporal Vandermonde reduces rank to the Fourier sensor blocks: paired sines vanish exactly at the stated gcd obstructions, and the one-dimensional endpoints never lose rank. The real Fourier columns are orthonormal. Writing the sensor block matrix as an orthonormal range basis times an invertible square factor and using the Schur complement gives its Gram volume times det(H)^2 times the restriction of H^-1 tensor I_2 to the missing directions. Root-of-unity products give the volumes 2/n^(n-1) and 1/n^(n-2). For n even the two missing sensor directions have same-plane dot product zero for d odd and one for d even; the restricted matrix has off-diagonal entry zero or h_0m accordingly. Products of coefficients of the two endpoint Lagrange polynomials have one common nonzero sign since the nodes are positive. The principal minor is positive, so even observable placements strictly lose, and d=1 is always admissible. Independent exact rational kernel constructions at tau=log(2) and twice that on C3 and C6 corroborated both formulas, the C3 parameter dependence, and 0=det(W_3)<det(W_2)<det(W_1) on C6. The frozen integer and mpmath scripts and outputs were inspected, not executed; their reported finite tests do not prove the formulas or tau independence.

## originality

PASS

Pass only for the repaired scope of contribution: the full even-cycle untreated trajectory determinant at m+1 samples and the strict parity gap. The odd branch is explicitly a benchmark in the replacement because there is an exact indexed specialization, regardless of how relative priority is interpreted. The known qualitative rank comparison is also not claimed as the new determinant result.

## value

PASS

The extra sample can restore observability without restoring D-optimality. An exact finite-horizon determinant and strict ratio distinguish designs that the rank criterion cannot distinguish and isolate the constant/Nyquist coupling as the cause. This remains useful without claiming novelty for the odd benchmark or guaranteeing performance for other horizons or other conditioning criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
