---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and limits

Run `python3 verify.py` using standard Python 3. The program enumerates nonempty voter groups and all their nonempty commonly approved sets using exact rational affordability, then evaluates reciprocal JR and EJR separately on each committee. Expected output: `EXACT_OK exhaustive=16551 sampled=240 sharp=9 separation=1`.

The exhaustive panel varies all nonempty support sets and qualities from `{1/3, 3/4, 1}` for `(n,m)=(2,3),(3,3),(2,4)`. The sampled panel uses a fixed seed, electorates of four through seven voters and two through six candidates. The additional exact cases cover the sharpness construction for two through ten voters and a profile where the two axioms have different feasible sets. The checks include the equality of optimum qualities, preservation of either member of an optimal rJR pair in some optimal rEJR pair, the one-replacement rEJR quality guarantee from every unrestricted optimum pair, and the approval-intersection criterion when a two-seat demand exists. They do not prove the result beyond these finite panels; the proof in `RESULT.md` establishes the claims for arbitrary allowed qualities and sizes.
