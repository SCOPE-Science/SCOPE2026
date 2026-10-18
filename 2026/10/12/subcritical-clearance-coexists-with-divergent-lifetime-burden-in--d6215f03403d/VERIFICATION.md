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

From the six source Caputo equations and 0<=S/N<=1, incidence g<=beta(I+theta A). The nonnegative infected linear Volterra majorant uses D=diag(sigma+d,kappa+r_I+d,r_A+d) and C coupling E to I/A. Exact determinant det(zI-D^-1 C)=z(z²-R0), hence R0<1 yields positive (I-Q)^-1 and a constant supersolution. Nonnegative fractional scalar kernels k_(nu,a) of mass 1/a and homogeneous Mittag-Leffler h_(nu,a)->0 imply the bounded majorant has limsup L<=D^-1 C L, forcing L=0 and all infected coordinates to zero for any real orders (0,1). Stable T,R,S resolvents prove global convergence, boundedness, and disease-free Lyapunov stability. Any nonzero infected-path seed contributes a positive multiple of nonintegrable h(t)~ t^-nu/(a Gamma(1-nu)); Tonelli transfer along E->I,A->g->E and I->T with kappa>0 forces all five ordinary-time integrals infinite even though coordinates vanish. With all orders 1, Hurwitz Metzler linear upper bound gives integrability. Exact independently checked symbolic characteristic polynomial and rational R0=1/24 example.

## originality

PASS

Best-of-knowledge implication comparison of assigned exact claim against primary literature and semantic Resultary search. Compared same six-compartment model and next-generation R0, not title alone; equal-order global stability does not directly cover unequal-order model or imply infinite ordinary-time integrals. The prior source’s local/rational stability and a related single-order global theorem do not imply global attraction for all real unequal-order tuples; even attraction alone cannot imply integrability and indeed homogeneous scalar power tails violate it.

## value

PASS

The same six-compartment unequal-order fractional epidemic model has a natural gap between asymptotic eradication and cumulative lifetime burden, which standard reproduction-number stability does not quantify. Showing coexistence of global clearance with nonintegrable literal occupancy and treatment incidence across all five compartments for arbitrary incommensurate orders is a meaningful qualitative distinction important when interpreting idealized fractional memory models; no claim about physical count forecasts is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
