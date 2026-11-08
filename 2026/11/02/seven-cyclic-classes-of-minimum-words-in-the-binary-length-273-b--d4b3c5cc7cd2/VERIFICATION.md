---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Syndrome conditions sum beta^j=sum beta^(3j)=0 are exactly the four BCH check-root conditions using Frobenius in GF(2^12). Reconstructed polynomial-field multiplication, checked alpha order 4095 and beta order 273, counted 36856 unordered exponent pairs, 210 complementary ordered matches with four distinct nonzero positions, 35 normalized weight-five sets containing zero, then seven full shift-orbits and 1911 supports; double-index Frobenius acts as a six-cycle and one fixed subgroup orbit. Counting normalization is exact since 5 and 273 are coprime. This exhaustive fixed-code enumeration is not an infinite BCH family proof.

## originality

PASS

Compared the precise final claim and its implications with same-object primary mathematics. The binary BCH family is already known; key exact object is the weight-five support orbit enumeration, not code parameters. Wang et al 2026 Theorem 17 covers minimum distance in family; same s=4 parameters in Example 18 are prior. No implication to exact count 1911 from parameters alone. Best-of-knowledge originality is supported for the narrower stated new contribution, not for previously established premises. Residual risks documented.

## value

PASS

The exact count and cyclic/Frobenius orbit profile of minimum-weight codewords are natural, reusable BCH code invariants relevant to decoding error-event multiplicities and the support design geometry; they are not implied by knowing [273,249,5] alone. One fixed finite code, not a pretend general family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
