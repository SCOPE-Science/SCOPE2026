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

# Verification details

The complete proof is in `RESULT.md`. Run `python3 verify.py` from the directory containing the delivered files. A successful verification prints `VERIFY_OK` after computing all \(4^m\) input words for each \(1\le m\le10\), checking the distinct image size, verifying each output's deterministic-cycle multiplicity, confirming the entire source count via its inverse fibers, and comparing the independent matrix-power and recurrence calculations for every \(1\le m\le200\). For example, periods \(1,2,3,4,5\) yield image sizes \(4,10,40,134,464\), and the associated closed-path traces are \(4,12,40,136,464\).

The all-length proof uses the hidden binary states, the three-state subset automaton, and the exhaustive classification of extra singleton-state cycles. Finite checks are not a proof of arbitrary-period completeness. Neither third-party audit nor external formal certification has occurred. The published noncyclic automaton and its Perron eigenvalue are not represented as new.
