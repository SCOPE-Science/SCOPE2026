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

Run `python checker.py` with NumPy, SciPy and SymPy installed. The script was run on the actual standalone file and reported: `PASS: 4 symbolic relations, 1050 randomized exact-step/secular/bound/sharpness families, 6 fixed-norm sequences`.

The fixed \(3\times3\) block has numerical eigenvalues \(-1.36264138536\), \(-0.46513000\), and \(1.57777138\), so the hidden correction relative to the retained \(-5/4\) eigenvalue is approximately \(0.11264138536\). The symbolic identities, direct matrix products, and finite tests do not by themselves prove the universal quantifiers. The proof's strict monotonicity and orthogonal block decomposition establish those.

Compression semantics tested: initialize \(b=He_0\) exactly; after the exact first update, retain old active entries and drop only previously zero leaf entries with update magnitude at most \(\tau\). No claim is made about full-algorithm termination from this state. An independent mathematical audit has not been performed.
