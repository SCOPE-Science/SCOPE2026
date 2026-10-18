---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: The local singular chart is the d-Veronese cone R_d=C[x,y]^(μ_d)=⊕ Sym^{dj}C², with rational normal curve Hankel quadratic presentation on z_0..z_d. For the Fitt₂ ideal every (d−1)-minor of the linear-relation Jacobian has degree >=d−1, so it lies in m^{d−1}. The d−1 genuine quadratic relations f_i=z0*z_{i+2}−z1*z_{i+1} have lower triangular Jacobian in z2..zd with determinant z0^{d−1}. GL2 action preserves the intrinsic ideal; polarization of (ax+by)^{d(d−1)} spans the entire degree-(d−1) Veronese component in char 0. Thus equality and, by direct-product Ω and Fitting-sum identities, gluing along smooth base gives I_Σ^{d−1}. Independently reconstructed symbolic Jacobian minors and Hilbert-length sums for d=3..8 using SymPy; finite checks supplement, not replace, the characteristic-zero general proof. Positive-dimensional base and non-torsion L are retained from claim; no positive-characteristic assertion.

## originality

PASS

PASS (best of knowledge): Satriano–Shen 2026 establishes the same projective quotient family is K_m-regular and non-LCI, and identifies weighted-projective fiber singularities, but its accessible abstract does not provide the intrinsic Fitting-scheme ideal or transverse multiplicity. Conca et al 2017 address Hankel determinantal ring singularities without an accessible exact power-of-maximal-ideal statement. The explicit unbounded thickness and Hilbert function are not known to be covered by a located primary result; classical toric/Veronese Jacobian algebra may contain implicit equivalent identities, an explicit originality risk.

## value

PASS

PASS: Explicit intrinsic singular subscheme thickness grows ~d³/2 in a natural projective, everywhere-K-regular finite-quotient family, distinguishing reduced smooth singular locus from arbitrarily thick canonical Jacobian detection. This natural scheme invariant has structural significance beyond merely listing small d values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
