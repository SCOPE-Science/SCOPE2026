---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

An independent check of the classical region uses the first two moments of t=cos(theta): after azimuthal twirling a coherent mixture has x=E[t] and 1-2b=E[t^2]. At fixed x the second moment ranges over [x^2,1], realized by interpolating between a point mass at x and a mixture of the two poles with mean x. This confirms the frozen PPT computation. Dephasing over rotations about the spin axis preserves the compact classical convex hull and is an orthogonal projection for the Hilbert–Schmidt inner product, so the unique metric projection of a diagonal target is diagonal. Its squared distance to (y,b') is (x-y)^2/2+3(b-b')^2/2. Feasibility is 0≤b'≤h(y)=(1-y^2)/2. For b>h(x), the minimizing section at y is the clamp of b to this interval; if b≤h(y), moving horizontally to the endpoint nearest x of {y:h(y)≥b} reaches the boundary without increasing distance. This reduces minimization to b'=h(y). The derivative there is (3y^3+(6b-1)y-2x)/2. Because |x|≤1-b and b>0, it has strict opposite signs at ±1; it is strictly increasing for b≥1/6. For smaller positive b, the Cardano radicand x^2/9-(1-6b)^3/729 is positive since x^2>1-2b>2/3. Thus there is exactly one real root and the closest state has parameter -1<y<1 on the boundary of the classical region. Substitution of x-y=3y(b-h(y)) gives the second distance formula. Three equally spaced phases cancel coherences of phase order one and two; the resulting diagonal state has rank three, giving a sharp lower bound on ensemble length. Supplemental frozen replay: verify.py in the package (not used to infer the continuum result). Its conditional low-b radicand test is not exercised by its listed numerical cases; the exact proof covers that regime, e.g. (a,b,c)=(9/10,1/10,0) has x^2+2b=101/100 and radicand 9/100-(2/5)^3/729>0.

## originality

PASS

The classicality boundary, the central ray x=0, and the pure |1,0> case have verified prior coverage. The distinct result is the explicit nearest-state and distance formula on the nonclassical off-axis diagonal region, including the exact three-coherent-projector length there. No inspected result gives or implies that full off-axis projection by specialization.

## value

PASS

Axially invariant mixed states form a natural full two-parameter class in the spin-1 closest-classical-state problem. The off-axis solution replaces numerical distance optimization with a unique scalar root and a proved minimal coherent-state realization, including states outside the previously solved pure-to-classical ray. This identifies the actual optimizer, not only a bound or test for whether the input is classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
