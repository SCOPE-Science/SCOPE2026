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

The stand-alone `verify_prism.py` requires Python 3.9 or later and SymPy (see `requirements.txt`). Run `python verify_prism.py` in the directory containing both files. An observed successful execution prints `VERIFIED_CIRCULAR_LADDER_SIGNED_HIGHER_INDEPENDENCE` with markers for the exact symbolic characteristic polynomial, independent exhaustive enumeration at all lengths three through eight, the integer signed values at all indices one through nineteen, and exact rational root certificates.

The checker constructs a sixteen-by-sixteen polynomial matrix, symbolically factors its characteristic polynomial, and directly compares it to the stated product. Its independent enumeration inspects every vertex subset of the graphs of order six through sixteen and compares the **entire** face-count coefficient vectors to transfer-matrix traces. It recomputes the integer recurrence samples and uses rational comparisons to bound the nonleading roots and the complete error at exponent twenty.

All-parameter correctness rests on the explicit transfer-bijection and analytic inequalities proved in the result, not on finite computations alone. The checker does not compute individual homology groups, torsion, full homotopy types, or independent mathematical validation.
