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

Independent reconstruction of the 14-vertex Fano incidence graph and exhaustion of all vertex subsets compared the component-size predicate to avoiding connected induced (r+1)-sets; a connected component of size larger than r contains such a set by growing a connected subset. For r=2 through 6 this gives respectively 2256, 4622, 6190, 7870, 9683 nonempty faces and Euler values −12, 2, 2, 2, −19. The threshold-three Morse matching has 2310 pairs, critical masks 256 and 10454 of dimensions 0 and 6, and an acyclic orientation of all 23884 cover incidences. One zero-cell and one six-cell attached to it give S^6. The relative certificates were independently replayed on the full current complexes, verifying unique immediate coface and maximal paired upper face, ending at the exact canonical targets: 840 pairs from I_5 to I_4 and 784 from I_4 to I_3. This proves the inclusion statements and integral homology, while the two different Euler values exclude equivalences at the adjacent thresholds. The frozen result, verification note and script were read but the uploaded script was not executed. Independent replay program and output are branches/42a22c83-6bf1-447f-8775-760848055924/audit_heawood.py and audit_heawood.out.

## originality

PASS

The checked records overlap in the exact threshold-two stage and in an S^6 homotopy type in another filtration. The verified pair of canonical higher-independence collapses under a component-size bound is not supplied by those records or the inspected broader work.

## value

PASS

The Fano incidence graph is a natural test case for higher independence outside chordal and tree families. The exact computations identify a maximal consecutive plateau at both boundaries and certify the behavior of the actual threshold maps, beyond equality of ranks or types. The comparison with the different induced-forest filtration makes the invariant and cutoff choice meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
