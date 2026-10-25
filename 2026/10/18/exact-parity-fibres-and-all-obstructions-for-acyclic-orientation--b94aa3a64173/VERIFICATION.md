---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For F_n=K1∨P_n, n>=2, summing indegrees gives necessary hub plus path parity =1 mod2 and fixed parity yields exactly 2^(n-1) unrestricted orientations by free choices of all n-1 path-edge directions. Define spoke s_i=0 for h->v_i and path e_i=0 for v_i->v_{i+1}, with e_-1=1,e_(n-1)=0. The identity p_i=s_i xor e_(i-1) xor e_i is exact at both endpoints. Every directed cycle in a chordal fan has a directed triangle; triangles are exactly h v_i v_(i+1), and a switch s_(i+1)=1-s_i is forbidden only when e_i=s_i. This yields the supplied 4-state DP. Directly checking the support-transition table from initial C gives C:0->U,1->A; A:0->B,1->C; B:0->A,1->U; U absorbing. Only support A lacks terminal odd xor, reached after odd processed length precisely by p0=1 and paired equal internal parities. Hence even-n obstruction p0=p_(n-1)=1,p_(2j-1)=p_(2j); counts 2^(n/2−1). Independent literal orientation enumeration with topological sorting, separately coded from source verify.py, checked n=2..8: 32768 orientations and 256 parity signatures at n=8, 8 excluded; sum acyclic 2*3^7=4374. Universal proof is structural, not finite inference.

## originality

PASS

Gravier–Petiteau–Sivignon 2026 treats acyclic orientations with parity constraints and necessary P/source/sink conditions, with published abstract emphasizing Cartesian products of paths/cycles, not fan-specific exact transfer counts. Its complete text was not obtainable through arXiv/OA here; authorized retrieval returned vpn_disconnected, so no whole-document exclusion is claimed. The stronger universal acyclic-orientation enumeration via chromatic polynomial yields only the unconstrained sum. Resultary published SCOPE fan dissociation polynomial and complete-graph-matching parity results involve different invariants/graphs. Best of knowledge PASS retaining the plausible unavailable paper as residual priority risk.

## value

PASS

Prescribed indegree parity plus acyclicity is a nontrivial orientation problem; a sharp complete existence criterion and O(n) exact fibre-count recurrence for a natural chordal fan family supply more information than total acyclic-orientation counts. The parity-only obstruction is a motivated mathematical boundary and the multiplicities are available for any labeled n, not an arbitrary tiny slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
