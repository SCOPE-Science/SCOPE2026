---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For the two-sided binary shift with allowed consecutive-1 distances b^k, a minimal forbidden word is 10^{r-1}1 of length r+1 for non-power r; therefore the canonical length-n cover excludes exactly nonpower r<n and is precisely D_{b,n}={b^k<n} union {r>=n}. Its renewal first-return equation has unique Perron root lambda_{b,n}>1; for n=1 it equals 2. At lambda_b, the missing power tail equals lambda_b^{-Q_b(n)}+O_b(lambda_b^{-2n}), while the finite unconstrained tail is lambda_b^{-n}/(1-lambda_b^{-1}). Taylor expansion about the negative slope -S_b, with derivative error O_b(n lambda_b^{-n}), gives uniformly lambda_b^n(h_{b,n}-h_b)=[(1-lambda_b^{-1})^{-1}-lambda_b^{-(Q_b(n)-n)}]/S_b+O_b(n lambda_b^{-n}). Fixed offsets t=Q-n and diverging offsets produce exactly the countably many stated cluster values and their unique limit; n being a power of b is exactly the one-step plateau condition, with strict entropy drop otherwise by proper irreducible-SFT inclusion. Independent transfer-matrix Perron roots vs renewal roots were computed for b=2,3,4 and n=1..14; high-precision large-n checks at powers and near boundaries for b=2,3 corroborated normalized phase. Finite checks are not infinite proof.

## originality

PASS

Best-of-knowledge priority judgment: close primary sources and published indexed findings are compared by mathematical statement, not just titles. Known general/ingredient results are credited; the precise asserted complete result is not shown to be covered by the material actually examined. Explicit source-access and possible stronger-result residual risks remain and do not become fabricated negative bibliographic claims.

## value

PASS

Canonical finite-type covers quantify approximations of nonsofic shifts. This naturally lacunary distance set produces a sharp uniform exponentially small entropy error but a genuinely discrete, noninterval phase spectrum, contrasting other natural languages with an interval spectrum. The exact plateau positions distinguish finite-scale language stability from entropy stability; both are motivated quantitative invariants of a standard symbolic dynamical object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
