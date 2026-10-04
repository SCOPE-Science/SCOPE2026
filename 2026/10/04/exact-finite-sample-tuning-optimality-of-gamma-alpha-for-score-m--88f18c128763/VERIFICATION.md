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

The finite-sample argument uses the exact SCoRE-MDR decision characterization from Bai and Jin.

For \(\gamma\le\alpha\), the decision is \(\mathbf{1}\{Q\le\gamma\}\), hence it is contained in the \(\gamma=\alpha\) decision.

For \(\gamma>\alpha\), selection additionally requires every candidate empirical-risk value to avoid \((\alpha,\gamma]\). At the admissible choice \(t=s(X_{n+1})\), \(\ell=1\), that candidate equals \(Q\). Therefore selection implies \(Q\le\alpha\), which is exactly sufficient for selection at \(\gamma=\alpha\).

The same substitution applies to the weighted characterization with \(Q_w\).

`artifacts/verify.py` checks the logical implications on deterministic random finite samples and constructs strict witnesses for \(\gamma<\alpha\) and \(\gamma>\alpha\). The script prints `VERIFY_OK` when all checks pass.

The computation does not establish validity of SCoRE itself; that validity is supplied by the cited source. It verifies only the finite-sample ordering and strictness constructions claimed here.
