---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For \(g_n=x^{n+1}+x^ny+y^nz+z^n\), the projective Jacobian forces the unique singular point and multiplicity \(n=d-1\). Factoring \(g_x=x^{n-1}L\) and using additivity of local intersection multiplicity gives \(\mu=(n-1)(n^2+1)\). The affine Euler relation puts \(z^n\) in the Tjurina ideal; the displayed six-element lexicographic Gröbner basis has initial ideal \((x^n,x^{n-1}y,x^{n-1}z^{n-1},xy^{n-1}z,y^n,z^n)\), whose standard monomials number \((n-1)(n^2-n+3)\). Hence \(\mu-\tau=(n-1)(n-2)\), and Saito’s isolated-hypersurface criterion gives the stated quasihomogeneity boundary. A fresh exact rational Buchberger replay checked all S-polynomial reductions and the count for multiple values through n=25; it corroborates, rather than replaces, the symbolic proof.

## originality

PASS

The exact same extremal family was inspected in the Fassarella–Medeiros source. That source identifies the polynomial, its unique singular point and the sharp inverse-degree role, but does not state the local Milnor/Tjurina formulas or the quasihomogeneity transition in the material read. Exact-family web searches and Resultary did not locate an equivalent local-invariant profile. Thus the result is not merely rebranding the known extremal Cremona construction.

## value

PASS

The family is mathematically distinguished as the sharp inverse-degree monomial Cremona family. Its exact Milnor–Tjurina profile gives natural deformation-theoretic invariants of the unique singularity and reveals a qualitative transition: only the cubic singular member has \(\mu=\tau\), while the defect then grows exactly as \((d-2)(d-3)\). This is a motivated infinite-family invariant, not an arbitrary slice or a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
