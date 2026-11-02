---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The admissible strict triangle side cone is convex. Set x=p-a,y=p-b,z=p-c>0 and x+y+z=p; homogeneity permits p=1. Direct differentiation of xyz/(x+y+z)^2 gives X=yz(1-2x), Y=xz(1-2y), Z=xy(1-2z), and side gradient ((-X+Y+Z)/2,(X-Y+Z)/2,(X+Y-Z)/2). If every slack is <=1/2, X,Y,Z>=0 and <=1/4; the two possible derivative sign patterns bound l1 gradient by 3/8. If x>1/2, the other two are below half and u=-X,v=Y,w=Z satisfy u+v+w=x(1-x)-yz-2xyz<=1/4; l1 gradient<=3/8. Integrating along the convex cone gives the global d-infinity Lipschitz bound. Along x=epsilon,y=z=(1-epsilon)/2, the side gradient tends to (-1/8,1/8,1/8), and perturbations with its signs are feasible, proving sharp unattained supremum 3/8. Independent exact rational checks computed the gradient and bound on 64824 triples.

## originality

PASS

Qualified PASS for the exact strength stability constant 3/8 when perturbations are measured directly in the l-infinity norm on the three side lengths. The source strength is Kurlin’s; prior dimension-2 stability theorem uses Euclidean vertex displacement and a distinct constant lambda_2=sqrt(3), neither directly implying the optimal side-space value without sharp converse. A prior calculus statement could nonetheless contain the same elementary sharp 3/8 gradient bound; this residual risk is explicit.

## value

PASS

Side lengths are the invariant input data for geometric triangles, so the optimal noise amplification of a stable strength descriptor in the natural coordinatewise side measurement norm is a motivated exact stability fact. The sharp degeneration mode and metric distinction prevent conflation with the known vertex-coordinate bound; no larger theorem or paper-sized consequence is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
