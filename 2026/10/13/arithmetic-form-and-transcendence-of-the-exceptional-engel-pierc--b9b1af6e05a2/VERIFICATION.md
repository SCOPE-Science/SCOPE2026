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

The proof is symbolic and applies to every admissible eventually consecutive Pierce tail. The included `verify.py` is a finite regression check only.

It verifies the exact two-term recurrence and derangement closed form for \(1\le m\le100\), compares the closed form with twenty defining alternating tail series under the rigorous alternating first-omitted-term bound, and checks seven finite-prefix gluings. It also checks that the \(e^{-1}\)-coefficient is nonzero in every recurrence case.

Replay command: `python verify.py`

Expected output:
`VERIFY_OK recurrence_cases=100 tail_cases=20 prefix_cases=7 max_error_lt_alternating_bound=1 nonzero_e_coeff=1`

The finite checks do not establish transcendence or the all-parameter recurrence; those follow from the proof in `RESULT.md` and the classical transcendence of \(e\).
