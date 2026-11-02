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

The proof computes a full basis of regular differentials, the exact Cartier matrix, and all rank blocks over an algebraically closed field of odd characteristic. The crucial nonstandard calculation reduces each block to evaluation of a polynomial basis at distinct elements of the prime field, proving the claimed infinite-family rank without extrapolating finite tests.

The standalone `verify_cartier.py` independently constructs Cartier matrices over the prime fields for \(p=3,5,7,11,13,17,19\), tests vanishing and nonvanishing coefficients, and verifies the block sum. The included checker was executed and returned `VERIFY_OK`. Its \(p=3\) check corroborates the previously known special case and is outside the novel theorem's \(p\ge5\) domain.

Unverified extensions: full Ekedahl–Oort types, Newton polygons, higher Cartier ranks, nontrivial coefficient fields as computational tests, and definitive historical priority. These are not claimed. No independent audit has been performed.
