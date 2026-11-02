---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Marked ordered cycles give E C_j=Z(n-j,2)/(jZ(n,3)), E(C_j C_k)=Z(n-j-k,1)/(jkZ(n,3)) for j≠k, where Z(m,h)=[m h]/m!. With k=n-j-r, r=floor(c√n), identities Z(m,1)=1/m, Z(m,2)=H_{m-1}/m and Z(m,3)=(H²_{m-1}-H^{(2)}_{m-1})/(2m) yield exact sign determinant D=1/2(H_{n-1}²-H_{n-1}^{(2)})−[nr/((n-j)(j+r))] H_{n-j-1}H_{j+r-1}. Expanding harmonic numbers for fixed j,c gives D=−(log c+γ/2)log n−γ log c−γ²/2−π²/12+o(1); at c=e^-γ/2 the constant is −π²/12<0. Substituting Z(n,3)~(log n)²/(2n) derives the two stated distinct covariance normalizations. Independently enumerated three-cycle permutations through n=7 and checked 40 bounded comparisons including critical-scale digamma signs. The floor error is O(1/√n) and does not change equality boundary.

## originality

PASS

The general Ewens sampling formula and Stirling factorial moments already encode the displayed finite conditional covariance; they are not claimed novel. Tavaré 2021 presents the conditioned sampling law and its moments, while Arratia–Barbour–Tavaré 1992 and Lugo 2009 study Ewens approximations/permutation profiles. No compared source supplies the cancellation and exact square-root residual-label sign transition with equality-boundary negative and an extra log power. The sharp asymptotic fact is independently derived rather than reading a table. Historical exhaustive priority is not established.

## value

PASS

The constrained sample space of three-cycle permutations naturally couples a fixed short cycle to a nearly spanning one. Determining whether their counts attract or repel, exactly where the sign switches on a √n leftover scale, and why the critical case loses a logarithmic order is a mathematically informative asymptotic classification, not merely repackaging Stirling numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
