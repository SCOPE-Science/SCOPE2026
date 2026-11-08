---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

At angular stationarity, the generator gives E e^{inθ}=r ν_n/(r+n²D_r) for each n≠0. First-harmonic relaxation at k=r+D_r gives velocity covariance e^{-kt} Cov(u0); integrating Green–Kubo gives D_eff=DI+(v²/k)(E[u0u0^T]-p1² diag(a²,0)). Since E cos2θ=p2 Reν2, Δ=Dx-Dy=(v²/k)(p2 Reν2-p1² a²). Jensen gives 2a²-1≤Reν2≤1 and sharp unique extremal laws ν=½(δ_{acos a}+δ_{-acos a}) and ν=((1+a)/2)δ0+((1-a)/2)δπ, with all intermediate values by mixing. The upper-bound sign is F(Λ)-a², F=(1+Λ)²/(Λ(Λ+4)), F′=2(Λ-2)(Λ+1)/(Λ²(Λ+4)²), minimum3/4 at Λ=2. This proves the forced-transverse open interval between the two exact roots for √3/2<a<1, the tangent case a=√3/2, and deterministic reset a=1 threshold Λ=1/2. Independently evaluated roots for a=0.9: ~0.9425886647 and ~5.5837271247. The axes are fixed by mean polarisation; off-diagonal terms need not vanish.

## originality

PASS

The original Baouche–Franosch–Meiners–Kurzthaler model explicitly permits resetting to a distribution of angles, so a novelty claim based only on allowing arbitrary reset laws would be false. Its explicit fixed-direction diffusivities are a special case recovered here. The newly assessed element is the globally sharp optimisation over all Borel reset laws of a prescribed first harmonic, unique extremizers and reentrant all-law sign phase diagram. The separate chiral relative-reorientation and anisotropic passive-particle works do not directly imply this constrained optimization, subject to broader moment-method priority risk.

## value

PASS

Steering uncertainty naturally fixes mean orientation rather than a full angle distribution. Exact anisotropy envelopes, extremal calibration distributions and a rate interval where every allowed law is transverse are concrete transport-design information; the reentrant sign boundary is not merely an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
