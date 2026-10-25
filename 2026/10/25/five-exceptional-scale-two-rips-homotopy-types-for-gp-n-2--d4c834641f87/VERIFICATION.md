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

# Reproducible exact checks

Place `verify_gp_small.py` beside `MORSE_CERTIFICATE.json` and run `python3 verify_gp_small.py`. Both files are included in full in the package. The code uses only the Python standard library; the certificate gives explicit matched and critical simplices for all five cases.

The verifier reconstructs all 254, 288, 342, 352 and 388 nonempty faces for the respective parameter values. It checks exactly 126, 143, 170, 175 and 192 matching pairs. Every pair is a valid codimension-one incidence, every simplex is matched exactly once or explicitly critical, and a whole-Hasse-graph topological sort establishes the acyclic condition. The code also computes independently the complete boundary ranks over \(\mathbb F_2\); these are auxiliary checks, not an integral homotopy argument.

The observed final line is `GP_SMALL_EXCEPTIONS_EXACT_CERTIFICATE_OK`. The mathematical passage from this finite certificate to the homotopy decomposition uses Forman's discrete Morse theorem and the elementary attaching-map observation for CW complexes with a single vertex and no one-cells.

Limitations: the calculation covers exactly the indicated five finite graphs at inclusive radius two. It neither enumerates larger parameters nor independently establishes novelty in the entire literature. Independent external audit is not performed.
