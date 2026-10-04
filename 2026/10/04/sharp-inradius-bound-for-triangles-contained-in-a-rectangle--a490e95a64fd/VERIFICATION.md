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
The analytic proof carries the universal quantifiers. The accompanying `artifacts/verify.py` is a supplemental replay that checks the core algebraic inequalities and deterministic grids.

It checks, for many exact rational values with \(0<h\le1\), that the squared Cauchy--Schwarz inequality
\[
(h-xy)^2\le(x^2+h^2)((1-x)^2+(h-y)^2)
\]
holds; this is the squared form of the bound used in the interior-saddle argument. It also verifies the boundary comparison inequalities after safe squaring and performs dense deterministic floating-point stress tests of the full quotient against
\[
\frac{h}{1+\sqrt{1+4h^2}}.
\]

The computation does not enumerate all real parameters and is not presented as an infinite certificate. Its purpose is to replay the formulae and catch algebraic or implementation errors. The proof in `RESULT.md` is the evidence for the infinite theorem.
