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

# Executable verification and limits

Run `python3 verify.py` using Python 3.8 or newer; no external dependencies are needed. This enumerates all possible vertex subsets for every graph with \(n=4,5,6,7,8\), compares the induced-degree criterion with connected-component breadth-first search, constructs all matched and unmatched cells using the explicit pivot orders, constructs all directed Hasse covering relations, and verifies acyclicity by complete Kahn topological sorting. Each reported critical dimension/multiplicity is checked against the independently specified expected table. The exact successful output is preserved in `verification_output.txt`.

The completed verification enumerates \(9,119\) nonempty faces and \(4,533\) matching pairs over \(42,798\) Hasse arrows, and reports `VERIFY_OK`. This finite exhaustive calculation is a proof certificate for the explicitly stated finite list when interpreted with the usual discrete-Morse theorem. It does not prove any conjectured classification for other values of \(n\), nor substitute for independent scientific review.
