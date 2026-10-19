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

# Reproduction and scope
Run `python verify.py` with Python 3. No third-party packages are required. The exact finite checker exhausts 1,364 periodic words for a two-letter free action of a group of order two, at periods 1–5, and 1,332 periodic words for the regular action of the nonabelian symmetric group on three letters, at periods 1–2. It tests group action freeness, gauge inversion, one-step conjugacy, one-to-one periodic coding and predicted counts. The script does not verify infinite groups, nonfree cases or arbitrary period by exhaustive computation; the analytic proof covers every finite group satisfying the hypothesis. Independent audit has not been performed.
