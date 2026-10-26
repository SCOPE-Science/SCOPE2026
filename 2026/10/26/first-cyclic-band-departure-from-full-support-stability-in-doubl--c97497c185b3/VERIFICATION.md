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

# Reproducibility

Run `python3 checker.py`. It requires only Python standard-library `fractions`. It recreates each supported-edge incidence matrix, inverts each grounded Gram matrix exactly, computes all \(440\) symmetry-representative \(\ell^\infty\) row sums, and verifies the finite strict-KKT witness at \(n=13\), \(k=7\).

The exact exceptional norm is \(3745290244/1096631627\) and its excess over full support is \(99556468/14256211151\). The witness uses positive inputs with perturbation size \(1/1000\); the smallest fitted active entry is \(77794225863/548315813500\), and the least off-support KKT multiplier is \(1094735762271/1096631627000\). All these are positive rational numbers, checked without tolerances. The checker ends with `ALL EXACT CHECKS PASSED`.

The finite exhaustive classification is **only** among consecutive cyclic bands for \(3\le n\le13\). The general graph-to-projection identity is proved algebraically in `RESULT.md`; the checker supplies the exact finite certificate. It cannot independently certify historical novelty or any unclaimed parameter ranges.
