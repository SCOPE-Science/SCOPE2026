---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For rate-one independent edges on a path, mapped U_i=1-exp(-xi_i) are iid uniform priorities. The boundary-empty probability h_m(u) satisfies h_1=1 and h_m(u)=1-∫_0^u h_{m-1}(v)dv by conditioning on the unique incident boundary edge, hence the exact alternating polynomial H_m. Conditioning on edge-i priority u leaves two independent subpaths and proves P(A_i=1,xi_i>t)=∫_{1-e^-t}^1 H_i H_(n-i)du. Alternating Taylor remainder bounds |H_m-exp(-u)|≤1/m! and summing 1/m! yields mean e^(-2-x)+O_K(1/n) for t=logn+x. Recursive greedy blocking has a decreasing-priority predecessor chain; crossing radius-L requires a monotone chain, giving ≤2/(L+2)!, union O(n/(L+2)!). For L=ceil(log n), distinct late marked successes are ≤e^-2t even if acceptance depends; distance>2L windows use disjoint input edges, so dependency-graph Chen–Stein yields O(logn/n) count TV. Mixed factorial moments of disjoint bounded spacetime rectangles have separated tuples plus O_k(L/n) close tuples; independent windows and first moments identify marked PPP e^-2 du e^-x dx. Upper and lower truncation in centered time justify last-k spatial marks and time ordering. Independently enumerated all edge orders through n=8 and integrated H_iH_(n-i) exactly at t=0. This does not itself prove limiting PPP.

## originality

PASS

De Smedt–Godrèche–Luck Section 5 already covers the scalar Gumbel jamming time at density one and factor e^-2; it must remain disclaimed. Full Gerin primary text supports last-deposition log-scale/localization but does not state the spatially marked Poisson field or the stated uniform Chen–Stein total-variation rate. Other deposition work contains tools and broad models rather than a proved implication to this marked limit; originality assessed only for these additions.

## value

PASS

The late-arrival process for the natural Page–Rényi parking model gains precise space-time extreme geometry, unlike a scalar completion-time law. Quantitative TV approximation and an exact finite-edge marginal are useful for rigorous extreme-position statistics and error bounds; the final k dimers acquire asymptotically independent uniform locations. Strong mathematical motivation is the natural one-dimensional random maximal matching dynamics and known jamming-time question, not an arbitrary finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
