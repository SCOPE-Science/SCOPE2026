---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For W_n=K1 vee C_n, a hub-containing initial set forces exactly when its rim trace contains an adjacent pair: a blue boundary rim vertex can then extend a run; a rim independent trace has no possible first force. Hub-free connected sets are either a rim arc or the full rim and force exactly when their size is at least 3, since an interior blue rim vertex first forces the hub. Counting hub cases subtracts the cycle independence polynomial from (1+x)^n; rim-only runs add n x^j for 3<=j<=n-1 and x^n. Marked cyclic gaps prove i_{n,k}=n/(n-k)*binom(n-k,k). Independently simulated every subset for n=4,...,10, matching all coefficients and z_c(W_n;3)=2n.

## originality

PASS

PASS best of knowledge: the 2025 Brimkov–Davila–Schuerger wheel proposition states Z_c(W_n)=3 and connected-forcing density, but not the complete structural classification nor its all-cardinality polynomial; general extremal coefficient formulas determine only some degrees. Earlier connected-forcing papers give definitions and other families.

## value

PASS

PASS: z_c(G;j) is an explicitly studied all-cardinality connected-forcing invariant. The polynomial gives a complete uniform classification for a standard infinite graph family and reveals a nontrivial link to the rim independence polynomial; it is not merely the known scalar forcing number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
