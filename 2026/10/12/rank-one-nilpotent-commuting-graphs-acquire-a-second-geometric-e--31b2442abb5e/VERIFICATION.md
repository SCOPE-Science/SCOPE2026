---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

A=u phi is rank-one nilpotent precisely when phi(u)=0 and defines an incident projective point/hyperplane flag. For distinct flags commuting cannot have equal nonzero rank-one AB and BA because that would force identical images and kernels, so both cross products vanish iff mutually incident. Degree from Q in H and K through span(P,Q) is T-1, T=a+(a-1)b. Common neighbors of adjacent same-point/hyperplane flags yield a+(b-1)b-2; cross edges yield (q+1)b+(b-q-1)c-2. Their difference q c((q-1)c+1)>0 for n>=4. Such cross edges exist only when two distinct hyperplanes can contain a given line, starting n=4. Multiplying through scalar clique size q-1 gives full matrix-graph profiles. Independent binary n=4 enumeration computed 105 flags, degree 24, and lambda_s=11 vs lambda_c=7 for 630 edges of each cross/same class; n=3 geometry argument checks no cross. Finite instance corroborates uniform proof.

## originality

PASS

Boroja–Kokol Bukovšek–Stopar arXiv:2602.07467 Section 5/Theorem 5.1 provides 3x3 finite-field point-line compressed commuting graph and its single same-point/line adjacency. In dimension 4 the mutual point/hyperplane incidence graph has an additional cross edge absent at n=3; exact two local count strata are not implied by the n=3 theorem. Dolinar–Kuzma–Oblak study full commuting graph maximal distances, while Ou–Zhong study upper-triangular rank-one matrices; those differ from the all-rank-one nilpotent induced graph. Resultary semantic search found no exact higher-dimensional flag profile. Higher-rank flag-graph terminology remains an explicit originality risk.

## value

PASS

The local common-neighbor distribution is a natural graph/finite-geometry invariant, and the sharp n=4 structural transition explains failure of edge-regularity after previously studied n=3 compressed graphs. The result is an all-q,n classification of a motivated induced commuting graph, not arbitrary small-case data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
