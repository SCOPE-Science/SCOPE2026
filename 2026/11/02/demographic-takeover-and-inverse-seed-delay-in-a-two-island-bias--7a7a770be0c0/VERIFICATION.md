---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For deterministic two-island bias-one no-self-weight map B(z,s)=zs/[zs+(1-z)(1-s)], drift sign is that of s-1/2. Starting (x,1-x), 1/2<x<1, both drifts are nonnegative for r>=h and nonpositive for r<=1/h, with strict drift by the second iterate even at equality; cooperative monotonicity and exclusion of interior coordinate limits force consensus (1,1) or (0,0). The polarized corner has diagonal multipliers 1/(hr),r/h, so for 1/h<r<h it attracts a neighborhood of complementary data. At r=h, writing e=1-u and v the minority opinion, the exact 1/v reciprocal increment is 2(1-v)(v-e)/[v(1-e+v)]. Geometric decay e<=delta q^t and telescoping yield T_eta(delta)=(2delta)^-1+O(log(1/delta)) for fixed h,eta. Independently numerically checked h=1.5 and h=3 at delta=0.005,0.001, obtaining delta T near 0.52 then 0.505-0.506; exact drift/reciprocal identities were also checked from algebra. This is not a theorem for stochastic/heterogeneous networks or uniformly h->1.

## originality

PASS

Best-knowledge PASS for the inclusive unequal-size demographic global takeover and universal inverse-seed delay. Dandekar–Goel–Lee analyze equal-sized homophilous islands r=1; their polarization theorem is not an unequal-size takeover theorem. Xia et al. treat stability and consensus for broader networks, and local corner multipliers are credited, but their inspected local stability result and all-one-side consensus premise do not imply an initially opposed two-island global r>=h criterion or the 1/(2delta) critical-time law.

## value

PASS

The sharp demographic/homophily phase boundary, inclusive critical equality, basin sharpness and asymptotic delay describe substantive dynamics of a canonical sociophysical model. The inverse-seed scaling gives a nontrivial slow critical regime beyond routine Jacobian linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
