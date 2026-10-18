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

# Reproduction and limits

The theorem reduces the equations for \(XY+YX\) to three explicit scalar polynomials. The arbitrary-field proof performs a full five-stratum rank computation and two geometric irreducibility arguments; these steps have been checked symbolically in the accompanying mathematical text.

The accompanying standalone `verify.c` checks all prescribed target fibers by linear algebra over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_7\). It independently enumerates **every input ordered pair** in \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\). It outputs `VERIFY_OK_NILTRIANGULAR_JORDAN_FIBERS` only if all required target counts and total-mass identities agree. Build: `cc -O2 -std=c11 -Wall -Wextra verify.c -o verify && ./verify`.

The finite tests do not prove the arbitrary-field classification, the irreducibility claims, or novelty. Those rely on the symbolic proof and specific literature comparison. No independent mathematical audit has been performed, and no scheme-theoretic reducedness statement is made.
