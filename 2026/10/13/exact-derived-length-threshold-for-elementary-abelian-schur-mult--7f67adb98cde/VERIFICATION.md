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

The theorem is proved symbolically in `RESULT.md`. The abelian lower bound uses the exact direct-product formula for Schur multipliers of finite abelian groups, and the metabelian upper bound uses the elementary-abelian construction in arXiv:2610.01312v1. The exceptional target \(C_2^2\) is covered by the source's separate cyclic action of order \(5\).

The packaged checker `verify_triangular_multiplier.py` exhausts all exponent tuples \(1\le a_i\le4\) for \(1\le r\le7\), totaling \(21,844\) tuples. It reconstructs the multiplier exponents \(\min(a_i,a_j)\) and confirms that every elementary-abelian case has rank \(\binom{r}{2}\) and at most one exponent greater than \(1\). It also confirms the equivalent odd-square test for \(1\le k\le100\). The recorded output ends with `CHECK_OK`.

These finite checks are regression tests only. They do not establish the infinite classification and are not used to replace the symbolic proof.
