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

Run `python3 verify.py`. The checker independently generates letters using base-\(q\) digit sums and tests the exact prefix formula for \(q=2,\ldots,9\), \(N\le3000\). It tests modular phase coverage for \(q=2,\ldots,6\), moduli \(1\le h\le12\), and for \(q=7\), moduli \(1\le h\le6\); then it searches additive block exponents for \(2\le q\le7\), \(1\le\ell\le3q\), in length-7000 prefixes. Each sample is finite. The all-base theorem and effective exclusion require the complete paper proof: eventual periodicity of powers modulo \(h\), disjoint-digit substitution gadgets, exact centered-prefix identity, and the contradiction on a nonzero cyclic residue of block endpoints. No independent external validation was performed.
