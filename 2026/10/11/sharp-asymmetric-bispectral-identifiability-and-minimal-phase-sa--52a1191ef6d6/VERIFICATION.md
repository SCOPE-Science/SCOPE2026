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

# Exact verification

The derivation uses only character multiplication on the nonzero Fourier support. The package includes `bispectrum_asym_check.py`, which independently constructs **all** permitted bispectral addition relations for every tested triple, constructs the proposed minimal data packet, and evaluates both integer Smith normal forms. The checker verifies the predicted lattice quotients, exact ranks, sample counts, and wrap arithmetic. Run `python3 bispectrum_asym_check.py` with Python 3 and SymPy installed.

Recorded execution on the included source:

`VERIFY_OK cases=1522 continuous=435 discrete=1087 exact_lattice_relations=310585 all_packets_rank_and_snf=PASS`

The exact computations cover only \(5\le n\le28\). The unrestricted claim follows from the explicit proof of phase propagation and wrap impossibility/necessity, not from the finite tests. The theorem does not address Fourier coefficient zeros within the specified support, noise, or the case where the power spectrum is not already known. The originality comparison has residual historical coverage risk, and no independent audit has taken place.
