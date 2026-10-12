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

The proof of the forced-pair theorem is exact: the omitted mass is \(A=\sigma(n)-2n\), so every omitted nonsquare complement pair has pair-sum at most \(A\); solving the quadratic gives the stated interval. The power-closure step uses Theorem 5 of arXiv:2609.36068v1.

`verify.py` exhaustively enumerates every complement-pair orbit for each integer \(2\le n\le720\). It checks by exact integer subset-sum dynamic programming that no \(n<720\) admits a strong representation whose omitted set contains \((1,n)\), and verifies the displayed five-pair witness for \(720\). Square-root divisors are represented as singleton complement-orbits.

Limit: the finite checker does not establish power closure beyond the proved sufficient condition and does not re-prove Wang--Zelinsky Theorem 5.
