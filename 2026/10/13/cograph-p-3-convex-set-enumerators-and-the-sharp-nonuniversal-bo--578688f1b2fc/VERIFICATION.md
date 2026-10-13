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
# Verification

The mathematical argument classifies every convex subset in a join and uses cotree induction; it is independent of finite tests. `verify.py` is a complete standalone Python 3 program using only the standard library. Its brute-force comparator tests every subset of every cograph in the labeled graph census of sizes one through six. The generator visits every labeled graph in these orders, accepting exactly the \(6{,}039\) instances with a valid join/union decomposition. Each accepted graph is compared coefficientwise with the polynomial produced by the cotree recurrence, and the upper bound/equality characterization is checked whenever its assumptions apply.

The program additionally checks four complete bipartite coefficient formulas and \(1{,}000\) reproducible randomly constructed binary cotrees of orders one through twelve against direct subset enumeration. Run `python3 verify.py`; the exact expected stdout is in `verify.out`.

Finite tests cannot establish the universal theorem. No independent scientific audit has been performed, and no claim of external certification is made.
