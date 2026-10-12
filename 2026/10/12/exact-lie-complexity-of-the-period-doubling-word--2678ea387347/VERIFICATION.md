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

Run `python3 verify.py` beside `certificate.json`.

The verifier generates the period-doubling fixed point directly from
\[
\delta(0)=01,\qquad\delta(1)=00.
\]
For each length \(1\le n\le192\), it forms the factor set in a prefix of length \(2^{15}\) and checks that the same factor set is already present in a prefix of length \(2^{14}\).

It then enumerates every cyclic-conjugacy class whose representatives all occur and compares the result with the two explicit morphic families
\[
[\delta^k(0)]_C,\ [\delta^k(1)]_C
\]
and
\[
[\delta^k(000)]_C,\ [\delta^k(001)]_C.
\]
It independently checks the doubling bijection for all half-lengths through \(32\), the two base cases, and the absence of \(11\) and \(0000\).

These finite computations are regression checks. Completeness for all lengths follows from the symbolic parity and desubstitution proof in `RESULT.md`, not from stabilization of a finite prefix.
