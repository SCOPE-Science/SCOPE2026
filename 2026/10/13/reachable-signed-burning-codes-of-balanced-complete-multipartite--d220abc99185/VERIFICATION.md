---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For every complete multipartite graph with r>=3 nonempty parts and balanced signing, a switching gauge epsilon transforms the signed process to the all-positive one. After first ignition x in part P, next simultaneous spread burns every vertex outside P with the same color; at most one additional vertex v within P can be ignited in the opposite color before the last spread, and this is possible precisely when P has size at least two. This proves the full terminal code {+/-epsilon} union {(+/-epsilon)^(v):v in nonsingleton parts}, cardinality 2+2m, and the unsigned weight enumerator 1+z^N+m(z+z^(N-1)). For an arbitrary sign word w the distance to the unsigned code is t-delta(w), t=min(number of positive,number negative) and delta=1 iff an eligible coordinate lies in a smaller sign class; optimizing gives radius floor(N/2) if m=0, N/2-1 if m>0 and N even, and for odd N=2h+1 gives h if s>=h else h-1. The claimed plurality formula then follows from gauge coordinate flips. Independent state-space exploration of all legal spread-first/ignite-after trajectories for 1,044 balanced-signature cases to N=6 corroborated the formula; the universal three-round argument provides the infinite proof.

## originality

PASS

The source process, gauge-equivariance and covering-radius/plurality correspondence belong to Fallat–Gupta–Khodamoradi–Zilles; the specific complete-multipartite terminal code, exact weight enumerator and singleton threshold require a nontrivial graph-family specialization, not just quoting those general propositions. Resultary searches reveal other complete-multipartite colorings but different processes. The exact 2026 primary article is highly relevant yet full text could not be lawfully accessed (arXiv/OA attempts unsuccessful; authorized Oxford download blocked by VPN); its unread contents are expressly not labeled noncovering. Based on accessible abstract, surrounding literature and independently reconstructed result, best-of-knowledge O PASS with MATERIAL primary-source coverage risk, subject to renewed full-text comparison.

## value

PASS

The complete set of reachable terminal colorings is the new central invariant in signed-burning dynamics, and complete multipartite graphs offer a natural dense graph family. The theorem determines every reachable word and signaturewise plurality as well as a sharp singleton-count phase boundary in Hamming covering radius. This is a nontrivial natural classification, not a mere numerical exercise or a renaming of known switching equivariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
