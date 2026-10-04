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

The proof was checked directly from the displayed definition of the first-attempt norm.

1. Pairwise disjoint test segments have pairwise distinct endpoints, so the quadratic variation is at most twice the Hilbert energy. The vector supported by values \(1\) and \(-1\) on one edge attains the resulting upper constant \(\sqrt2\).
2. The recursive three-edge coloring is proper: the two outgoing colors at each nonroot node are precisely the colors different from its incoming edge. Hence every color class is a matching and is an admissible family of disjoint one-edge segments.
3. Expanding the full edge energy and applying \(2|ab|\le t|a|^2+t^{-1}|b|^2\) with \(t=1/\sqrt2\) gives coefficient \(3-2\sqrt2\) at every nonroot vertex and the larger coefficient \(2-\sqrt2\) at the root. Thus the lower comparison holds for every finitely supported vector, not merely for a finite-level truncation.
4. For a segment indicator, each nonzero variation has size one and consumes a distinct node of the support, giving the upper count \(|s|\). The branch-off one-edge segments give exactly \(|s|\) disjoint unit variations, proving equality.

No finite experiment is used as an infinite proof. Decimal constants in the accompanying report are evaluations of the closed forms only. The lower comparison constant is not claimed to be optimal, and no assertion is made about the final \(X_\alpha\) norm.
