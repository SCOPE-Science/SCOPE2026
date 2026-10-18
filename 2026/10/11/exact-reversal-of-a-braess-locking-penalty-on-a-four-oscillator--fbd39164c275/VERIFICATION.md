---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

At equilibrium the interior balances force equal sine flows on all path links. Branches with a flipped path cosine have explicit negative directions of the quotient Hessian, so cannot be strictly stable. The all-cohesive angle t has scalar flow (1+3a)s-4as^3 (s=sin t), with strict stability precisely 1+3a-12as^2>0. Maximizing on s in (0,1) gives sup=1-a for a<=1/9, and (1+3a)^(3/2)/(3 sqrt(3a)) beyond; reciprocal yields exact Kc, stable states approach but do not require inclusion at marginal endpoint. Independently symbolically differentiated log Kc=(1-6a)/(2a(1+3a)), located maximum a=1/6 and numerical larger crossing a=0.40889386563522584. The supplied verifier is a finite diagnostic rather than universal proof.

## originality

PASS

Best-of-knowledge PASS for the complete all-a edge-weight threshold and exact beneficial switchback, distinguishing prior unweighted ring/chain comparisons and general perturbation formulas. A fully read primary 2016 four-oscillator counterexample uses a different cumulative frequency vector and only ring-vs-chain comparison. Arches et al and Manik et al supply general methods/qualitative Braess effects, but an exact formula at these frequencies is not inferred from accessible statements. Hidden routine specialization of general cycle-flow work is an explicit residual risk.

## value

PASS

The mathematical question is naturally posed by adverse first-order edge sensitivity: can a qualitatively harmful infinitesimal edge eventually improve locking? A complete two-regime sharp threshold and unique inversion weight for the minimal cycle answer this exactly, including the multiply marginal path endpoint, not merely another simulated counterexample. Scope is strict transverse linear stability only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
