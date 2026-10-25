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

# Reproducibility
Run `python3 verify.py` (Python standard library only). The program enumerates all loop-free unary directed edge relations whose simple undirected support is a forest for state counts one through four, including one-way and two-way arcs on each edge. It follows subset dynamics from the initial singleton state until repetition and checks that the eventual subset period divides two. Its tested counts are 1, 4, 37, and 586, and it terminates with `VERIFY_OK`.

This finite check is not a proof for arbitrary states. The infinite forest-parity classification and the one-hole exact optimum follow from the reversible two-step walk argument and explicit automata, fully stated in RESULT.md. No independent audit or validation was undertaken.
