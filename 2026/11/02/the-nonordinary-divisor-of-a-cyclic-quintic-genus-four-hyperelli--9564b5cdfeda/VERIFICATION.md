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

# Reproducibility and limits

Run `python3 verify_cyclic5.py` in the same folder using Python 3 and its standard library. The program expands the genus-four hyperelliptic Cartier matrices directly from coefficients in \(\mathbf F_p[\lambda]\), recomputes symbolic determinants via all \(4!\) permutations, and tests the one-step and four-step semilinear ranks at all admissible coefficients in \(\mathbf F_3\) and \(\mathbf F_{49}\). Expected final line: `CYCLIC5_EXACT_DETERMINANTS_AND_STABLE_RANKS_OK`.

The checks observed exact determinant polynomials of degrees \(3\) and \(9\); the geometric nonordinary support consists of \(1\) point in \(\mathbf F_3\) and \(3\) points in \(\mathbf F_{49}\). These computations verify polynomial identities and sample field outcomes. They do **not**, by themselves, prove the uniform geometric rank dichotomy in arbitrary characteristics \(p\equiv2,3\pmod5\); that is established by the four-cycle argument in RESULT.md. No machine-formal proof or independent external mathematical audit is claimed.
