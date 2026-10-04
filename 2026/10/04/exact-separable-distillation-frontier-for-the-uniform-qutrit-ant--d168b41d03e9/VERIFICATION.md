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

The universal claim is proved analytically in `RESULT.md`; no finite experiment is used as an infinite proof. The following checks were completed.

1. Every nonzero success product Kraus branch has local rank two and a common one-dimensional kernel, leaving exactly one contributing antisymmetric direction.
2. On that support, the coefficient-matrix identity and Schatten Hölder give \(\operatorname{Tr}(XY)\ge2\sin(2\theta)|\alpha|^2\).
3. The swap is block-positive on product vectors, so its pairing with the separable failure effect is nonnegative and yields the global converse.
4. The six displayed product Kraus operators attain the target. Their total effect has coefficient \(2p\sin(2\theta)\) on \(|ii\rangle\) and \(p\) on \(|ij\rangle\) for \(i\ne j\); at the claimed \(p\), all coefficients are at most one, so the remaining diagonal effect is separable.
5. The boundary values \(\theta=\pi/4\) and \(\sin(2\theta)=1/2\) agree from both formula branches. The proof excludes \(\theta=0\), where the target ceases to have Schmidt rank two.

The scientific limitation is essential: the converse uses separability of the failure effect and therefore does not automatically apply to an isolated success map with an unrestricted completion.
