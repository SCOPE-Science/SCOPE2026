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

The theorem is proved in `RESULT.md` using an exact binomial optimum-split correspondence, elementary moment bounds, a bounded-increment central limit theorem, and uniform Stirling/method-of-types bounds. The finite checker is a secondary consistency test rather than the source of the limiting theorem.

Run `python3 verify.py` (Python 3 standard library only). In every approval profile for each integer \(m\) from \(0\) through \(7\), the script constructs all allocations of jointly approved goods, directly maximizes the two-agent sorted-utility vector, and compares the result to the independently expressed binomial-coefficient count. For all \(341\) profiles with \(m\le4\), it additionally enumerates every ternary assignment of each good (unassigned, to agent one, or to agent two), imposes the clean constraints independently, and compares the globally optimal cardinality to the reduced formula. It also checks the exact iff test \(K_m>1\iff |a-b|<c\) and a separate Laurent-polynomial coefficient formula for the expected count at \(p=1/2\). Total profiles checked: \(\sum_{m=0}^{7}4^m=21845\). The recorded execution terminated with `PASS`.

The source code does not numerically certify the \(m	o\infty\) limit, publication priority, or invariance to changed assumptions. There is no independent scientific audit or independent validation recorded here.
