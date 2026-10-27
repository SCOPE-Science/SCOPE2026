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

Run `python3 verify.py` in the same directory as the scientific documents. Only the standard Python library is required. In the completed package this program was executed and printed a PASS confirmation.

The program enumerates all eight candidate parent choices and independently tests whether every non-root vertex reaches the root without cycling, obtaining precisely five rooted in-arborescences. It determines the path and lowest-common-ancestor events on the accepted trees, uses exact rational arithmetic on seventeen values of the positive parameter, checks the closed probability and quotient identities, checks strong connectivity of the ambient digraph, and checks the witness quotient \(593/306\) at \(z=1/8\).

The proof's universal assertions are not extrapolated from seventeen samples: they follow from the complete symbolic enumeration of the fixed five-tree family for arbitrary \(z>0\), followed by exact polynomial algebra and a one-variable limit. The uniqueness of the positive threshold follows from strict derivative negativity of \(1-3z-4z^2-z^3\). The code does not establish novelty or replace independent mathematical assessment.
