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

## Checks and limits

- Exact substitution was checked for \(\xi<0\) by expanding the traveling-wave equation in \(q=e^{c_k\xi}\); both coefficients match for \(2c_k^2-kc_k-1=0\).
- For \(\xi>0\), the profile and every PDE term vanish.
- At \(\xi=0\), the flux \(\phi_k\phi_k'\) and the derivative of \(\phi_k^2\) have zero traces on both sides, so no interface Dirac mass is introduced.
- \(c_k>0\) for every real \(k\), since \(\sqrt{k^2+8}>|k|\).
- No numerical computation is required. The claim does not assert uniqueness, minimality, stability, or convergence from arbitrary initial data.
- Independent audit has not been performed.
