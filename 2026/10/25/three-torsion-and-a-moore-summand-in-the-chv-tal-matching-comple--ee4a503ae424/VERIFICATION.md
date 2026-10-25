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

# Reproducible verification

Use Python 3.10 or newer and run `python3 verify.py`. The source embeds the complete graph edge list and deterministic face-poset matching procedure; it does not download data, invoke optional libraries, or require remote services. The captured `verify_output.txt` comes from executing that exact file.

The verifier independently reconstructs all matching faces, checks 24 edges and graph regularity/triangle-freeness, counts face incidences and matched/critical faces, proves matching acyclicity by exhausting all 2835 Hasse vertices, recomputes the signed 34-by-6 Morse boundary, computes 5-by-5 and 6-by-6 determinants with exact integer arithmetic, checks its ranks modulo 2, 3 and 5, and computes boundary ranks directly on the raw complex over fields with 2, 3, 5 elements. The 5-by-5 determinant -1 and 6-by-6 determinant 3 together with rank five modulo three prove integral invariant factors (1,1,1,1,1,3). Forman's discrete Morse equivalence and the homotopy classification in `RESULT.md` are mathematical deductions from these checked finite data.

Limits: The script tests this one fully specified finite graph and does not itself confirm any external literature's uniqueness or provide independent scientific certification. The original Chvátal note's full text could not be inspected. The independent audit status remains not performed.
