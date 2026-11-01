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

# Reproducibility and verification

Run the included standalone program with `python3 verify.py`; it needs only Python's standard library. It reconstructs \(\Delta_k(P_n^2)\) directly from disconnected complement sets. For 66 pairs with \(5\le n\le15\), \(2\le k\le n-3\), it evaluates the signed chain Lefschetz sum without using the closed character formula, independently counts reflection-symmetric connected complements, and checks trace bounds and parity. For eight selected pairs, it explicitly constructs oriented simplicial boundary matrices in the \(\pm1\) eigenspaces of reversal and computes modular ranks over \(\mathbb F_{101}\). All these checks passed when the packaged script was executed.

The finite chain computations confirm the formulas in tested cases but do not establish the infinite-parameter theorem or integral lattice structure. The proof's infinite step instead uses the published shellability and complement classification together with exact orbit and palindromic-gap enumeration. No independent external mathematical audit has been performed.
