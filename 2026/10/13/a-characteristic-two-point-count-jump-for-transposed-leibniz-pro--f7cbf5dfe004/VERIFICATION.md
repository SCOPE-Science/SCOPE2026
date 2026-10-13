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

# Verification of the finite-field parameter theorem

Run `python3 verify.py` from this extracted directory with Python 3.8 or later. Only the standard library is required. A completed run prints `VERIFY_OK` after (a) checking compatibility rank \(8\) over \(\mathbf F_2\) and rank \(13\) over \(\mathbf F_3\) for the eighteen symmetric structure coefficients, (b) testing complete table associativity/compatibility for every parameter tuple over \(\mathbf F_2\) and \(\mathbf F_3\), (c) counting all table solutions over \(\mathbf F_4\), \(\mathbf F_5\) and \(\mathbf F_7\), and (d) enumerating square-zero extension character/rank fibers over \(\mathbf F_2\), \(\mathbf F_4\), \(\mathbf F_8\) and \(\mathbf F_{16}\). The finite-field multiplication tables use irreducible binary polynomials of degrees \(1,2,3,4\), and the odd fields checked are prime.

The recorded check returned `VERIFY_OK`. Even-characteristic counts in increasing field size were \(108\), \(5872\), \(323520\), and \(18808576\); odd-characteristic counts over \(\mathbf F_3\), \(\mathbf F_5\), and \(\mathbf F_7\) were \(99\), \(725\), and \(2695\). The script checks computational consequences of the theorem but does not certify the all-fields algebraic reasoning. The proof uses a complete symbolic reduction and the determinantal/extension stratification independently of these experiments.

All comparisons with published work and any originality determination remain part of a self-review. No independent audit has been performed.
