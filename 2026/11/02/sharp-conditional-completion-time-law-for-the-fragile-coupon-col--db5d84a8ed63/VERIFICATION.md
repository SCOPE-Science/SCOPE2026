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
# Verification record

The complete conditional-stage proof is in `RESULT.md` and the independently repeatable finite checks are in `verify.py`. Running `python verify.py` under Python 3 standard-library dependencies produced `verification_output.txt`, reporting 462 exact rational or numerically tolerance-controlled assertions. The direct state recursion enumerates seen-type subsets and independent unseen-type survival, and is therefore independent of the derived conditional-stage convolution. Numerical checks cover the asymptotic signed first-order coefficient for representative fixed survival parameters but do not replace the infinite-proof argument.

The main nonstandard step is verified mathematically by the product Radon–Nikodym density and a uniform integrable bound on its scaled error. The signed measures converge in `L1` on all independent part multiplicities, and contraction under the part-count map yields the claimed sharp total-variation constant. The proof does not claim a dimension-uniform or endpoint-uniform error rate. Independent audit has not been performed.
