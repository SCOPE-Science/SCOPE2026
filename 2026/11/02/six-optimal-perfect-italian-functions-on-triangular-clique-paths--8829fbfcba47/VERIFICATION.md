---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each graph K_3 square P_n, n>=4, a zero in the middle of three columns a,b,c has total neighbor weight w(b)+a_r+c_r, so the zero-vertex condition equals exactly 2 for every zero row. This gives an exact 27-column alphabet and 729-pair min-plus/tied-count transfer automaton with boundary phantom zero columns. Independent construction from scratch found 306 reachable ordered pair states and EXACT full-state D14=shift_1(D13), with base minima and multiplicities (n+2,6) for all n=4..14. The transition and terminal acceptance commute with uniform shifts, so this finite exact identity extends the optimum and six minimizers inductively for all n>=4, not by finite extrapolation. The six explicit row-permutation periodic assignments have weight n+2 and satisfy each zero-neighbor equation; since the counted number of minima is six there are no other minima or label-2 minima. n=2,3 excluded.

## originality

PASS

Best-of-knowledge PASS after comparing the actual complete 2024 original article text, the 2019/2023 product theorem and the original perfect Italian 2-fair equivalence. No prior inspected theorem determines both gamma_I^p(K3 square Pn)=n+2 for every n>=4 and exactly six optimal labeled functions; natural rigidity and all-length complete count survive.

## value

PASS

The infinite family K3 square Pn is the first three-row triangular clique strip beyond the prism and adjacent path-product families. Its exact minimum plus complete six-function rigidity is a natural extremal enumeration, not just a generic dynamic-programming recipe or a trivial isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
