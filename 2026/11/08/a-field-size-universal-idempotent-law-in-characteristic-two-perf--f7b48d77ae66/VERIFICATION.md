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

# Reproducibility

The C++17 source `verify.cpp` enumerates all invertible structure matrices and all vectors over explicitly represented binary finite fields, counts solutions of \(x=M^{\mathsf T}x^{[2]}\), subtracts the zero idempotent, and compares exact histograms. It uses irreducible polynomials \(z^2+z+1\) for \(\mathbb F_4\) and \(z^3+z+1\) for \(\mathbb F_8\). Integer arithmetic is exact; no randomized sampling is used.

Build: `g++ -std=c++17 -O3 verify.cpp -o verify`

Execute: `./verify`

Expected terminal status: `VERIFY_OK cases=6 matrices=205482`. The exact recorded output is included as `verification_output.txt`. Checked cases are \((n,q)=(2,2),(2,4),(2,8),(3,2),(3,4),(4,2)\). These are *finite regression checks*, not exhaustive verification for arbitrary \(n\) or \(q\).

# Independent audit and scientific boundaries

An independent audit has not been performed. The mathematical proof of the general statement is in `RESULT.md`. The classical general-linear-group fixed-space formula is not a new theorem; the new theorem identifies it with characteristic-two evolution-algebra idempotent counts. Historical-priority assessment has residual limits concerning general semilinear finite-field literature.
