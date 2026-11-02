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

The proof checks the copula construction, almost-everywhere derivative identity, an exact repeated least-concave-majorant lemma, reflection of the predictor, and the Frechet uniform bound. No finite calculation substitutes for the all-copula theorem.

Reproduce the checks by running `python3 verify.py` and comparing the output with `verification_output.txt`. This uses only Python standard-library exact fractions. Every centered integer step profile of lengths two through six over the alphabet `[-2,-1,0,1,2]` is checked at replicate counts two, three, and five. Closed-form FGM and comonotone cases check the endpoint laws. The 13,796 assertions completed successfully.

The checker does not establish global originality or validate the continuum lemma independently. The published projection theorem and both comparisons are identified by URL in `RESULT.md`. Independent mathematical and bibliographic audit has not been performed.
