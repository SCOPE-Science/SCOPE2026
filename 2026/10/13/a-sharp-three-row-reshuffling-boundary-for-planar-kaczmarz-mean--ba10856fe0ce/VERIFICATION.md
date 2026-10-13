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

## Exact algebra and reproducibility

For the unit normals \(a_1=a_2=(1,0)\) and \(a_3=(c,s)\), the proof uses \(PQP=c^2P\) and \(QPQ=c^2Q\). The two Gram matrices after one three-update epoch are derived symbolically by three reshuffling words and a repeated independent-draw Gram channel, respectively. Their exact difference is \((1-c^2)[(8+5c^2)P+(1-2c^2)Q]/27\), and its determinant establishes the sharp sign boundary. No numerical approximation is used to prove the all-angle statement.

Execute `python verify.py` in the directory containing this package. The self-contained script uses `fractions.Fraction`, enumerates the six labeled orderings and 27 independent triples, tests five rational unit directions, and asserts the rational example with risks \(48/625\) and \(1179/15625\). It additionally checks an exact rational three-distinct-row reversal and the two-row formula. A successful replay prints `VERIFY_OK`. These finite checks independently corroborate, but do not replace, the algebraic proof for all real angles.

The claims exclude an arbitrary-row universal sampler ranking, multiepoch rates, and comparisons of mean iterates or spectral operator norms. Independent external audit has not been performed.
