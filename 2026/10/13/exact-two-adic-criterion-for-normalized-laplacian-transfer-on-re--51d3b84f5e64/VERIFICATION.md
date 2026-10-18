---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For an arbitrary simple k-regular m-vertex base graph H, both apexes have degree d=m+epsilon; base degree k+2. Symmetric and antisymmetric apex modes reduce normalized adjacency to 2x2 block [[epsilon/d,sqrt(2m/(d(k+2)))],[sqrt(2m/(d(k+2))),k/(k+2)]] and anti eigenvalue -epsilon/d. The symmetric normalized-Laplacian eigenvalues are 0 and theta_s=[m(k+4)+2epsilon]/[(m+epsilon)(k+2)]; anti eigenvalue theta_a=(m+2epsilon)/(m+epsilon). Positive weights w,1-w force exact phase conditions exp(-it theta_s)=1 and exp(-it theta_a)=-1. With theta_s/theta_a=p/q reduced, simultaneous phases exist iff p even and q odd, equivalently ν2(m(k+4)+2epsilon)>ν2((k+2)(m+2epsilon)); least t=pi q (m+epsilon)/(m+2epsilon) and all others odd multiples. For epsilon=0 iff k≡0 mod4, while edge-connected epsilon=1 can change feasibility in either direction. Independent exact rational 2-adic checks on small graphic parameters corroborate unrestricted direct quotient proof; no connectivity assumption on H required.

## originality

PASS

On inspected evidence this exact final claim is not a mere restatement or implication of a known stronger theorem; all four formal comparisons below and material primary-source inspections distinguish what is already known. Originality is best-of-knowledge, not independence or certification.

## value

PASS

A natural infinite family of graph quantum walks is given a complete, explicit arithmetical perfect-transfer classification and least transfer time for the physically distinct symmetric normalized Laplacian, including a counterintuitive edge-toggle transition. This solves a meaningful operator-specific parameter problem; spectral quotient phase conditions alone do not supply the final two-adic taxonomy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
