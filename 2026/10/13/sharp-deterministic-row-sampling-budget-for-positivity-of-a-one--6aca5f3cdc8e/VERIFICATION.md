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

The analytical proof reduces all admissible matrix choices to the operator interval \(0\preceq B\preceq I\) and computes the two nonzero eigenvalues of the symmetric rank-two operator \(Q\). This establishes the endpoint law for every real unit trial vector and every admissible row subset; worst-case row-selection optimality follows from averaging coordinate energies and a uniform-vector witness. The positivity threshold follows by an exact inequality rearrangement.

Reproduce the finite supplementary checks with `python3 verify.py` (Python 3 standard library, no installed dependencies required). The program checks rational matrix/projector identities, validates numerical endpoint constructions and rank-one spectral bounds for several dimensions and budgets, and tests strict inequality/equality cases. Finite checks cannot prove the universal theorem, assert exhaustive uniqueness in the literature, or give a floating-point guarantee. No independent audit has been performed.

Latest direct script execution: `VERIFY_OK rational_Q_identities= 1336 exact_rational_endpoint_witnesses= 80 nonflat_endpoint_checks= 2940 phase_boundary_checks=8`. The script uses exact rational arithmetic for the displayed projector constructions and independently checks arbitrary nonflat vectors numerically. No infinite-dimensional inference is drawn from the numerical tests.
