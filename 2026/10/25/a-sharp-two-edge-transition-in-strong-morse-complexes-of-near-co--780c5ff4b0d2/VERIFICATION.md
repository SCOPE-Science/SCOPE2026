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

The proof classifies every filtration-generated matching on the stated graph family by analyzing the first four positions of the vertex ordering. Every later position has at least two earlier neighbors; a three-pair gradient is excluded by the two missing-edge configuration. The eight per-vertex edge types and the isolated ordered pairs yield the homotopy type and the integral symmetry modules via explicit square loops and parallel-path differences.

The standalone script `verify.py` uses only Python standard-library modules, enumerates four-vertex prefixes for orders 4 through 11 and all full permutations for orders 4 through 8, and confirms every one-simplex, the absence of higher faces, component counts, cycle ranks and selected equivariant Lefschetz traces. Run `python3 verify.py`. Its recorded output is `verify_output.txt` and terminates in `VERIFY_OK`.

The finite checks do not certify the infinite quantifier; that follows from the symbolic first-four-position argument in RESULT.md. No independent audit or external validation has been performed.
