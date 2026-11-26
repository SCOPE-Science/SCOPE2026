---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Take the interface displacement as η and the vertical coordinate increasing upward. The rigid-wall cosh potentials give interface traces +Γη coth(kH)/k below and −Γη coth(kH)/k above. The lower-minus-upper actual linear pressure jump is [Δρg−(ρ_h+ρ_l)Γ² coth(kH)/k]η; balancing T k²η verifies the sign and normalization of the dispersion. On the growing band write b=Tk²/(Δρg), x=kH, and q=2x/sinh(2x). The normalized derivative of Γ² is 1−3b+(1−b)q. It decreases strictly from 2 to −2 since b increases to 1 and q is positive and strictly decreasing (sinh u<u cosh u for u>0). Thus the unique stationary point is the global peak. There b=(1+q)/(3+q), giving Γ_*²/(A k_*)=2 tanh x/(3+q), strictly increasing continuously from 0 to 2/3. Its inverse fixes H=x/k_* and T=Δρg b/k_*²; 1/3<b<1/2 ensures the constructed stationary point lies inside the growing band, and the positive observed growth rate then matches, not merely its square. The shallow and deep expansions follow from q=1−2x²/3+O(x⁴) and q=4x exp(−2x)+O(x exp(−6x)), respectively. This is an analytic check of RESULT.md §§Assumptions–Proof. VERIFICATION.md and CHECK.py were inspected as frozen evidence; the numerical cases were not rerun and are not needed for the proof.

## originality

PASS

The forward finite-depth capillary dispersion is established prior work and is not credited as new. The distinct claim supported by the available comparisons is the global inverse classification and sharp feasibility interval for the particular data consisting of the height and position of the unique unstable growth peak. The inspected prior statements do not supply the needed global injectivity and sufficiency arguments. This is a best-of-knowledge decision, not a priority certification.

## value

PASS

Two directly interpretable peak observables suffice for two otherwise unknown physical parameters. The strict wedge is a falsifiable model-consistency test and the reconstruction is single-valued without a local fit or the entire dispersion curve. The deep-water asymptotics usefully separate exact identifiability from stable recovery. The claim is relevant specifically to continuous linear modes and does not pretend to recover parameters from nonlinear or noisy patterns without further analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
