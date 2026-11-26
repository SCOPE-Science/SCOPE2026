---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The sum and difference modes are orthogonal and have the same token normalization. At relative variable t=(1-c)/(1+c), the unnormalized sum multiplier is 1-η and the difference multiplier is 1-ητ(t)>0, with τ(t)=tanh(κt/(1+t)). Thus t'=t[(1-ητ)/|1-η|]² and the ordered vector result retains both orientation signs. At η=1 a noncollinear pair becomes antipodal exactly. For 1<η≤2, 2ηtτ'≤κ<1-ητ, so the scalar map is strictly increasing; the ratio t'/t is strictly decreasing. Comparing it with one proves monotone escape to infinity below or at η_a, trapping and convergence to the unique interior fixed t* above η_a and below 2, and monotone decrease to zero at 2. For η<1 the ratio is greater than one throughout. The interior derivative is strictly between zero and one, and the actual orbit is the signed swap (x1,x2)→(-x2,-x1), not an ordinary swap. The monotonic alternatives exclude additional cycles. Consensus is fixed, undefined, or sign-flipping as stated across η=1; the antipodal multiplier stays positive. At η_a, t'/t=1+4κ(1+tanh κ)/t+O(t^-2); at 2, 1/t'-1/t=4κ+O(t). Averaging these increments and using 1+c=2/(1+t) and 1-c=2t/(1+t) yields both constants for every noncollinear initial pair. Numerical diagnostics are supplementary, not the proof.

## originality

PASS

The closest indexed statements concern local cycles with a mixed-sign or anisotropic value matrix. A formal threshold match outside their hypotheses is not a theorem for the isotropic negative map. The publicly inspected self-inclusive family has a positive-simple-top-eigenvalue assumption for its principal analysis; the matching repulsive sign in the other paper uses diagonal masking. No checked source supplies the inclusive, isotropic global classification and both critical time constants under valid hypotheses.

## value

PASS

The smallest genuinely interacting self-inclusive repulsive model yields a complete global classification in an explicit parameter rectangle. Input-independent parabolic constants and an exact signed-swap window distinguish global dynamics from endpoint linearization and from diagonal-masked repulsion; they give a concrete benchmark for analytic attention dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
