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

The proof is symbolic and valid for every finite field. The computational artifact is a regression check, not an exhaustive proof over all field sizes or dimensions.

`verify.py` performs three independent checks: it exhausts all linear maps on the four-dimensional vector space over \(\mathbb F_2\) and recovers exactly \(32\) Lie automorphisms; it confirms that none of these is fixed-point-free; and, for several prime fields and dimensions, it directly enumerates the scalar pairs \((a,b)\) and matches them against the divisor-sum formula.

The output `verify_output.txt` ends with `VERIFY_OK`. Prime-power examples such as \(q=4,8,9,16,25\) are evaluated from the divisor formula only; the infinite theorem for prime powers is justified symbolically by the cyclicity of \(\mathbb F_q^\times\).

Unproved limits: no claim is made about nonstandard filiform Lie algebras, conjugacy classes of automorphisms, or exact order distributions within the fixed-point-free locus.
