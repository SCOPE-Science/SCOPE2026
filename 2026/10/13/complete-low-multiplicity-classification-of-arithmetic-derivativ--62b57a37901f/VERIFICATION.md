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

# Finite corroboration and logical scope
Run the standalone scientific checker using `python verify.py --limit 500000`. It computes \(D(n)\) by the product-rule recurrence using least prime factors, computes \(\sigma(n)\) by independent divisor accumulation, and counts prime factors with multiplicity. A completed check returned:

`VERIFY_OK limit=500000 omega_le4_checked=373796 composite_zeros=[12, 18, 220] boundary_omega5=396`

The assertion tests the biconditional at every \(2\le n\le500000\) with \(\Omega(n)\le4\). It separately checks \(\Omega(396)=5\) and \(D(396)=\sigma(396)-396=696\). The proof in RESULT.md, not this finite enumeration, establishes the theorem for all positive integers in its stated multiplicity range. No independent validation or external proof certification has been carried out.
