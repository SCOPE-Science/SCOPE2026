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

# Reproduction

Execute `python3 verify_stern.py` with a standard Python 3 interpreter; no additional libraries or data files are needed. The script checks the primality of all small coefficient primes and factors by exact trial division, the primitive-root property of 2 modulo each indicated prime, the complete factorization of \(2^{p-1}+1\), and the congruences for the Stern polynomial modulo \(2\) and \(\Phi_p(X)\).

Observed output closes with `VERIFY_OK primes= 9 nonzero_certificates= 22`. There are 22 nonzero order-obstruction residues and nine vanishing residues. The last index n is quantified by the group-order proof, rather than enumerated.

This is computational verification of finite certificates and a mathematical proof for infinitely many indices; it is not an independent external audit. Results outside the nine prime parameters are unproved.
