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
# Verification and limits

The executable `verify_quotient_spectrum.py` is Python standard-library code that enumerates the two known geometric short orbits as permutation sets for \(q\in\{8,16,32,64,128\}\), checks all expected involution fixed-point counts, and recomputes quotient genera. Execution returned `QUOTIENT_SPECTRUM_SANITY_OK`.

The mathematical proof for all \(q=2^h\ge8\) is separate: use the group presentation and two stabilizer orbits established in the original article, the count of two geometric fixed points of the elliptic involution, weak ramification on ordinary curves, and the degree-four biquadratic intermediate-field construction. To verify the rational equation, pull the quotient Artin–Schreier class back across \(E\to\mathbb P^1\) locally at each point of \(T\) and compare the coefficient by the residue of \(f\omega\). These are symbolic infinite-family arguments, not consequences of the finite checker. Independent audit has not been performed.
