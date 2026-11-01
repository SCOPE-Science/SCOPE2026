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

The proof uses an integral chain isomorphism of the pair consisting of the higher-independence complex and its contractible subcomplex of faces missing at least one hub. In relative chains, the oriented hub edge shifts the augmented leaf-skeleton complex by two degrees, with a sign under hub exchange. The augmentation-kernel exterior-power identification is over integers, not merely over rational coefficients.

Execute `python3 checker.py`. The self-contained checker uses adjacency-based component enumeration and independent signed Lefschetz summation, giving `PASS: 128 homology cases, 1050 signed-character cases, 27412 total faces enumerated`. The finite calculation is a diagnostic only. It does not independently establish the proof or test every parameter value.

Literature boundaries: the ordinary homotopy type and sphere count were already established in Deshpande–Singh (2020/2021), Theorem 3.10 and Corollary 3.13. The assertion evaluated here is restricted to the integral automorphism module and its character; it is not an equivariant homotopy equivalence. An independent audit has not been performed.
