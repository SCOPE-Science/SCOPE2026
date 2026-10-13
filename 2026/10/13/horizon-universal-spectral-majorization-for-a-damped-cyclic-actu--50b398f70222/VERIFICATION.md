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
# Verification record

The general claims are established by the analytic arguments in `RESULT.md`; the standalone exact arithmetic script is a separate calculation within the same mathematical package, not a proof of universal quantifiers or any external audit.

Run `python cyclic_gramian_checker.py` with Python 3. It checks the direct finite/infinite sum and the factorization \(W_H=CD_HC^{\mathsf T}\); the phase-weight order; exact determinants, trace and inverse-trace inequalities; and a three-state non-coordinate signed orthogonal orbit. On the included tests it prints `VERIFY_OK 108 exact-rational Gramian, determinant, and inverse-trace cases`.

The proof checks singular Gramians separately, establishes equality cases without relying on samples, and covers all dimensions \(n\ge2\), all \(0<r<1\), every integer horizon \(H\ge n\), and the infinite horizon. The code does not check general eigenvalue majorization symbolically; that follows analytically from the variational characterization of sums of largest eigenvalues. The tests also do not establish historical originality.

Independent audit has not been performed.
