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

# Reproduction and limitations

Run `python3 verify.py` with Python 3 and the standard library. The script must print `VERIFY_OK_FREE_CLASS2_FIXEDSPACE_CENSUS` after exact checks. It independently constructs the exterior-square action on the commutator space and tests the claimed joint eigenspace multiplicities against all invertible three-by-three matrices for field orders \(2,3,4\). In field order four it uses polynomial arithmetic modulo the irreducible polynomial \(z^2+z+1\) over \(\mathbb F_2\). It also directly constructs and ranks all \(86016\) binary Lie automorphisms, checks the full polynomial, and verifies symbolic normalizations for eleven prime-power orders. The theorem for all prime powers follows from the written proof, not from finite enumerations. No independent mathematical validation is claimed.
