---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The primary 2026 DAPW paper Section 3.3 Eq. (14) was read directly from the freely accessible full paper text, and has lower-record factor p(L_i)/F(L_{i−1}); Eq. (15) correctly has upper factor p(U_i)/(1−F(U_{i−1})). For strict lower records, the waiting draw is the first future X<ℓ, so conditional value j<ℓ has probability p(j)/Pr(X<ℓ)=p(j)/F(ℓ−1), not denominator F(ℓ). This is a normalization defect, not a convention change: the published factors sum to F(ℓ−1)/F(ℓ)<1 if p(ℓ)>0. Correct conditional record likelihood is p(L_1)∏_{i>=2} p(L_i)/F(L_{i−1}−1), and ratio of published to correct likelihood is product F(L_{i−1}−1)/F(L_{i−1}). Independently evaluated distribution from source PMF/CDF with high-precision decimal for α=2, θ=1/2, β=1, observed records 2>1>0: source ≈0.029669639318996232, corrected ≈0.059739036479455242, ratio ≈0.496654132163646. Admissible initial records have F(previous−1)>0; the discrete record stopping-plan issue is outside the claim.

## originality

PASS

The off-by-one strict discrete record normalization is classical probability and receives no novelty credit as an abstract theorem. The assessed new result is specifically identifying and exactly correcting the printed lower-record equation in Elkalzah et al. 2026 and quantifying parameter-dependent likelihood distortion, while distinguishing the correctly normalized upper records. Full primary paper Section 3.3 Eq14/15 was materially examined (including the source’s explicit assumption of discrete iid strength observations). Focused queries for the DOI, formula and corrigenda and Resultary semantic records found no earlier documented same-paper correction. The 2026 paper’s other truncation issue is independent.

## value

PASS

An explicit correction of a named, published likelihood used for inferential procedures is scientifically consequential even though the conditional-probability derivation is elementary: wrong parameter-dependent denominators alter maximum-likelihood and Bayesian inference. Restricting to the printed strict-lower-record component avoids unsupported assertions about numerical simulations or all DAPW models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
