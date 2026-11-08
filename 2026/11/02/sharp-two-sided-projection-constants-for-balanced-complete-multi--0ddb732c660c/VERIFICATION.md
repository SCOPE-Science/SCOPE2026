---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For G=K_{q,...,q}, r>=3,q>=2, symmetrize any real edge-ℓ1 projection under S_q≀S_r; the conjugation average remains a projection to the same invariant range and cannot increase the norm. The fixed-edge stabilizer and sign-reversing part swap force an equivariant T=DP to factor S D with S=sI+tqR on zero-sum vertices. Identity on the cut space implies SL=L and invertibility of L, hence S=I and unique invariant cut projector Q=D^T L^+D. Complementation/adjoints prove unique invariant cycle projector I−Q. The Laplacian has positive eigenvalues rq and q(r−1); its edge-response potential has a=(rq−1)/(rq²(r−1)) and b=1/(rq²(r−1)). Exhaustive symbolic edge class counting gives λ(C)=2(q²r²−q²−2qr+2)/(q²r(r−1)) and λ(Z)=(3q²r²−q²r−2q²−8qr+8)/(q²r(r−1)). The difference 1−4(rq−1)/(rq²(r−1))>0 follows from q(r−1)>=4. Independent numpy pseudoinverse calculations checked idempotence and every column 1-norm in four (r,q) cases, 117 columns. Finite tests support rather than prove all parameters.

## originality

PASS

Best-of-knowledge new evaluated complete multipartite cut/circulation pair, acknowledging the general invariant-projection principle and prior related graph family computations.

## value

PASS

A complete natural two-parameter Banach-space projection classification with explicit globally minimal norms for complementary canonical graph subspaces, a strict gap, uniqueness among symmetry-invariant minimizers, and contrasting large-r and large-q limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
