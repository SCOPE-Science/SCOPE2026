---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

On A²(B_2), normalized monomials have squared norms 2u!v!/(u+v+2)!, so the companion maps each monomial to the unique orthogonal shifted monomial with singular weight exp(-epsilon u-epsilon^a v)*m/(m+k)*sqrt(prod(v+j)/(m+2+j)). Independently verified factorial-weight identities for k=1..4, u,v<=6. For v large, ratio to (v/(u+v))^(kp/2) has uniform O(1/v) relative error; finitely many v cost lower order. Inner positive decreasing sum differs from v*H_q(p epsilon v) by at most 1. Uniform Laplace asymptotics and v-scale epsilon^(-a) Riemann sums yield gamma/p², (1-a)log/p², 1/[p²(q-1)] coefficients in q<1,=1,>1. Compactness for epsilon>0 follows exponential damping. Domain fixed a in (0,1), p>0.

## originality

PASS

The three-regime quantitative two-rate singular-value blow-up is not stated in accessible source material on companion membership, and is genuinely more precise than compactness at each epsilon. Dong–Xu (2026) is same-model literature inaccessible in full and must remain explicit priority risk; no invented definitive whole-document exclusion.

## value

PASS

Sharp transition at kp=2 distinguishes integrable/nonintegrable angular weighting and gives a natural complete quantitative degeneration law with logarithmic critical regime for a compact operator family approaching identity, including quasi-Schatten p<1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
