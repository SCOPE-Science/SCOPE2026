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
# Verification of the resource-ancestry extinction inequalities

Reproduce the finite analytic consistency checks with `python3 VERIFY.py` (Python standard library only). This program reports `PASS: 52 independent numerical algebra/series checks` when run in the checked environment. The checks include four subcritical offspring means, the first singularity and moment domain, root solutions of the generating-function equation and their independent positive Borel-series expansions, and six critical parameters testing \(-\log(1-u)-u=h\) and \(u\le\sqrt{2h}\le\sqrt{2/(\delta t)}\). All series evaluations use log-domain terms to avoid floating-point overflow.

The proof's nonstandard step is the source-marked coupling; it is verified analytically in RESULT.md by decomposing resource into initial and corpse components, equating birth intensity to consumed-mass rate for each component, sampling independent Poisson processes on finite mass-coordinate intervals, and embedding actual births as a subset of potential families. This pathwise argument is essential: neither finite numerics nor standard branching-process formulas on their own prove it.

The exponential tail applies only for \(0<\theta<1\) and \(0<q<\delta(1-\theta e^{1-\theta})\). The critical estimate at \(\theta=1\) is only an upper bound and supplies no matching lower asymptotic. No computer-assisted infinite proof, independent validation, or external certification is claimed.
