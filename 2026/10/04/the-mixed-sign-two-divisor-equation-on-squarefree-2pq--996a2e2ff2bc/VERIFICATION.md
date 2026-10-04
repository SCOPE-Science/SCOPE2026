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

The checker directly verifies the eight ordered divisor witnesses for
\[
\sigma(2pq)=4pq+d_1-d_2.
\]
It also reconstructs the finite algebraic reductions for \(p=3,5,7\).

For \(p\ge11\), the proof uses the symbolic inequalities
\[
pq-3p-3q-3>2p-1,
\]
together with the congruence obstruction for two \(q\)-multiples and the two remaining coefficient cases \(t=1,2\). The verifier checks the boundary inequalities used in that argument.

As an independent regression test, the program scans all odd prime pairs below \(2000\) and finds exactly
\[
30,42,70,78,110,130,154,170.
\]
This bounded scan is not used to infer the infinite theorem.

A successful replay prints `VERIFY_OK`.
