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

# Verification and boundaries

Use `python3 verify.py` with Python 3 (standard library only). Expected output contains `VERIFY_OK exact_polynomial_identity exact_floor_counting sample_n0= 99`. The package verifier checks an exact bivariate rational polynomial identity for the Faulhaber correction and finite exact-fraction tests of the floor estimate and the \(2B\)-shift recurrence. It also exercises the cutoff on a specific floating-point example.

**Analytic verification:** The theorem holds for all real \(B,d_1,d_2>0\), not just rational inputs. For every \(E\ge B\) the magnetic oscillator/transverse label count is the displayed finite floor sum. Writing \(t=M+\delta\), the exact polynomial expansion and \(0\le\varepsilon\le M\) imply the global remainder bound in the proof. Summing the three estimates cancels the \(E^{3/2}\) terms and leaves the positive linear term. The shift by one Landau spacing adds precisely one label per transverse mode below the stated cutoff, which is \(O(\sqrt E)\). The explicit quadratic is strictly positive beyond its positive root. The min–max endpoint comparison and continuity of the fibers then cover every adjacent \(2B\)-interval and hence the entire high-energy tail. These arguments, not the finite sample checks, prove the global result.

**Scope limits:** The bound is sufficient rather than optimal; the number of low-energy gaps is not calculated. Eigenvalue coincidences are counted with multiplicity. The absence of gaps does not assert uniform density of states or any stability against perturbations. Bibliographic originality has only been checked against sources described in the review; it is not independently certified.
