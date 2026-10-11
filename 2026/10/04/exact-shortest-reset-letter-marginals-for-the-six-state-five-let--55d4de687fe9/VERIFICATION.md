---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

I independently reconstructed all five transitions and the complete 63-state nonempty power automaton. The singleton distance is 20 with unique target 3. Re-running weighted shortest-path dynamic programs separately for each letter reproduces the claimed total and all marginal coefficient arrays; the \(b\)-histogram is concentrated at degree zero. Thus the statements are exhaustive consequences of the finite shortest-path DAG.

## originality

PASS

The defining paper proves the general reset threshold and shows existence of a shortest word using a restricted alphabet, but it does not characterize every shortest word or give these marginals. The general shortest-reset algorithm literature likewise does not state the six-state all-shortest census. Resultary search found no exact match.

## value

PASS

The six-state case is the endpoint of the defining fixed-alphabet small-state investigation, and the result upgrades a reset threshold to the full one-letter composition statistics of all optimal controls. The universal absence of \(b\) from every shortest word is a structural statement not supplied by the existence proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
