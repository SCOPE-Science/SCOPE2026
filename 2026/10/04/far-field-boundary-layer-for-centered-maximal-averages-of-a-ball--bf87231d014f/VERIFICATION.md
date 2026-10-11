---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof was reconstructed from the frozen RESULT.md rather than accepted from its prior review. In axial coordinates at the farthest point of the unit ball, the missed full cap is exactly the region 0<=u<delta and the partial transition ends at u_*=(2B delta-delta^2)/(2(B-1)); hence its width is O(delta/R). Integrating the cap cross-sections gives C_n delta^{(n+1)/2} with C_n=2^{(n+1)/2} omega_{n-1}/(n+1). Expanding the radius denominator balances delta/B against delta^{(n+1)/2}, forcing delta=t B^{-2/(n-1)}. The limiting objective G_n(t)=nt-a_n t^{(n+1)/2} has a unique positive maximizer and gives exactly the stated c_n and kappa_n. The localization argument excludes delta bounded away from zero and scaled t escaping to zero or infinity. An independent quadrature/maximization check for n=4,R=200 gave scaled optimizer ratio about 1.017, consistent with the asymptotic but not used as proof.

## originality

PASS

Best-of-knowledge PASS with a material access risk. The primary abstract for Solyanik arXiv:2609.27687v1 explicitly distinguishes an elementary closed formula for M_c(chi_U) in R^3 from an arbitrary-dimensional two-ball intersection formula. The final claim begins at n>=4 and adds a singular far-field argmax asymptotic and two-term maximal-value expansion. Resultary searches for the optimizer law returned the same audited record and unrelated one-dimensional centered-maximal findings, not a covering prior. The highly relevant preprint full text could not be obtained through arXiv/open-access routes; after those failures the single authorized institutional fallback returned worker unavailable, and no retry or bypass was made. Under the owner rule this inaccessible plausible source is retained as a residual risk rather than treated as evidence of novelty or as an automatic failure.

## value

PASS

The optimizing radius is an intrinsic quantity for the canonical test object in the motivating maximal-operator problem. Identifying its exact dimension-dependent boundary-layer scale and the first correction to the maximal value is a structural asymptotic, not a fixed-radius Taylor exercise. It isolates the competition between cap loss and denominator gain and can inform perturbative constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
