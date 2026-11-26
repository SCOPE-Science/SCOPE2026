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

On a simple cycle each zero has one zero neighbor by restraint and must have a 3 as its other neighbor. Hence all zeros occur in pairs, and each intervening positive run begins and ends at 3. Relative to length including the preceding zero pair, a singleton run 3 has excess 0, and any longer run costs at least 2 extra. Equality in the latter bound forces all interior labels to be 1; precisely 33, 313 and 3113 qualify. At optimum the total excess is zero for 3|n and two otherwise; reducing the length of the unique longer run modulo three selects 33 or 313. With no zeros, the set of 2/3 vertices dominates and adds at least ceil(n/3) above n. Only n=4,5 can tie in the nonzero residues: one 3 cannot dominate, whereas two 2's work at any pair on C4 (six choices) and exactly at the five nonadjacent pairs on C5. The periodic word has period three; the single 33 or 1 marker makes the defect words full period. Reversal gives a rotation, and the no-zero extra orbits are identified by pair distance. Replacing coefficients 3j by 3 for j>=2 in the baseline sum of n t^n gives the stated subtraction; the two small exceptions give +6t^4+5t^5. Independent exhaustive comparison of entire winner sets at n=3..8 passed using /workspace/review_checks.py (cycles); this corroborates but is not the all-orders proof. The supplied checker was inspected, not executed; its transfer recurrence counts labeled cyclic words through a fixed index, not orbits.

## originality

PASS

Passes for the exhaustive minimizer classification and labeled and dihedral censuses, not the scalar optimum or canonical witnesses. The strongest same-problem primary source proves the optimum by reduction to a path, without classifying equality cases. Closest indexed census results concern different constraints or graph families.

## value

PASS

The full optimum set for a standard graph family is useful information beyond the invariant's value. The excess lemma explains uniform dihedral rigidity and exactly where it breaks at orders four and five; neither a table of minimum weights nor one construction reveals either phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
