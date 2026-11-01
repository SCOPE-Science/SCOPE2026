---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The checked primary Theorem 6.1 in Micalizzi–Torlo identifies the common endpoint scalar stability polynomial P_p(z)=sum_{j=0}^p z^j/j! for the specified bDeC-family variants on constant linear systems. For Q with d transient pure-birth states and one absorbing state, binomial expansion of the transient block −I+S gives A_{p,k}=h^k/k! P_{p−k}(−h), and the absorbing column equals h^r/(r−1)! G_{p−r,r}(h), G_{m,r}=sum_{j=0}^m(−h)^j/[j!(r+j)]=integral_0^1 t^(r−1)P_m(−ht)dt. Even m factors stay positive; odd m P_m and G_m,r are strictly decreasing to negative infinity and have unique positive zeros. Thus the minimum finite root set is an exact first-and-only positivity horizon for all initial probability rows. Comparison of increasing odd P roots and G_m,r>beta_m proves H_{p,d}=1 for d≥p, p/(p−1) for d=p−1 and beta_3 for d=p−2, p≥3. Fixed d asymptotics follow via the exact Taylor integral remainder, endpoint Laplace estimate and Stirling: W_0(e^(−1)) except d=1 even orders with e^(−1). Independent rational arithmetic verified 3276 entries for p=2..8, d=1..8, h∈{1/3,4/3,11/5}; it is not substituted for the infinite asymptotics.

## originality

PASS

Best-of-knowledge PASS for the exact dimension-dependent stochasticity horizon of the unmodified Taylor endpoint and fixed-dimension p-asymptotics. The underlying common stability polynomial and asymptotics of zeros of exponential partial sums are known. Finite-constraint minimum and dimension staircase are separate Markov-cone statements not implied by generic SSP constants or results for Padé/SDIRK rational maps.

## value

PASS

The exact Markov-chain positivity window is a natural and practically relevant numerical-analysis invariant. It exposes strict separation between all-generator SSP restrictions and finite absorbing-state endpoints, including two sharp finite-size staircase transitions and an unusual even/odd p split for one transient state. It is not merely a reparameterization of a known scalar stability interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
