---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

On symmetric ray subspace, normalize root a and depth-coefficients y_j; w0=sqrt(m)a gives exact ||H_m f||²-4||f||²=||Cw||²-4||w||²+3(1-1/m)|w0|². For finite w=(1,1/4,1/6,...,1/40,0,...) set S=sum w, T=sum_{j>=1}w_j², Z=sum w_i w_j h_max(i,j), and ||Cw||²=ζ(2)S²-Z from the infinite tail Gram identity. Independently recalculated exact 203-term rational lower bound ζ(2)>41/25 and surplus (41/25)S²-Z-2-4T=189621663106457667280588609/63582532975129101742448640000>1/400. At m=3 squared operator-norm excess >0.006182528..., and 3(1-1/m) increases with m, establishing strict >2 for every m>=3 without finite-output extrapolation. Published Abhinand et al. sphere/disk-spectrum theorem for leafless narrow trees supplies r(H_m)=2; it is not asserted re-proved.

## originality

PASS

Bounded statement-and-implication comparisons with published primary and related research did not identify coverage of the precise new assertion, and the distinct contribution is established by the indicated independently checked argument; priority remains subject to specifically recorded access risks.

## value

PASS

The m=3 threshold is the first trivalent rooted star, a natural minimal branching boundary for Cesàro normaloidity after published m>=5 root-vector obstructions. An exact reproducible finite-support witness on an infinite-dimensional operator closes two missing natural cases (3 and 4), and is an independently useful counterexample even without an exact operator norm or the two-ray case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
