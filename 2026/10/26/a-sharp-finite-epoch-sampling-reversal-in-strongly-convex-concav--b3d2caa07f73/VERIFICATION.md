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
The finite expectations consist of two reshuffled ordered products and four IID ordered products. The symbolic derivation in `RESULT.md` establishes the exact risk comparison for every real starting direction and the sharp step-size threshold. The included `verify.py` reconstructs the full symbolic matrix and uses independent rational matrix arithmetic to check the same identity for 45 parameter tuples. It also checks three exact boundary/sample points and strict component-step contraction.

Run `python verify.py` using Python 3 and SymPy. A successful replay prints `PASS: symbolic identity and 191 independent exact rational assertions`.

The computational tests validate algebraic transcription and sample parameters; they do not serve as a proof of all parameter choices. The theoretical proof depends only on explicit two-by-two matrix products, sign analysis, and positive-principal-minor tests. Independent audit: not performed.
