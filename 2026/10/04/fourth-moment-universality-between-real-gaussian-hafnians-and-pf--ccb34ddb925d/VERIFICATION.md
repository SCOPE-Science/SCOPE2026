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

The claim was checked from the defining perfect-matching expansion. Conditioning on one vertex gives an exact centered Gaussian and reduces the fourth moment to the square of its conditional variance. For two distinct cofactors, deleting the two corresponding vertices and conditioning on the common odd vertex set gives two independent centered Gaussians with a shared variance. Introducing one fresh vertex identifies the second moment of that shared variance with exactly one third of the preceding-order fourth moment. This proves the recurrence
\[
M_n=(2n-1)(2n+1)M_{n-1},
\qquad M_1=3,
\]
and therefore the stated closed form. The parallel second-moment recurrence gives \(\mathbb E H_n^2=(2n-1)!!\).

Boundary checks are exact: \(n=1\) is one standard Gaussian entry and has kurtosis \(3\); \(n=2\) gives kurtosis \(5\), consistent with the known sign-flip equivalence between the order-two hafnian and Pfaffian. These checks are sanity checks only; the proof covers every \(n\ge1\).

The claim does not depend on numerical enumeration, symbolic fitting, an asymptotic approximation, or a finite computation. The literature comparison was limited to statements that can imply the theorem: the same real symmetric model and its Pfaffian benchmark, the exact complex Gram fourth-moment result, and the antisymmetric Gaussian product reduction. The remaining literature risk is stated in the review.
