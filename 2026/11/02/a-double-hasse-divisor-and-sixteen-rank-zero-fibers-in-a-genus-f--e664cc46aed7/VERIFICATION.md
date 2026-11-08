---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For smooth y³=x⁵+u x³+v x+1 in characteristic seven, genus=(3-1)(5-1)/2=4 and Cartier splits into [H=u²+2v] and 3×3 B. Independently recomputed the f²/f⁴ differential coefficients and exact identities det(B)=H·Delta and Delta(u,3u²)=3(u^5-1)². On H=0, v=3u² and u^5 !=1 (smooth), M(u) has rank exactly two. Exact polynomial two-iterate minors gcd is u(u^5-1)^9(u^5+1)(u^10+1); third semilinear Frobenius product vanishes modulo the squarefree S=u(u^5+1)(u^10+1). Therefore rank two except at the 16 distinct roots of S, where stable rank is zero; a-number two on H and zero off. Factor degrees of S are (1,1,2,4,4,4). Re-read the actual symbolic polynomial verifier and finite-point-count program; independent symbolic reconstruction matches the reported factorization and quotient-ring certificate. Bounded point checks do not prove whole-field result; exact polynomial identities do.

## originality

PASS

PASS best-of-knowledge for complete marked Hasse double divisor, sixteen zero-rank fibers and no intermediate rank-one/three fibers. General superelliptic algorithms and nearby a-number classifications are acknowledged but do not themselves specify the stable 7-rank locus. The directly relevant 2025 Sohn full text was inaccessible under authorized VPN and remains an explicit priority risk.

## value

PASS

Nontrivial exact Frobenius semilinear rank stratification and reduced exceptional parameter scheme for a natural genus-four trigonal family. The double divisor plus sixteen-point lower-rank locus is a precise reusable arithmetic-geometric classification, beyond merely running a general algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
