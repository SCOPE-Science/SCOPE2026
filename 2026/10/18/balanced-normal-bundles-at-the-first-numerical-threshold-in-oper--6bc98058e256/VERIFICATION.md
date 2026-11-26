---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Set m=2k-1. The two rows define a rank-two subbundle because they are individually nonzero and occupy complementary coordinate blocks. The first block is a Veronese embedding and can be recovered from the two-plane by intersecting with that coordinate block on the incidence locus where the intersection has dimension one. The map is therefore an embedding, even though the second row factors through a degree-two map. The coefficient vectors in both blocks span their blocks, giving the stated nondegeneracy, and det(S*) has degree m+2k=4k-1. For the two line inclusions the adjacent syzygies (-y,x) and (-y^2,x^2) generate the respective kernels pointwise, including x=0 and y=0 where the truncated matrices retain full rank. Thus Q splits as O(1)^m plus O(2)^k. Tensoring with S* gives precisely the four displayed tangent blocks. In the chart x=1, pairing the derivative of the monomial row with its j-th adjacent syzygy gives -j t^j+(j+1)t^j=t^j for j=0,...,m-1. These are the complete degree-(m-1) sections globally, with the other chart included by homogenization. The resulting O(2) injection into O(m+1)^m has quotient O(m+2)^(m-1), using the split adjacent-syzygy kernel of the dual complete evaluation map. Since the projection is a subbundle injection, the other tangent blocks inject into the full normal bundle, with the displayed quotient. Extension classes vanish because each degree difference of a left summand minus the quotient degree is 0 or 1. The multiplicities are consequently 5k-3 and k. Rank 6k-3 and degree 12k^2+k-3 independently follow from dim Gr and the Plücker tangent degree. Irreducibility of the degree-fixed map space gives genericity: on the open embedded nondegenerate locus the normal sheaf is a family of bundles, and H^1(End N)=0 is open by semicontinuity and equivalent to balancedness on P^1. The exhibited point belongs to the open balanced locus; rank and degree force the same splitting generally. For k=2 this gives O(5)^7 plus O(6)^2. The exact identities were reconstructed analytically; CHECK.py and VERIFICATION.md were inspected, not executed. The result is over C and for general curves only, not arbitrary maps or positive characteristic.

## originality

PASS

The supported new claim is the actual balanced splitting of this infinite boundary family, not the numerical obstruction, universal 2-balancedness or low-dimensional cases. Primary statements of Coskun–Larson–Vogt and Cao do not prove this series. Ran's Theorem 13 must be translated before comparing: its odd and 2 mod 4 branches do not establish the target degrees, and its 0 mod 4 branch can meet the numerical conditions but then needs a further balanced curve in lower dimension. The named base results do not discharge that input in the checked cases. That conditional overlap is material but is not evidence of an unconditional prior proof.

## value

PASS

This is an infinite family at the first positive side of a sharp numerical obstruction where the prior universal bound leaves a real possibility of a two-degree gap. The explicit construction proves which side the generic splitting takes, beginning beyond the dimensions of Cao's case theorem. The projected Veronese differential and degree-compatible extension splitting are structural inputs; the result is not obtained by merely rounding the average normal degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
