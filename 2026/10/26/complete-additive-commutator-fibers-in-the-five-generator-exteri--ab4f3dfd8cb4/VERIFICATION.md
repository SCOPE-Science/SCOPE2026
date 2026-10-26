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

Run `python3 verify.py` with the Python standard library. It prints `VERIFY_OK_EXTERIOR5_COMMUTATOR_FIBERS` only after the checks complete.

The checker enumerates all \(3^{10}\) ordered linear-input pairs over \(\mathbb F_3\); constructs a literal exterior multiplication table; determines the linear span of fourth-degree outputs; computes representative fiber cardinalities by rank-nullity; and verifies them against the formula. It also examines \(18750\) selected pairs over \(\mathbb F_5\), constructs two hundred fifty random complete thirty-two-coordinate pairs in each tested prime field, and compares literal associative commutators with the degree-two/four decomposition. The output-mass identity is evaluated at four field orders, including nine as a polynomial check.

These computations independently test normalization, signs, exceptional targets, and fiber weights in finite cases. They neither exhaust all \(\mathbb F_5\) inputs nor independently prove the formula for every odd field. The algebraic proof is in RESULT.md. No independent audit has been performed.
