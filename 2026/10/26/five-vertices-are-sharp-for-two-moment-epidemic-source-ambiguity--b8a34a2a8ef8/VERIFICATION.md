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

The two independent arm lengths have tails p^j, with mean and second moment obtained by summing p^j and (2j-1)p^j respectively, as claimed. The expected size is strictly increasing in p; moving one step centerward changes it by p^k-p^{n-k}>0 before the center, so equality for known p identifies the reflection orbit. The full law identifies p from its all-open atom. For n=3 and 4 an independent component-interval reconstruction with exact probabilities p^(internal edges)(1-p)^(boundary edges) and factorial moments reproduced both equal-mean variance identities by polynomial remainders. The n=3 identity is strictly positive; at n=4 equal means force q<p and 1+2p>1+p+p², giving strict positivity. At n>=5 match means uniquely with q(p)<p for arms (1,m) and (2,m-1), m=n-2, since the latter mean at the same p exceeds the former by p²-p^m. The small-p expansions give q=p-p²/2+O(p³) and variance gap -2p²+O(p³). Near p=1, a single failed edge truncates one arm by a loss j, with each j on that arm available once to first order, yielding A=sum j in the mean deficit and B=sum j² in the variance. At equal mean near n the gap sign is that of B1/A1-B2/A2, strictly positive because A1-A2=m-2 and B1-B2=(m+2)(m-2), while B2/A2<=m-1<m+2. Continuity gives a nontrivial collision, and sources 2 and 3 are not reflections for n>=5. Independent exact elimination using the interval moments reproduced 4p²(p-1)P(p), exact endpoint signs of the rational bracket, and the reported p, q and mean. Positivity of P' on (0,1) and the existence proof remove ambiguous and extraneous resultant roots.

## originality

PASS

The distinct supported finding is the sharp order-five boundary for unequal-parameter, two-population-moment ambiguity of the source orbit, plus persistence for sources 2 and 3 at all larger orders. The strongest inspected same-model overlap is a later same-parameter variance crossover; known forward laws, fixed-parameter comparisons and mean-field identification do not cover this inverse claim.

## value

PASS

Even with a known path and exact population moments, estimating a source orbit with unknown edge retention has a sharp loss of structural identifiability. The mechanism is the sign reversal of the variance contrast after equalizing the means, not sampling noise. The comparison to known retention and the full size law specifies exactly which observation loss is responsible in this model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
