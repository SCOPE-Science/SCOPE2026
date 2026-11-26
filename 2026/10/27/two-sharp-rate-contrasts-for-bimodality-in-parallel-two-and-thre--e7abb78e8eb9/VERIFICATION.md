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

With x=bt and k=a/b (a rate ratio), the component derivatives are w k²e^(−kx)(1−kx) and (1−w)xe^(−x)(2−x)/2. They have a common sign outside the open interval joining the component modes, so only interior odds intersections matter except for the coincident modes at k=1/2. Log-differentiating their absolute ratio gives N_k divided by x(kx−1)(2−x), whose denominator is positive in the interval. Independent symbolic algebra reproduced the discriminant 4(2k−1)²P(k) and exact real-root isolation for P; the rational transforms in the proof give one root below 1/2, none from 1/2 to 1, and one above 2. For k<k_− exactly one cubic root is below the interval: N<0 on x≤0 and N is increasing on [0,2] with opposite endpoint signs. N is positive and increasing from 1/k onward by its first two derivatives there. For k>k_+, an omitted justification in the written proof is that N_k(−x) has coefficient signs +,+,+,−, so Descartes gives exactly one negative root of N_k; convexity on [0,1/k] and decreasing negativity from 2 onward then put the other two roots inside the interval. This omission does not alter the claim. At a threshold the two roots coalesce in the interior (the endpoints are nonzero and a distinct off-interval root persists). The odds curve remains strictly monotone at that double root; k=1 is handled directly by N=−x²+2x−2. With two simple turns, precisely the odds levels strictly between their heights have three transverse intersections, giving max/min/max from the endpoint signs of the hydrograph derivative. An equality level adds only a non-extremal tangency. The given k=3 example has its middle root exactly at x=1, where N_3(1)=1>0, and two outer sign crossings; the independent numerical checks give 0.54843840694 and 1.70584152814. Replay: /workspace/branches/independent_small_checks.py; the supplied verify.py was read, not executed.

## originality

PASS

The full unequal-shape, unequal-rate slice has a new explicit pair of rate contrasts to the best of the inspected evidence. The hydrograph model, the gamma mixture and the generic odds/turning-point technique are not new. The best-matching general theorem supplies only the weights once the turning-point problem has been solved, not the global classification of when two turns exist.

## value

PASS

The adjacent small Erlang shapes 2 and 3 are the first distinct series depths for which both individual modes are strictly interior. The two separate rate regimes, closed all-weights unimodality region and exact necessary-and-sufficient mixing windows resolve a concrete peak-splitting question in this natural model. The result does not claim a new physical routing model or field validity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
