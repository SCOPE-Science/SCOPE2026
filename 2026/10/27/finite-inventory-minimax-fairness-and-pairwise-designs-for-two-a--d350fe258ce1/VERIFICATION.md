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

For a binary support of size t, the first MMS is h=ceil(t/2). With a uniformly drawn costly pair for the second agent, a deterministic first choice with q costly chores gives payoff b_q+(2-b_q)^+ (t-q)(t-q-1)/(t(t-1)), where b_q=max(1,q/h). This is strictly decreasing up to h; beyond h its successive differences times h are 1-(t-q-1)(3(t-q)-2+2(2h-t))/(t(t-1))>0. It has a unique minimum at h; averaging over seeds yields a fixed input pair, so the lower bound uses only oblivious adversaries. A pair-balanced retained r-set, r=t-h, gives an upper bound for all second supports by binning them in pairs or singletons, and zero-support agents cause no exceptional cost. Consequently the worst pair forces equality of all pair-retention probabilities and the unique minimizing size forces |S|=r. Extra zero-cost chores do not affect the lower-bound pair; the upper policy assigns them to agent one. Maximizing over support sizes uses the increasing even subsequence and the smaller following odd values, giving the frozen R_m. The affine construction has exactly 2(t-1) hyperplanes and the required probability, with rejection sampling costing O(log t) expected fair flips. The printed rank calculation is for even t only; the same proof works verbatim in matrix form for every t≥4: summing the common pair probabilities against a fixed item yields diagonal r/t (since r>1), giving eigenvalues r(t-r)/(t(t-1)) on the orthogonal complement of the all-ones vector and r²/t on its span. Full rank gives the stated support bound also for odd t. Independent exact arithmetic for t≤12 corroborated lower and upper bounds but is not needed beyond the proof.

## originality

PASS

Pass is for the full finite-support frontier together with the equality characterization of all optimal policies in the all-positive case and its sparse-sampler consequences. The closest paper has the same lower-bound family and upper pair-block argument, with exact finite hypergeometric terms that nearly give the even-size refinement. It gives the limiting optimum, not the all-sampler equality theorem or the full parity-sensitive fixed-support statement. The affine hyperplanes and the rank method themselves are standard design theory, not asserted as new combinatorics.

## value

PASS

The exact finite minimax law resolves the small-inventory cases hidden by the asymptotic 5/4 guarantee. The equality theorem identifies exactly how much balancing an optimum needs; the support lower bound and sparse construction provide an actionable reduction from exponentially many candidate blocks to linear support on powers of two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
