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

# Reproducible checks

Run `python3 verify_insertion_linear.py` with Python 3.9 or newer; it needs no external packages. The exact output of the successful run is included in `verification_output.txt` and ends with `VERIFY_OK`. In particular, the checker verifies that there are precisely 788035 distinct length-nine rank-six reduced-row-echelon matrices representing distinct subspaces and that exactly 1786 satisfy every received-word list-size constraint. It also rejects all 43435 rank-seven length-nine subspaces and checks analogous counts for all shorter lengths. A separate forward insertion routine obtains each witness's parent multiplicities without reusing the inverse deletion masks.

The proof relies on completeness of the canonical RREF enumeration and exhaustive finite arithmetic. Code was executed from the included package content before scientific review; its output alone is not treated as an infinite theorem. No result is asserted beyond length nine. No independent audit or external formal verification has been carried out.
