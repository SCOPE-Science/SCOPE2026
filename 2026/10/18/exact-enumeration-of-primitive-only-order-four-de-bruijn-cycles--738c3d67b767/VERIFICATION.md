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

# Reproducibility and limits

Run `python3 verify.py` in the same directory; it requires only the Python 3 standard library.

The code constructs both directed overlap graphs from their literal four-word arcs and exactly computes integer reduced Laplacian determinants for \(q=2\) and \(q=3\) using fraction-free elimination. It checks directed-tree counts and the BEST factorial product. Separately it computes the complete-graph low-rank determinant as exact fractions for \(2\le q\le8\). Exhaustive binary cyclic-rotation representatives at length 12 are tested directly against all required primitive four-factors. Successful execution prints `ALL_CHECKS_PASS`.

Numerically: \(t_0(2)=16\), \(t_P(2)=4\); \(t_0(3)=94143178827\), \(t_P(3)=10331213040\). Their ratios agree with the symbolic values \(1/4\) and \(80/729\), respectively. The resulting cycle totals are \(4\) and \(2708265511157760\). Finite tests are not a proof for unbounded alphabets; the result's general proof is the low-rank Laplacian calculation in `RESULT.md`. Source priority remains subject to independent bibliographic review.
