---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The mathematical proof is in RESULT.md. In the noncontractible range, verify the face condition for the link of the central vertex, the contractible cone cover of the missing-near-vertex part, and the relative-chain boundary contraction. The latter identifies the actual integral lattice, avoiding reliance on coefficient-field calculations. The homotopy wedge follows from the same decomposition and the simplex-skeleton homotopy type.

Execute `python3 check_subdivided_star.py` from the extracted directory (Python standard library only). The checker constructs every face from the induced-component condition, reduces all boundary maps modulo two, and independently computes signed Lefschetz traces for all permutations of the arms for five small arm counts. The observed successful output is `PASS: 30 independent mod-2 chain homology tests; 1438 signed Lefschetz-character tests.` These are finite consistency checks, not a proof for all parameters nor an integer Smith-normal-form calculation.

The theorem assumes equal arms of two edges, at least three arms, and thresholds at least two. The rational character checks cannot on their own determine an integral group-action lattice; the direct relative-chain identification in RESULT.md does. Independent mathematical validation has not been performed.
