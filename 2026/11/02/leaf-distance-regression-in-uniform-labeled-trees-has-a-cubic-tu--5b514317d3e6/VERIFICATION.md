---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each fixed labeled a–b path of s=k+1 vertices, classical rooted-forest determinant hN^(N−h−1) gives exactly s n^(n−s−1) tree extensions. For r prescribed off-path leaves and q prescribed path endpoints, removing these leaves gives (s−q)(n−r−q)^(n−s−1) extensions, so the joint inclusion probability is ((s−q)/s)((n−r−q)/n)^(n−s−1) (zero for q=s). Inclusion expansion yields the full conditional probability-generating polynomial, and singletons yield the stated mean. Exact subtraction gives signed factor 2(n−1)−k(k+1)^2 over a positive denominator, with a unique discrete sign transition, possible two-point plateau, and maximizing k∼(2n)^(1/3). At n=3 mean is 2 and at s=n the negative exponent cancels correctly. Separate independently written Prüfer enumeration tested 14 (n,k) conditional-mean cells for n=3..6; this finite check does not establish the unrestricted proof.

## originality

PASS

The full eligible-leaf conditional law and cubic nonmonotonic total-leaf regression are distinct from known fixed-endpoint-degree regression. Remmel–Williamson leaf-set enumeration and Bousquet-Mélou–Chapuy rooted Cayley profiles may encode pieces through nontrivial summation; the specific signed cubic and distribution were not identified as theorems in the materially inspected sections. Best-knowledge originality is qualified, not a categorical historical priority certificate.

## value

PASS

Total leaf number is a canonical global branching statistic; distance between prescribed vertices is a geometric statistic in the same natural uniform tree. The exact sign transition from short-distance increase to long-distance suppression, the n^(1/3) peak scale and complete inclusion law are structurally informative and not a mere isolated numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
