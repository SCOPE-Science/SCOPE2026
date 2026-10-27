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
# Exact verification

Run `python verify.py` using Python 3 with SymPy. The script constructs the three displayed \(2,2\) sections over \(\mathbf F_3\), enumerates all 13 projective rational combinations, confirms their independence, and independently performs two exhaustive algebraic smoothness checks per curve: the binary-quartic discriminant has no repeated geometric root (including at infinity) and all four affine-chart Jacobian ideals have reduced Gröbner basis `[1]` modulo three. The recorded output is embedded as `verify.txt`.

This proves smoothness over the algebraic closure because a proper subscheme cut out by the Jacobian ideal on any chart would correspond to a common zero over an algebraic closure; `[1]` excludes one. For a smooth \(2,2\) divisor, the genus is one. The general dimension bound and rational basepoint exclusion are exact symbolic first-jet arguments, not computational extrapolations.

Checks do not classify all nets or establish smoothness for nonrational members. No external independent audit has been performed.
