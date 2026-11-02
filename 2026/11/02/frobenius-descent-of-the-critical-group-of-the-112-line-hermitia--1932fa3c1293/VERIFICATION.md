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

Run `python hermitian_lines.py` and then `python frobenius_coinvariants.py` using Python 3. The first enumerates 280 isotropic projective points, their 112 Hermitian lines, their 1680 meeting pairs and the full ordinary Smith valuations; the second enumerates eight Frobenius fixed lines and 52 pairs, checks the induced complete bipartite graph, constructs the 60-by-60 orbit Laplacian, and determines its 59 nonzero local Smith factors. Both procedures use exhaustive exact finite arithmetic.

The prime-power moduli (2^16, 5^8, 7^8) exceed all observed nonzero valuations, and the rational rank 59 and the characteristic-polynomial product independently fix the number of pivots and torsion order. A run that fails any assertion is not a verification. Certificate JSON output is included for convenience. The 2019 comparison source could not be inspected in full; there is no independent scientific audit.
