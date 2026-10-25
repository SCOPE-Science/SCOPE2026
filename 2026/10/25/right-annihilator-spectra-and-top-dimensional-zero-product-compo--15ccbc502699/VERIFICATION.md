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

# Finite verification and proof obligations

The standalone program `verify.py` reconstructs the field matrices and multiplication. It enumerates every upper-triangular first factor, independently ranks its leading principal corners, and computes the predicted right-annihilator multiplicities. For the smaller cases, it also loops over *all* second factors and checks literal multiplication to compute all solutions of \(AB=0\).

Executed command: `python3 verify.py`. Selected output: \(Z_2(2)=26\), \(Z_2(3)=129\), \(Z_2(4)=388\), \(Z_3(2)=632\), \(Z_3(3)=16497\), \(Z_3(4)=160192\), \(Z_4(2)=42560\), \(Z_5(2)=7891968\). The runs exhaust the first-factor matrix spaces in nine configurations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\). Full ordered-pair multiplication is checked only in the smaller configurations explicitly identified in the program; larger cases are checked by direct rank reconstruction. A separate arithmetic calculation verifies the predicted leading exponent and coefficient for every \(1\le n\le40\).

Expected terminal marker: `VERIFY_OK_TRIANGULAR_ZERO_PRODUCTS 9_FINITE_CASES 40_TOP_DEGREES`.

Neither the finite enumerations nor the leading-degree checks prove the assertions for arbitrary \(n\) and arbitrary finite fields. The universal proof is the rank-extension argument, vector-bundle irreducibility argument, and explicit dimension maximization in `RESULT.md`. Full historical-priority verification and independent mathematical audit have not been performed.
