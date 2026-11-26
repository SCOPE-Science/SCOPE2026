---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Counting incidences gives MM^T=M^T M=qI+J and constant row and column sums q+1; each side has N=q^2+q+1 vertices. The two constant sectors and the paired zero-sum subspaces reduce both kernels to scalar ± blocks, with restricted singular value sqrt(q). For D_p the antisymmetric constant block starts at −1 at p=0 (off-diagonal convention) and is strictly decreasing because (q+1)log 2<q log 3; the lower paired block is strictly negative. The upper paired block changes sign at the unique root of (3/2)^p−(1/2)^p=1/sqrt(q), an increasing function from zero to infinity. At the root precisely N−1 mean-zero eigenvalues vanish; the centered Gram matrix has rank N there and 2N−1 strictly below. The zero diagonal and strictly positive off-diagonal squared distances give distinct points in the Gram realization. For the exponential kernel at t>0, the constant symmetric eigenvalue and upper paired block are positive; the two remaining displayed inequalities are exactly the other eigenvalue tests. Below or at the exponent threshold strict positivity for every t>0 follows from the Fourier representation of the Gaussian on the distinct embedded points. For p=1 and z=exp(−t), the two tested blocks factor as (1−z)(1−qz+q^2 z^2) and (1−z^2)(1−sqrt(q) z). The former is positive, and the latter gives exactly t=(log q)/2 as the positive boundary, with kernel rank N+1 there; t=0 is the separate rank-one case. For supercritical p the small-t derivative is negative on the positive distance block, while the large-t limit is I. Independent symbolic factorization and an exact shortest-path check on a cyclic Fano difference-set model gave boundary rank 8 and reproduced the stated q=2,p=2 example with the antisymmetric inequality failing alone.

## originality

PASS

The exact negative-type root and both Gram embedding ranks have material separately indexed coverage and are not credited here as a distinct contribution. The supported distinct component is the evaluated projective-plane powered-exponential covariance region, including its exact positive ordinary-distance threshold and covariance endpoint rank. The strongest primary sources provide the equivalent Gibbs/Q-matrix problem and general radial positivity machinery, not an evaluated projective-plane cutoff or this powered two-parameter region. The prior generalized-quadrangle classification is for a materially different graph and has a different phase and nullity.

## value

PASS

For a natural infinite family of diameter-three finite geometries, the result tells exactly which powered radial exponential matrices can be covariance matrices, including examples where only one of two genuine obstructions fails. The simple ordinary-distance positive threshold and its large boundary nullspace quantify a sharp difference from all-bandwidth negative type and from the known quadrangle phase. The covariance classification and rank are useful even without counting the connected components of the powered parameter region.

The dated certificate retains the supplied scientific assessment, sources and limitations.
