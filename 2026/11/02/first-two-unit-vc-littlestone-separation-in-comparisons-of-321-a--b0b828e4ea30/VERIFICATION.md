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

# Reproduction

Requires Python 3.9 or newer, no third-party modules. In the unpacked directory run:

```
python3 verify.py
python3 upper_obstruction.py
```

The first command exhaustively regenerates every involution with forbidden pattern testing for each size 1 through 12, verifies the established cardinality \(\binom{n}{\lfloor n/2\rfloor}\), enumerates every shattered query support, evaluates the exact complete-tree recurrence, and verifies the complete depth-seven and depth-eight certificates with a concrete distinct witness at each terminal leaf. It cross-checks the concept enumeration against all ordinary permutations for sizes at most eight. The second command independently recomputes Boolean depth feasibility and rejects depths eight and nine at sizes eleven and twelve, respectively.

The critical count checks are \(462\) concepts, VC search 27,977 recursion nodes, and adaptive recursion 28,764 memoized version spaces at eleven; \(924\) concepts, 257,991 VC nodes, and 272,863 memoized version spaces at twelve. Root query minority maxima are \(126\) and \(252\), giving immediate impossibility of the next adaptive depths. The stored trees contain respectively 128 and 256 distinct terminal witness indices, and their comparison responses are checked at every branch.

`make_certificate.py` is optional and regenerates the included `tree_certificate.json`. The verification exercises only the stated finite ranges; it does not prove that observed formulas extend to larger sizes or that no equivalent historical result exists.
