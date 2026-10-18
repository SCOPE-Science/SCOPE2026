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
Run `python3 VERIFY.py` with `CERTIFICATE.json` in the same directory, using only the Python 3 standard library. The verifier reconstructs oriented rook-placement faces from first principles, checks that successive boundaries compose to zero, verifies the eight-triangle octahedral two-cycle, and checks the integral identity \(\partial_3 w=3z\) with exactly 68 unit tetrahedral coefficients. It evaluates every one of the 600 rational dual coboundary inequalities using integer numerators over denominator three and checks the exact pairing \(\langle y,3z\rangle=68\).

It also constructs a mod-three boundary column basis of rank 423 and confirms \(z\) reduces to a nonzero remainder; exhaustively examines all six-vertex vertex subsets and counts the 1800 induced octahedral spheres in two row/column-interchanged types of size 900 each. These are exact finite checks, not floating-point or randomized sampling. The included primal and dual certificate data are sufficient to replay the sharpness bound independently.

# Mathematical limits
No inference is made to arbitrary board dimensions, nonsymmetric cycles, or other chain norms. The program does not prove novelty or publication priority, and the homological generator's classical description is attributed to prior work. An independent scientific audit has not been performed.
