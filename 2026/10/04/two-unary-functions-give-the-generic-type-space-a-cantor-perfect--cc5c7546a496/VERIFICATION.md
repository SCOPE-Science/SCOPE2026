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

The proof is deductive. The checker supplies bounded sanity tests for its two constructive mechanisms.

`verify.py` exhaustively enumerates all reachable pointed deterministic algebras with two unary functions on \(n\le 4\) states. It quotients by rooted isomorphism and obtains the isolated finite-orbit counts
\[
1,\ 12,\ 216,\ 5248
\]
for orbit sizes \(1,2,3,4\). It also verifies that every rooted automorphism is trivial, as follows abstractly because the distinguished root generates the entire algebra.

For the density argument, the checker constructs finite completions whose equality pattern agrees with the free two-function term tree through depths \(0,\dots,5\). For the perfect-kernel mechanism, it checks the symbolic placement of two distinct infinite extensions beyond every visible depth \(0,\dots,7\): both preserve the visible free cylinder but differ at a later \(F\)-transition while an untouched \(G\)-ray remains infinite.

Running the script prints `VERIFY_OK`.

These bounded checks do not certify the infinite theorem. The infinite proof is the finite-diagram argument in `RESULT.md`, using quantifier elimination and the fact that the empty theory imposes no restrictions on completing a finite partial unary-function diagram.
