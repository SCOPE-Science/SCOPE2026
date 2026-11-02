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

**Analytic checks.** Multiplying the displayed block matrices verifies the bracket. Fixing one mixed component turns every remaining commuting component into a scalar multiple; no exceptional characteristic is excluded. The affine parameter count divides by the free multiplicative scalar action and attaches independently free central blocks. Geometric components follow from the standard irreducibility and dimension of the rank-one determinantal cone. The maximal linear abelian subalgebras follow by centralizer classification.

**Reproducibility.** Run `python3 verify_thin_middle.py` using the exact companion file. It enumerates all noncentral tuples in 13 cases over two prime fields and an explicit degree-two binary extension, compares commutativity against the predicted union and exact count, then enumerates all linear subspaces and maximal abelian ones in two cases. A successful execution prints `THIN_MIDDLE_COMMUTING_GEOMETRY_OK 13 2`. The checker is a finite corroboration, not a substitute for the universal proof.

**Limits.** Only reduced components are classified. The group statement counts commuting tuples, not conjugacy classes; the subgroup statement is for \(k\)-linear Lie subalgebras. Publication priority and independent validation are not certified.
