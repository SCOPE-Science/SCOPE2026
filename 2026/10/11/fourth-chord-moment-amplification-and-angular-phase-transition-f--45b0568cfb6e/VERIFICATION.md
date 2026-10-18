---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Independently derived the centered independent-pairs fourth-distance identity 2E|X|^4+2(E|X|^2)^2+4tr(Cov(X)^2). Area law uses independent U,V uniform[-1,1], boundary law uses four edges length-weighted by A/(A+B), B/(A+B). With A=|a|,B=|b|, z=a·b, exact M_I=8/45(6A^4+5A²B²+6B^4+10z²); independent symbolic derivation reproduces boundary M_S from its second/fourth/covariance moments and proves M_S−M_I strictly positive polynomial for A,B>0. The identity D=(61/17)M_I−M_S is affine in c²=z²/(A²B²); at A/B=1+t>=1 both c²=0,1 endpoints factor into polynomials with nonnegative coefficients, with equality only t=0 and c=0 (square). Long orthogonal rectangles tend to R4=1 without attaining. Differentiate rational ratio w.r.t z²: sign is G=B^6 r^3(4v³+4v²−21v−8), v=r+1/r>=2. Cubic value at v=2 is −2 and derivative positive for v>=2; exactly one v*>2, giving angle decreasing/invariant/increasing trichotomy at r*=1.2363261915. Independently symbolic-reduced all factor identities, including limit and unique root, and checked a nonorthogonal rational geometry against exact fourth pair moments. Endpoint c²=1 used only algebraically, not admitted as a nondegenerate shape.

## originality

PASS

Best-of-knowledge statement/implication assessment: No read prior theorem implies the claimed complete sharp upper range or angular zero locus. The closest same-sampling all-p paper was checked only via public abstract and remains a named source risk, not a definitive NOT_COVERING judgement. Relevant primary exact-object sources and indexed findings were checked by object, invariant and quantifiers; inaccessible plausible material is retained explicitly as risk, not treated as automatic scientific rejection.

## value

PASS

The ratio of fourth Euclidean pairwise-distance moments for boundary-uniform vs area-uniform sampling is a canonical dimensionless convex-geometric statistic. The complete sharp 61/17 extremum with rigid square equality is a nontrivial upper counterpart to known one-sided lower moment comparisons, while the algebraic aspect-ratio phase transition identifies a previously uncontrolled angular effect. An explicit exact invariant valid for every nondegenerate parallelogram has independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
