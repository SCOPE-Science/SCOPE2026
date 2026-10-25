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

Run `python proper_colour_symmetry_checker.py` with Python 3 (standard library only). The executable recomputes every proper-colouring word for the prescribed small lengths and checks the exact Markov transition numerators, two-letter prefix/suffix counts, and cycle chromatic counts. It independently enumerates equality-signature classes of ordered endpoint-word pairs for ternary palette lengths two through six, verifying free six-member palette orbits and their numbers.

Observed execution output:

`PROPER_COLOUR_SYMMETRY_EXACT_OK 5090 69742 2046`

This is a finite regression check. The conclusion for arbitrary first-order sentences and unbounded length is established by the Markov-chain plus Hanf-locality argument in `RESULT.md`, not by enumerating a finite number of words. Hanf locality and its effective parameters are used as classical mathematical results. The actual run compared the standalone code extracted from the package with the code embedded here; its checks have not been independently validated.
