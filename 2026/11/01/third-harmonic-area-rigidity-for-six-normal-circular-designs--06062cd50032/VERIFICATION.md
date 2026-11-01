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

Run `python verify.py` with Python 3. The standalone script depends only on standard library modules and performs 10,919 numerical checks of closing edge vectors, equal-weight design moments, shoelace area, third-harmonic area, endpoint behavior, and the sharp quadratic ratio. Deterministic seed: 428621.

The mathematical proof does not rely on the script: Newton identities plus the self-inversive root polynomial establish the complete six-node shape classification; a signed-edge shoelace computation establishes the area; an elementary triple-angle identity produces the two best constants. Finite tests do not prove those universal steps.

Full text of the 2026 motivating geometric source and 2025 group-orbit source was inspected. Two historical circle-design references could be identified only through their metadata or summaries; priority for the exact area law is provisional. A separate independent scientific audit is not part of this verification.
