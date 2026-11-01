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

# Finite verification certificate

The standalone artifact `verify.py` uses the Python 3 standard library only. It constructs the one-deletion/at-most-one-substitution output balls in two different ways for every input at lengths \(3\) through \(9\), checks exact agreement, then constructs all pairwise compatibility edges and verifies each explicit codebook. Its exact maximum-clique routine uses a sound greedy-coloring upper bound and branches over every remaining choice. The upper bounds are logically exhaustive because a clique contains at most one vertex from each proper-coloring class, and every omitted branch is dominated by an existing witness.

The recorded result is provided verbatim in `verification_output.txt`, ending with `EXACT_CERTIFICATE_OK`. The maximum at length \(9\) is \(16\), with a concrete 16-word witness; the exhaustive program checks the corresponding upper bound. A separate exact graph-clique implementation independently gave matching sizes for lengths \(6\) through \(9\).

The completeness claim concerns only these finitely many lengths; it does not extrapolate to all binary lengths. The evidence is a finite mathematical derivation and a replayable enumeration, not an independent mathematical audit or a formal-proof-assistant certificate.
