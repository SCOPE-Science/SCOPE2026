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

The two self-contained Python programs implement convolution multiplication independently of the proof's conjugacy argument. Both use only the Python standard library and are included here as `verify.py` and `verify_ext.py`.

`python3 verify.py` exhaustively enumerates all incidence-algebra elements for nine explicitly listed small prime-field posets in characteristics two and three. It checks the power equation directly, then checks the independently computed sum over diagonal subsets and radical \(p\)-nilpotent fibers, and tests the evaluated height formulas when applicable. Its observed terminal message was `VERIFY_OK`.

`python3 verify_ext.py` uses a self-contained model of \(\mathbb F_4\) and exhaustively checks the three-point chain and three-point fork, returning respectively 269 and 89 solutions. Its observed terminal message was `VERIFY_EXTENSION_OK`.

The general theorem is established by the five explicit mathematical proof steps in `RESULT.md`. Tests are finite and do not prove the general or asymptotic claim. The polynomial-zero argument's coefficient is nonzero for a selected strict \(p+1\)-vertex chain, by substituting 1 on exactly its \(p\) successive intervals and 0 on all others. There has been no independent mathematical audit.
