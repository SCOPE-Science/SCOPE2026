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

# Verification

The standalone file `verify.py` uses only Python standard library. Executed command: `python3 verify.py`. Output: `PASS; checks: 1537`. It independently reconstructs all two-stage oscillator updates and checks 750 deterministic random frequency-step-state triples against the closed map and energy factor (1,500 assertions). It certifies strict rational sign brackets around both roots using alternating exponential series and exact fractions; the two exponential arguments are less than one. It also checks the nontrivial energy phase and four long-time asymptotic examples. These finite checks are not a substitute for the strict-convexity and derivative proofs in RESULT.md.

Numerical enclosures with exact rational sign certificates:
\[
1.577421180854<s_*<1.577421180856,\quad
1.026544029217<s_{\mathrm d}<1.026544029219.
\]
Unproved here: general Hamiltonian symplecticity, higher-dimensional coupled oscillator behavior, finite-precision effects, and independently certified publication priority. The shape parameter is defined from exact frequency information; the source's statewise quotient must be continuously extended at coordinate zeros.
