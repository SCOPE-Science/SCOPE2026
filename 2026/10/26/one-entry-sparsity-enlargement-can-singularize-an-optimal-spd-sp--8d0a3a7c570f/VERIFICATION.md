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

The unique minimizers separate by columns. For A0, leading principal minors 1,2,2 establish SPD, while squared column norms 3,35,126 yield positive diagonal M0. The enlarged second-column normal equations [[3,9],[9,35]]c=[1,3] give c=(1/3,0), making M1 rank 2; exact residuals 509/315 and 97/63 differ by 8/105. In n=2, a full-diagonal-plus-one-offdiagonal pattern remains triangular with both diagonal entries positive (untouched diagonal SPAI coefficient and positive diagonal of A inverse), proving minimality. For A_epsilon, det A=2-8e-e²>0 on (0,sqrt(18)-4); symbolic least squares gives c1=(e²+7e+8)/(2(e²+6e+12)), c2=-e/(2(e²+6e+12)), det M1=-5e/[3(e²+6e+12)(e²+10e+126)] and positive squared objective gap (e²+7e+8)²/[2(e²+6e+12)(e²+10e+35)]. Rank-two limiting AM1 with nonzero singular values bounded away from zero and determinant Theta(e) implies minimum singular value Theta(e), hence condition number Theta(1/e); diagonal baseline and A remain uniformly conditioned. Independently re-derived all polynomial formulas with SymPy, checked five rational parameters and algebraically verified the 2x2 diagonal positivity; these bounded checks are not proofs of the asymptotic statement.

## originality

PASS

The known generic Frobenius SPAI construction, one-index residual descent, and arbitrary-pattern possible singularity are prior art, especially Ferronato (2012). The assessed claim is the stronger exact minimal-dimensional SPD diagonal-plus-one-entry obstruction and a nearby uniformly SPD family for which the improved exact Frobenius objective accompanies an unbounded relative preconditioned condition number. Full materially relevant 1997, 2010, and 2012 primary texts were compared at claim and implication level; no exact covering theorem or example was identified. Unindexed historical priority remains a real risk, not settled by negative searches.

## value

PASS

A nonsingular effective preconditioner is required for equivalently solving the original system. The precise minimum-dimensional one-entry support obstruction and a robust family with strict objective improvement but unbounded preconditioned spectral condition provide a motivated structural boundary for Frobenius approximation criteria. This is a nontrivial failure of a tempting monotonic-stability inference, not a claim that adaptive implementations necessarily select the entry, nor a numerical frequency prediction. The unbounded-conditioning perturbation complements the sharp exact rank collapse and clarifies why small-residual invertibility bounds are needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
