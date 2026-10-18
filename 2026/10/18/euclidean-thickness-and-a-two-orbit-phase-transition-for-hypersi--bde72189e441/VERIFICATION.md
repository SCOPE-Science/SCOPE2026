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

# Verification of the Euclidean hypersimplex-width classification

The independent geometric cross-check enumerates vertices of \(\Delta_{n,k}\), enumerates all of their pairwise differences, computes an orthonormal basis of the zero-sum hyperplane, and uses convex-hull facet equations to obtain the least centered support-plane distance. This method does not reuse the analytical norm-maximization argument. All eight rank/dimension pairs with \(3\le n\le6\) and \(1\le k\le\lfloor n/2\rfloor\) agreed with the theorem to better than \(4\times10^{-9}\) in squared width.

An independent random-direction check evaluated the exact sum of the largest and smallest \(k\) normal coordinates for 3,250 zero-sum unit normals across 13 rank/dimension cases, including both sides of the first nontrivial tie, and compared them with the asserted lower bound. No violations occurred. In addition, 2,449 exact-rational pairs of integers checked the equivalence between equality of both squared candidates and the formula \(n=4m^2-1\).

**Reproduction:** run `python verify_width.py` with NumPy and SciPy available. The program prints the counts and exits unsuccessfully on any failed assertion. Inputs are deterministic. Its location and dependencies are contained in the present package.

**Non-computational proof obligations:** the reverse inclusion in the difference-body formula, the support-function/inball identity, both maximizing-norm equality cases, and the even-parameter Diophantine exclusion were checked algebraically in the accompanying proof. Finite trials do not establish the all-dimensional claim, nor do they establish originality.

**Scientific limits:** Euclidean widths use the canonical intrinsic coordinate metric. The study does not treat arbitrary affine copies or general matroid base polytopes. No independent mathematical audit or certification has been performed.
