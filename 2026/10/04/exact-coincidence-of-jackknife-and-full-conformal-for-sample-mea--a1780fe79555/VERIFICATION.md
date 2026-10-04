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

The proof has two algebraic checkpoints. First, the leave-one-out mean satisfies \(\widehat\mu_{-i}=\bar Y-d_i/(n-1)\), and its absolute residual is \(n|d_i|/(n-1)\), giving the proposed jackknife+ endpoints exactly. Second, for a candidate \(x=y-\bar Y\), direct expansion verifies
\[
((n+1)d_i-x)^2-n^2x^2=(n+1)(n-1)(d_i-x)(x+c_nd_i).
\]
This factorization identifies each full-conformal residual comparison with one of the endpoint intervals. The remaining step is the exact integer identity \(n-\lceil(1-\alpha)(n+1)\rceil+1=\lfloor\alpha(n+1)\rfloor\).

The included `verify.py` uses exact rational arithmetic. It checks the factorization on a grid of \(n\), \(d_i\), and candidate values; reconstructs jackknife+ endpoints from direct leave-one-out fits; evaluates the original full-conformal residual rule on every cell separated by the algebraic breakpoints for several rational samples and levels; checks the \(\alpha<1/(n+1)\) whole-line convention; and exhausts a five-point exchangeable orbit with distinct augmented residuals, recovering the predicted coverage rank count. Successful execution prints `VERIFY_OK`.

These computations are consistency checks, not substitutes for the symbolic proof. No exhaustive claim over regression algorithms is made. The exact coverage fraction requires distinct augmented residuals; in the presence of ties only the deterministic set equality and conservative exchangeable coverage statement are asserted.
