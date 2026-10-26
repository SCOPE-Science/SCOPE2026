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
# Reproducibility

The proof is supplied in `RESULT.md`. The standalone program `verify.py` uses only exact integers and rational fractions from Python's standard library. From the directory containing this document run `python3 verify.py`.

Actual tests performed: independently enumerate the \(12\) complete periods through \(m=12\); calculate \(900\) residue-pair covariances with \(1\le a,b\le30\); check \(1200\) Jordan divisor convolutions; and compare gcd-double-sum and Jordan-floor-sum variance expressions for \(126\) values of \(m\). The expected completion message is `VERIFY_OK full_periods=12 pair_covariances=900 jordan_divisor_convolutions=1200 large_m_checks=6 all_exact_rational=PASS`.

These finite tests do not establish the infinite theorem or its asymptotic coefficient; the complete proof addresses those claims. The first public source date is tied to the 2025-09-12 initial submission of arXiv:2509.10592. Priority beyond the inspected sources remains for independent examination.
