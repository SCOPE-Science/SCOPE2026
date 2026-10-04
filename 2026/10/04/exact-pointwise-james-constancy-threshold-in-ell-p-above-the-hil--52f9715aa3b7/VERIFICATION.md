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

# Verification

The analytic proof uses two published inputs: the exact global James type profile of real \(\ell_p\) for \(p>2\), and Clarkson's inequality. No finite experiment is used to infer the infinite-dimensional statement.

For the nonconstancy branch, a unit vector \(y\) paired with \(e_1\) is reduced exactly to \(a=|y_1|\). The two chord lengths satisfy
\[
A(a)^p=(1+a)^p+1-a^p,
\qquad
B(a)^p=(1-a)^p+1-a^p.
\]
Strict Clarkson inequality gives a strict \(p\)-mean bound for \(0\le a<1\); the endpoint \(a=1\) is checked directly. Compactness then converts pointwise strictness into a strict supremum bound.

The script `artifacts/verify.py` was replayed from the packaged path and returned `VERIFY_OK`. It samples representative reduced profiles and checks the exact witness formula at \(t\ge p\). Those checks are supplementary only.

Unproved limits: the package does not classify \(1\le p<2\), finite-dimensional \(\ell_p^n\), or general \(L_p(\mu)\) spaces.
