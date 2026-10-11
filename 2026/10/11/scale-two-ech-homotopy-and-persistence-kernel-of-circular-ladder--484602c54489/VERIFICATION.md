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

# Reproducibility and limits
Run `python3 verify_prism.py` in a directory containing the embedded script. The script uses only Python's standard library, explicitly enumerates all closed vertex neighborhoods of the circular ladder, checks every proposed elementary collapse has exactly one maximal coface, and reconstructs the exact residual union of tetrahedral boundaries. It also independently computes mod-two homology via boundary-column elimination. The ten tested orders are \(n=5,6,7,8,9,10,12,16,20,30\); successful replay prints `VERIFY_OK`. This is a finite audit of computation and definitions, not proof of the universal quantifier. The all-parameter combinatorial and integral arguments appear in `RESULT.md`; in particular the map kernel is established by an integral cycle-lattice basis, not inferred from mod-two ranks.
