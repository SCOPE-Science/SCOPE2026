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
The proof is symbolic.

The packaged checker `artifacts/verify.py` exhaustively enumerates all matrices for
\[
(q,a,b)=(3,2,2),(3,2,3),(3,3,3),(5,2,2),(5,2,3)
\]
and compares every rank stratum with the closed formula. It then verifies
\[
\sum_i\operatorname{ch}(K_{a,b},i;q)q^{2i}=q^{a+b+ab}.
\]

For \(K_{2,2}\) over \(\mathbf F_3\), the rank counts are \(1,32,48\) and the character multiplicities are \(81,288,48\).

The checker returns `VERIFY_OK`. Finite enumeration is not used in the proof.
