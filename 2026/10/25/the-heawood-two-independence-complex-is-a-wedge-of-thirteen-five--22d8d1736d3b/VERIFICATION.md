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
# Verification and exact limits

Execute `python3 verify_heawood.py` with Python 3.8 or later and compare stdout exactly with `verification_output.txt`. It uses only the Python standard library and makes no network calls. Its graph definition is seven Fano triples and fourteenth-bit masks, with independent local-degree and connected-component definitions of the face condition. It verifies the unique-line design property, every admissible face, full f-vector, one-to-one matching, every critical mask, and acyclicity through a topological sort of **all** directed face-cover relations. A separate reduced mod-two simplicial boundary calculation supplies cross-checks.

The exact Morse certificate has 2,256 nonempty faces, 1,121 matched nonempty pairs, and exactly one unmatched vertex and thirteen unmatched dimension-five simplices. The full directed Hasse graph has 10,150 arrows and is acyclic. These counts and the standard discrete-Morse theorem constitute a complete integral finite homotopy argument; the mod-two Betti calculation alone would not suffice.

The result says nothing about all incidence graphs or about integral group actions. Scientific novelty is based on explicit comparisons with accessible literature and public records; a failed query cannot establish global priority. No independent external audit was performed.
