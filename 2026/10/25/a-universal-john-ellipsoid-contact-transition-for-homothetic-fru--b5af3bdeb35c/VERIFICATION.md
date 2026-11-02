---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For d>=2 and any full-dimensional compact convex base K, affine-normalize the base John ellipsoid to B_{d-1} and apply its nonsymmetric contact design. The proposed frustum ellipsoid has center height b=min{1/2,1/((d+1)(1-q))}, horizontal radius a=sqrt(1-2(1-q)b), with b=1/2 at q=1. Containment follows from max_w{a sqrt(1-w²)+(1-q)b w}=sqrt(a²+(1-q)²b²)=1-(1-q)b; axial heights stay in [0,1]. With t=(1-q)b/[1-(1-q)b], s=sqrt(1-t²), lateral normals (s u_i,t) weighted lambda_i/s² and cap weights [1+(d-1)t/(1+t)]/2 and [1-(d-1)t/(1-t)]/2 satisfy zero mean and covariance I_d. The latter upper weight vanishes iff q<= (d-1)/(d+1), and is positive above. John sufficiency and uniqueness establish the full all-base theorem, not just symmetric examples. Independently recomputed weighted identities at (d,q)=(2,0),(3,.35),(4,0),(5,.7),(8,1).

## originality

PASS

The general nonsymmetric John-contact characterization is classical; the strongest matching frustum-like predecessor, Güler–Gürtuna arXiv:0709.0707, explicitly states on page 3 that its truncated second-order-cone Section 8 solves the outer circumscribed ellipsoid and leaves the inner inscribed ellipsoid unsolved. Thus that paper does not imply the submitted inner formula, still less the arbitrary-base affine-transfer contact theorem. Related published exact John computations for capped cubes and cones concern different truncations/bases. Best-of-knowledge priority with residual uncatalogued literature risk.

## value

PASS

It solves an explicitly open inner-ellipsoid computation for an entire natural affine class of homothetic convex frusta, including arbitrary asymmetric/nonpolyhedral sections, with a sharp universal cap-contact threshold and formulas useful as benchmark convex-optimization certificates. Neither a routine affine substitution into a known solved general frustum theorem nor a minor finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
