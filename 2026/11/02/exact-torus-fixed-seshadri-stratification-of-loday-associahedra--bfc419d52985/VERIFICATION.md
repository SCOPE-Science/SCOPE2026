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

# Reproducibility and scope

Execute `python3 check_associa.py` using Python 3 with only its standard library. The script constructs rooted full binary trees, independently recomputes Loday vertex coordinates, generates all rotations and uses integer gcds to compute lattice edge lengths. It exhaustively checks the binary trees for every integer parameter from 2 through 8, and all coordinate-cut widths in that range; a coefficient recurrence verifies the algebraic generating series through 11 internal nodes. Expected terminal line: `VERIFY_OK`.

The key analytic and all-dimensional mathematical arguments are the toric invariant-curve nef calculation, the Loday rotation-coordinate identity, the maximal-depth cherry bound, the avoidance-class root decomposition, and the lattice-width cut bound. Those are mathematical proof steps, not claims established solely by the finite checker.

The dense-torus identity is attributed to Ito's 2026 theorem; no independent assessment of that paper or other external work is claimed. Independent mathematical audit: not performed.
