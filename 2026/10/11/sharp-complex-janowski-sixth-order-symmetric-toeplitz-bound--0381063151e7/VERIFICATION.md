---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For real -1<=B<A<=1, odd normalization and a complex Schwarz subordination reduce to an even Schwarz function v(z²), since the Janowski Möbius map is injective. Parity splits T6 into two identical symmetric 3x3 blocks, giving D=(1-a5)(1+a5-2a3²) and T6=D². Write d=A-B, R=|u|², t=u², v2=(1-R)eta: a3=d u/2, a5=k t+ell(1-R)eta, k=d(A-3B)/8, m=d(3A-B)/8, ell=d/4. Expanding D gives 1-St+Kt²+ell(m-k)t(1-R)eta-ell²(1-R)²eta², S=d²/2, K=km. Independently factored the symbolic identity. Angular derivative of |1-St+Kt²|² in cos(arg t) is negative on [-1,1] using K>=-S/8 and S<=2, hence unique t=-R for R>0. The quantitative radial bound P(-1)-|D|>=(1-R)3d²/16 forces R=1. Then v(zeta)=u zeta, u=+i or -i, yielding unique f± and squared bound ((8+d(A-3B))(8+d(3A-B))/64)^2; at (1,-1) it is 16. Equality, nondegeneracy d>0, endpoints B=0 and B=-1, and symmetric-not-Hermitian normalization are all checked. The package script confirms identities/finite meshes only; the arbitrary-parameter proof is the strict analytic angular/radial inequality.

## originality

PASS

The self-contained global complex Janowski sharp law is not covered by the inspected September 2026 full primary article, which explicitly leaves this class open. Real bounds and parity factorization are credited to that article; originality is restricted to complex optimization, strict radial equality, and parameter-dependent maxima.

## value

PASS

The parameter-uniform exact extremal constant with a full equality classification resolves a natural open problem in a recently published Toeplitz-class classification. It demonstrates a global real-versus-complex discontinuity for the SAME Janowski parameters, from real maximum 1 to >1 for every d>0, reaching 16 at a natural starlike endpoint. This is not merely symbolic expansion of a known bound; the strict two-complex-variable Schur optimization supplies the missing result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
