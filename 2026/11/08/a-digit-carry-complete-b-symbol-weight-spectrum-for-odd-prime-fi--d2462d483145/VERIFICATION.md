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

# Verification and reproducibility

The proof is in `RESULT.md`. Run the standalone standard-library script with `python verify_prime_rm.py`. It independently computes the product-form enumerator and independently enumerates all affine functions and cyclic zero windows.

Observed result during review: `PASS: 117 complete enumerator comparisons`. It exhausts every allowable window length for \((p,m)\in\{(3,1),(3,2),(3,3),(5,1),(5,2)\}\), checks additional odd-prime configurations at \((5,3)\) and \((7,2)\), and includes small binary consistency checks only as benchmarks. Every tested predicted enumerator also has the expected number of codewords for the fully enumerated configurations. Examples: \(W_{3,3,2}=1+6z^{19}+6z^{20}+12z^{21}+6z^{24}+12z^{25}+12z^{26}+26z^{27}\); \(W_{5,2,2}=1+20z^{21}+20z^{24}+84z^{25}\).

The key general proof requirements are: (i) zero intervals have length \(Q\) before block-boundary joins; (ii) no two joins share a zero interval; (iii) the affine constant is a block-index translation when a higher coefficient is nonzero; (iv) digit carry transitions are exactly counted, including wraparound; (v) the prefix-sum map on coefficients is bijective. These steps are mathematically proved in `RESULT.md`, not inferred from output logs. This file does not constitute independent audit or formal proof certification.
