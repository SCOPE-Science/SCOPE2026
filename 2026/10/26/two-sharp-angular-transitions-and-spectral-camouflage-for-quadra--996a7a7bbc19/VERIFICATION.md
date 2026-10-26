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

Run `python check.py` with Python 3, NumPy, SymPy, and mpmath installed. In the accompanying execution, it returned the exact content of `check_output.txt` (3,302 successful assertions). The checker is independent of any earlier stored result and works directly from the formulas written in `RESULT.md`.

The rational tests cover five even dimensions and many unions of two rational radial intervals. An independent direct six-by-six polynomial Gram calculation covers three disk masks, the disk camouflage moments use exact square-root algebra, and high-precision roots check the distinct transitions and their quadratic corrections in six dimensions. These checks do not, by themselves, prove the all-dimensional or all-mask theorem. The analytical invariant-sector decomposition, diagonal comparison identity, conditional-mean monotonicity, and exact moment identities in `RESULT.md` supply that proof.

Scientific limitations: the mask must be radial and the polynomial degree at most two; threshold expansions fix dimension and send squared-radius half-width to zero. Originality is best-knowledge only and requires independent priority verification. No external independent audit or validation is asserted.
