---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The killed diffusion with Poisson resetting and linear mean-growth generator is a rank-one positive perturbation of Dirichlet diffusion. Positive resolvent eigenvalue equation 1=r E[F_{lambda+r-g}^{(L)}(LZ)] has a unique principal solution, and the lambda=0 branch has a unique L_c by scaling of Brownian exit time. For s=r-g positive, killed resolvent F_s(Lz)=(1-cosh(Lz sqrt(s/D))/cosh(Lsqrt(s/D)))/s is strictly concave in w=z^2; for s negative and L below the first Dirichlet pole it is strictly convex; at s=0 it is affine L^2(1-w)/(2D). Jensen and endpoint chord inequalities at fixed Ew=sigma^2 therefore identify unique shell W=sigma^2 and unique center/edge W in {0,c^2}, with EZ=0 forcing their symmetric masses. The ordering of the resolvent reverses at r=g and the ordering of L_c reverses accordingly. At r=g every admissible law has L_c=sqrt(2D/[g(1-sigma^2)]). Independently numerically solved the three continuous Dirichlet-resolvent roots at r/g=.3,1,3 and checked strict reversal and resonance. The proof is for principal mean growth, not almost-sure nonextinction.

## originality

PASS

Menon–de Castro–Anteneodo directly studies critical habitat sizes and resetting but to a fixed resetting position; its distributed-reset extension is not the quantified all-law second-moment comparison. Méndez–Flaquer-Galmés–Campos and Julián-Salgado–Dagdug–Boyer give distributional resetting and first-passage/rate optimization in different unbounded geometry. Their renewal tools may derive a resolvent but do not in inspected passages imply both sharp variance-constrained extremizers and their growth-rate reversal. Exact comparison with a more general convex-order theorem is a plausible priority risk rather than a demonstrated covering source.

## value

PASS

Sharp minimax design over all atomic, nonsymmetric and mixed reset laws with fixed variance and bounded fractional habitat support is a natural, motivated constrained optimization. The jump from center-plus-edge law to two-site shell at r=g, strict uniqueness off resonance and law independence at resonance give a complete structural result for a mean-growth habitat threshold rather than a two-case numerical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
