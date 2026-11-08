---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each theta in (1,2), the displayed branches are full onto and strictly expanding, and the paper source Proposition 4.1 supplies a W2,1 contraction with essential factor (1+theta/2)^(-2)<1. Convex combining yields uniform Doeblin Fortet bounds; compact W2,1→W1,1/L1 and L1 contraction yield uniform essential spectral radius <1. Every p has a strictly positive-probability full-branch component whose expanding inverse cylinders shrink, so positive eigenfunction modulus and equality in the positive triangle inequality force any peripheral phase to be constant; fixed modulus strictly positive inside via topological exactness. This proves eigenvalue1 simple and alone on unit circle; L1 contraction precludes Jordan chains. Norm-continuity and compact p then yield a uniform spectral gap and real-analytic normalized Riesz eigenprojection across [0,1]. Independent symbolic expansion of inverse weight yielded 2w(z)=a z-(3/4)a r z²+(5/8)a r² z³+..., and A C-B²=p(1-p)a0a1(r1-r0)² gives the stated Peano jet inversion and discriminant. The finite source verification only checks algebra, not operator spectra. Endpoint is Peano C1 data, not a claimed C3 density.

## originality

PASS

Best-of-knowledge PASS for all-mixture p globality. The exact source primary already proved per-map W2,1 Lasota Yorke, exactness and sufficiently-small-p analytic response, including local jet, but not a full interval uniform spectral gap. Extra positivity plus compactness closes the gap. General PF/quasicompact random-map results may encompass this as a corollary, but no checked theorem directly covers these critical cusp maps for all mixture weights.

## value

PASS

The distinction between local perturbative analytic response and uniform mixing for every bias is a substantive dynamical-systems question; it supplies global identifiability of the mixture parameter via endpoint jets and robust control of mixing beyond infinitesimal perturbation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
