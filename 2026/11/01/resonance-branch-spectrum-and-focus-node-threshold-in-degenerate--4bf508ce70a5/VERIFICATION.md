---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

PASS: Direct Cayley-Hamilton recurrence gives P_n=af_n-df_{n-1} and normalized symmetric J_n(c) continuant. Irreducible tridiagonal J has simple real spectrum with strict interlacing, rank-one c perturbation fixes signs and bounds all but largest in (-2,2). det(2I-J)=n+1-cn yields exact focus-edge crossing c=(n+1)/n. The hyperbolic eigenvalue equation lambda^{2n+1}(lambda-c)=1-c lambda gives limit c+c^-1 and expansion coefficient (c²-1)² c^(-2n-3) in t. Rank-one spectral counting gives arcsine bulk and complete accumulation set. Independent numerical/high-precision spectral edge and recurrence checks confirm 25+ finite parameter instances; finite checks do not establish all n. No admissibility of R^nL itineraries claimed.

## originality

PASS

PASS (bounded best knowledge): Simpson already derives candidate flat-branch slope and displays selected zero-slope loci, and Jacobi/Chebyshev methods are classical. The additional *all-degree* root, sign, focus/node transition and exponentially approached outlier classification for this concrete dynamic trace does not appear in the checked primary source statements.

## value

PASS

PASS: A complete spectral organization of all candidate flat branches in the concrete zero-determinant border-collision model resolves the degree-dependent focus/node threshold and outlier; these are mathematically motivated boundaries not just arbitrary Chebyshev identities or a plot of small n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
