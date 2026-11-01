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

# Verification and scope

The primary mathematical verification is the complete proof in `RESULT.md`. Its indispensable steps are (i) the Löwner contact criterion for the unit disk, (ii) the exact available cosine interval after a consecutive deletion, (iii) the upper bound \(\mathbb Ec^2\le BC\) when \(\mathbb Ec=0\), and (iv) the nonnegative convex interpolation of two explicit moment distributions when \(3(k+1)\le n\). The bound \(\cos(\pi/n)\cos((\pi-\pi/n)/3)\ge1/2\) supplies the parity-sensitive endpoint case. These arguments cover every integer in the stated domain; neither a numerical search nor a general algorithmic feasibility assertion substitutes for them.

Execute `python verify_erasure.py` in the directory containing that file. The packaged Python 3 script needs no third-party libraries. On its actual execution, the script reported `PASS: 60375 parameter pairs; 20010 explicit isotropic certificates` and `PASS: all angular-obstruction thresholds agree with k_max=floor(n/3)-1`. It validates the constructed weights, their nonnegativity, total mass and vanishing complex Fourier moments of frequencies one and two, for \(6\le n\le350\). A separate SciPy linear-programming diagnostic checked 10,875 finite instances through order 150, with agreement. Those computations are finite numerical diagnostics only.

No claim is made about nonconsecutive deletion patterns, ellipsoid semiaxes outside the tolerance region, full novelty certification, or independent validation. Scientific literature inspections are documented separately in `AUDIT.json` and `REVIEW.md`.
