---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Deleting the hub gives arm blocks strictly below 4 by the positive quadratic form in RESULT.md. At and above 4 the hub Schur complement is scalar, so inertia at 4 counts at most one generalized eigenvalue in [4,infinity), and any nullspace there is one-dimensional. The inverse entry h_L obeys h_1=1/(lambda-1), h_{L+1}=1/(lambda-2-h_L); at 4 this gives (2L-1)/(2L+1). The scalar q+sum h_L-mu*lambda is strictly decreasing and has edge value 4(sum L/(2L+1)-mu), giving all three mass cases. Above 4 the reflected geometric arm solution has alternating signs and successive magnitudes with ratios below rho. The edge marginal increments decrease strictly. At fixed lambda>4 the continued fraction gives strictly positive increments, with successive increments in ratio h_{L+2} h_{L+1}<1; thus balancing and concentration strictly order the scalar functions for unequal profiles, and order their roots when above 4. Capping at 4 accounts for all ties below the band. As all lengths tend to infinity the inverse entries approach rho from below; bracketing the zero gives the limit q^2/[mu(q-mu)] when mu<q/2, with monotonicity under coordinatewise lengthening. Each finite threshold is strictly less than q/2. An independent incidence/edge-space eigensolver checked 462 threshold/count/vector cases as well as sampled capped rankings and long-arm limits. At mu=6/5 the example tops were about 4.110839 and 3.938173, respectively.

## originality

PASS

The unweighted edge result and unweighted length-majorization literature are prior. The inspected statements do not cover the finite free-arm crossing as a function of hub inertia together with its sharp allocations and resulting above-band frequency ordering. The infinite-arm formula is credited as a limit of the model, not a claim to invent junction localization.

## value

PASS

The spectral edge has physical meaning independent of the finite star. At fixed total material and hub mass the exact allocation range decides whether rearranging arm sites can create or eliminate a localized mode. The strict frequency ordering also guides allocation when several geometries already have a mode above the edge. These are distinct design decisions that unweighted existence alone does not resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
