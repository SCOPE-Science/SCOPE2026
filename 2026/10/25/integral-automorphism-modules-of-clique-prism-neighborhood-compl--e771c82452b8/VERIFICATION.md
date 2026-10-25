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

# Reproduction and limits

From the folder containing the included standalone `verify.py`, run `python3 verify.py` with Python 3 and its standard library. It enumerates all simplices of the Lovász open-neighborhood complex of the clique prism for sizes \(n=5,6,7\), checks the two-part cover and the crown-graph intersection, and independently computes mod-two homology at sizes five and six. For each automorphism of the five- and six-index prisms, and ten automorphisms of the seven-index prism, it computes the reduced Lefschetz number by signed fixed simplices and compares to the separately derived character formula. The output ends in `VERIFY_OK` after 1690 signed character comparisons.

The infinite-family integral theorem is proved by the chain-level connecting morphism of integral Mayer–Vietoris and graph cycle-lattice identification; finite mod-two computations and Lefschetz tests cannot establish it. No external audit, formal verification, or full survey of all mathematical literature has been performed.
