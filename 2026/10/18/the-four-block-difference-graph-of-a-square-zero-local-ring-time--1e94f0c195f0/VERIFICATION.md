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

# Reproduction

Execute `python3 verify.py` using Python 3 with no external packages. Successful output concludes `VERIFY_OK 11 rings`. The program constructs 11 finite rings, enumerates all nonzero zero-divisors and all nonzero annihilator witnesses for both endpoints of every candidate edge, directly tests the weak-graph and ordinary-graph definitions, and compares their edge difference to the proposed four-block structure. It also checks vertex/edge counts, a sharp coloring, a sharp independent set and the twin-class partition.

The code handles explicit prime-field cases and two different square-zero local constructions, including characteristics \(2\) and \(4\). The analytic theorem includes arbitrary finite fields and arbitrary finite local rings with nonzero square-zero maximal ideal; the proof, not these test cases, supplies that coverage. The intrinsic graph-reconstruction step is symbolic and is backed by the quotient-path twin argument. No external or independent audit is claimed.
