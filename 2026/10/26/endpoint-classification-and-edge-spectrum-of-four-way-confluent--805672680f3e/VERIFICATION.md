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

Under left-to-right composition the forward condition propagates a nonempty row upward in source index and orders row maxima; downward propagates the other way and orders row minima. Backward and upward give the same two tests on columns. Conversely the appropriate extreme is a witness in each condition. The empty relation is separate. For given extrema, the intersection P of the row and column intervals contains all possible cells; requiring the row and column endpoint cells F makes each nonempty choice preserve exactly those extrema. Hence each feasible quadruple gives the stated binomial contribution, without overlap. Starting at the identity, adding an upper-diagonal edge (i,j) raises a row max to j, which the successor row already reaches when it exists, and lowers a col min to i, which the predecessor column already reaches from above when it exists; the other extrema stay fixed. The lower-diagonal insertions are the transposed argument, so every size between n and n² occurs. At n edges one gets an increasing permutation, necessarily the identity. Fixing the first and last rows and columns makes all interior bits free for n>=2 and gives the required entropy squeeze. Independent raw witness tests agreed for all matrices through order 4; a separate row-mask DP tracking first and last occupied rows in each column gave 2,5,34,538,23415,3567130 for orders 1–6. Replay python3 /workspace/branches/4bb26c7c-5703-4f23-8659-cc8a008bea47/four_way_direct_check.py and python3 /workspace/branches/4bb26c7c-5703-4f23-8659-cc8a008bea47/four_way_count_reproduction.py 6.

## originality

PASS

Credit the existing individual and pair confluence normal forms: the four-extreme characterization follows already by combining the published row-pair characterization with its transpose, where transpose interchanges forward with backward and downward with upward. Do not count the endpoint observation itself as a new theorem in isolation. The verified distinct content is the exact joint edge-count enumerator and finite census, and the all-order edge spectrum for the intersection. The strongest inspected adjacent fiber count concerns observational equivalence of arbitrary relations; it does not impose the joint column constraints or enumerate this intersection.

## value

PASS

All four confluences come from a natural modal frame problem, and their intersection has markedly different finite counts from either known pair. The joint polynomial gives exact conditioning on the edge budget, the sharp spectrum eliminates any further numerical edge-count obstruction, and the entropy limit quantifies the large difference between local restrictions and global matrix freedom. These are useful finite-chain statements, not claims about modal decidability or asymptotically sharp enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
