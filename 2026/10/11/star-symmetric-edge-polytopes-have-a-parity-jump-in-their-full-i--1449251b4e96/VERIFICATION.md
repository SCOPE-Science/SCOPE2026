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
The complete symbolic proof for every integer \(m\ge1\) appears in `RESULT.md`.

The reconstruction is determined by the following explicit checks:

- For each \(\varepsilon\in\{\pm1\}^m\), the unique facet normal in the zero-sum hyperplane is
  \[
  f^\varepsilon=\left(S/(m+1),S/(m+1)-\varepsilon_1,\ldots,S/(m+1)-\varepsilon_m\right),
  \quad S=\sum_i\varepsilon_i.
  \]
- Every norm satisfies the exact identity
  \[
  \|f^\varepsilon\|^2=m-\frac{S^2}{m+1}.
  \]
- The parity-constrained smallest \(|S|\) is \(0\) for even \(m\), and \(1\) for odd \(m\). Opposite facets certify the maximal inscribed radius.
- The span of maximum-length normals has rank \(m-1\) or \(m\), respectively. For even \(m\), all centers at maximal radius are forced to have the form \((-mu,u,\ldots,u)\).
- The exact remaining center constraints are
  \[
  |Su|\le1-\sqrt{1-S^2/(m(m+1))}.
  \]
  Their threshold ratio is strictly increasing for positive admissible \(S\), so \(|S|=2\) alone fixes the nontrivial endpoints.
- Each antipodal vertex pair gives squared-distance average \(2+\|c\|^2\), proving the unique enclosing sphere.

The embedded `verify.py` independently enumerates all facets for \(1\le m\le11\), checks the normal formulas and sign-vector counts, solves the complete inradius linear program, verifies the extreme attainable centers and their contact counts, and solves auxiliary linear programs for the full optimal-center range. The script reports only finite corroboration, not an infinite computational certification.
