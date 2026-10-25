---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For the sufficiently subdivided Q3 unordered two-particle deleted-product model there are 28 vertices,72 edges,42 squares; independently reconstructed signed cellular boundaries satisfy d1*d2=0, rank d1=27 and rank d2=39. The source projection.json gives an exact 45-square determinant -1 from 39 square boundaries plus 6 integral cycles, proving a primitive H1 basis and torsion-freeness. Five stationary-particle cube cycles map surjectively to H1(Q3), the exchange loop spans the kernel. The 48 signed automorphism matrices satisfy their 2304 compositions; the three generator systems uA−delta*u=b have unique solution u=(-1,1,-1,1,-2)/3, obstructing a Z-equivariant section but defining one over Z[1/3]. Order is exactly 3 in the extension group. Three opposite-face product tori are cycles with unit determinant minor and rank-3 kernel, giving full integral H2; antipodal eigenlattice determinant is 4 with primitive minors. I independently reconstructed cell ranks, unimodular quotient, and rational section from transparent verify.py/projection.json, not relying solely on VERIFY_OK.

## originality

PASS

Barnett–Farber studies ordered two-point graph configurations and planar intersection/rank formulas, not this integral Aut(Q3)-module extension. General graph braid presentations and published SCOPE rational symmetry modules for a different graph do not calculate the canonical three-primary integral equivariant obstruction on Q3. Distinction is coefficient-module extension versus mere Betti counts.

## value

PASS

The exact order-three obstruction is an intrinsic integral symmetry invariant not visible to homology ranks or rational irreducible characters. The concrete canonical total-motion extension and index-four gluing are motivated natural topological data for particle exchanges on a familiar graph and could be reused in equivariant graph configuration comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
