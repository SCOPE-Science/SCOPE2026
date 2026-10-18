---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Exact one-probe variance is 2(||A||_F^2-sum a_ii^2), and Cauchy--Schwarz bounds the diagonal-square sum by tr(A)^2/n. Real Schur--Horn attains this lower bound for every eigenvalue spectrum with a constant diagonal. Scaling spectrum to [1,kappa] reduces to maximizing Q/S^2. The single-coordinate derivative 2(ts-q)/(s+t)^3 has only a minimum internally; thus some optimizer uses endpoints. With r upper eigenvalues the objective derivative changes + to - exactly at r=n/(kappa+1), so neighboring integer multiplicities suffice, including kappa=1 zero case. Corrected no unsupported inference from finite grid: independent exact Fraction check n=2..35 with rational kappa plus n=4,kappa=3 witness 1/6; analytic proof covers continuum.

## originality

PASS

Best-of-knowledge PASS with notable scalar-extremal risk: Avron--Toledo and Roosta-Khorasani--Ascher establish Hutchinson identity and sample complexity / columnwise off-diagonal energies, rather than the exact finite n spectral-kappa envelope. The continuous Kantorovich-type inequality and Schur--Horn theorem are acknowledged as known ingredients. Originality limited to their sharp finite integer-multiplicity combination for Rademacher variance; an older bounded finite sample coefficient-of-variation theorem may encode same formula.

## value

PASS

A sharp worst-case variance bound using only matrix dimension and condition number is a natural numerical-linear-algebra performance invariant; exact finite-n integer spectral multiplicity changes practical guarantees beyond a smooth continuous bound. Equality is genuinely attainable by SPD matrices, not just scalar eigenvalue sequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
