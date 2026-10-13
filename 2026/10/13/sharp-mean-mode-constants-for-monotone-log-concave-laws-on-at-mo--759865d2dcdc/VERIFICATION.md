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

The analytic proof reduces the decreasing case to successive positive ratios. For four atoms, \(\mathbb E X\ge1\) is exactly \(ab(1+2c)\ge1\), while \(1\ge a\ge b\ge c>0\); hence \(a^2(1+2a)\ge1\). For five atoms the corresponding identity is \(ab(1+2c+3cd)\ge1\), giving \(a^2(1+2a+3a^2)\ge1\). Strict monotonicity of the two polynomial profiles gives unique roots and equality forces every successive ratio to equal the first. Reflection covers increasing laws.

`verify.py` computes the roots by bisection, checks that the associated normalized truncated geometric laws have mean exactly \(1\) to high precision, and performs a finite rational-grid diagnostic over ordered ratio tuples. The finite grid is supplemental and is not used to justify the universal theorem.

Unproved limits: no constant is asserted for support size at least six, and no extension is asserted to nonmonotone log-concave laws.
