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

# Reproducible verification

`VERIFY.py` uses only the Python 3 standard library and exact integer arithmetic. It reconstructs all 28 odd theta coordinates and enumerates all \(315\) XOR-zero four-sets. It checks that each coordinate occurs in \(45\) tetrads and every unordered pair occurs in \(5\) tetrads, as predicted by the classical design. It verifies that the augmented binary rank is \(7\), which makes the congruence map onto \(\mathbb Z/4\mathbb Z\oplus\mathbb F_2^6\) surjective after an even-vector adjustment.

The file then selects the \(28\) columns by the precise zero-based indices in `RESULT.md` and applies fraction-free Bareiss elimination to their integer incidence matrix, asserting exact determinant \(-256\). The index equality follows by algebra from these two certificates and generator containment. A successful invocation prints `VERIFY_OK`.

The finite exhaustive enumeration is of the *complete* 28/315 incidence configuration, not a bounded search over possible lattice coefficients. Historical novelty remains qualified; this verifier does not independently audit authorship, priority, or the classical theta-to-bitangent geometric identification.
