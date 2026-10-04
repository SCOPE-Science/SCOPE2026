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
Compile `verify.cpp` with a C++17 compiler and run the resulting executable.

The proof first reduces every relevant ordinary component to
\[
q=m^2,
\qquad
1\le m\le10^9,
\]
using the parity of \(\sigma(q)\). The verifier therefore scans every odd root in that complete interval.

The segmented sieve reconstructs each root's prime factorization and evaluates
\[
\sigma(m^2)=\prod_{r^e\parallel m}(1+r+\cdots+r^{2e})
\]
with exact 128-bit unsigned integer arithmetic. It tests
\[
d=2m^2-\sigma(m^2)>0,
\qquad
d\mid\sigma(m^2),
\qquad
p=\frac{\sigma(m^2)}d.
\]

A successful replay prints `VERIFY_OK`, reports that exactly two square members occur in the full range, and lists only
\[
(q,p)=(1,1)
\]
and
\[
(q,p)=(9018009,22021).
\]
The latter is checked to satisfy \(22021=19^2\cdot61\).

`scan_output.txt` is the exact stdout of the packaged replay. The computation is exhaustive over the stated finite domain; it is not evidence beyond \(q=10^{18}\).
