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

# Reproduction and mathematical verification

Run the accompanying `verify.py` using Python 3 and its standard library only. It exhaustively enumerates independent possible sampled subsets in \(3\le m\le12\) with minority corruption and checks both exact state transitions, sampled-rank selection, the median identity, odd-rank sign transition under full support, and the sample cutoff. It then tests selected large-sample asymptotic ratios and a specified finite-population rare-event example. The observed replay output is `VERIFIED 431104 deterministic exact-combinatorial and numerical assertions`.

The infinite-number-of-iterations conclusions use the exact iid median construction plus the standard independent-event law; no finite run certifies almost-sure behavior. The sharp growing-sample theorem follows from the uniform falling-factorial comparison (logarithmic error \(o(1)\)), Stirling asymptotics, and dominated convergence for the binomial tail; finite experiments are not substituted for that proof. A nondegenerate stationary variance requires positive transition mass in both directions; the exact formula also handles degenerate stationary measures when unique.

The comparison with prior publications is a same mathematical model literature assessment, not independent validation. Method selection conventions and exceptional cases are specified in `RESULT.md`. The relation \(c_s/m_s=\beta+o(1/s)\) is essential for the stated sharp constant; outside that regime the constant may change.
