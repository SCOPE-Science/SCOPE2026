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

The proof is mathematical and applies over any field, including the prime field of two elements. The computer checker supplies finite corroboration rather than a substitute for the infinite proof. Run `python3 checks/verify.py` and require the terminal line `FREE_CLASS2_LOCAL_DERIVATIONS_OK`.

The checker constructs all elementary actions \(\rho(E_{ij})\) and, for every alternating bivector \(z\) over the test field, computes the annihilator of its evaluation span \(\{\rho(A)z\}\). These annihilators determine a linear constraint system for endomorphisms \(R\) that satisfy pointwise derivation matching. It verifies the dimensions of the resulting solution spaces and of \(\rho(\operatorname{End}V)\). Cases are \((n,p)=(3,2),(4,2),(5,2),(3,3),(4,3),(3,5)\).

The checker additionally constructs an explicit normal-form sample local derivation and directly confirms the matching condition by span calculations on **every Lie algebra element** in dimensions \(n+\binom n2\) for \((n,p)=(3,2),(4,2),(3,3)\), totaling \(64+1024+729\) tested points. No claim of complete enumeration for higher dimensions or arbitrary non-prime finite fields is made.

The supplied program is standalone, standard-library-only Python, with no external files, services, or trusted certificates. The underlying infinite proof is in `RESULT.md`. Independent mathematical audit has not been performed.
