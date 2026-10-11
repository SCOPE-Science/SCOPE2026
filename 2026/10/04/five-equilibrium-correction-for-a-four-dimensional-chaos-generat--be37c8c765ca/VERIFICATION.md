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

The equilibrium equations were eliminated independently. Besides \(E_0=(-1/30,0,0,0)\), every nonzero branch satisfies \(s=|y|=(x^2-360)/(10x)>0\) and the quintic \(x^5+9x^4-720x^3-492480x^2+113400x+1166400=0\). Exact Sturm counting gives precisely three real roots, numerically near \(-1.4295404143\), \(1.6562987482\), and \(78.9241446448\); the middle root violates the admissibility sign condition, while the other two each give two sign-related equilibria, for exactly five total. At \(E_0\), \(w|y|\) is differentiable with zero derivative and the characteristic polynomial is \((\lambda+12)(\lambda-1)(\lambda^2+37\lambda-323999/900)\), whose remaining roots are about 7.999979 and -44.999979. Thus the displayed point has two positive and two negative eigenvalues. The finite numerical root values are witnesses to an exact Sturm/factorization proof, not a substitute for it.

## originality

PASS

Originality passes as a source correction. The complete open primary article prints the exact audited four-dimensional system, asserts that the new system has only one equilibrium, displays the point \((-1/30,0,0,0)\), and lists an eigenvalue zero. The source's own characteristic polynomial is incompatible with that zero eigenvalue. Fresh exact-system and semantic searches found no prior correction giving all five equilibria or the corrected local spectrum.

## value

PASS

Equilibria and their local indices are basic structural data for a chaotic system used as the dynamical engine of an encryption scheme. Missing four equilibria invalidates the published equilibrium classification, and the zero-eigenvalue error misidentifies the displayed point's local type. The correction is therefore substantive dynamical information, not a cosmetic numerical adjustment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
