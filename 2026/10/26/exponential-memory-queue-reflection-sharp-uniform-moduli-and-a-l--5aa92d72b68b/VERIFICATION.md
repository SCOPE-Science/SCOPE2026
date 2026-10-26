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

# Reproduction and verification

Run the standalone file `verification.py` with Python 3 (standard library only). Its independent event recursion evaluates the memory and integral regulator for sampled right-continuous step inputs, then checks against the direct weighted-supremum evaluation. It also tests sharp uniform examples and terminal-time separation for time-shifted pulses; the event implementation computes memory decay and reflects continuously on elevated plateaus.

The analytic proof, rather than the finite program, establishes the solution for all real càdlàg input paths, the two exact operator constants, the quantitative \(J_1\) bounds, and both global \(J_1\) obstructions. To reproduce the latter regulator obstruction, use two pulses with the **same start** and endpoint difference \(h\): the total regulator changes by exactly \(\beta Hh\) while the input \(J_1\) distance is at most \(h\).

Scientific limits: no claims for arbitrary nonexponential kernels; no independent audit or external mathematical certification has been performed.
