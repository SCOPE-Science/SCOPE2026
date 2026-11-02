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

# Verification and reproducibility

The theorem is proved analytically in `RESULT.md`. Its quantified correctness is not inferred from finitely many tests.

Run `python3 check.py` using Python 3's standard library. The embedded test source performs **5,942 deterministic checks**, including: exact `fractions.Fraction` identities for the hexagonal witness and 2,205 exact convex-majorization comparisons over integer power orders; numerical checks of the scalar derivative equation and maximizing profile at seven finite orders; and high-order consistency checks using the explicit boundary profile. Its observed result was `PASS: 5942 deterministic finite checks (not an infinite proof)`.

The nonstandard load-bearing scientific premise is the published sharp Birkhoff arithmetic triangle bound \(A_2^B(X)\le3/2\), with the affine-regular hexagon as its equality class, stated explicitly in Qi–Yin–Liu 2026, Eq. (23). Everything beyond that premise is shown in the proof: radial chord constraints, convex majorization, uniqueness of the critical root, compactness/equality rigidity, the exact quadratic value, and the limiting law.

Independent mathematical audit and independent publication-priority verification have not been performed. Residual scientific scope limits are finite order \(t\ge1\), real dimension two, and Radon norm geometry. Older equivalent convex-majorization formulations remain a priority risk.
