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

PASS: For noncomplete connected SRG (v,k,lambda,mu), adjacency A²=(k-mu)I+(lambda-mu)A+mu J gives L0²-SL0+mu v(I-J/v)=0 where S=2k-lambda+mu, nonzero eigenvalues q1,q2 sum to S and multiply to mu v. With t=ch, d(z)=1+z/2+z²/12, [2/2] Padé map is I-t L0 d(tL0)^-1. Rational interpolation at 0,q1,q2 yields edge coefficient t(1+mu t/2-mu(v-S)t²/12)/(d(tq1)d(tq2)) and nonedge coefficient mu t²(1/2+St/12)/den. Denominators>0, nonedges strictly positive t>0, diagonals strictly positive since Padé scalar numerator and denominator are positive for nonnegative spectrum and P is symmetric positive definite. Edge quadratic F(t) has unique positive zero precisely if Delta=v-S>0, producing H=(3/(c Delta))(1+sqrt(1+4 Delta/(3mu))); otherwise all steps positive. Strict beyond-endpoint negativity and asymptotic expansions follow from top-degree coefficients. Independent exact Fraction inversions and formula comparisons for Petersen, C5, triangular T5 and rook4 at t=1/2 agree entrywise.

## originality

PASS

PASS, qualified: Bendito et al (2012) Proposition 6 explicitly characterize the Moore–Penrose graph Laplacian M-property for SRGs by mu>=k-k²/(v-1), equivalent via SRG parameter equation to S>=v; conference, complement duality and T_m cutoff are prior. Zappavigna et al (2012) analyze positivity of Padé maps generally, with sufficient small-step conditions and counterexamples, but not the exact SRG time-dependent formulas or sharp finite interval in examined full text. New mathematical content is the finite-step rational sign kernel and unique exact horizon; underlying static graph threshold is not claimed new.

## value

PASS

PASS: Positivity preservation of a stable high-order rational diffusion map is a natural structural invariant; for a major strongly regular graph family, this theorem gives complete all-time interval, sharp step bound, strict sign mechanism and singular asymptotic regimes. The static M-property alone cannot determine the finite positive horizon, making the result substantive beyond a known classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
