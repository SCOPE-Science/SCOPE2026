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

The proof is symbolic and unbounded. A separate exact-integer regression checker enumerates every \(N\) with
\[
2\le N\le200000,\qquad \omega(N)\le3,
\]
computes
\[
\sigma^*(N)=\prod_{p^e\parallel N}(p^e+1),
\]
and tests the equivalent divisibility condition
\[
N\mid \sigma^*(N)+1.
\]
The sole hit is \(N=2\), for which \(M=(\sigma^*(2)+1)/2=2\).

This computation is only a consistency check. It neither establishes the infinite theorem nor excludes solutions with \(\omega(N)\ge4\). The mathematical proof in `RESULT.md` supplies the unbounded classification.
