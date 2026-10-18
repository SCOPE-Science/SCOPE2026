---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Norm N10=max{|u+v|,|ru+v|,r|v|,r|u|,|u+rv|}, r=(sqrt5-1)/2; real plane. The described ten polygon vertices satisfy its support inequalities and the displayed Q,R generate the needed dihedral symmetry to reduce x to one half-edge (alpha in [0,1/2]) and y to five antipodal edge classes. For each edge y=p+beta(q-p) and t in either [0,r] or [r,1], substitute w=t beta, yielding affine support values in alpha,t,w on a triangular prism. Candidate upper envelope L(t)=1+(sqrt5-1)t/4 and (1+sqrt5)/4+r t. Failure of upper bound requires a pair of 10 signed linear supports simultaneously above L; the maximum of their minimum over a prism is attained at an original vertex or equality-plane intersection with an edge (possibly a face degeneration covered by a vertex). Inspected exact Q(sqrt5) verifier constructs all eight prism vertices, every equality/facet/facet candidate, and evaluates 5*2*10*10=1000 cases exactly; tabulated maxima low=(0,0,0,0,0), high=((-9+3sqrt5)/4,(-3+sqrt5)/4,0,0,(-3+sqrt5)/2), all <=0. Independently solved same 1000 small linear max-min programs numerically; agrees to double precision (not substituted for exact proof). At both branch endpoints, unit pairs (-1,0),((3+sqrt5)/4,-(1+sqrt5)/2) and (-1/2,-1/2),(phi,-phi), phi=(1+sqrt5)/2, attain branch norms, and convexity/support affinity extends their exact equalities throughout. Homogeneity J(lambda)=s F((1-s)/s), s=max(lambda,1-lambda), yields two stated weighted branches and threshold s=r, for 0<lambda<1. Midpoint ordinary J is a derived known value, not the new claim.

## originality

PASS

The theorem is the entire continuous weighted James profile on an affine-regular DECAGON with a genuine golden-ratio branch switch. Known ordinary James midpoint for the decagon does not determine a function of lambda. Liu-Sarfraz-Li 2021 defines the functional and establishes general bounds; the relevant inspected sections contain no decagon-specific piecewise law. Previously audited octagon weighted profile and real lp formula concern distinct unit balls and do not imply this law. Equivalence under different affine norms or the chord parameter was explicitly considered; remaining alias-literature risk stated.

## value

PASS

The regular/affine-regular decagon is a canonical new shape in polygonal Banach geometry, and the full weighted generalized James invariant is a natural continuum geometric profile. A verified nontrivial golden-ratio transition of the sharp extremizer and complete exact formula are stronger than a known midpoint value and require a substantive sharp continuous polyhedral bound. This is a motivated exact classification, not an arbitrary unmotivated slice or a trivial parameter rename; the distinct phase of optimal pairs may inform norm geometry examples and comparison work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
