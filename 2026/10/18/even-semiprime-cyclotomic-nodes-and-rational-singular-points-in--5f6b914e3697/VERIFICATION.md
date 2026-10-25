---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Jacobian rank on hyperplane sum xi=0 forces coordinates into a projectively normalized mu_(2p) root list. Cyclotomic polynomial Phi_p forces equal positive-minus-negative multiplicity at all p residues; free scaling gives N!/(2p) weighted coefficient. Nontrivial Galois projective stabilizer forces coordinate ratios +/-1 and p-1 degree otherwise; nonzero Hessian determinant makes singularities ordinary nodes and finite etale. Burnside rotates p-tuple multiplicities. Independently enumerated normalized root lists for (p,N)=(3,5),(3,6), reproducing (A,R,Q)=(60,0,30),(340,10,165). Proof applies to odd prime p, N>=5, char0; no positive-characteristic assertion.

## originality

PASS

Statement-level best-of-knowledge check: Fermat hypersurface ED degree, diagonal hyperplane singularities, vanishing root sums, antipodal cancellation and necklace orbit counts searched as equivalent contexts. Lam-Leung 2-prime theorem covers vanishing-sum semigroup; Lee ED-degree theorem counts a different critical locus. Neither supplies scheme-theoretic singularity/Galois refinement of X_{p,N}. Even from Lam-Leung root-sum classification, the Jacobian/Hessian/projective Galois and Burnside deductions remain necessary; geometric theorem not stated as immediate established corollary in inspected sources.

## value

PASS

The arithmetic-geometric singular scheme of a natural Fermat hyperplane family, including rational versus cyclotomic residue degrees and permutation orbits, is a natural exact invariant; these refinements are not implied by generic root-weight semigroup statements alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
