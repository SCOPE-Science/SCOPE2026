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

# Reproducibility and scope

Run `python3 verification_code.py` with Python 3.10+ and only its standard library. The included `verification_output.txt` was recorded from a successful execution of that exact code. It reports 595 connected labelled graph instances, 578,628 bounded candidate configurations, 48 unicyclic constructions, eight book-graph energy distributions, and 1,380 additional constructive state checks. The code independently compares direct three-step microscopic trajectories against the phase-convolution coefficient formula, verifies the two contiguous energy bands and reciprocity, and tests a unicyclic closed form. Exhaustive bounded-configuration tests are exhaustive only for the listed graph instances; they do not certify the infinite graph-family theorem. The theorem's general quantifiers are instead justified by the displayed algebraic and combinatorial proof in `RESULT.md`.

The accepted mathematical statement is restricted to primitive temporal three-cycles, standard nonnegative integer parallel chip-firing on finite connected simple graphs, and enumeration by conserved chip total. Existing general phase constructions and period-existence results are acknowledged; no claim of independent review is made.
