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

# Reproducibility and verification

Run `python3 check_frog_window.py` using Python's standard library. The script compares two exact rational finite-\(n\) recurrences, checks the preassigned-trajectory indegree-zero factorial moments and their inclusion–exclusion inversion, and verifies the one-step root-death atom. Expected status: `PASS`, with 545 initial and 720 additional exact assertions (total 1,265). No seed or external data are needed.

The infinite theorem is proved analytically in RESULT.md: the critical ingredients are the forbidden-set avoidance identity, a factorial-moment Poisson estimate with growing truncation length, the birth–death supermartingale, and a uniform union bound over hidden unreachable subsets. The finite checker does not certify these asymptotics. The main remaining historical risk is a broader epidemic theorem with the same sharp first correction; independent validation has not been performed.
