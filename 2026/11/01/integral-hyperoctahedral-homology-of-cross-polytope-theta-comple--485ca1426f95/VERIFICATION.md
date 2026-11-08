---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: For n>=2 and 1<=k<=n-1, a signed subset is independent of (k+1)-face hyperedges precisely when its support meets at most k antipodal pairs. Projection to the (k-1)-simplex skeleton has a positive-vertex section, with section∘projection contiguous to identity; hence it is a B_n-equivariant homology isomorphism even though the section itself is not equivariant. The augmented simplex chain complex over Z is exterior powers of E_n with contraction by coordinate sum; its top skeleton cycles are wedge^k U_n, with no lower homology/torsion. Signed combinatorial Alexander duality on the ambient 2n-vertex set twists by the ambient vertex-permutation sign: each pair-block permutation is even, each sign flip is odd, giving eta. Integral UCT yields H_{2n-k-2}(Theta;Z)=Z_eta⊗(wedge^k U_n)^* and vanishing otherwise. The coefficient formula for traces follows from the exterior-power determinant. For k=1,n>=3, modulo any prime p|n the root lattice U_n mod p has the all-ones invariant, whereas its weight dual quotient has no invariant, proving integral nonisomorphism though rationalizations agree. Checked n=2 and endpoint k=n-1 in the universal construction; finite character/lattice verifier is only a corroborating check, not proof of the infinite theorem.

## originality

PASS

PASS on best-of-knowledge: nonequivariant theta sphere multiplicities and integral Alexander duality are credited prior ingredients; the full signed integral B_n module and root/weight obstruction are more informative and are not stated by the inspected prior theorem. An unindexed specialization of equivariant general duality remains a concrete risk.

## value

PASS

PASS: The natural symmetry action on the integral homology of the full cross-polytope face-hypergraph theta family is a structural invariant not resolved by its known wedge-of-spheres topology. The weight-versus-root distinction persists integrally despite identical rational characters, so the exact B_n module supplies genuinely useful information for equivariant topology and torsion-sensitive calculations; it is not merely a parameter rename or ordinary Betti recount.

The dated certificate retains the supplied scientific assessment, sources and limitations.
