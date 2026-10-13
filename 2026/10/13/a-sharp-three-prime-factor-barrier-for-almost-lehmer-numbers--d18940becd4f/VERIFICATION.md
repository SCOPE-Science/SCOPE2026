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

The universal theorem is verified by the symbolic argument in `RESULT.md`; no finite enumeration is used to infer an infinite statement.

For a numerical regression check, `verify.py` uses the reduced denominator
\[
d=\frac{\varphi(n)}{\gcd(\varphi(n),n-1)}.
\]
If \(\varphi(n)\mid\ell(n-1)\), then \(d\mid\ell\). Conversely, if \(d\) is squarefree and divides \(n-1\), choosing \(\ell=d\) gives an admissible multiplier. Therefore, for semiprimes the code can test existence of a multiplier without searching multiplier subsets.

The program exhaustively checks every pair of distinct odd primes \(p<q\le5000\), totaling \(222778\) semiprimes, and finds no almost Lehmer example. It separately checks
\[
1729=7\cdot13\cdot19,
\]
for which the reduced denominator is \(3\) and \(1296\mid3\cdot1728\).

Observed output:

`VERIFY_OK semiprime_pairs=222778 max_prime=5000 sharp_witness=1729 denominator=3`

Limit: the finite search is only a regression test. Correctness of the unbounded claim rests on the proof in `RESULT.md`.
