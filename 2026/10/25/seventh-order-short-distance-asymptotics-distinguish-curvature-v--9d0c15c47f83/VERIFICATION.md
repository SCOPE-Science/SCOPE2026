---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

PASS: The distance CDF is the radial integral of the directional covariogram. A tangent-local graph with fourth graph derivative equal to κ_ss+3κ³ yields the t³ correction κ/24 and fifth correction (κ_ss+3κ³)/1920−κ_s²/(1152κ); integrating over normal angles and using ∫κκ_ss ds=−∫κ_s² ds gives r^7/A²[(∫κ⁴ds)/2240−(∫κ_s²ds)/2520]. No r⁴/r⁶ terms. Independent exact circular case matches 1/(1120π); ρ_m=1+cos(mθ)/2 yields sign polynomial 27/35840−17m²/161280, positive m=2 and negative all m≥3. Uniform C6 positive curvature supports remainder; checks are finite corroboration, not a proof of the uniform asymptotic.

## originality

PASS

PASS, qualified best-of-knowledge: Known general covariogram formulas and directional third derivatives do not yield this fifth derivative or its κ_s² contribution without higher-order geometry. Shape gradient makes the coefficient sign-indefinite, unlike earlier positive κ² term. Residual risks: Bianchi–Segala–Volčič JDG 60 (2002) full text unavailable after OA/preprint attempts and the authorized Oxford request returned vpn_disconnected (job dcee92f75247be82b5ce18705e6f47aa); this plausible source remains an explicit historical overlap risk. No authentication bypass or retry was attempted.; Gates 1987 chord-distribution primary full article not read, and the Gečiauskas Russian text was not fully translated.

## value

PASS

PASS: The signed seventh coefficient distinguishes smooth strictly convex ovals that share curvature-radius distributions and perimeter. It identifies the new curvature-gradient energy in a familiar stochastic geometry invariant, with explicit sign-changing analytic examples beyond the known fifth-order term.

The dated certificate retains the supplied scientific assessment, sources and limitations.
