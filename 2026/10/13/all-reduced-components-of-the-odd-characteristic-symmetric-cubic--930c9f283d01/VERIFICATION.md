---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n>=3 over algebraically closed odd characteristic p, ∂_i e3=e2−x_i e1+x_i², so critical-point coordinates lie among two roots of a common quadratic. If a,b are distinct values with multiplicities m,r, subtracting gradients yields (m−1)a+(r−1)b=0, while a direct same-block derivative gives (m−1)a²+(r−1)b²=0. Since a≠b and 2 invertible, obtain (m−1)a=(r−1)b=0. A single nonzero value is allowed exactly at |S|≡1 (mod p), while two nonzero values force n≡2 (mod p) and both block sizes 1 mod p. The resulting unions of equal-coordinate lines or two-block planes are all of V(I), hence their linear-ideal intersections give radical via Nullstellensatz. Distinct equal-dimension subspaces cannot contain one another; number and projective degree equal support/bipartition counts. Hessian blocks have ranks n−1 on generic line points or n−2 on generic planes, establishing generic smoothness of critical scheme. Independent finite-field evaluation for p=3,n=3..6, p=5,n=3..5, p=7,n=3..4 checks critical-point membership/count only; the all-n,p theorem relies on the displayed algebra.

## originality

PASS

Best-of-knowledge original contribution is the explicit line radical and component decomposition for n≢2 (mod p), not the previously characterized extremal two-block planes. Checked same-object full primary source, general structural source, alternative zero-and-gradient formulation, and two Resultary searches; remaining historical equivalence risk is noted.

## value

PASS

A complete radical/minimal-prime decomposition in the previously unclassified one-dimensional regime is a natural structural invariant of a characteristic-dependent Jacobian ideal. It distinguishes the true critical scheme from hypersurface singularities in degree-dividing characteristic and provides component counts, projective degrees and generic smoothness, not a renaming of the known dimension result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
