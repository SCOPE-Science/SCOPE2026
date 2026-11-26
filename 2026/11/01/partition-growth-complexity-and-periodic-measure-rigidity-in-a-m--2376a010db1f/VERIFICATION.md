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

The consecutive-marker condition is local in forbidden blocks; zero extension proves sufficiency for each finite word and creates no new marker triple. For span s between the extreme ones, the sorted positive gaps are an arbitrary partition of s, with n−s placements; s=0 handles a single one and the all-zero word is separate. This gives c_n and C(z). In the Hardy–Ramanujan sum c_n−1=Σ_r r p(n−r), the r/√n window has limit kernel u exp(−a u/2), a=π√(2/3). For r≤n/2 the ratio p(n−r)/p(n) is uniformly bounded by a constant times exp(−ar/(2√n)); the remaining contribution is at most n²p(floor(n/2))=o(np(n)). The integral is 4/a², giving the asserted constant, entropy zero and dimension 1/2. Periodic gaps must be equal cyclically, so each q|n contributes exactly q nonzero points in one orbit and the zero point contributes once. The Euler product for ζ then yields the first differences including n=0. Any strictly increasing successive-gap pair occurs at most once; constant-gap supports with an endpoint are also nonrecurrent (use a run of at least q zeros immediately beyond the endpoint, where q is the common marker distance). Poincaré recurrence on a countable cylinder basis therefore puts all invariant measure on the disjoint periodic orbits, with uniquely determined uniform-orbit masses. An independent enumerator matched all finite words through length 16 and cyclic states through length 12, as well as first differences through index 15; the ratios to the leading asymptotic at n=200,400,800 were approximately 0.9955643, 0.9969964, 0.9979437. No frozen script was executed.

## originality

PASS

The distinct claim is the exact simultaneous realization of the partition word count, its first-difference identity with the periodic zeta function, and periodic-point/measure rigidity for one specified two-sided shift. Partition asymptotics and the zeta product over primitive periodic orbits are classical inputs. Exact nearby results for single words, partial maps, and other symbolic growth constructions do not give the same object or identity. The named increasing-gap paper remains incompletely accessible; this is a best-of-knowledge finding, not a priority guarantee.

## value

PASS

This one elementary shift provides an exact comparison between substantial but subexponential word growth and entirely periodic invariant measures. In addition to the growth scale, it gives a sharp asymptotic constant and a coefficient identity tying the periodic zeta function to the full language. The identity is more informative than a proof that systems with entropy dimension 1/2 exist, and the example can be used to separate language growth from the behavior of all invariant measures without a fitted parameter sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
