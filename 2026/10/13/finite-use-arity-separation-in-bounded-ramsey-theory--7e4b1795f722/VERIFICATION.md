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

The load-bearing source statement is Patey--Shafer's Theorem 1.7:
\[
\forall k\in\mathbb N\qquad
\mathsf{BRT}^{3}_{2,4}\not\leq^k_\omega\mathsf{RT}^{2}_{2}.
\]

The additional simulation is explicit.

Given a valid bounded-pair instance
\[
(\ell,f),
\qquad
f:[\mathbb N]^2\to2,
\]
use \(f\) itself as an \(\mathsf{RT}^{2}_{2}\) instance.

If an infinite Ramsey-homogeneous set \(H\) had color \(1\), then any \(\ell\)-element subset of \(H\) would violate the bounded-instance promise. Hence every possible infinite Ramsey solution has color \(0\) and solves the bounded instance.

Therefore each use of the bounded pairs principle can be replaced by one use of ordinary pair Ramsey. Any reduction with a fixed finite number of bounded-pair calls would induce a reduction with a fixed finite number of ordinary pair-Ramsey calls, contradicting Theorem 1.7.

## Limits

The argument rules out only bounded finite iteration.

It does not settle unrestricted \(\omega\)-reducibility.

No computational experiment is needed.
