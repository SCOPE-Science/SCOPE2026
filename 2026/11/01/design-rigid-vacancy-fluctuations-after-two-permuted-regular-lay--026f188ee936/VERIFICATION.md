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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 and its standard library. It deterministically checks all \(\binom73=35\) sample subsets in the seven-vertex example and all \(\binom{13}4=715\) sample subsets in the thirteen-vertex example, both before and after degree-preserving incidence switches. It verifies direct subset enumeration against the pair-overlap covariance identity, attainment by known projective planes, strict increase after a switch, and exact biclique-defect decompositions. A non-design nine-vertex example and several binomial identities are also tested.

Expected final line: `PASS 39 exact assertions`. File `verification_output.txt` records the actual output of this checker. The analytical proof of the full theorem and the infinite-prime-power asymptotic is contained in `RESULT.md`; finite computation does not certify it. No external independent audit has occurred.
