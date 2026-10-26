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

Run `python3 verify.py` with Python 3 and no third-party packages. The program implements the theorem's finite construction and separately checks independent-set feasibility, maximality for every unallocated item and every agent, and the exact EF1 comparison for every ordered agent pair.

Output observed on the embedded source:

```text
PASS exhaustive 187375 instances; branch counts {'large': 141858, 'doubleton': 35676, 'singleton': 9841}
PASS randomized 6000 instances
PASS common monotone set valuation 4885 instances
PASS four-agent K(3,3) contrast; 420 maximal allocations, none EF1
```

The exhaustive portion covers part profiles up to eight goods and additive weights \(0,1,2\). The monotone-set-function tests include normalized monotone Boolean functions on four goods and sampled monotone upward envelopes for larger small domains. The four-agent contrast independently enumerates all candidate allocations for the established six-good instance. Exact comparisons use integers and no numerical tolerance.

Finite checks cannot establish a theorem for arbitrarily many goods. The general guarantee depends on the last-received-item lemma, the maximality argument using nonempty bundles, and the doubleton singleton-value comparison in `RESULT.md`. The known four-agent impossibility is separately proved there. The verification has not been independently audited.
