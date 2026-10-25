---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The objects are two-dimensional pencils W of quadratic forms on F2^5 for which every one of the three nonzero rational members is a geometrically smooth quadric; not every degree-four del Pezzo surface. The polar matrix has alternating rank 4 and a unique projective radical with nonzero quadratic value exactly when each quadric is smooth. An independent Python enumeration of all 32767 nonzero form masks counted precisely 13888 smooth quadrics and, for the designated q0=4144, exactly 5760 ordered other members with q1 and q0+q1 smooth, i.e. 2880 pencils containing q0. The actual quadric_p4.cpp and orbits.cpp sources describe complete finite loops and stabilizer orbit representatives 778,792,793,808,938 with sizes (720,360,360,720,720), giving global pencil counts 9999360 and twice 1666560. Dolgachev-Duncan’s half-discriminant criterion ensures squarefree degree-five half-discriminant makes X smooth; rationally nonsingular three members exclude linear factors and possible degree-five splittings beyond irreducible (5) or (2,3). Separately, independent exact Groebner Jacobian-ideal tests over F2 on all four projective charts for every one of 31 hyperplanes of each five representatives reproduced the full smooth/singular rational-point distributions: A has 12 smooth cuts, B 15, C 9, each surface seven F2 points, with the two other representatives matching A. This geometric singularity test is over algebraic closure via ideal generation, not finite rational-point sampling. The total 13,332,480 pencil count is obtained from the inspected exhaustive code/orbit-count method, not a separate independent all-pairs run.

## originality

PASS

The published general classification of characteristic-two regular pencils and their half-discriminants is credited; exact 31-hyperplane smooth versus singular section spectra with rational counts and their weighted pencil frequencies do not appear in the inspected foundational source. Best-of-knowledge; unindexed finite-field tables are possible.

## value

PASS

The first exhaustive finite-field Bertini hyperplane-section distribution of a natural class of anticanonically embedded del Pezzo surfaces gives the exact proportions of smooth genus-one sections and shows geometrically different profiles with identical rational surface size. It is a meaningful complete classification of a natural small-field arithmetic geometry question, not a relabelling of the old normal form or an arbitrary finite subsample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
