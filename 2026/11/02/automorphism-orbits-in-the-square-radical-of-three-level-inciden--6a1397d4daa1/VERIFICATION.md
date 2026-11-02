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

# Finite computational verification

Run `python3 verify.py` with a standard-library Python 3 interpreter. The program independently compares coefficients of the rational Burnside formula to directly constructed projective-multiset orbits, for seven alphabet sizes and several widths. It separately enumerates the complete orbit partition of actual two-row finite-field matrices under row swaps, row and column nonzero scalings, and column permutations, for eight small configurations; the nonprime field is implemented explicitly as `F_2[z]/(z^2+z+1)`. Finally, it checks the width-two closed formula for eight values of the field size.

The program reports `INCIDENCE_LOEWY_ORBITS_OK 23 independent parameter checks`. Matrix orbit counts (rank zero, rank one, rank two) include \((1,4,2)\) for \(q=2,t=2\), \((1,6,9)\) for \(q=3,t=3\), \((1,6,10)\) for \(q=4,t=3\), and \((1,4,4)\) for \(q=5,t=2\). This is finite verification only: it does not constitute a proof of the all-parameter result or a publication-priority certificate.
