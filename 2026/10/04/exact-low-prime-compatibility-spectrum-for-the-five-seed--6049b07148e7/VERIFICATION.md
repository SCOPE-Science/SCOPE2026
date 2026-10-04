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

`verify_compat5.py` uses only the Python standard library. It performs the complete \(3^4=81\) census twice in the same pass: first with exact `Fraction` arithmetic and second through
\[
A=12-60w_1-30w_2-20w_3-15w_4,
\qquad
\operatorname{num}(R)=A/\gcd(|A|,60).
\]
It asserts equality of the two representations for every coefficient vector, asserts that no residual is zero, checks the exact set of \(32\) absolute reduced numerators, factors them by trial division, and checks both the incompatible-prime set and its prime complement through \(137\).

Expected successful output begins with `VERIFY_OK`. The finite program establishes only the exact compatibility classification. The propagation to \(5p^k\in\mathcal U\) for every \(k\ge1\) is proved symbolically in `RESULT.md`; no finite experiment is used as a substitute for that infinite argument.

Limit: the verifier does not constitute an independent audit and does not establish literature novelty.
