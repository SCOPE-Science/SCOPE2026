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

The proof is given in `RESULT.md`. Run `python verifier.py` in the same directory as `certificate.json`, and compare its exact one-line JSON output to `certificate.json`. It enumerates every binary incidence matrix with no zero row/column for all two-guild sizes \(r,c\ge2\) and \(r+c\le8\), modulo sorted row masks, and groups by degree multisets for both guilds. Integer polynomial comparisons are divided exactly by endpoint factors \(q\) and \(1-q\), so a reduced list of strictly positive polynomials proves the finite exclusion for the whole open interval \(0<q<1\).

The witness is also checked directly by enumerating all \(32\) configurations of five extinct or surviving pollinators at exact probabilities \(1/5,1/4,1/2,3/4,4/5\). Those finite witness checks are not an infinite proof: the displayed variance factorization is an exact algebraic identity for every parameter. The certificate covers all smaller graphs; it does not address heterogeneous survival, repeated interaction weights, or ecological cascades.
