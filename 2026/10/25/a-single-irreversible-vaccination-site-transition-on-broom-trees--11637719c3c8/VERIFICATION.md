---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every k>=2, L>=1 and real 0<p<1, the tree has N=k+L+1 vertices. Uniform seed among N-1 survivors makes expected final component size the ordered-pair path-connectivity score S_v/(N-1). Removing hub gives k+H_L; removing v_t gives k+H_t+H_{L-t}+2k sum_{j<=t}p^j+k(k-1)p^2. The exact identity D_t=2p(1-p^t)(p^{L-t}-1+k(1-p))/(1-p)^2+k(k-1)p^2 and adjacent difference 2p/(1-p)[p^{L-t-1}-(1-k(1-p))p^t] were independently checked for 1056 rational (k,L,t,p) combinations. For t<=L/2, polynomial coefficients of D_t have at most one sign change, so Descartes plus D_t>0 near zero guarantees at most one interior root, and it is from hub-better to path-better. At p=1, D_t(1)=k(k-1)+2t(t+k-L), whose strict minimum yields switch iff d=L-k>=2 and 2 floor(d^2/4)>k(k-1). Leaf deletion is strictly dominated by deletion of its neighbor for positive p, covering all vertices and boundaries. For p>1-1/k the adjacent-difference sign change yields the stated discrete path optimum. Lengthening L strictly decreases D_t for every fixed admissible path site, giving strictly decreasing thresholds once they exist. The positive correction to D_infinity tends to zero for t=floor(L/2); the bracket k(k-1)p(1-p)^2-2[1-k(1-p)] has one zero by monotonicity in u=1-p on (0,1/k), yielding the stated limit. The known k=2,L=5 threshold is p^2+p^3=1; all algebraic and domain checks agree.

## originality

PASS

Best-of-knowledge comparison on actual final mathematical statement for One-way optimal vaccination-site transition on broom trees. Four distinct implications were checked, including known covering numeric/special-case portions that are explicitly excluded from the originality claim. Sources and access limits are detailed below.

## value

PASS

A sharp family-wide optimizer transition identifies exactly when perfect one-site protection shifts from a high-degree hub to the handle, including its unique critical transmissibility and infinite-handle limit. The integer condition and monotonicity supply structural answers for a natural one-seed percolation vaccination problem; this is more than a single numerical benchmark or substitution of a standard pair-count formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
