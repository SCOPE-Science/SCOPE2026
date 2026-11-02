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

Parametrize a zero-sum vertex vector by leaf-hub differences y_i; the Rayleigh denominator is y^T H y with H=I−11^T/(m+1), and numerator ∑w_i y_i², hence λ2>=ℓ iff diag(w)−ℓH is PSD. By positive homogeneity maximizing λ2 under the linear price budget reduces to minimizing ∑c_i v_i subject to diag(v)>=H. Strict SDP feasibility yields a dual over Z PSD with fixed diagonal c_i, maximizing tr(HZ)=C−||∑u_i||²/(m+1) for Gram vectors ||u_i||=√c_i. The minimum attainable vector sum is δ=max(0,2max s_i−∑s_i), by polygon closing or opposite collinear vectors. In the nondominant case v_i=1 meets the dual and any optimum must equal it by complementarity with positive diagonal Z and Z1=0. In the dominant case the unique complementary solution is v_j=1−δ/((m+1)s_j), v_i=1+δ/((m+1)s_i) otherwise; its PSD slack has zero Schur complement, and cost exactly C−δ²/(m+1). Thus unique positive optimum w=(B/T)v; kernel dimension of slack equals m−1 or 1, verifying Fiedler multiplicity (m=2 always 1). For one exceptional price r and m−1 unit prices, δ=0 iff √r<=m−1 for m>=3; for m=2 only r=1. The large-r ratio to uniform weights is (m+1)/m. Independent Laplacian eigenvalue calculations verified λ2=B/T and budget for seven price vectors across both regimes, including exact price threshold [9,1,1,1] and dominant [100,1,1,1]; positive optimal spokes checked.

## originality

PASS

Fiedler's unit-average absolute algebraic connectivity, Göring–Helmberg–Wappler's equal-price total-weight SDP/embedding dual and Boyd's general convex framework are preexisting. The newly assessed result is the complete heterogeneous-edge-price star solution, unique allocations and exact √price polygon/multiplicity threshold. The inaccessible Fiedler full paper leaves qualified risk but its abstract does not state this variable-price optimization.

## value

PASS

Optimally allocating a fixed conductance budget across unequally priced spokes is a natural exact spectral-network design problem. The result gives a complete solution for all m and price vectors, a sharp √price polygon threshold at which the unique equal-weight optimum changes to an asymmetric one, and an associated Fiedler-space multiplicity transition. This is a structural infinite-family optimization classification useful for analysis of graph diffusion/consensus rates, not a mere tiny numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
