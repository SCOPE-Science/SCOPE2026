---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

With u_j=m_j+b_j xi, W=diag(1,1/3) is exactly the physical norm and the Fourier generator is [[z-1,z-1],[3(1-z),-3(1+z)]]. The SSPRK3 polynomial R=I+nu L+nu²L²/2+nu³L³/6 gives D=W-R*WR. The source proves exact rational identities D11=2nu(1-c)Q and det D=-(4/9)nu^4(1-c)^2 F(nu,c), with F affine in c, one edge factor containing p(nu)=18nu^4-9nu^3+3nu²+5nu-1 and the other negative up to 1/5. All 18 tensor Bernstein coefficients of Q on [0,1/5]x[0,2] are strictly positive; verified rational certificate source VERIFY.py establishes identities by 13x13 degree-bounded interpolation, and independent recalculation matched determinant at several rational values. p strictly increases and has unique positive zero 0.18645728037; constant Fourier mode is nonexpansive below threshold. Above it, near-zero nonzero Fourier angles have det D<0, and dense roots of unity give some real finite-grid input with strict one-step energy growth. No assertion of instability on each fixed grid nor nonlinear entropy.

## originality

PASS

Best-of-knowledge originality of the precisely scoped sharp theorem survives comparisons to primary antecedents; generic tools, original model/method and known broad phenomena are explicitly credited. Detailed four implications below distinguish genuinely new claimed conclusions from prior theory; remaining literature-access/priority risk is material but not in itself a known covering theorem.

## value

PASS

An exact necessary-and-sufficient physical L² CFL threshold for a canonical P1 upwind RKDG scheme is a natural missing stability parameter, stronger and operationally different from an unspecified sufficiently small CFL. The algebraic root, determinant onset at long waves, and finite reproducible certificate are genuinely useful for selecting safe steps and studying nonnormality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
