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

# Verification and reproducibility

The analytic proof is recorded in `RESULT.md` and uses a centered finite-difference exponential generating function, leading Gegenbauer coefficients, Schoenberg's zonal positive-definiteness characterization, and the published Bernstein inequality for Legendre polynomials (Gautschi–Giordano, Eq. (56)). The all-dimension sign formula and the S² preservation claim are proved symbolically, not from enumeration.

Run `python3 CHECK.py` in the same directory as these files. The packaged checker uses exact rational `fractions.Fraction` arithmetic and passed **292 exact assertions**: the claimed normalized Gegenbauer coefficient at dimensions 2–9 and degrees 1–12, its degree-four two-sphere specialization, and low-degree positive Legendre expansions for input orders 0–64.

These tests are finite consistency checks and cannot establish the universal quantifiers. The Legendre Bernstein inequality is used as a published theorem rather than independently reproved here. The classification of lower degrees for dimensions greater than two is not provided. An independent audit has not been performed.
