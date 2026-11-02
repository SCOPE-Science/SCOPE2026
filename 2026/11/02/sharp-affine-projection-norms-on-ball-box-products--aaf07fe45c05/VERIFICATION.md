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

# Verification of the affine-projection norm theorem

The proof is analytic. All sampled comparisons are supplementary.

`python3 verification.py` checks the finite Irwin–Hall positive-part expression against separately integrated absolute kernels for \(1\le d\le6\) and \(0\le k\le3\), an exact rational-polynomial evaluation for \(d\in\{1,3,5,7\}\) and \(0\le k\le5\), the exact circular-cylinder value \(17/9+3\sqrt3/(4\pi)\), and four illustrative monotonicity comparisons. The program completed with a passing summary: 24 raw-integral comparisons, 24 rational comparisons, one symbolic benchmark, and four numerical sanity checks.

The program does not prove strictness for arbitrary parameters, the infinite-dimensional asymptotic, or historical priority. Those are handled by the printed arguments and literature comparisons. The input extremizer is an ordinary kernel-sign function; no numerical search is necessary to establish attainment. Independent audit: not performed.
