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

The proof was replayed with `verify.py` from the packaged artifact path using Python standard-library exact rational arithmetic.

Checks performed:

- all \(70\) weak compositions of four into five cells were enumerated and the quadratic certificate was checked pointwise against the Simes rejection indicator;
- all thirteen extremizer weights were checked to be nonnegative on \([0,2/5]\) by exact quadratic minimization and to sum identically to one;
- the first moments, same-cell factorial moments, and cross-cell moments were checked coefficient-by-coefficient as exact polynomials in \(\alpha\);
- every support cell was checked to be an equality cell of the quadratic certificate;
- the attained rejection polynomial was checked to be exactly \(\alpha+13\alpha^2/16\);
- at \(\alpha=1/20\), the value was checked to be exactly \(333/6400\).

Replay output begins with `VERIFY_OK`.

Limits: this finite certificate proves the stated range only. It does not determine the sharp continuation for \(\alpha>2/5\), nor does it establish that no historically equivalent formulation exists outside the inspected sources.
