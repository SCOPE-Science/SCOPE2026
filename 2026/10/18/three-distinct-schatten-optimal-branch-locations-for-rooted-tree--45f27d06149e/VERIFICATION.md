---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The checked kernel of TT* is the length of the common rooted-path prefix. Direct diagonal and squared-kernel integrals give ||T||_S2²=L²[m-(m-1)t²]/2 and the displayed fourth moment with derivative 2(m-1)t[(6m-1)t²-9mt+3m]/3. Independent SymPy manipulation recovered both identities and the unique S4 interior root, checked at m=2,3,4,8,13. For the infinite-dimensional operator norm, identify T as inverse of rooted Sobolev differentiation: radial Dirichlet–Neumann–Kirchhoff eigenvalue root F(k,a)=((m+1)cos(kL)-(m-1)cos(k(2a-L)))/2 has strictly negative k-derivative over (0,π/(2L)] and at fixed k is uniquely smallest at t=1/2; transverse first eigenvalue is no smaller. This yields the unique 1/2 operator-norm optimizer with value L/[2 arctan(m^-1/2)]. Endpoint collapsed edges and m>=2 verified; numerical Nyström checks are only corroboration, not an infinite proof.

## originality

PASS

The same path-integration operator and the same fixed m,L broom family must be compared across three different Schatten norms, not merely tree spectral estimation. The relevant tree Hardy approximation-number and metric-tree eigenvalue papers supply bounds/decomposition tools; inspected materials do not assert the exact three distinct optimizer locations. Resultary searches returned related Volterra rearrangement for rank-one-corrected weighted integration, not this m-branch topology optimization; novelty is best-of-knowledge, not historical certainty.

## value

PASS

A canonical rooted Hardy operator on the simplest nontrivial metric tree has three provably incompatible optimal branch positions under standard S2,S4,S_infinity objectives; the transition is concrete and mathematically motivated rather than an arbitrary tree slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
