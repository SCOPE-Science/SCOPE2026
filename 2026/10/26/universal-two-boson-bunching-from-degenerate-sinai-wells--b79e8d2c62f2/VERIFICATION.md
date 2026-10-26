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

# Reproduction and limits

Use `python3 verify_condensate.py` with Python 3.11 or later; no extra packages, network access, random seeds, or external data are required. The program terminates with `PASS: 142018 exact or deterministic assertions`.

The verified tests independently count every sign path through length 12; reconstruct coefficients of the Catalan excursion decomposition; compute exact rational canonical weights on small chains and boson counts, checking detailed-balance ratios and bounded pair probabilities; establish exact clean-chain occupancy moments on finite uniform weak compositions; compare high-loading samples with the corresponding Dirichlet moments; and check the geometric tail series at three truncations using 110-digit decimal arithmetic.

Analytic facts checked in the proof: each bond's forward/reverse rate ratio equals its stationary weight ratio; nonminimal occupations have summable geometric envelopes at fixed chain length; ground allocations are uniform weak compositions; the Catalan excursion generating function takes value one-half at fugacity one-half; each fixed minimum multiplicity has limiting weight \(2^{-k}\); and the geometric sum equals \(4\log2-2\).

The computed finite assertions are not an exhaustive proof for arbitrary chain length or particle number. The relevant limits rely on the stated dominated-convergence, weak-composition, and coefficient-convolution arguments. Independent audit has not been performed.
