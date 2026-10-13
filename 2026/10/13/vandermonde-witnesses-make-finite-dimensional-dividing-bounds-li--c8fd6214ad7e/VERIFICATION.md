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

The bundled `verify.py` uses only Python's standard library and exact `Fraction` arithmetic. It checks the finite linear-algebra core of the construction for every \(2\le k\le10\) and \(1\le r\le5\).

For each \(k\), the checker forms Vandermonde coefficient matrices for sample points \(1,2,\ldots,s\). For every \(s<k\), it verifies
\[
\operatorname{rank}(V_s)=\operatorname{rank}([V_s\mid y_s])=s,
\]
where \(y_s=(1^{k-1},\ldots,s^{k-1})^T\), certifying consistency of those interpolation equations. At \(s=k\), it verifies
\[
\operatorname{rank}(V_k)=k-1,
\qquad
\operatorname{rank}([V_k\mid y_k])=k,
\]
which is the finite rank form of \(k\)-inconsistency.

For each tested \(r\), it also checks block additivity of the forced parameter span, \(r(k-1)\), and that this lower dimension is strictly below the published universal upper bound \(2kr\), as expected.

Running

```text
python verify.py
```

returns

```text
VERIFY_OK 198 exact rank assertions
```

The finite computation is not used as a substitute for the general proof. The arbitrary-\(k,r\) argument is the exact Vandermonde determinant/root-count argument in `RESULT.md`.
