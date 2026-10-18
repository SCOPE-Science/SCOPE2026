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

# Reproducibility and checks

Run `python3 verify.py` with Python 3 and no external packages. This executable performs an independent finite check of the original sequence generation and the postorder characteristic word, followed by exact integer checks of all hierarchical-stage extrema and attainment. Its output is `VERIFY_OK cases=24 positions=154770`.

For the infinite proof, inspect the induction proving that every word \(W_h\) has total weighted sum \(1\), prefix minimum \(0\) and prefix maximum \(1+h(k-1)\); then apply this to the \(q\) repeated copies plus the terminal negative-weight symbol, and finally compare the stage lengths to \(k^h\). The finite program supports these formulas but is not an exhaustive check for all parameter choices or all indices.

Scientific limitation: the characteristic-word correspondence is a theorem from the cited literature. Independent external validation has not been performed.
