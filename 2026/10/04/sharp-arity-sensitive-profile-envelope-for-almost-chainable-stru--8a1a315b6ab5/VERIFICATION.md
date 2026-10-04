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

The bundled `verify.py` uses only the Python standard library. It evaluates the proposed sharp envelope
\[
E_k(m)=\sum_{j=0}^{\min(k,m)}inom{k}{j}
\]
for `0 <= k <= 8` and `0 <= m <= 10`, checks its stabilization at `2^k`, and independently enumerates the finite induced substructures in truncations of the sharpness construction with unary singleton predicates.

For a truncation with kernel labels `0,...,k-1` and sufficiently many ordinary points, every `m`-subset is mapped to the canonical invariant consisting of the singleton predicates it realizes. The verifier checks that the number of distinct canonical invariants is exactly `E_k(m)` throughout the tested range. It also verifies that every kernel label is forced into any chaining set in the construction by exhibiting the one-point predicate-preservation obstruction.

Replay command: `python3 verify.py`. Expected final line: `VERIFY_OK`.
