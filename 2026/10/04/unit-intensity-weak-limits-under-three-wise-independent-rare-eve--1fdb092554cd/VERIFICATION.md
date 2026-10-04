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

The proof was checked at the level of exact identities and limiting hypotheses.

For necessity, three-wise independence gives the exact first three factorial moments as sums over distinct indices. The rare-event assumption makes all repeated-index corrections vanish. The bounded third ordinary moment is explicitly derived from \(S^3=(S)_3+3(S)_2+S\), so passage of the first two moments uses uniform integrability rather than weak convergence alone. The third-factorial conclusion is only the lower-semicontinuity inequality \(\mathbb E(Y)_3\le1\), which is the strongest justified statement.

For finite-target sufficiency, substituting the displayed \(\delta_{0,n},\delta_{1,n},\delta_{2,n},\varepsilon_n\) verifies exactly: total mass change \(0\), mean change \(0\), second-factorial change \(-1/n\), and third-factorial change \(a_{3,n}-c\). The perturbations at \(0,1,2\) are \(O(n^{-1})\), while the added mass at \(n\) is \(O(n^{-3})\), so fixed positive base masses remain nonnegative for large \(n\).

For the exchangeable row, conditional uniform sampling of a \(K_n\)-subset gives joint all-one probability \(\mathbb E(K_n)_r/(n)_r=1/n^r\) for \(r=1,2,3\). Bernoulli inclusion-exclusion converts these identities into the full product law for every subfamily of size at most three.

For the general-target reduction, the reference law on \(\{0,1,2,3\}\) was checked to have first factorial moment \(1\), second factorial moment \(1\), and third factorial moment \(1/2\). Tail restoration at \(0,1,2\) exactly replaces deleted mass, mean, and second factorial moment while adding no third factorial moment. Finite third moment follows from the three stated target constraints.

No numerical experiment, finite enumeration, or external certification is used to establish the infinite theorem. The unproved limits are the possible extension to intensities other than \(1\), higher orders of limited independence, point-process limits, and any claim of absolute bibliographic uniqueness.
