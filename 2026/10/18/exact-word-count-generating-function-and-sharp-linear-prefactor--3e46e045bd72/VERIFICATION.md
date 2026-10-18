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

# Reproducibility and boundaries

The standalone `verify.py` included with this result must be run under Python 3.9 or later and uses only the standard library. It compares (i) complete enumeration of nonzero-reduction bracket words, (ii) a dynamic program giving a multiplicity \(M^{H}\) to every coarse word, and (iii) formal power series coefficients of the algebraic generating function. Verified ranges: \(M=2\) through length \(9\), \(M=3\) through length \(7\), \(M=4\) through length \(5\); the algebraic and weighted checks continue through length \(18\) for each. The check is finite. It does not establish the general case or mathematical originality, which rest respectively on the proof and comparison with the cited primary literature.

The infinite part is the formal first-passage decomposition and the double-pole calculation. In the complex disk \(|z|<(M+1)/(2\sqrt M)\), no other denominator zero occurs; Cauchy's estimate then proves exponential control of the *normalized* error for any permitted \(\vartheta\). Parameter independence relies on the published coding theorem. Independent mathematical validation has not been performed.
