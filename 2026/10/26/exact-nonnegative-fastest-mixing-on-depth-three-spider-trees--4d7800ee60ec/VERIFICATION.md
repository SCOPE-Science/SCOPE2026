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

The convex spectral-norm objective is nonincreasing under averaging by all arm permutations, so optimizing the invariant family gives the unrestricted global minimum. Its Laplacian decomposes into a four-dimensional radial block R and k-1 copies of three-dimensional contrast block B; interlacing bounds the gap by min(B). Put gamma=2/(3k+5+sqrt((3k+5)^2-24k)) and a=(1-5gamma)/(3gamma)>0. The positive contrast vector (a,a+1,a+2) obeys B*v=gamma*v at x=1/k,y=(2-gamma)/3,z=(1+gamma)/3. For any feasible weights, its Rayleigh quotient is (x*a^2+y+z)/norm(v)^2<=gamma because x<=1/k and y+z<=1. Equality forces x=1/k,y+z=1 and the final eigenvector equation uniquely gives z, y. The radial characteristic factors as t(t-1-gamma)[t^2-(2+1/k-gamma)t+(3+1/k)(2-gamma)/9]; checking q(2-gamma)=(2-gamma)(3k-8)/(9k)>0 and the vertex ensures max radial and contrast eigenvalues <2-gamma. Hence SLEM exactly 1-gamma and all boundaries/loops are feasible. Independent eigenspectrum reconstruction for k=3..22 passed. Nonsymmetric uniqueness is not claimed.

## originality

PASS

Boyd et al supply general convex FMMC formulation rather than this exact constrained spider optimum; the closest same-topology symmetric-star consensus solution permits negative root holding, and the 2020/2025 reversible formula assumes a stationary-mass inequality that fails here under uniform mass. Resultary balanced-spider mixing law addresses a fixed lazy walk, not optimization. Historical specific formulas remain possible.

## value

PASS

The family is a natural mixing-design optimization under the physically essential nonnegative stochasticity and uniform stationary law. The exact optimum and unique invariant edge weights identify which holding constraints bind (root and depth two zero) and quantify spectral-gap asymptotics, sharply separating feasible Markov-chain design from earlier unconstrained consensus weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
