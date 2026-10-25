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

Run `python3 CHECK.py` with a standard Python 3 interpreter. The self-contained checker uses `fractions.Fraction` and verifies one-step planar matrix updates, squared-norm identities, all sampled-pair coupling formulas, interpolation in sampling correlation, the quartic threshold differences, and the rational strict-separation example. The execution recorded 1,490 passing exact-rational assertions.

The all-parameters classification is proved in RESULT.md from exact algebra, not from a finite enumeration. The checker does not constitute a formal proof of an infinite family. Expected squared error \(\mathbb E\|z_k\|_2^2\) is the only long-time convergence criterion certified here; no almost-sure or non-bilinear theorem is asserted.
