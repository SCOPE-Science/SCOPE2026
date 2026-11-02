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

Run `python3 VERIFY.py` from a directory containing the bundled file. The program constructs the friendship graph's hub-plus-matched-pair adjacency, generates configurations modulo precisely the wreath-product symmetries of peripheral pairs, and recursively tests whether some legal move reaches a stacked or cleared configuration. It checks all canonical configurations through mass \(4m\) for \(m=1,2,3,4,5\). The final mass-\(4m\) canonical counts are 9, 92, 759, 5265 and 31807; all are both stackable and clearable. It also checks that nonstackable witnesses occur at mass \(4m-1\). These are finite independent checks and do not imply the statement for arbitrary \(m\). The general argument is in `RESULT.md`, using only explicit local pebbling moves, elementary balance equations, and the published triangle-clearing lemma.
