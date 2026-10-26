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

Run `python verify.py` from this document's directory with the dependency specified in `requirements.txt`. The actual checker executable was run directly and printed:

`VERIFY_OK rational_strict_comparisons=147; grounded_exact_inversions=18; graph_cases=7; count_certificates=7`

The exact rational comparisons cover \(2\le q\le8\) and \(2\le d\le7\), checking all \(d-1\) adjacent Hamming-distance inequalities. Independent direct rational matrix inversions cover \((q,d)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)\), each for every leader-distance class, for 18 inverses. Seven finite antipodal pair counts also match \(q^d(q-1)^d/2\). `verification_output.txt` is a frozen textual copy of this actual output. These checks do not by themselves prove the universal assertions; the finite character decomposition, exact grounding identity and strict likelihood-ratio/covariance argument in `RESULT.md` do.

The independent-audit status in the exact JSON front matter denotes **not performed**, not a negative or positive external verdict. The claims apply only to unit-conductance Hamming graphs and two noise-free leaders; other dynamics are unproved.
