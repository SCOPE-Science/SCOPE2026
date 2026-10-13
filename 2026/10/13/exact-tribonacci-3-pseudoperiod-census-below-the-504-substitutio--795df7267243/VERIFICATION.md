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

Run `python3 verify.py` beside `certificate.json` and `triples.tsv`.

The checker regenerates the Tribonacci prefix \(\sigma^{15}(0)\), whose length is \(10609\). For every \(1\le m\le504\), it extracts all observed length-\(m\) factors and verifies that their number is exactly the published total \(2m+1\). This certifies that the finite prefix contains every factor required by the proof.

It then exhaustively recomputes every triple \(1\le a<b<c<504\). The mismatch engine requires the intersection of the three mismatch-factor bitsets to be empty and must reproduce the stored `triples.tsv` list exactly. A separate direct-string pass then rechecks every one of the \(9352\) stored survivors against every relevant factor.

The cumulative substitution-scale counts and the first nine triples are recomputed from the verified list. The computation is exhaustive in the stated finite domain and makes no inference from sampling or timeout behavior.

Independent audit has not been performed.
