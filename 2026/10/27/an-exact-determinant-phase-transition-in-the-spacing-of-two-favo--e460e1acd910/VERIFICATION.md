---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For u_j=(B^j)₁₁, trace expansion leaves exactly the varying term δ²u_i u_(m−i), i=k−1, m=n−2. The determinant is common. In this family A≥B≥0 and B² is strictly positive (its off-diagonal entries are b(r+d) and c(r+d)), so every period product is positive even at an allowed zero diagonal or determinant. Its simple larger eigenvalue increases strictly with trace at fixed determinant. Matrix multiplication gives u_m−u_i u_(m−i)=(B^i)₁₂(B^(m−i))₂₁>0 for 0<i<m, establishing strict adjacency. Diagonal similarity to a symmetric matrix gives u_j=αλ_+^j+βλ_−^j with both weights positive and λ_+>|λ_−|. A positive λ_− gives strict log-convexity and the balanced minimum; zero makes interior products constant. For λ_−/λ_+=−t with 0<t<1, the varying term is (−t)^i+(−t)^(m−i). For even m only odd i can minimize, and t^i+t^(m−i) strictly decreases toward the midpoint; for odd m the negative terms in the first half are −(t^i−t^(m−i)), also uniquely smallest at i=1. Reflection gives the listed minimizers, including the single nonadjacent orbit at n=4,5. The three n=6 differences follow by multiplying B to obtain u₁ through u₄ and using the trace identity (in particular u₁u₃−u₂²=bc(rd−bc)). Independent exact computation: python3 /workspace/branches/independent_checks.py 3, output /workspace/branches/independent-3.txt; 1,242 direct integer matrix products for n=4,…,21, including nonsymmetric matrices, all determinant signs, zero diagonal cases and a singular A case. The frozen 1,989-check transcript was inspected as recorded evidence, not reenacted. The symbolic proof, not either sample, establishes the real-parameter theorem.

## originality

PASS

Credit the known periodic growth framework, schedule sensitivity and overlapping four-season algebra. The surviving distinct mathematical result is the exact all-period two-copy spacing classification, including the nonadjacent determinant-sign switch, not the existence of ordering effects or of a different determinant-sign law. The strongest checked cases do not imply it; this is best-of-knowledge, not a claim of historical priority.

## value

PASS

Exact placement is a natural choice variable in periodic structured growth. The theorem distinguishes a universal clustered maximum from a minimum that moves between two genuinely different nonadjacent schedules as the subdominant eigenvalue changes sign. The first possible distinguishing period and exact trace gaps give a useful sharp benchmark, not just a case study or an instance of the four-season inequality. Its interpretation is limited to the specified rank-one linear seasonal change, not a general ecological management prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
