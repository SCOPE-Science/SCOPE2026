---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Write X-Y=Ua+Vb with independent triangular U,V, and Gram entries A=|a|^2,B=|b|^2,C=<a,b>, S=A+B,Q=AB,T=Q-C^2>0. Direct even moments yield m2=S/6, m4=S^2/15-7Q/90+C^2/9, m6=S^3/28-31SQ/420+2SC^2/15. Eliminating Q proves T=105/(41m2)*(m6-75*m2*m4/7+18*m2^3), reconstructs Q and |C|, and hence the Gram matrix up to congruence. The positive-definite region at S=1 maps invertibly to the stated triangle with precisely the degenerate Q=0 and T=0 sides deleted. At fixed first two moments, the admissible line has a positive-length section except at square Q=1/4,C^2=0; m6 separates the other shapes. The inverse has uniform one-half Hölder bound via square roots and a square Gram perturbation shows no greater uniform exponent. I independently expanded all moments rationally and recovered T symbolically; source verify.py checks rational multinomials and direct seeded interior sampling.

## originality

PASS

Best-of-knowledge originality for the precise final claim after statement-and-implication comparison, preserving explicit priority/access risks; details in four required checks.

## value

PASS

The exact inverse of random Euclidean pair-distance moments for a natural three-parameter geometric family, its attainable data triangle and minimal moment count are useful to inverse stereology/tomography; it is not merely another forward formula or a known width observable. Exact squared-area recovery and sharp 1/2 stability are nonroutine structural consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
