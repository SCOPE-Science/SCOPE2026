---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

I independently rebuilt \(\mathbb F_4\), the two source generator components and all seven cyclic shifts. Exhausting all \(4^7\) messages reproduced the exact weight distribution \(1+357z^{11}+735z^{12}+1176z^{13}+1869z^{14}+2835z^{15}+3234z^{16}+3045z^{17}+2079z^{18}+756z^{19}+210z^{20}+87z^{21}\). Independently enumerating every distinct span of up to six generator-matrix columns gave counts \((1,21,210,1330,5761,12159,2205)\) and maximal column intersections \((0,1,2,3,5,7,10)\); the standard column-span formula therefore gives the claimed hierarchy. Wei duality then gives the stated dual hierarchy. These computations independently reproduce the package certificate rather than relying on its log.

## originality

PASS

The exact source preprint was inspected in full through its theory section and appendix after ordinary open full-text retrieval failed. Its appendix Table A3 row 47 gives the same \([21,7,11]\) Hermitian LCD code and generator data, while the paper studies minimum-distance bounds and LCD constructions rather than generalized Hamming weights. The 2025 index-three quasi-cyclic paper contains another optimal \([21,7,11]\) code as a Hermitian dual, but likewise gives parameters and dual structure rather than a hierarchy. Exact hierarchy searches found no prior statement of the seven values.

## value

PASS

Generalized Hamming weights are canonical support invariants used in secret sharing and higher-order erasure performance. Computing the entire hierarchy of a newly published optimal Hermitian LCD code gives substantially more structure than its minimum distance alone, and the exact dual hierarchy follows as an immediate additional invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
