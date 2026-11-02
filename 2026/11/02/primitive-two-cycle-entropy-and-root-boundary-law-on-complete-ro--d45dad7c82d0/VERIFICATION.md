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

# Reproducibility and verification

Execute `python3 verify.py` using the Python standard library. Its deterministic expected end marker is `FULL_TREE_CHIP_CYCLES_VERIFY_OK`.

The checker uses two structurally distinct finite approaches: (1) enumerate all edge subsets of explicit breadth-first rooted trees, discarding those that leave a vertex isolated, and sum the products of the selected-edge degrees; and (2) directly update each chip configuration in the finite confined box and check the definition of a primitive two-cycle. The first method also checks the predicted complete root-edge histogram. Integer-recursion results must agree exactly with all enumerated values.

It covers edge subsets for binary height one, two and three; ternary height one and two; quaternary height one and two; and the five-ary star. Direct microscopic checking covers binary height one and two and ternary and quaternary stars. It verifies the five displayed binary counts. For fixed \(d=2\), it prints an approximation using 48 exact recursion stages with a mathematically bounded positive series tail; floating-point rendering itself is not a formal interval arithmetic certificate.

The proof for arbitrary \(d\) and \(h\) is analytic and does not depend on testing finitely many instances. In particular, enumeration cannot establish the general two-phase criterion, the finite-height formula, or the limiting entropy. The full argument for those assertions is in `RESULT.md`.
