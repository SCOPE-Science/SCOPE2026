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

# Verification of the habitat-component theorem

The complete claim and its all-order combinatorial proof appear in `RESULT.md`. Run `python3 verify.py` using the Python standard library; compare its sorted compact JSON standard output, followed by one newline, to `certificate.json`. The exact checker enumerates Prüfer-labeled trees on \(2\) through \(6\) vertices, eliminates isomorphic duplicates using explicit vertex permutations, enumerates every retained vertex subset, verifies equal first and second component factorial-moment coefficients, checks the universal third-cumulant coefficient law in the finite test range, and checks the four coefficients of the unique six-vertex witness.

The all-order theorem for arbitrary \(n\) is *not* inferred from these finite checks. It rests on the forest identity, the triple-edge-pattern proof, and polynomial divisibility established in the manuscript. Numerical simulation is not used. The study assumes exact independent homogeneous survival and makes no statistical estimation guarantee.
