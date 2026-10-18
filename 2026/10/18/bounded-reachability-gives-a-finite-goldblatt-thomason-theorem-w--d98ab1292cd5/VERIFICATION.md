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

Execute `python3 verify.py` with a standard Python 3 interpreter. The checker enumerates all binary relations on one or two points and the values \(h=0,1,2\), tests frame-radius membership, and compares two independently implemented finite conditions: whether a rooted surjective bounded morphism exists, and whether a root diagram has a satisfying valuation. There are exactly 2,412 comparisons. The run prints `BOUNDED_MODAL_VERIFY_OK 2412`.

The theorem's general validity is established by the proof's path-lifting, finite-depth diagram, and closure argument; enumeration only corroborates those steps for tiny carriers. The same checker also tests the terminal self-loop versus deadend witness for the sharpness boundary. No formal proof-assistant certificate or independent scientific audit is claimed.
