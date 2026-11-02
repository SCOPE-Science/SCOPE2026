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

# Reproducibility and proof boundaries

`check.py` is standalone Python 3 code. Run `python check.py` from a folder containing the extracted file. It exhaustively compares brute-force enumeration, the full \(b\)-state transfer product, and the two-state overlap-code formula for all \((b,n)=(3,3),(3,4),(4,3)\), totaling 1,066 schedules. It checks 64 finite code-signature cases over four alphabet sizes and four strict period-two spectral orderings.

The proof of the universal prefix-count formula is the rank-two factorization in `RESULT.md`. The injectivity of the complete binary code follows from its strictly positive update coordinate, not from experiments. The periodic growth exponent follows from the Perron root of a primitive transfer product; equality with geometric Hausdorff and packing dimensions invokes the published homogeneous moving-hole dimension theorem. No finite computation substitutes for an all-length or infinite-asymptotic proof.

The result has not received independent mathematical review or historical-priority certification. The publicly accessible texts most relevant to the claim are Kong–Sun–Wang arXiv:2505.02336v2 (Section 2 and Theorems 1.1/1.8), Kong–Li–Ma–Simon arXiv:2610.31128v1 (Introduction and Theorem 1.1), and Cheriyath–Agarwal arXiv:1905.11767v5 (Introduction and Sections 2–3).
