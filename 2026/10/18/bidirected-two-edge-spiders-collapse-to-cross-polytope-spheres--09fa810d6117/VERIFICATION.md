---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For each n>=1 faces are arc sets with in/out degree at most one and no antiparallel pair; underlying undirected tree excludes longer directed cycles. The subcomplex of outer arcs C_i,D_i is exactly (S^0)^{*n}. The first selected center arc A_i or B_i has respectively C_i or D_i as a valid toggle and gives a unique relative matching of all faces outside B_n. In the oriented Hasse graph no center arc can ever be inserted, so a directed cycle fixes its center-arc set; with the pivot fixed, every other outer arc only deletes and the pivot only inserts, ruling out cycles. Since B_n is a subcomplex, the relative acyclic-matching collapse lemma gives actual elementary simplicial collapse X(D_n) searrow B_n for all n. The join orientation z=*(C_i-D_i) yields a single integral homology line in degree n-1, S_n sign under factor permutations and (-1)^n under simultaneous arc reversal. The 0/1/2-center-arc partition exhaustively gives the claimed enumerator. Independent face construction (separate from repository verify.py) enumerated every compatible face and oriented Hasse cover for n=1..7, reproduced face counts 7,41,207,945,4023,16281,63423, B counts 3^n, pair counts 2,16,90,432,1890,7776,30618 and n=7 381024 covers; all graphs acyclic. A separate free-pair deletion simulated actual simplicial collapses for n=1,2,3. Finite computations are corroborative, not the all-n proof.

## originality

PASS

Qualified best-of-knowledge originality for the genuinely branching n>=3 bidirected once-subdivided star, not for n=1,2 already treated as bidirected paths. Actual primary theorem hypotheses, graph topology, arc-face definitions and homology representations were compared. Caputi–Collari–Smith gives bidirected path and polygon results plus a suspension operation, but no direct implication of this all-n fully bidirected branching-spider simple collapse and integral S_n×C_2 sign character was identified. The older multipath homotopy paper and directed-acyclic graph comparison results concern orientations not containing the same antiparallel-arc 2-cycles. The published bidirected double-star record studies two adjacent hubs and does not subsume the one-hub two-edge-arm family. The Resultary record for the same underlying extended star concerns its discrete-Morse matching complex, a different simplicial complex. No claimed global novelty proof or assertion that failed searches establish priority.

## value

PASS

A fully bidirected once-subdivided star is a canonical single-branch-hub infinite family beyond the path cases and distinct from the two-hub double stars. Determining an actual elementary simplicial collapse for every n, rather than merely rational Betti numbers or a finite census, explains the topological cancellation of center-arc faces. The natural integral S_n-by-global-reversal character and exact full face enumerator add structural invariants relevant to study of multipath complexes of bidirected trees. The result is limited to precisely two-edge arms, but this is a motivated natural family, not an arbitrary computational slice. Proof is short and uses standard matching tools, yet the closed all-parameter classification and module action are mathematically useful as reference examples/boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
