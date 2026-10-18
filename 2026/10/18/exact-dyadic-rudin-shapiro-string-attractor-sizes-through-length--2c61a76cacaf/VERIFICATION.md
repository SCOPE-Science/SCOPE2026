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

# Reproduction and finite-proof boundary

From this directory, execute `python3 verify.py`. It requires only Python 3.10+ and local `certificates.json`. It regenerates the Rudin–Shapiro prefix in two independently stated ways, enumerates every distinct factor, reconstructs the inclusion-minimal position coverages, checks the stored antichains by equality, verifies four explicit attractor sets and four integer dual lower bounds, and runs a complete finite exact-cover search to exclude equality at lengths 128, 256, and 512.

Observed fresh-package execution:

```text
PROOF n=128 factors=7008 minimal=48 lower_dual=9 exact_cover_states=30 options=16 memo=30 optimum=10
PROOF n=256 factors=28128 minimal=64 lower_dual=10 exact_cover_states=2566 options=45 memo=2566 optimum=11
PROOF n=512 factors=112608 minimal=80 lower_dual=11 exact_cover_states=1316 options=82 memo=1316 optimum=12
PROOF n=1024 factors=450528 minimal=96 lower_dual=12 optimum=12
VERIFY_OK Rudin-Shapiro dyadic attractor profile = 10,11,12,12
```

The certificate verification is finite and exhaustive for the four concrete words only. In the exact-cover step, every hypothetical attractor saturating the dual lower bound must select positions meeting exactly the indicated number of positive-dual coverages, with each such coverage met exactly once. The verifier enumerates all assignments of these incidences, rejecting an assignment only when the remaining required coverage cannot possibly be reached; it uses only provably dominance-preserving candidate reductions. An upper witness together with the dual-plus-unsatisfiability certificate proves the listed exact values; an optimization transcript by itself does not.

No outside expert review, formal-system certification, or independent audit is claimed. Novelty may be affected by inaccessible full prior records or unindexed earlier calculations; those limits do not affect the self-contained correctness check.
