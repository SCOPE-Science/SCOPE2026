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

For a length-n word w, sample a labeled predecessor path at successive boundaries of copies of w. The resulting path in the four-state Boolean relation R_w forces a directed cycle. Conversely a directed cycle lifts to a repeating predecessor for w^infinity, possibly with period a multiple of n. Thus count words with cyclic relations once each, not input paths, rotations modulo shift, or self-loops only. The relation automaton gives P(n)=e_I T^n f, including formal P(0)=1. For a proposed recurrence of degree d, its defect at index n=k+d is e_I T^k v for a fixed vector v. Cayley–Hamilton for the N-state matrix proves all defects vanish if they vanish for k=0 through N-1. A separate exact checker reconstructed the relation graphs and checked those defects, all class assignments and initial data, and all table counts at periods 1–8. An additional data check confirmed each of the 31 recurrences has c0=1 and exactly d initial terms starting with 1. Expanded-phase cycle detection independently agreed at all 2048 rule/period pairs for periods 1–8. All 256 rules were verified: 31 distinct eight-term vectors, max N=2375, max degree 56. Rules 7 and 25 have common prefix (2,4,5,12,22,43,79) and eighth counts 148 and 156. Within-class initial terms and recurrence therefore suffice for equality at all periods, while the sharp witness defeats every earlier prefix. Formal logarithms identify equality of these sequences with equality of the zeta functions.

## originality

PASS

The supported distinct contribution is the complete 256-rule classification into 31 all-period spectra and the sharp eight-term prefix. Rationality and the finite-state counting framework are prior theory. A distinct same-day source gives the exact Rule 110 spatial zeta function, which covers that entry but not the census. The strongest other family-level exact catalog result has a superficially identical cutoff but tests equality of a different invariant.

## value

PASS

This is a complete census of a natural small family for a standard dynamical invariant, with a minimal comparison prefix and an explicit witness. The verified tables let a researcher identify equal zeta functions or calculate higher-period counts without redoing every count, and the proof correctly distinguishes periodic outputs from equally periodic input rings. The contribution is the full certified classification, not general rationality or a count from a single cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
