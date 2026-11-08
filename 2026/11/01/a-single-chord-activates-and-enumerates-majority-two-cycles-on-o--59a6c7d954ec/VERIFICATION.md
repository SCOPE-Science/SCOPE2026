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

On a primitive two-cycle in strict-majority-with-tie-inertia dynamics, a flipping degree-two vertex forces both its neighbours to flip. Hence each chord-endpoint path interior either flips entirely or is stable; the two degree-three chord endpoints must flip in any nontrivial orbit. This leaves exactly endpoint-only, one-full-path, or all-vertices flipping masks. Stable paths with both endpoints flipping are precisely binary words whose constant runs have length at least two, with a one-interior-vertex length-two special case. Compositions into k runs give binom(ell-k−2,k−1), partitioned into U_ell (odd runs) and V_ell (even runs). Endpoint parity conditions then yield N=2(U_dU_m+V_dV_m)+2[1_d_odd(U_m+V_m)+1_m_odd(U_d+V_d)]+1_n_even. Standard rational run generating functions produce the stated Fibonacci and six-periodic correction. Bare odd rings cannot alternate, while any legal chord has ≥4 orbits by explicit classes. Independently enumerated actual bit updates over ALL n=4..12 and legal chords and found exact agreement in three flip-mask classes; finite checks corroborate the all-n mask-and-run proof.

## originality

PASS

Best-of-knowledge novelty is the exact labelled temporal two-cycle count for one-chord cycles and its three-mechanism/Fibonacci structural law. Goles/Olivos prove universal eventual period≤2, not a count by one chord separation in accessible abstract. Benjamini et al extend majority dynamics to graph classes with period bounds, not a chord census. Nakar/Ron classify homogeneous one-dimensional cyclic local rules, whereas the chord changes vertex degrees and their update rule at two marked sites. Resultary exact query returned unrelated periodic systems, no dominating count. The Goles original full article was inaccessible (authorized Oxford vpn_disconnected); this alone is not a scientific failure, but remains a material originality risk.

## value

PASS

Adding one chord is the minimal topology-changing perturbation of an odd majority ring and creates temporal oscillations where the unchorded ring has none. The exact census for every legal n,d, with disjoint mechanisms and Fibonacci/six-periodic behavior, is a natural infinite family classification rather than an arbitrary finite sample. It gives a meaningful quantitative answer to how one edge changes recurrent dynamics, without claiming basin sizes or more chords.

The dated certificate retains the supplied scientific assessment, sources and limitations.
