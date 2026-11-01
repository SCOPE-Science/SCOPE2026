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

Run `python3 verify_dyck_n3.py` with Python 3.10 or newer; it requires only the standard library. The checker enumerates admissible rational Dyck words from their defining prefix inequality and constructs faces from actual consecutive `DU` positions. For length three it checks vertices, edges, connected components, isolated vertices, and integral graph cycle ranks for ten parameter values. For lengths four through six it checks additional component cases; all computations terminate with assertions or print verified counts.

The proof of the infinite families is combinatorial and independent of the finite checks. No higher-length higher-homology computation or independent review is claimed.
