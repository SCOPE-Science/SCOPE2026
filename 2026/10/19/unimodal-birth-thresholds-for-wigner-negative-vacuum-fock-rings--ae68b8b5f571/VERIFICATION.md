---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Under the stated 1/(2π) Wigner convention, the Fourier Gaussian in Mehler's series yields exp(−(1−u)(q²+p²)/(1+u))/(π(1+u)); comparison with the ordinary Laguerre series gives the factor e^(−s/2)/π and bracket 1−t+t(−1)^n L_n(s). The n simple positive zeros (orthogonality) and Rolle plus degree give exactly one simple critical point in each interior sign gap and none outside. Thus each negative lobe produces one component precisely at strict exceedance of its depth threshold. The initial odd lobe is monotone up from −1, and t=1/2 includes no negative origin; the subsequent component is a disk. At interior threshold the second s-derivative of Q_n is nm_j/s_j>0 and the t-derivative of the bracket is −(1+m_j), giving the stated square-root fold locally at each contributing radius, even for simultaneous births. For t=0 the bracket is positive; for t=1 the regions coincide with the strict negative lobes. Differentiating L_n²+s(L_n′)²/n gives (2s−1)(L_n′)²/n; strict decrease then increase on either side of s=1/2 orders the sampled squared depths, with one possible ambiguous/tied adjacent step across that point. The endpoint energy is 1. A new exact-rational script /workspace/reproductions/01_laguerre.py certified the finite cutoff: three independent derivative sign-change brackets and a Descartes upper bound after a Möbius interval map certify the first three roots, and rational bisection and a derivative error bound certify the depth comparisons and displayed enclosing intervals at 22 and 24. It returned m₂>m₁ for each even degree 4..22 and m₁>m₂ at 24. Frozen verification notes, checker, requirements and recorded output were inspected, not executed; the new replay does not substitute for the all-degree proof.

## originality

PASS

The Fock Laguerre Wigner formula and the zero-coherence positivity test are prior ingredients, and the disk at order one is already implicit in a known qubit formula. The supported distinct contribution is the complete, depth-ordered set of negative-component births for the incoherent family, including the single-turning-point law and the exact first innermost even-order reversal. The inspected positive-region/coherence and Laguerre-primitive results do not give those statements. This is a bounded comparison, not a priority certification.

## value

PASS

The exact number and ordering of negative components give geometry that neither integrated negativity nor the first positivity threshold captures. The universal radial ordering constrains every number state, and the certified comparison marks the first even level at which the two innermost annuli exchange birth order. The compared radii and even subfamily are natural, not an arbitrary computational slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
