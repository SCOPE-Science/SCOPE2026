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
The proof uses the smooth \(\ell_4\) Birkhoff equation to reduce every admissible pair to
\[
x(t)=\frac{(t,1)}{(1+t^4)^{1/4}},
\qquad
y_{\pm}(t)=\pm\frac{(1,-t^3)}{(1+t^{12})^{1/4}},
\qquad0\le t\le1.
\]

`verify.py` symbolically checks the branch-difference factorization, constructs the positive-branch constrained derivative and its exact resultant, verifies the degree-fourteen polynomial, and performs Sturm root counts. It confirms that the small resultant root is extraneous to the original positive-branch stationarity equation and that the root in \((0.8255,0.8256)\) is the only compatible interior critical value of \(t^4\). Endpoint and derivative-sign checks then certify global maximality.

The decimal value is printed only after the algebraic checks. Numerical sampling is not used as a proof of the supremum.

No independent audit or independent validation has been performed.
