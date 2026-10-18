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

# Verification and scope

The exact Laplace transform is reproduced from the quadratic Feynman--Kac equation, with the parameter \(g=\sqrt{2\lambda}\). The saddle equation is \(\theta=1/(2g)+c^2/(2g^3)\), and the complex second derivative gives the strictly positive Gaussian variance proxy \(v=1/(2g^3)+3c^2/(2g^5)\). Algebraic cancellations in the path-density ratio give the Ornstein--Uhlenbeck Girsanov density, which integrates to one. The contour proof uses a strict spectral-gap inequality for \(\operatorname{Re}\sqrt{g^2+2iu}\) for every \(u\ne0\); the finite checks alone do not certify uniform asymptotics.

Run `python verify.py` from the folder containing this document. It uses Python's standard library, makes no network calls, and prints a check count. Validation is finite; the proof of the infinite limiting statement is in `RESULT.md`.

**Scope limitations.** Only bounded initial states, a fixed positive budget rate, and \(\mu_T^2/T\to c^2<\infty\) are proved. No infinite-horizon total variation claim. Independent audit: not performed.
