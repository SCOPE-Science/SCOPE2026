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
# Reproducible exact checks

Execute `python3 verify_tight_cycle_dihedral.py` with Python 3 standard library only. The program independently enumerates noncover simplices and their signed fixed-face traces at each of 126 dihedral elements for \(6\le n\le12\); separately enumerates invariant independent subsets in the Alexander dual at each of 180 dihedral elements for \(6\le n\le14\). It checks the four-state transfer identities at 100 exponents and path lengths. The expected terminal string is `TIGHT_CYCLIC_NONCOVER_DIHEDRAL_CHECKS_OK 180 126`.

The infinite part is mathematical: the determinant identity \(\det(xI-M)=x(x-1)(x^2+1)\), the Cayley–Hamilton recurrence and the equivariant Alexander-duality sign formula, as detailed in RESULT.md. Finite enumerations alone do not establish any all-size assertion. Nonequivariant homology concentration is sourced to the full-text theorem of Kim and Kim rather than independently recomputed. No independent audit was performed.
