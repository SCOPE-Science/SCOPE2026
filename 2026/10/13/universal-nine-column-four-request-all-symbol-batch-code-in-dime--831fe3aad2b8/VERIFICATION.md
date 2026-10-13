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

The two accompanying artifacts are `certificates.json` and `verify.py`. Run `python3 verify.py` with both files in one directory. The verifier checks that the matrix begins with the identity, that every listed coefficient is an integer equal to \(\pm 1\), that every recovery identity equals the requested generator column over \(\mathbb Z^4\), and that the four supports in each of the nine four-equal and 36 two-pair bundles are pairwise disjoint. It then checks the elementary reduction by explicitly verifying all 495 four-request multisets. The observed result was:

`VERIFY_OK: 9 column targets, 36 two-pair targets, all 495 request multisets, exact integer identities`

These fixed integer identities prove recovery over every field by specialization. The lower bound nine follows from the published exact three-request length and strict monotonicity in requests (Boruchovsky et al., arXiv:2601.04041v2, Propositions 18 and 10(iii)). The paper's Theorem 23 and Proposition 24 were compared for coverage. An independent scientific audit has not been performed. No uniqueness, functionality for arbitrary target vectors, or broader parameter family is certified here.
