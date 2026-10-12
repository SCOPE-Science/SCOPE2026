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

For two independent Bernoulli variables with parameters \(p,q\), write \(s=p+q\) and \(\Delta=(p^2+q^2)/s\). The proof uses the exact identities
\[
2pq=s(s-\Delta),
\]
\[
r_1=e^s(1-s+\Delta),
\qquad
r_2=e^s\left(1-\frac{\Delta}{s}\right),
\]
and the exact feasible bounds
\[
\Delta\le s\le2\Delta.
\]
The first ratio decreases and the second increases in \(s\) at fixed \(\Delta\), yielding the two endpoint candidates \(e^\Delta\) and \(e^{2\Delta}/2\). Their equality point is exactly \(\Delta=\log2\).

The standalone `VERIFY.py` reads no external data. It checks the exact ratios against their closed forms on a dense grid of rational Bernoulli parameters, verifies the sharp fixed-\(\Delta\) envelope numerically, checks representative equality cases on both sides of \(\log2\), and verifies that the envelope is strictly smaller than \(1/(1-\Delta)\). The finite checks are regression tests only and are not used to justify the analytic theorem.

Unproved limit: nothing in this package proves the conjectured \(\Delta\)-bound for three or more active Bernoulli parameters.
