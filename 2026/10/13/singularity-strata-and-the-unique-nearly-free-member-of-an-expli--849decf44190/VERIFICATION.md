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

# Verification

The companion `verify.py` checks exact symbolic identities for the four quadrics and all six pairs, including all moving-conic discriminants. It checks the two special nonordinary triple contact patterns by truncated formal power series, tests all stated exceptional triple-point incidences, confirms the degree-three Jacobian syzygy, and certifies full rank for the degree-one and degree-two syzygy matrices over the prime field of order \(1000003\). That last full-rank test is a valid proof of injectivity over characteristic zero for an integer matrix, not an extrapolation from a sample.

The local-type conclusion uses the standard analytic equivalences between two smooth branches of intersection multiplicity \(m\) and \(A_{2m-1}\), three transverse branches and \(D_4\), and the local equality \(\mu=\tau\) exactly for quasihomogeneous plane curve germs. Counting is exhaustive through all six conic pairs, with Bézout total \(24\) pair-incidences. The near-free conclusion invokes the established degree-eight numerical characterization, not a computational heuristic. The computation is reproducible by running `python verify.py` with SymPy \(\ge1.12\); it does not constitute independent external validation.

**Explicit limits:** The singular fourth conic at \(t=-1\) is outside scope. The two contact-pattern triple germs at \(t=0\) are described by pairwise intersection multiplicities, rather than assigned a nonexistent ADE type. Bibliographic completeness beyond inspected accessible sources is not certified.
