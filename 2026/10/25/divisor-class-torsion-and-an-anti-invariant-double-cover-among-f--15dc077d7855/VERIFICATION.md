---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Finite matrix calculations and limits

Execute `python3 verification_quotients.py` using the packaged file and the standard Python library. The verifier transcribes the four published generating sets and enumerates all finite products. It constructs normal closures of generator commutators, obtains exact derived groups, computes orders of all abelian quotient elements, checks that the 288-element group is a normal index-two subgroup of the 576-element group, and checks that conjugation by the extra generator inverts the smaller abelianization.

Expected checks: group orders \(36,24,288,576\); derived orders \(9,6,32,288\); abelian-quotient order distributions \(\{1:1,2:3\}\), \(\{1:1,2:3\}\), \(\{1:1,3:8\}\), \(\{1:1,2:1\}\), respectively. The final output is `VERIFY_OK four_group_abelianizations_and_cover_involution`. These calculations have been executed using the packaged source.

The source matrices and their geometric identification come from Burek–Cynk, arXiv:2610.16962v1, Appendix A. The inference from finite abelianizations to affine Weil class groups invokes the Benson theorem as formulated in Schmitt, DOI:10.1112/blms.13100, Section 2.1. The mathematical scope and remaining priority risks are described in `RESULT.md` and `REVIEW.md`. No external audit has been performed.
