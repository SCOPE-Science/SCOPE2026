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
# Verification record

The self-contained scientific program `verify.py` requires Python 3 and SymPy. Execute `python verify.py` beside this document. It uses exact symbolic coefficients and prints three `VERIFIED` lines if all assertions pass. It checks all independent triples from twelve signed distance inequalities, exact whole-interval slack feasibility, the eighteen dual vertices, the twenty-eight norming pairs, ten dihedral tensor orbits, ten explicit decompositions, the piecewise crossing identity, and each of the twenty-eight numerical-radius inequalities for both sharp operator families on their full parameter ranges. Its inequality routine checks endpoints and algebraic real derivative-critical points of polynomial numerators, not a sampled parameter grid.

The argument for arbitrary real \(t\in[1,2]\) requires the finite-dimensional extreme-pair reduction and the group-orbit completeness proof in `RESULT.md`, in addition to the checked identities. The checker is not independent scientific validation; the real-field/metric-family restrictions and bibliographic risks are recorded in the result.
