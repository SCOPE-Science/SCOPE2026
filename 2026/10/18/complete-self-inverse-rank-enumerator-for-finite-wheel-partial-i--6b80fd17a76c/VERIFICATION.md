---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A partial bijection equal to its inverse has an invariant domain and is an order-at-most-two permutation there. Ambient rim distances are 1 for rim adjacency and 2 otherwise, so these maps are exactly involutive automorphisms of induced rim subgraphs. On a nonempty proper domain, a marked run gives n choices of its first vertex, r!/prod(m_j!) length words and binom(n-k-1,r-1) positive gap compositions, with exactly r marked versions per labelled subset. For m_j equal-length components, t transpositions can be chosen in m_j!/(2^t t!(m_j-2t)!) ways, with a_j choices per fixed component and per paired component pair, since the reverse is forced. On the full rim the dihedral possibilities are the identity, n reflections, and one extra half-turn for even n; the empty coefficient is one. Adding a fixed hub multiplies the rim sum by z, in addition to the maps omitting it. If the hub is exchanged with v, any other domain vertex x has d(v,x)=d(0,alpha(x))=1, and its image is likewise a rim neighbor of v. An arbitrary involution on any subset of the two rim neighbors preserves all distances with the swapped pair and within the subset. The empty, singleton and pair choices give 1,2,2 per v, proving the correction in exactly ranks 2–4. Fresh bounded brute-force distance checks reproduce every coefficient for rim lengths 5,6,7, including the intermediate vector (1,7,42,86,98,54,20,8). Replay with python3 /workspace/branches/12dc9ffb-b009-43ed-b4c7-a6420659384d/independent_wheel_involution_check.py; output is reproduction-small.txt in the same directory. The uploaded checker was inspected but not executed; its n=3–9 evidence is recorded, not claimed as a fresh run. Finite checks are not the all-n proof.

## originality

PASS

The ambient graph and wheel monoid are prior; in particular the small-rank bound for a moving hub and broad partial-automorphism structure are known. The strongest checked enumerator counts all maps at each rank, not fixed points of inversion. The related cycle involution enumerator uses a different metric. Neither provides the stated involution-weighted induced-run sum and hub coefficients.

## value

PASS

This is the full inversion fixed-point statistic of a natural graph inverse monoid at all domain sizes, not a handful of small instances or only the dihedral unit group. It separates the equal-length path-component symmetries from the low-rank effects specific to the hub. For example, with the all-map polynomial the result gives the rank profile of inverse pairs versus self-inverse maps coefficientwise; the total rank data alone cannot recover that profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
