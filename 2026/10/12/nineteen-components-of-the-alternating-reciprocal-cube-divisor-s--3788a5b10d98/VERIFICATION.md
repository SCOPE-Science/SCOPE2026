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

# Reproducibility checks

Execute `python3 verify.py` using only the Python standard library. The executable computes all local alternating divisor factors and their 32 rational low-prime interval blocks, checks five finite reciprocal-cube prime-witness inequalities and the three-prime Nagura bound, and certifies all mergers and strict gaps using the exact rational bounds
\[
\sum_{k=1}^{180} k^{-3}+(2\cdot181^2)^{-1}
<\zeta(3)<
\sum_{k=1}^{180}k^{-3}+(2\cdot180^2)^{-1}.
\]

The final line is `EXACT_CERTIFICATE_OK local_states=32 components=19 gaps=18 overlaps=13 zeta_terms=180 tail_witnesses=5`. The printed table consists of nineteen exact rational lower and upper coefficients. All conclusions about the infinite prime tail come from the mathematical proof and the cited Nagura theorem, not from this finite script. This check is reproducible but is not an independent scientific audit.
