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
# Reproducibility

The file `verify.py` is standalone and requires Python 3 with no third-party libraries. Execute `python verify.py` in the directory containing this document and the script.

The program enumerates binary matrices of dimensions 1 through 4, tests invertibility by elimination, computes all coordinate-permutation stabilizers, and checks the exact transposition-centralizer count. It additionally enumerates all invertible linear maps in dimensions 1 through 3 and directly checks algebra multiplication preservation; these independent checks verify that there are no missing non-permutation automorphisms in the tested cases. The expected final marker is `ALL_BINARY_EVOLUTION_SYMMETRY_CHECKS_PASSED`.

The finite census validates finite instances, not the all-dimension asymptotic proof. The proof's critical infinite estimates are the binary-matrix ordered-pair orbit codimension inequality, the uniform positive lower bound for invertibility, and the Bonferroni overlap bound. They are explicit in RESULT.md and should be checked mathematically for general dimension.

Independent audit or certification has not been performed.
