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

The assigned matrix M=[[0,u,v],[a,0,u],[0,a,0]] is nonnegative and irreducible even at both feasible endpoints for a,B,c_u,c_r>0. I independently expanded det(tI-M)=t^3-2aut-a^2v. On the budget 2c_u u+c_r v=B, the polynomial at t_*=a c_u/c_r equals a^2(B_*-B)/c_r, B_*=a c_u^3/c_r^2, independent of the split. The unique positive Perron root is respectively below/above t_* on each side of the threshold. Comparing polynomial signs at another split proves strict reversal of monotonicity and the all-splits tie at B=B_*. Endpoints yield radii (a^2B/c_r)^(1/3) and sqrt(aB/c_u); inverting the maximum gives min(c_r r^3/a^2,c_u r^2/a) for the threshold budget. Actual frozen RESULT.md and verify_corridor.py were separately inspected; independent symbolic determinant and anchor identities pass. Regression roots are corroboration, not a proof over all real parameters.

## originality

PASS

Best-of-knowledge comparison of statements rather than titles: close primary results supply tools, partial parameter regimes or weaker scalar/qualitative conclusions but do not directly cover this particular exact claim. Inaccessible plausible broader results are named and retained as specific historical-priority risks, not treated as automatic failure.

## value

PASS

The smallest directed recruitment motif offering a long return circuit versus two local reciprocal feedback loops presents a motivated economic design question: which link restoration maximizes linearized spectral growth for a fixed cost? The exact all-positive-parameter reversal, unique endpoints away from the crossover, a continuum of critical ties, and sharp minimum target-growth budget are a complete useful structural classification; not an arbitrary numerical example. No stochastic persistence or general-network result is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
