---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: From [H,H]=kz a Lie homomorphism has F(z)=cz and F(v)=Av+ell(v)z. A^T J A=cJ, A^2=A, c^2=c and ell A+c ell=ell follow without dividing by two, so characteristic two is included. The c=1 branch is identity because A is invertible idempotent and ell=0. On c=0, im A is isotropic, A a projection along a complement, and ell descends to a functional of im A. Conversely these choices give all proper retractions. The split idempotent decomposition makes rank locally constant on the functor, so its rank strata are open-closed; complement+functional parameters form a Zariski-locally trivial affine bundle over the smooth irreducible isotropic Grassmannian. Its dimension r(2n-r)-r(r-1)/2 +r(2n-r+1) equals (8nr-5r^2+3r)/2. Isotropic frame choices divided by GL(r,q) give the stated q-Gaussian product. The finite difference d(r)-d(r-1)=4n-5r+4 proves the maximal-rank transition. Independently enumerated 3D Heisenberg projections over F2/F3 (rank profiles 1,12,1 and 1,36,1) and all 65536 4x4 binary A with admissible functionals (proper counts 1,240,960). Finite samples do not establish general scheme geometry; the displayed argument does.

## originality

PASS

PASS, qualified: Symplectic isotropic Grassmannians and projection parameterization are standard pieces, but the inspected nearest primary papers concern automorphisms, almost-direct factors, and unital-algebra augmentations, not the exact all-characteristic idempotent Heisenberg scheme, its finite-field rank census or the dimension-maximizing-rank phase transition. Semantically compared reductions rather than matching titles; no stronger directly covering theorem located. All-geometry classification may be implicit in broader endomorphism-variety literature; priority is not certified.

## value

PASS

PASS: Idempotent Lie endomorphisms are natural retracts; the complete component geometry and exact finite-field distribution resolve a structural enumeration for the canonical two-step nilpotent Lie algebra. The non-obvious rank-dominance switch at n>=5 supplies motivation beyond matrix substitution and routine isotropic-subspace counts. This remains a self-contained classification even without a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
