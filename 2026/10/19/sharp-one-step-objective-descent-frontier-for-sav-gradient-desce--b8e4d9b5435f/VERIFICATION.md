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

# Verification of the scalar SAV descent frontier

The reproducible `verify.py` is included as an independent source file and may be run with `python verify.py` in an environment containing SymPy and mpmath. It reconstructs the first step directly from the published SAV update, independently simplifies the rational step to the stated squared-state form, computes the exact rational positive-energy witness, differentiates the key rational term, and evaluates the symbolic asymptotic limits. High-precision root finding produces \(u_*=0.09974525904287852385\ldots\) and \(h_*=0.97493280401545327419\ldots\). A fixed-seed set of 4,000 numerical probes cross-checks the subcritical descent statement. The symbolic limit identities and exact fraction witness are exact; the finite samples do not prove the infinite claims.

**Analytic proof components.** The equality test inside \(0<x^2<2\) follows from the two equal-energy squared amplitudes \(x^2\) and \(2-x^2\), with the step sign determined at \(0<h\le1\). Strict concavity of the one-variable function \(d\) and the bound \(d(u)<2\) for negative \(u\) yield a unique global worst case. For larger amplitudes the exact update remains between the original state and zero, where the quartic energy bound applies. The case \(h>1\) follows from linearization at a minimizer. The explicit family with \(h=\varepsilon^{-3}\) supplies the asymptotic original/auxiliary energy gap.

**Limitations.** The proof is mathematical and exact arithmetic; the Python checker verifies critical computations but is not a formal proof assistant. There is no external independent audit, no claim about methods with relaxation/stabilization, and no proof of publication priority from negative searches.
