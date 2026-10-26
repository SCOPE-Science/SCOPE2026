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
Run `python3 verify_squarezero_semisimple.py` with Python 3 standard library. The script directly enumerates upper-triangular matrices over prime fields and a four-element extension field, tests the quartic identity, evaluates the canonical idempotent, checks its commutation and square-zero remainder, and obtains separately the ranks on the zero and one generalized eigenspaces. It compares the exact joint histograms with the theorem's recurrence. The tests cover \((n,q)\) equal to \((1,2),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(3,4),(2,5)\).

The seven additional numeric recurrence sweeps use integer substitutions \(q\in\{2,3,4,5,7,9,11\}\) and \(0\leq n<25\); these sweeps are arithmetic checks rather than exhaustive extension-field matrix enumerations. Over \(\mathbb F_4\) the script uses the irreducible polynomial \(t^2+t+1\). The terminal success marker is `VERIFY_OK_TWO_EIGENVALUE_SQUAREZERO_JORDAN`.

The proof's unbounded claims rest on the canonical polynomial splitting, idempotent conjugation and last-column recurrence, not the finite runs. The assessment reported here is not independent audit.
