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

# Reproduction and scope of verification

The accompanying `verify_crown.py` requires Python 3.8+ and no external libraries. Execute it with `python3 verify_crown.py`. It constructs the labelled graph implicitly by omitting the matched neighbour at each vertex; every state is tested with two literal synchronous majority rounds. `verification_output.txt` records the execution performed for this result.

The computation enumerates all \(2^{2n}\) labelled binary configurations for each \(n=3,4,5,6,7,8,9\), checks the exact fixed and recurrent counts, checks the unique nontrivial two-cycle for every checked odd parameter, and verifies \(F^3=F\) for each checked even parameter.

The infinite-family theorem is established by the proof in `RESULT.md`: the strict symmetric cross-time energy limits all periods to one or two, while an exhaustive symbolic split of cardinality regimes identifies the periodic points. Neither successful finite tests nor the energy argument alone implies the exact census; the middle-layer case analysis is necessary.

No claim is made about every odd-case transient depth, basin distribution, or independence from all possible unpublished material. Independent audit has not been performed.
