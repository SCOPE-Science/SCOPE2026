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

The proof classifies the exact simplicial object for every integer \(n\ge2\). Its central nonstandard steps are the identification of signed complementary-pair coordinates, the stabilizer-consistency calculation of the invariant subspace, and the binomial count of negative transposition eigenvalues. The quotient statements use finite-group rational transfer and Armstrong's orbit-space theorem.

`verify.py` reconstructs actual subset-complement pairs and signed permutation matrices, checks every permutation in \(S_4\), \(S_6\), and \(S_8\), and verifies transposition fixed-space dimensions for \(2\le n\le8\). It additionally checks cyclic invariant dimensions by two independent finite methods: orbit-sign propagation and character averaging. The recorded output in `verify_output.txt` is `ALL_VERIFY_OK`.

These finite checks do not prove the universal binomial or group-action statements and do not address integral torsion in the quotient. The mathematical proof provides the unrestricted argument. No independent mathematical audit or external certification was performed.
