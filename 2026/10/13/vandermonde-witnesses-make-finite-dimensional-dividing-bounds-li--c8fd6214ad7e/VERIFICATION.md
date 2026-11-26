---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The bundled `verify.py` uses only Python's standard library and exact `Fraction` arithmetic. It checks the finite linear-algebra core of the construction for every \(2\le k\le10\) and \(1\le r\le5\).

For each \(k\), the checker forms Vandermonde coefficient matrices for prefixes of the sample points \(0,1,\ldots,k-1\). For \(1\le s<k\), it verifies
\[
\operatorname{rank}(V_s)=\operatorname{rank}([V_s\mid y_s])=s,
\]
where \(y_s=(0^{k-1},1^{k-1},\ldots,(s-1)^{k-1})^T\). At \(s=k\), it verifies
\[
\operatorname{rank}(V_k)=k-1,
\qquad
\operatorname{rank}([V_k\mid y_k])=k.
\]

For each tested \(r\), it also checks the block dimension arithmetic \(r(k-1)\) and its strict inequality with the published universal upper bound \(2kr\).

The recorded command is `python verify.py`, with reported output `VERIFY_OK 198 exact rank assertions`. These are finite sample checks over the rationals, not a test of indiscernibility, the model-theoretic minimum, or the full characteristic range. The construction and general proof are in `RESULT.md`.
