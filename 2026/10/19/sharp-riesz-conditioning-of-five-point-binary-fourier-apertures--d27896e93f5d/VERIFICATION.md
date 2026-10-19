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

Run `python3 checker.py` in the directory containing this document and `checker.py`. It uses the Python standard library only and exact integer arithmetic. `CHECK_PASS` indicates completion of every asserted finite certificate.

The checker examines all \(\binom{16}{4}=1820\) unordered four-column subsets of the binary four-cube. It calculates each \(4\times4\) determinant both by the fraction-free Bareiss algorithm and independently by its explicit \(24\)-term permutation expansion. It confirms the magnitude distribution \(0:880\), \(1:835\), \(2:100\), and \(3:5\), together with all five maximal column sets and their realization as rooted translates of the dual simplex.

The same package separately enumerates all \(\binom{16}{5}=4368\) frequency choices for each canonical five-point affine support type. The independent type has determinant magnitudes \(0:1360\), \(16:2672\), \(32:320\), \(48:16\). The affine-dependent type has \(0:3344\), \(32:1024\). These are reproducibility checks and small-dimension consistency tests, not an extrapolation to arbitrary dimension.

The analytic steps requiring mathematical inspection are the logarithm/variance inequality, the use of complementary minors for the order-eight Walsh matrix, the row-and-column normalization that gives a binary four-minor, and the counting of quotient lifts. The full proof and its bounds are in `RESULT.md`. No independent mathematical validation has been performed.
