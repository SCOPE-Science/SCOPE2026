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
# Verification and limits

The complete proof is analytic and works in infinite dimensions over both scalar fields; no numerical enumeration or executable certificate is needed for correctness. The following steps were reconstructed directly from the definitions:

1. \(a_n=\varphi(e_n)\) is absolutely summable for every \(\varphi\in\ell_\infty^*\); finite-coordinate modifications leave the singular functional invariant and prove \(\|\varphi\|=\|a\|_1+\|\varphi_s\|\).
2. \(J^{**}\varphi=(a_n)\) follows from the canonical dual basis; its norm is the supremum absolute coordinate.
3. The upper hull bound is preserved by norm-closed convexification. The lower hull bound holds by convexifying explicit unit near-attainers \(\varphi_s+(1-\|\varphi_s\|)\theta e_n\); singular mass exactly \(\delta\) is treated by norm approximation.
4. Contractivity of the singular projection gives the distance lower bound; scaling the singular component gives the identical upper bound.
5. Hahn–Banach applied to the norm-one class of the constant sequence in \(\ell_\infty/c_0\) supplies a nonzero norm-one singular functional. Its positive-radius multiples lie outside the near-attainment hull for suitable \(\delta\).

The statement relies on **norm** closure; a change to weak-star closure changes the question. The positive-radius failure has not been claimed for every generating operator, and no independent audit or external proof certification has occurred.
