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
Run `python3 verify.py`.

The verifier independently constructs prime factorizations through
\[
10^6,
\]
computes
\[
D(n),\qquad \varphi(n),\qquad G(n)=D(n)-(n-\varphi(n)),
\]
and checks the complete claimed fibers from \(2\) through \(9\).

It also verifies the exact prime-power identity, the exact two-prime-support identity, and the three support lower bounds on every integer in the regression range. A successful run prints `VERIFY_OK`.

This finite replay is not used as a proof beyond the checked range. The all-integer proof is the symbolic argument in `RESULT.md`.
