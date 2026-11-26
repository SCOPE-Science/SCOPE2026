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

For fixed α>−1/2 and c>0 the Bessel series gives a self-adjoint trace-norm sum of rank-one terms with coefficients c^(α+1/2+2j)(−1)^j/[2^(α+2j) j! Γ(j+α+1)]. For a fixed wedge degree m the trace norms are bounded by products of the individual trace norms, giving a summable bound after removing the leading c-power on 0<c≤1. The unique minimal sum of indices is 0+…+(m−1); the remaining scaled exterior-power sum vanishes in trace norm. Its leading operator norm gives the product of the largest m singular values without any assumption about the signs of Hankel eigenvalues; division by the preceding positive product isolates the n-th singular value. I independently evaluated the Gram determinant quotient by the Cauchy determinant with entries 1/[2(α+i+j+1)]: it is (n!)²/[2(α+2n+1) times the square of product_(j=1)^n(α+n+j)], agreeing with the monic shifted-Jacobi value including the Lebesgue factor 1/2. Q=cH² multiplies each squared singular value by c, giving exponent 4n+2α+2 and the claimed Gamma/binomial coefficient; the adjacent-mode ratio follows from strict positivity of both leading coefficients. Replay: python /workspace/checks/2.py (mpmath), an independent 16-node Gauss–Jacobi Nyström calculation evaluating the Bessel kernel directly, checks concentration-eigenvalue ratios at c=0.01 for n=0,…,3 and α=−0.49,0,0.5,1.75 (all ratios within 0.000013 of one). That computation is corroboration, not the proof. The frozen supporting notes and check.py were inspected, not executed. No uniformity in order, index or bandwidth is asserted.

## originality

PASS

On the inspected primary and indexed evidence, the supported distinct claim is the exact fixed-order, fixed-index small-bandwidth concentration coefficient in the stated normalization, not the classical finite Hankel operator, Jacobi identities, or general index-decay estimates. Slepian IV remains a material unresolved historical-priority comparison after reasonable open-copy attempts. This is a best-of-current-knowledge verdict, not clearance against that text or a proof of absence.

## value

PASS

For a classical concentration operator, the normalization-dependent leading coefficient for every fixed mode supplies precise relative suppression and conditioning information near zero bandwidth. The nth exponent and coefficient distinguish consecutive modes and quantify the low-bandwidth cost of retaining them. The all-fixed-index result requires controlling mode separation in a compact-operator limit, not just substituting a Bessel Taylor term or reporting a small numeric case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
