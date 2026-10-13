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

# Reproduction and boundaries

Run `python verify.py` with a standard Python 3 interpreter and no external dependencies. Expected final line: `VERIFY_OK`. The checker enumerates 2,849 small formulas across all 16 two-variable teams (45,584 formula-team instances), then uses a fixed-seed collection of 4,800 three-variable instances. It compares brute-force split semantics with the guarded Boolean normal form and tests the canonical greatest satisfying subteam by enumerating every subteam. A successful exit is finite regression evidence.

The universal result is proved by structural induction in RESULT.md; no enumeration of finite examples can replace that proof. The logspace upper bound requires a sequential read-only input scanner, syntax offsets and established logarithmic-space Boolean formula evaluation. No code-level complexity proof, L-hardness, strict split, modal operators, or exhaustive all-size enumeration is claimed.

The accessible full text of arXiv:2510.08122 was compared against the proof and the prior polynomial-time algorithm. arXiv:2503.21850 was reviewed through abstract/bibliographic information only; this is a material residual literature risk. Independent audit has not occurred.
