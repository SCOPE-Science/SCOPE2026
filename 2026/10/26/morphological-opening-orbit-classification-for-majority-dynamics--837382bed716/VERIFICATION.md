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
The standalone `fan_majority_verify.py` program constructs the full majority rule from the fan adjacency, enumerates all states for \(3\le n\le12\), and independently computes the polynomial transfer census. It confirms two fixed states and \(\(2+2H_n\)\) periodic states at each tested length, including the absence of two-cycles at \(n=4\). The complete mathematical proof covers every integer \(n\ge3\); finite enumeration is a corroboration only.

To reproduce, run `python3 fan_majority_verify.py` in the directory containing this document and compare stdout to `fan_majority_verify.out`. No nonstandard Python packages are used. This computation does not certify historical uniqueness or independent scientific validation.
