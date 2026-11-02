---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The spherical hemisphere Gram operator decomposes by signed azimuthal order into a 2x2 block with diagonal 1/2 and cross term I_m=∫_0^1 S_(ell,m)S_(ell+d,m). The associated-Legendre Sturm–Liouville Wronskian identity reduces I_m to boundary products divided by d(2ell+d+1); double factorials determine top coefficient and signs. Order-raising recurrences give |I_(m+1)|/|I_m|=R_m^{±1}, R_m>1 increasing, and two-step R_(m+1)/R_m>1 on the top parity class; opposite-parity modes are dominated by next top-parity mode, so |m|=ell unique. The next distinct top coefficient and spectral theorem give sharp stability gap. The squared B ratio at successive ell reduces to an exact rational expression with sign determined by q_d(ell)=2d²+2dell+d-4ell²-12ell-9; it is positive through ell=d-2 and negative from d-1, giving the unique peak. ell=0 and ell=1 central-mode edge cases are explicitly treated. Independent direct associated-Legendre hemisphere quadratures for ell up to 13 and d=3,5,7,9, plus peak checks to ell=25, corroborated ratios and top eigenspace; finite checks are not the all-degree proof.

## originality

PASS

Previous arbitrary-degree-mask half-energy theorem classifies only the multiplicity of eigenvalue 1/2 by Cauchy rank, explicitly without nonzero singular values; that broader degree-mask result does not imply the sharp positive top and second eigenvalues or location of degree peak. Simons–Dahlen–Wieczorek and Michel–Plattner–Seibert provide general spherical Slepian concentration operators and polar-cap reductions, not this finite two-band odd-gap arithmetic classification. Adjacent-degree d=1 is prior and excluded. Best-of-knowledge PASS with classical Legendre-identity historical risk.

## value

PASS

Sparse two-band harmonic packets are natural spectral concentration problems; determining the optimal azimuthal order, exact spectral rigidity and a nonmonotonic interior lower-degree peak is a qualitative structural result over all odd nonconsecutive gaps, beyond a numerical coefficient or a trivial restriction of a general rank law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
