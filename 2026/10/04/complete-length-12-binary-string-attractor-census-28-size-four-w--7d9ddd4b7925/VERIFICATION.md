---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A string attractor is exactly a hitting set for the cover sets of all distinct nonempty substrings. An independent exhaustive implementation formed those cover sets for every binary word and tested candidate position sets exactly. It confirmed that lengths through \(11\) have minimum-attractor size at most \(3\), and at length \(12\) the exact distribution is \(2,1332,2734,28\) for minimum sizes \(1,2,3,4\). The same independent run recovered all \(28\) size-four words and exactly nine reversal/complement orbits with the nine representatives and orbit sizes stated in the source package.

## originality

PASS

The exact-computation literature supplies general algorithms, and OEIS records the maximum minimum-attractor size and the number of size-two words, including the first appearance of size four at length \(12\). However, the inspected complete exact-computation paper and the checked OEIS entries do not give the full \(2/1332/2734/28\) distribution, the full list of \(28\) extremizers, or the nine reversal/complement classes. Resultary returned no equivalent census.

## value

PASS

Length \(12\) is the first binary length at which the worst-case minimum-attractor size reaches four. Classifying every extremizer at this first boundary, together with its full distribution and symmetry quotient, is a natural finite cutoff rather than an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
