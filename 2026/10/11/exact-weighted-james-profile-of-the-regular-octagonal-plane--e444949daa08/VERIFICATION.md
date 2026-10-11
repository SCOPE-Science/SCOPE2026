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

The proof uses one published general inequality, the published premise \(J(X_8)=\sqrt2\), and an explicit sharp pair. The analytic lower bound is exact over \(\mathbb Q(\sqrt2)\): for \(0<\lambda\le1/2\), both weighted vectors have norm \(1-(2-\sqrt2)\lambda\), with the only sign split at \(\lambda=1-1/\sqrt2\). Parameter symmetry gives \(1/2\le\lambda<1\).

Run `python verify.py` in an environment satisfying `requirements.txt`. The script symbolically checks the coordinate identities, both facet inequalities on their exact parameter intervals, the symmetry-compatible affine target, and the strict Hilbert-profile separation. A successful replay prints `VERIFY_OK`.

The checker is a replay of finite algebraic identities, not a numerical search and not a substitute for the proof of the infinite supremum. The upper bound depends on the cited Theorem 5.2 and on the cited classical James value.
