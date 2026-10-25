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

# Reproduction of the exact finite checks

Run `python3 heawood_induced_forest_verify.py` with Python 3.8 or later and the standard library. A successful run ends with the literal text `VERIFY_OK`. All results are generated from the seven Fano lines \(\{t,t+1,t+3\}\) modulo seven, not external data files.

The checker performs both induced-forest face tests on all 16,384 masks, verifies the complete face vector, constructs and checks every Morse pair, checks all 81,648 oriented incidences for acyclicity by topological sorting, constructs all 168 matrices in \(\mathrm{GL}_3(\mathbb F_2)\), checks graph incidence preservation, computes the signed simplicial Lefschetz character and matches it term-by-term with the building graph's first-homology character. It checks that the character is irreducible and has no invariants. The attached `heawood_induced_forest_verify_output.txt` is the recorded expected run output.

The Morse theorem and the character argument turn those finite checks into the particular integral homotopy and rational representation conclusions. The check establishes no corresponding universal graph theorem, does not provide a canonical equivariant equivalence of spaces, and is not an independent external audit.
