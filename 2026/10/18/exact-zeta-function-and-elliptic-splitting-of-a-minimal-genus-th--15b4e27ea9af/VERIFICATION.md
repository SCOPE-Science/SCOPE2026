---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

PASS: For y³-y=x²+x+1/x over F3 the projective homogenization XY³-XYZ²-X³Z-X²Z²-Z⁴ defines a smooth quartic: affine partial derivative in Y is -X at X≠0, and both points at infinity are smooth with nonzero Z or X derivative. It has genus three, two F_(3^n)-rational points above poles, and #C(F_(3^n))=2+3#{x≠0:Tr(x²+x+x^-1)=0}. Independent polynomial-basis computations over F3,F9,F27 reproduce counts 5,17,44, giving Frobenius power sums -1,-7,-16. Newton identities + genus-3 Weil reciprocal functional equation force P(T)=1+T+4T²+9T³+12T⁴+9T⁵+27T⁶=(1-T+3T²)^2(1+3T+3T²). Elliptic F3 curves with traces 1 and -3 give ordinary and supersingular factors by Tate; P(1)=63. Factorization independently verified. No claim of polarized isomorphism.

## originality

PASS

Best-of-knowledge claim-versus-prior assessment with direct source comparisons; see four named checks, source inspections and retained risks.

## value

PASS

PASS: Exact zeta function, rational Jacobian order and mixed elliptic isogeny factors are natural arithmetic invariants of an explicit geometric extremal genus-three curve. These facts refine an automorphism/p-rank existence construction and distinguish its arithmetic type; exact fixed-object calculation has independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
