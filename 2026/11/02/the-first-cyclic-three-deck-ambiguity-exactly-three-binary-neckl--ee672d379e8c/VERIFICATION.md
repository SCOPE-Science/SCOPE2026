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

# Reproduction and verification

Run `python3 verify.py` from the directory containing the extracted files. It requires Python 3 and the standard library only. A successful replay prints complete length-by-length profile distributions and ends with the exact string `VERIFY_OK`.

The checker independently implements the same three-binomial signature in two ways: `explicit_deck` enumerates every index combination according to the mathematical definition, while `recurrence_deck` builds all counted subsequences from left to right. It compares both at every cyclic root and checks every canonical binary necklace for \(1\le n\le8\) (93 representatives, 596 indexed roots, 510 input words before symmetry reduction). It asserts the exact three exceptional necklaces and their cut-index pairings at length eight, full distribution per length, and the global three-deck distinct counts for lengths three through eight against published benchmark values.

All computations use exact integers. The exhaustive finite loops are proof-relevant: they do not sample, infer by interpolation, or rely on error bars. The cut-invariance identity in `RESULT.md` gives an independent algebraic necessary condition for an equal-profile pair. The direct displayed witness can be checked by hand or by the same code.

Scientific limits: the exhaustive argument proves statements only through length eight and only for binary words; no larger-size conclusions are extrapolated. The prior-literature comparison is qualified by limited access to one specialized full text. Independent mathematical and historical-priority validation has not been performed.
