---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed exact block diagonalization f=(p+x,p-x,q+y,q-y), z=p-q with z_dot=-2z and (x,y)_dot=-[[2w+1,1],[1,3]](x,y). The Lipschitz unit ball is |x|,|y|<=1/2 and |z|+|x+y|<=1, whose extreme edge amplifications are max{alpha+(1+|w-1|)beta, e^-2t+|w-1|beta}. The killed-chain row sums are <=1. Spectral comparison alpha+beta>=e^-2t for w<=1 and <= for w>=1 produces the stated exact branches. Right derivative -min(2w,3-w) at 0 and semigroup submultiplicativity give best exponential exponent; w<=3 gives nonexpansion by beta<=t e^-2t and w>3 has positive short-time slope. The sharp global envelope 3/2 is unattained at finite w,t but attained in limit w->infinity, t=w^-1/2. Independent fresh 4x4 heat matrix and integral graph-Lipschitz polytope enumeration verified 50 w,t pairs, including thresholds; universal conclusions rest on analytic proof, not those finite cases.

## originality

PASS

Qualified PASS: Ollivier/Kantorovich duality and Veysseire W1 curvature contraction are general principles, not exact weighted one-edge C4 heat norms. Lin-Lu-Yau compute unweighted degree-normalized C4 curvature, not this generator. Resultary matches to four-state ell4 cyclic convolution norms or variable edge-metric numerical index concern different operators or quantities. No located theorem supplies the two-branch w,t norm and nonattained 3/2 envelope; unindexed transport computations remain a risk.

## value

PASS

PASS: Single-edge jump-rate perturbation of the smallest square is a natural nonhomogeneous diffusion model. Exact contractivity breakdown w=3, sharp exponential rates and noncommuting fast-rate/short-time 3/2 amplification identify genuine transport stability boundaries beyond broad curvature bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
