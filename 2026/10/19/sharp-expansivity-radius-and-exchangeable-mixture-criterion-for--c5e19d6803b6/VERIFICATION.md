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

The accompanying standard-library checker can be run with `python verify_examples.py` from the extracted result directory. In the tested environment it reported:

`PASS: 51 exact weighted sums, 200 interval thresholds, mixture normalization and witness radii`

The checker performs finite rational-arithmetic identities: it checks \(S_K=3-2^{1-K}\) for \(0\le K\le50\), the thresholds of 200 uniform-support intervals, countable-mixture partial-sum normalization, and finite witness-radius inequalities. It is not a certificate of Borel–Cantelli, the de Finetti representation, or the all-target all-radius theorem; those are proved mathematically in RESULT.md.

In the main proof, the probabilistic step is the second Borel–Cantelli lemma on independent disjoint coordinate blocks with a uniform strictly positive event-probability lower bound. For the mixture converse, only positive mixing mass on components of small enough diameter and a finite covering of their support midpoints are needed. No numerical approximation or external theorem about convergence speed is used.

The review above is an internal consistency assessment only, not independent validation. The classical de Finetti theorem and second Borel–Cantelli lemma are used as established mathematical results. No external audit has been performed.
