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

PASS: Checked the operator acts on monomial z^beta w^b as rho^b (N+b)/(N+b+k) z^beta w^(b+k), with N=|beta|; normalized target monomials are distinct, so the singular values are exactly their weight ratios (rather than merely comparable). Reconstructed the Fubini/Beta monomial squared norm pi^n beta!/(b+1) Gamma(1+(b+1)/m)/Gamma(N+n+(b+1)/m). Fixed-b gamma quotient yields sigma_{N,b}~rho^b A_b N^{-k/(2m)} and multiplicity binom(N+n-2,n-2), giving p*=2m(n-1)/k and coefficient (n-1)!^{-1}sum_b rho^{b p*}A_b^{p*}. The uniform gamma ratio bound C rho^b(1+b)^a(1+N)^(-a) ensures a summable degree-by-degree counting envelope for every fixed rho<1; rho=0 leaves b=0 only. A_b^{p*}~m^{-(n-1)}b^{n-1}, and standard Abelian series asymptotics give (1-rho)^n L ->m^{-(n-1)}p*^{-n}; this order of limits is essential. At rho=1, fixed N and b->infty makes singular weight tend to 1 on orthogonal columns, giving essential norm=norm=1; rho<1 compact, converges strongly but distance always 1. Independent numerical checks recomputed 16 exact gamma/singular-value specializations (n=m=k=2, b=0,1,3,9 and N=1,5,30,100), and the closed constant L=1/[2(1-rho²)^2] at rho=0,.2,.5,.8; all agree to floating precision. These finite numerical checks corroborate but do not prove the Weyl law.

## originality

PASS

The searched primary statements were compared for mathematical implication, with prior scalar/global ingredients explicitly credited. A best-of-knowledge PASS attaches only to the incremental claim and retains genuine residual risks, not to any global proof of historical priority.

## value

PASS

PASS: The partially collapsed self-map retains full boundary tangency in the z directions, so relatively compact composition-range exponential spectral estimates do not apply; its exact gamma-series Weyl coefficient yields information substantially sharper than Schatten-membership thresholds. The precise nth-order blowup as transverse contraction vanishes quantifies a natural compact-to-noncompact transition, with a closed checkable type-four dimension-two benchmark and a logarithmic critical singular-value residue. These are analytically motivated spectral invariants, not parameter relabeling or a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
