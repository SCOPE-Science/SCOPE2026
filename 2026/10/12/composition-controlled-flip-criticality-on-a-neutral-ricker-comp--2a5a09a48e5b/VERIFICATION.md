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

The identity \(x^+/(y^+)^{\alpha}=x/y^{\alpha}\) and the strictly increasing equation \(Ky^{\alpha}+\alpha y=R\) establish the exact invariant foliation and one equilibrium on each positive leaf. The derivative \(\lambda=1-R+(\alpha-1)y_K\) crosses \(-1\) precisely once. A sign argument for \(f_K^2(y)-y\) proves existence of a genuine positive two-cycle for all \(K>K_c\), without using finite enumeration.

At the critical fixed point the derivatives \((-1,-t/y_c,[4+(5-\alpha)t]/y_c^2)\) imply the flip coefficient \(Q/(12y_c^2)\); the discriminant of \(Q\) supplies the exact sharp strength threshold. `verify.py` recomputes these identities with symbolic algebra for unrestricted symbolic \(\alpha\), checks the two rational critical examples, and uses high-precision numerical orbits to illustrate opposite stability types. Run `python verify.py` with SymPy and mpmath. Approximate cycle values are neither rigorous error enclosures nor substitutes for the analytic existence and normal-form arguments.

The proof asserts neither full-plane asymptotic stability nor a global census of cycles, and the cubic test is silent at \(Q=0\). No independent scientific audit or external certification has been performed.
