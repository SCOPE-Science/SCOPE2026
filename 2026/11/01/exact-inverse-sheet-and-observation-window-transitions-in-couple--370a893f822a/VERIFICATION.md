---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: Read frozen RESULT.md c42e6f2 and rational verifier. For lambda=1-epsilon>0 define output coordinates u=g_mu(X)-Y and v=(X-lambda g_mu(u)-epsilon Pu)/lambda. Explicit inverse X=lambda(g_mu(u)+v)+epsilon Pu, Y=g_mu(X)-u proves a global diffeomorphism and Psi o T=(x,h(y)); this is NOT dynamical conjugacy. Cubic h(t)=(1+a)t-abt^3 has exactly 3,2,1 distinct roots for |v|<H, =H, >H; s=sqrt((1+a)/(3ab)), H=2(1+a)s/3. The block Jacobian reduces to lambda^N product h'(y_i). Scalar extrema at ±s and three-zero roots 0,±sqrt(3)s establish the sharp closed-window transitions 1,2^N,3^N at L=s and sqrt(3)s (strict inequality at the first threshold). Independently checked the rational N=2 inverse and full Jacobian determinant symbolically; original checker uses exact fractions N=2,3,4. No multistep growth is inferred.

## originality

PASS

PASS, best-of-knowledge for the network-wide target-coordinate factorization, its exact inverse-sheet stratification and sharp closed-cube thresholds. Classical cubic folds and three-to-one patterns are old, but the inspected motivating coupled-ring research addresses forward clustering rather than this global inverse equivalence; explicit comparison avoids crediting known scalar cubic analysis as new.

## value

PASS

PASS: The coupled noninvertible network is a natural dynamical model; precise one-step ambiguity and observation-window injectivity thresholds separate apparent coupling complexity from true inverse multiplicity. A sharp dimension-dependent preimage count and window phase transition are meaningful for inverse reconstruction even though scalar cubics are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
