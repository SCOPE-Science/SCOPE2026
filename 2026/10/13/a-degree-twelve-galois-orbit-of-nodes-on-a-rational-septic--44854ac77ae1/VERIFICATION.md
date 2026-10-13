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

# Verification protocol and limits
Run `python verify.py` with a standard Python 3 environment providing SymPy. The script uses exact algebra: it checks the implicit resultant, \(x\)-discriminant, discriminant of \(D\), the three Jacobian congruences, and Rabin's irreducibility test modulo seven. Direct counts over \(\mathbb F_3\), \(\mathbb F_7\), \(\mathbb F_{11}\), \(\mathbb F_{13}\), \(\mathbb F_{71}\), and \(\mathbb F_{89}\) are illustrative only. The written proof, not finite samples, proves the statement over every permitted characteristic. The proof does not establish the complete Galois group or classify excluded primes. Independent audit: not performed.
