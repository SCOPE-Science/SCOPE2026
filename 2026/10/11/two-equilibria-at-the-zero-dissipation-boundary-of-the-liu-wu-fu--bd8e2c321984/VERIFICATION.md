---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

At d=0 and abc !=0 the exact stationary equations split exhaustively: z=0 implies ay=0 and cx=0, hence the origin; z!=0 forces x=b, y=-c and z=a. Both are distinct. Directly formed Jacobians [[0,a,0],[0,0,-b],[c,0,0]] and [[0,0,c],[a,0,0],[0,b,0]] have characteristic cubics mu^3+abc and mu^3-abc. For nonzero real abc each has one real root and one complex pair with complementary real-part signs, giving hyperbolicity and unstable dimensions 2/1 or 1/2. The polynomial vector field has divergence -d, and the source branches S1,S2 tend to these two while S3=(b,0,bc/d) escapes when bc !=0. Independent symbolic determinant/cofactor reconstruction confirmed the algebra; absence of other equilibria follows by exact case split, not the script alone.

## originality

PASS

Best-of-knowledge comparison of mathematical statements and implications against named primary sources, published findings and exact source-object searches. The current Resultary hit for the very assignment under audit is not independent novelty evidence. A mirror of this assigned 2026-10-11 finding returned as the highest-ranked Resultary hit is not counted as independent prior art.

## value

PASS

The d=0 boundary is the natural divergence-free limit of a named scroll flow, not an arbitrary substitution. Correcting the literature’s false uniqueness count supplies the missing hyperbolic saddle branch and its complementary unstable dimension to support local bifurcation and separatrix analysis. Its significance is bounded to faithful zero-dissipation phase-space description, not a broad new chaos theorem. The characteristic cubics alone are routine; the coupled exhaustiveness-and-misclassification correction provides the justification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
