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

The universal proof is in `RESULT.md`. The attached checker is corroborative and uses exact integer prime counts from a sieve of Eratosthenes.

It verifies every case with
\[
kn<17
\]
by the exact integer comparison
\[
\pi(kn)^{k+1}>\pi((k+1)n)^k.
\]

It then checks the original conjecture for every
\[
5\le n\le2000,\qquad1\le k\le n,
\]
using logarithmic comparison as a finite stress test; the small boundary cases above remain exact integer comparisons.

For the same rectangle it checks the parity increment bound
\[
\pi((k+1)n)-\pi(kn)\le\left\lceil\frac n2\right\rceil
\]
and, whenever
\[
kn\ge17,
\]
the sufficient inequality
\[
\pi(kn)\log\pi(kn)>k\left\lceil\frac n2\right\rceil.
\]

Finally it checks
\[
\pi(x)>\frac{x}{\log x}
\]
for every integer \(17\le x\le100000\), as a stress test of the cited classical bound. This finite replay is not used to extend the bound beyond its checked range.
