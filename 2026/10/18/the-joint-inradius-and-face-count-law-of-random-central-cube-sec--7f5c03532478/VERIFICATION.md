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

Run `python3 verify_joint_cube_section.py` with standard Python 3 from a directory containing that file. The script constructs 2,500 random exact intersection polygons from the cube's 12 edges, computes each section inradius from independent projected polygon edges, and checks the analytic type threshold. It performs deterministic Simpson quadrature on each angular-density branch and checks the total mass, the known unconditional hexagon probability to \(10^{-8}\), and strict monotonicity at 99 interior points. An executed run printed `VERIFY_OK`.

# Mathematical scope and unproved limits

The proof in `RESULT.md` covers every real direction except geometric null sets and obtains the probability law by exact spherical area. The executable finite experiments verify concrete sample cases only, and the quadrature has numerical rather than symbolic exactness. The code does not certify absence of earlier priority, uniqueness of every possible representation, non-Haar plane measures, or higher dimensions. No independent audit was performed.
