---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The final claim was checked by reconstructing the proof from the stated definitions rather than by numerical sampling.

1. For every \(N\ge1\), the interval \((a,d_N)\), where \(d_N=c+(1-c)/(N+1)\), has positive Lebesgue measure and therefore positive \(\mu\)-measure under measure equivalence.
2. Ergodicity implies that \(\mu\)-almost every orbit visits that interval, so its survivor set is \(\mu\)-null.
3. The direction \(\operatorname{Leb}\ll\mu\) transfers this nullity to Lebesgue measure. This is why equivalence, rather than only \(\mu\ll\operatorname{Leb}\), is in the claim.
4. The focal paper's Proposition 5.2 self-survival characterization and Proposition 5.1 realization argument imply the parameter-cover inclusion used in its Example 5.1. That symbolic step does not use the piecewise-linear slope computation; the latter is used there only to prove fixed-hole nullity.
5. Countable subadditivity establishes the pullback-null condition \((P)\), after which the focal Corollary 3 supplies continuity, monotonicity, and almost-everywhere local constancy of survivor entropy.

No finite experiment, numerical approximation, or unproved infinite extrapolation is used. The proof does not establish existence of the assumed invariant measure for a general decreasing Lorenz map, and no independent audit has been performed.
