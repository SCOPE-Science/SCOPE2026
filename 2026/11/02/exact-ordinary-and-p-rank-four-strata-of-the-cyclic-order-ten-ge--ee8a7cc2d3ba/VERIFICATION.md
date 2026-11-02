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

The proof in `RESULT.md` covers every prime \(p=10n+1>13\) and every smooth parameter \(\lambda\) over an algebraic closure. It uses the Cartier extraction rule, coefficient-ratio identities, a Gauss differential-equation transformation, and a height/dimension argument for the fifth-root character decomposition of the Jacobian's \(p\)-divisible group.

The included `verify.py` requires only Python 3. Running `python3 verify.py` produces `VERIFY_OK`. It checks primes \(31,41,61,71,101\), constructs all three Cartier blocks exactly over the relevant prime field, tests their asserted polynomial factors and root square-freeness, tests the full-rank third block through its determinant polynomial, and verifies inversion symmetry and the parity of the exceptional parameter \(-1\). These checks are exact finite examples, not a proof of the infinite-family statement.

No independent audit, external certification, complete Newton-polygon determination, or historical-priority certification was performed.
