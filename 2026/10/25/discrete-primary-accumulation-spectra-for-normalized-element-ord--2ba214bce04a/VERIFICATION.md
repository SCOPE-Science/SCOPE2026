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

# Exact verification

Execute `python3 verification/check_moments.py` with Python 3 (standard library only). The checker generates every partition of each integer up to 10 (corresponding to all abelian \(p\)-group invariant-factor types in that range). For each \(p\in\{2,3,5\}\) and \(k\in\{1,2,3,4\}\), it independently enumerates element-order multiplicities, computes \(F_k\) using exact rational arithmetic, and compares with the identity involving \(E_{p,k}(H)\) whenever \(\ell>b\). Exactly **624** partition/prime/moment cases satisfy this restriction and are checked. In separate parameter sweeps it checks the asserted positive correction and quantitative upper bound for \(p\in\{2,3,5\}\), \(k\in\{1,2,3\}\), \(0\le b\le4\), and \(\ell\in\{b+1,b+3,b+7\}\).

Observed output: `VERIFY_OK exact_partition_cases= 624  and uniform error bounds`.

The checker does not enumerate all finite groups or establish any infinite limiting property. Those follow from equations (1)–(5) and the complete argument in `RESULT.md`. All arithmetic checks use `fractions.Fraction`, avoiding numerical rounding. Independent scientific audit is not performed.
