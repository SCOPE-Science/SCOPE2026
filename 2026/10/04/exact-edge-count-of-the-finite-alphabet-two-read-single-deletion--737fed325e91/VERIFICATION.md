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
# Verification

The proof has two logically separate ingredients. First, the published Type-A characterization identifies the exact source pairs whose one-deletion balls have two common descendants. Second, the present counting argument gives a unique encoding of every such unordered pair by an interval, a common outside word, and an unordered pair of alternating symbols.

`verification/verify.py` independently reconstructs each distinct deletion ball from coordinate deletions and independently tests the canonical alternating-interval condition. It checks that these predicates agree for every unordered source pair for binary blocklengths \(2\) through \(9\), ternary blocklengths \(2\) through \(6\), quaternary blocklengths \(2\) through \(5\), and alphabet size \(5\) at blocklengths \(2\) through \(4\). It also verifies that every tested deletion-ball intersection has size at most two and that brute-force counts equal both the interval sum and the closed form.

The recorded execution ends with `VERIFY_OK`. The binary edge counts at blocklengths \(2\) through \(10\) are \(1,5,17,49,129,321,769,1793,4097\).

The finite computation is not a certificate for all \(q\) and \(n\). Universality comes from the published Type-A theorem plus the explicit bijection and finite-sum identity. No claim is made about the degree distribution, independence number, or chromatic number.
