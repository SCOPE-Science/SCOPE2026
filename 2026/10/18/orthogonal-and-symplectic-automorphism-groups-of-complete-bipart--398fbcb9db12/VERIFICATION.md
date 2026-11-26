---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The hypotheses are positive integer part sizes with m·1_K and n·1_K both nonzero. The product spans the characteristic two-plane Ku⊕Kv and, there, u²=mv, v²=nu and uv=0. Invertibility and preservation of uv=0 force the two lines to be preserved or exchanged. Independently, rank-one left multiplications are precisely the nonzero vectors supported in just one part, which also detects the two parts intrinsically. In the preserved case comparison of bilinear products (not division by two) gives invertible A,D with AᵀA=bI, DᵀD=aI and zero off-diagonal blocks. Their action on the all-ones vectors yields b=a², a=b², hence a³=1, and rescaling gives the full orthogonal stabilizers. The exchange case has injective cross maps both ways, requiring equal dimensions, and the coordinate exchange conjugates by swapping factors and inverting a. The orthogonal complement has determinant square class 1/s; this gives χ((-1)^k s) as the split sign in even orthogonal dimension. In characteristic two admissible s is odd and x·x=(Σx_i)² makes the complementary form alternating and nondegenerate, giving the symplectic order. For s=3, χ(-3)=-1 over F5 so the order is 12; directly the exhibited matrix has row sums 11 and Gram diagonal/off-diagonal 41/40 before reduction. Over F4, Sp_2 has order 4(4²−1)=60 and there are three cube roots of unity, giving 180. The recorded prime-field enumeration and stabilizer tests were inspected, not run; the example's modular Gram identity, not the script's real-rank check, certifies invertibility over F5.

## originality

PASS

The supported distinction is the uniform full-group identification over arbitrary admissible fields, including the characteristic-two symplectic case, not classical group order formulas, graph-induced subgroups, or a separate priority claim for the odd finite-field range. The later odd-field indexed result is a material overlap, with a proof whose initial similitude reduction is itself field-independent; the exact overlap and extension are recorded below. Its additional divisible-size regimes are not part of this finding.

## value

PASS

Complete bipartite graphs give a natural large family where adjacency rank is two, so standard nonsingular monomiality does not describe their evolution algebras. Determining the entire group reveals hidden nonmonomial symmetries and identifies the field-dependent classical form. The characteristic-two identification gives exact counts that can differ substantially from graph permutations and from odd-field counts; the cited group-order formulas themselves are not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
