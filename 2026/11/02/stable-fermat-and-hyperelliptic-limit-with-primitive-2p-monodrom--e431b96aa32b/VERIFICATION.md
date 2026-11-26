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

The diagonal-2/off-diagonal-t gradient system on the active X^p,Y^p,Z^p coordinates gives precisely the stated exceptional finite parameters. At -2 the conic is smooth and the power map is étale off the coordinate axes. Its pullback has precisely 3p candidate points on the axes; each is a unibranch cusp by the displayed local equation. The coordinate-square map from the Fermat curve is generically one-to-one (no other generic sign choice works); its image has degree 2p by pullback of O(1), hence is the whole reduced special fiber. In the local equation write the deformation coefficient as the unit U(A,B), and replace A,B by A U^(-1/2),B U^(-1/p); division by U gives x²−4y^p+s^(2p)=0 exactly. In the (p,2,1)-weighted blowup the s-chart gives a²=4b^p−1. Its missing point is visible in the y-chart x=u^p v, y=u², s=u t, where v²=4−t^(2p). The residual sign exchanges the v=2 and v=−2 neighborhoods (p odd), so one chart suffices, with the transverse node u t=0 and smoothing s=u t. This gives precisely one tail at each cusp and no extra branches. The central and tail genera give a stable compact-type tree and a product connected Picard variety. Over the new disc, separating vanishing cycles give trivial action on H¹; the deck action is identity on the central component and (-a, ξ^(-2)b) on each tail. Differentials b^j db/a and conjugates supply all primitive 2p-th roots once per tail, with no graph cohomology. Thus the full polynomial and exact order follow. The inspected finite symbolic checker only tests algebra for sample primes; it was not run and is not the geometric proof.

## originality

PASS

Best of current knowledge: the pencil and its smooth locus are prior, as is the local method of replacing a smoothed cusp by a hyperelliptic tail. The supported distinct contribution is the explicit compact-type model at this boundary together with the global descent action and full cohomological polynomial. The same-pencil candidate Z1 is a smooth Riemann surface by Proposition 5, so is not this reducible stable fiber; §5.2 does not identify the asserted model. No priority claim is made.

## value

PASS

A natural singular member of an established pencil is resolved explicitly for all stated primes. The component equations and the descent spectrum answer different useful questions: the former identifies the limiting Jacobian and potential good reduction, while the latter determines finite inertia on H¹, beyond what an existence theorem or local cusp genus alone would give.

The dated certificate retains the supplied scientific assessment, sources and limitations.
