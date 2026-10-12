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

The symbolic proof in `RESULT.md` is the evidence for the infinite theorem. It uses only Beatty complementarity, exact floor identities, the fact that \(2<\varphi^2<3\), and irrationality of \(\varphi^2\).

The bundled `verify.py` is a finite corroboration. It computes the lower and upper Wythoff sequences with exact integer arithmetic via \(\lfloor n\varphi\rfloor=(n+\lfloor n\sqrt5\rfloor)/2\), reconstructs the representation function directly, and checks both rank formulas and the conservation identity for every \(1\le t\le1000\). No floating-point approximation is used.

The finite replay does not certify the infinite quantifier. The infinite claim depends on the proof steps in `RESULT.md`; in particular, it depends on Beatty complementarity for \(\varphi\) and \(\varphi^2\).
