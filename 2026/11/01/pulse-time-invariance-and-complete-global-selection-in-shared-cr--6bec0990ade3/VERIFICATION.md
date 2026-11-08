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

The flow formula x_i(t)=u_i E_i(s,t)/(1+sum_j u_j int_s^t b_j(v)E_j(s,v)dv) follows by direct differentiation, including pulse end-point convention. Exact projective composition L_(n,d) o L_(m,c)=L_(n*m,c+m*d) yields strictly positive c_j, pulse-time-independent mu_i, and the geometric-series iterate for every k. The three cases max mu>1, =1 and <1 follow by dividing the common denominator by max(mu)^k, by k, or using convergence of geometric series. Active ratios force common multipliers for cycles; the scalar increasing Beverton-Holt map rules out nonfixed cycles. At maximizing fixed simplex the Jacobian has tangent 1, radial 1/Lambda and transverse mu_j/Lambda; this is normal attraction, not isolated asymptotic stability. Negative or zero initial populations are not included in global selection; fixed-face classification includes nonnegative supports. Independent exact-rational flow/pulse witness gave multiplier vector (2,3), c=(7/4,3/2); shifted timing gives c_2=5/2 and winner abundance 4/5 rather than 4/3. Finite corroboration is not the proof.

## originality

PASS

The return-map form itself is an established equal-row multispecies Leslie–Gower recurrence, not independently new. Novelty assessed only for a constructive exact realization under arbitrary finite asynchronous species-specific pulses, phase-independent competitive winner, closed all-iterate global classification, critical inverse-time rates, neutral fixed-simplex stability and no subharmonics. The 2026 pulsed competition preprint was accessible at abstract level but not in full; plausible priority risk is recorded.

## value

PASS

The exact global dynamics under arbitrary finite asynchronous positive species pulses is a natural and ecologically motivated mathematical question because pulse timing alters abundance while total multiplicative growth fixes the competitive winner. The sharp extinction, threshold 1/k, tied-winner simplex, no-subharmonics and local spectrum answer nontrivial boundary cases of the general class. The recurrence algebra is classical and value rests on the combined genuinely all-parameter pulse interpretation, not renaming the Leslie–Gower map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
