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

The standalone `verify.py` reproduces the finite graph construction from the stated local majority rule, cyclic SCC decomposition, exact characteristic determinants by integer Newton identities, primitive-component periods, rational Perron-root bounds, and direct enumeration of all states at four cylinder circumferences. All checks executed successfully, producing `verification_output.txt`.

This computational evidence proves finite matrix identities by exhaustive finite algorithms; the all-size implications additionally rely on the transfer-walk bijections, the self-contained period-two energy argument, and Perron--Frobenius theory. The finite direct enumerations are not substituted for an all-size proof. The matrix factors are independently recomputed from exact traces in the verifier. No independent external audit has been performed.
