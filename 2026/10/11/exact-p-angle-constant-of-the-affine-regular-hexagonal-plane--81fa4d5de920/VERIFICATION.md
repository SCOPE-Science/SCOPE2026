---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Reconstructed the final real two-dimensional theorem from the actual frozen RESULT.md and seven Git blob hashes. Unit ball is the six intersections of signed facets ±s, ±t, ±(s-t). For unit x,y with x!=±y let A=N(x+y)>0, B=N(x-y)>0. Dual support forms f,g attaining A,B yield A+B <= max_{f,g}(||f+g||_*+||f-g||_*)=3; each A,B<=2. The desired cosine <=1/4 is equivalent to q=2A^2+2B^2-AB<=8. If s=A+B<=2, q=2s^2-5AB<=8; if 2<=s<=3, (2-A)(2-B)>=0 implies AB>=2s-4, giving q<=2s^2-10s+20<=8 by convexity and endpoint values 8. For x=(1,1),y=(1,0), A=2,B=1 and cosine=(4+1-4)/(2*2*1)=1/4. Independently reconstructed the tree SHA f7253024a1d326e0bf7dded092ef3c755cbb0eee from all seven actual Git blob SHA-1s; independently derived the six vertices and 36 facet-pair table exactly. Exhaustive rational 180-point edge-grid gives 32040 admissible pairs consistent with the sharp bound; this finite grid is corroboration, not its proof. Yang–Li Definition 3.1 is used as a formula in dimension two, despite its introductory dim>2 convention, as Remark 3.2 explicitly discusses two dimensions.

## originality

PASS

Best-of-knowledge originality for the exact S_P value on a canonical non-ell_p six-gonal Banach plane. The primary Yang–Li source defines S_P and universal bounds but not this plane; the full earlier same-invariant ell_p theorem excludes this norm; an octagon theorem has a different 8-facet norm. Exact same-space von Neumann–Jordan and Radon Birkhoff constants have different admissible pairs and expressions. The single exact same-result Resultary hit is a mirror of this assigned finding, not evidence of independent prior coverage. A fresh facet inequality and quadratic envelope are needed to obtain the claimed sharp value. Unindexed or alternate-named equivalent work remains a residual risk.

## value

PASS

This exact invariant is mathematically motivated: the affine-regular hexagon is the smallest centrally symmetric non-parallelogram polygon and a canonical non-Hilbert Radon normed plane, while Yang–Li S_P measures departure from the Hilbert relation via a concrete unit-pair angular supremum. The exact 1/4 locates this canonical model strictly between Hilbert zero and the universal 1/2 endpoint and supplies a sharp 6-facet benchmark distinct from the ell_p and regular-octagon cases. The reusable sharp support-functional bound N(x+y)+N(x-y)<=3 and explicit attaining pair make the fact independently reproducible and usable for comparing other polyhedral angular constants. A natural exact one-plane invariant can be valuable even without a full polygon classification; this is not merely a renamed known constant or a negative normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
