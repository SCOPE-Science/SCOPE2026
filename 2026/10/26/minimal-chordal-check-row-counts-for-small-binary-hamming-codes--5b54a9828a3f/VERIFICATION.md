---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Because every nonzero F_2^r vector occurs once as a column, selecting r independent parity checks and changing basis permutes the variable columns; all presentations reduce to r basis functionals plus t arbitrary extra functionals. Four columns labeled e1+e2,e2+e3,e3+e4,e4+e1 induce an unchorded 4-cycle without extra checks. The r=5 one-extra and r=6 one/two-extra obstructions reduce to all 31/63/1953 possibilities. The source enumerator uses an exact bit-parity support graph and MCS plus PEO verification; an independent implementation used networkx chordality, covering all 1953 r=6 pairs via 37 complete coordinate-permutation orbits, none chordal. The obstructions extend to higher r by induced coordinate restrictions. Adding checks on disjoint coordinate pairs yields a true-twin blowup of intersecting nonempty subsets of <=3 groups, a chordal graph, giving matching r<=6 constructions. The finite exhaustive part is a complete finite proof paired with analytic reduction, not a sampled experiment.

## originality

PASS

Qualified PASS for first exact representation row-cost function of canonical Hamming codes; not a claim to invent chordal codes, MCS or Gaussian-elimination gains. Chen–Guo–Li–Zhu (arXiv:2610.17934, October 13 2026) introduces chordal code representations and describes general decoding; the accessible abstract does not state this Hamming-specific classification. Full same-paper arXiv/OA attempts were unsuccessful, and authorized institutional retrieval reported disconnected VPN; do NOT infer paper-wide noncoverage from abstract. A relevant unpublished example or stronger bound remains a named serious residual originality risk, but access failure alone is not a scientific FAIL.

## value

PASS

Number of additional equations needed to make a fixed parity-check code column-primal graph chordal is a natural representation/decoding complexity invariant, with code held fixed and all basis transformations allowed. The exact first four redundancy values and universal lower obstacles quantify a real tradeoff for the familiar perfect Hamming family; the classification is exhaustive across representations, not an arbitrary small matrix table. Does not assert exact h(r) for r>=7.

The dated certificate retains the supplied scientific assessment, sources and limitations.
