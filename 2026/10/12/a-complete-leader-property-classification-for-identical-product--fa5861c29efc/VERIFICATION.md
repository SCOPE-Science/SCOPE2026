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

The proof is analytic and does not depend on numerical enumeration.

1. For one coordinate and a fixed sample index, conditioning on its observed value gives exactly \(u_n=\mathbb E[F(X)^{n-1}]\), which includes all ties.
2. If \(t=\Pr\{X>b\}\), then on \(X\le b\) one has \(F(X)\le1-t\), hence \(u_n\le(1-t)^{n-1}+t\).
3. With \(n=\lceil\log(1/t)/t\rceil+1\), the elementary inequality \(1-t\le e^{-t}\) gives \(u_n\le2t\).
4. Coordinate independence is used only for one fixed candidate leader index, giving probability \(u_n^d\). The subsequent bound \(a_n\le n u_n^d\) is a union bound and requires no independence between candidate indices.
5. The limit \(t^{d-1}\log(1/t)\to0\) for \(d\ge2\) proves the no-terminal-atom branch along the selected subsequence.
6. If the finite essential supremum carries mass \(p>0\), the probability that at least one sampled vector equals the all-top vector is \(1-(1-p^d)^n\to1\), proving the other branch.

The argument establishes only zero liminf when there is no terminal atom; it intentionally does not assert full-sequence convergence. Literature-search uncertainty is recorded separately in `AUDIT.json` and is not used as a correctness premise.
