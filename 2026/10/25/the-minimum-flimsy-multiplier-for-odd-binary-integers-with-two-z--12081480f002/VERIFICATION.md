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
# Reproducibility

Execute `python3 verify.py` in a directory containing this file and `verify.py`. The verifier enumerates exactly 70 triples satisfying \(1\le a,c\le4\), \(0\le b\le4\), and \(a+b+c+2\ge7\). For each, it calculates the weights of four odd multiples by native arithmetic and an independently programmed bit-serial carry recurrence, and compares the least successful one with the five-case theorem. The output on a successful run starts with `VERIFIED`.

The infinite deduction requires the explicitly proved four-one saturation lemma and the lower bound for the weight of a positive multiple of \(2^r-1\). Finite sampling alone would not establish those statements. Extra checks through length \(80\) are solely corroborative; no claim is made beyond the theorem's domain.
