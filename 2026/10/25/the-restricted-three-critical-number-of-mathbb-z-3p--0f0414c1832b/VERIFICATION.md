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

The proof checks the two possible fiber patterns: three nonempty fibers, or exactly one empty fiber. The prime-field inequalities used are \(|2^{\wedge}B|\ge\min\{p,2|B|-3\}\), \(|3^{\wedge}B|\ge\min\{p,3|B|-8\}\), and Cauchy–Davenport for sums of nonempty subsets of \(\mathbb F_p\). The lower-bound construction has size \(p+2\) and omits two explicit targets, so the lower and upper bounds match.

A finite sanity check verified the obstruction for \(p=7,13,19,31\) and sampled 300 subsets of size \(p+3\) for each of these primes. Those checks are not used as proof of the infinite claim. Scope is limited to primes \(p\ge7\) with \(p\equiv1\pmod3\). Independent audit and independent validation have not been performed.
