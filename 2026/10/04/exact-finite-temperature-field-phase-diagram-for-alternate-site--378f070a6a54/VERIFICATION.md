---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Starting from the primary source's explicit \(u,v,y,Z\), \(y\) simplifies to a nonnegative affine function of \(\cosh(2|B|/T)\), so concurrence positivity is equivalent to the sign of \(y^2-uv\). Independent expansion reconstructs exactly the stated quadratic coefficients. The leading coefficient is positive exactly when \(\sinh^2x>\cosh(\sqrt2 x)\); its difference is strictly increasing for \(x>0\), giving a unique root. Above the corresponding temperature the quadratic is negative for every admissible field; below it, opposite-sign roots and negativity at zero field yield exactly one positive threshold. Standard asymptotic expansion of those exact coefficients gives the stated low-temperature activation law and high-field positive tail. The numerical root \(x_*=1.4195389207530749\ldots\) and \(T_*/|J|=0.7044540909589808\ldots\) were independently reproduced.

## originality

PASS

The direct Cao--Zhu paper supplies the exact reduced Gibbs state and concurrence but gives a numerical/qualitative field picture rather than the exact one-boundary positive-temperature classification. The closest later broader four-qubit field-plus-DM paper was read in full through authorized institutional access: it reproduces the next-neighbor setup, studies critical-temperature plots, and explicitly treats concurrence below \(10^{-4}\) as disappearing in one figure; it does not state the zero-D quadratic sign reduction, universal temperature ceiling, vanishing low-temperature activation scale, or strictly positive high-field tail. Fresh Resultary searches did not locate an equivalent theorem.

## value

PASS

The field-induced alternate-site entanglement switch is the central phenomenon of the source. Replacing a finite-resolution bounded-looking field window by an exact one-boundary positive-temperature phase diagram, with a universal ceiling and two singular asymptotic laws, is a motivated structural correction rather than a routine numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
