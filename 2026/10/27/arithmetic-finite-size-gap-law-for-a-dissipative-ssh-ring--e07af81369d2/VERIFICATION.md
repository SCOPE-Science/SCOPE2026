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

# Verification and limitations

The proof gives a branch-independent gap formula and a uniform two-sided local expansion, so zeros and small-divisor asymptotics are analytic results rather than inferences from a finite grid. Replay `python3 verify_gap.py` using Python 3. The calculation evaluates the cited two-branch Bloch spectrum directly for rational and quadratic-irrational test parameters; it tests selected finite sizes only and cannot establish the infinite statements. Source normalization: arXiv:2203.01333, Eqs. (2.5), (2.23), and Appendix A. Classification: MSC 81S22. No independent audit was conducted.
