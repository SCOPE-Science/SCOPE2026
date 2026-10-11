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

The proof uses the full graph definitions and the invariant-space quotient, plus the exact polynomial identity for the quotient cofactor. The standalone `verify.py` needs only Python 3 and emits `VERIFY_OK` if all checks pass.

The six-by-six quotient cofactor depends polynomially on \(r\) with degree at most six. Seven exact substitutions \(0\le r\le6\) and integer Bareiss elimination verify the proposed polynomial identity for all \(r\), not merely those seven values. The other invariant-block determinants are checked directly.

As an independent finite calibration, the program constructs both edge graphs from their combinatorial definitions, confirms their \(2d+2\) vertex and \((d+3)(d-1)\) edge counts, and compares full Laplacian cofactors with the asserted products for every integer \(3\le d\le10\). In the exceptional case \(d=3\), this supplies the separate count \(336\) for the truncated triangular prism. The general result relies additionally on the proved invariant decomposition; these finite full-graph cases alone would not establish it.

The strict order follows from a displayed positive-coefficient polynomial after substituting \(h=d-3\); it is not inferred from numerical experiments. Remaining risks concern only possible equivalent literature under different graph terminology and lack of independent validation.
