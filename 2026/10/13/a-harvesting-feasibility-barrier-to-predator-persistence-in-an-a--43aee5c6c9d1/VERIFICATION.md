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

Run `python verify.py` from the extracted package directory with Python 3. The standard-library exact-rational checker prints `VERIFY_OK` if all stated witness identities hold. Its checks include feasibility, the two distinct positive unharvested equilibria, the source case-(1) inequalities, the positive uniform mortality gap, and the nonrestocking impulses.

The proof of absence of **all** positive periodic orbits is analytic: \(x\le h_l/\eta\) on every flow segment implies \(\dot y/y\le-\delta\); impulses multiply by \(1-p_2E_l<1\); uniform reset gaps exclude infinitely many events in finite time. The finite checker is not an exhaustive trajectory proof. The existence and stability of nontrivial periodic orbits beyond the stated strict decay regime and the case of positive predator restocking remain unresolved here.
