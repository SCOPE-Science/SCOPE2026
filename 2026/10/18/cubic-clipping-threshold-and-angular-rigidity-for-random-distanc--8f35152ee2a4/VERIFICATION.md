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

# Verification of the geometric formulas

The proof consists of four exact mathematical identities or comparisons: an affine-product covariogram for \(K\), Gaussian integration of its pairwise absolute-linear term, a monotone integral representation of \((f(t)-1)/t^2\), and disjoint local spherical-cap asymptotics at the smallest face altitude. Each works for **every** invertible \(3\times3\) matrix, including tied minimum face separations. The cap coefficient is strictly positive because all unaffected factors at active cap tips remain positive.

Run `python3 checker.py` in the directory containing `RESULT.md` and `checker.py`. The standard-library checker constructs four independent full-rank dual-normal matrices: a cube and three skew examples. For each, it reconstructs the cutoff, fifth coefficient and stability inequality, integrates spherical moments numerically and compares the small-cap clipped excess to the exact leading coefficient. The unit-cube control has fifth coefficient \(8/5\), sixth coefficient \(1/6\), and threshold-amplitude \(2\pi\). The checked terminal marker is `PROFILE_AND_CUBIC_ONSET_CHECK_OK 4 profiles`.

Numerical integration and four configurations do **not** prove the general theorem; the proof in `RESULT.md` does. No claim of external certification or independent scientific review is made. Older unindexed exact formulas may affect scientific priority. The global distance law beyond the first cutoff, and an elementary evaluation of its sixth coefficient for all skew shapes, remain outside scope.
