---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Diagonalizing the SPD Hessian gives the exact three-state scalar matrix and cubic characteristic polynomial in the package. Independent symbolic Schur reduction reproduces \(1+u+v=a/(1+\beta)>0\) and shows that the active condition is \(a<2(1-\beta)/(1+2\beta_0)\), while the \(|v|<1\) constraint is weaker. Substituting \(a=\eta_0(1-\beta)h\) cancels \(\beta=\beta_1^2\). At equality the polynomial has root \(-1\); above it a real root lies below \(-1\). The base-rate formula follows from the source noise normalization and decreases from \(2\) to \(\sqrt2\). The standard positive-learning-rate domain is essential: zero learning rate is not claimed stable.

## originality

PASS

The defining paper states the same interleaved PNM recurrence, controls noise through \(\beta_0\), normalizes the learning rate by the noise amplitude and proves a sufficient stochastic convergence theorem. It does not state an exact deterministic quadratic spectral boundary, the cancellation of \(\beta_1\), or the noise-amplification/stability tradeoff. Resultary returned stability results for other methods but no PNM covering theorem.

## value

PASS

The source explicitly motivates its normalization as avoiding retuning while \(\beta_0\) changes. The exact quadratic theorem quantifies the deterministic cost of that same control knob, including the practically used \(\beta_0=1\) setting and the unexpected cancellation of \(\beta_1\), making it a natural optimizer-stability benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
