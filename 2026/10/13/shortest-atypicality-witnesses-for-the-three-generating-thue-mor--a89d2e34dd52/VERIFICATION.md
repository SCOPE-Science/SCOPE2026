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

Run `python3 verify.py` beside `certificate.json`.

For each of \(\mathtt{aabab}\), \(\mathtt{abaaba}\), and \(\mathtt{aabbaab}\), the verifier enumerates every nonempty ordered pair \((\varphi(a),\varphi(b))\) whose induced image length is at most the claimed minimum. This is enough to prove both the lower bound and the complete set of ties.

Candidate images are tested against the exact finite Thue–Morse factor language using Proposition 2.1 of Almeida and Klíma. As an implementation cross-check, the verifier independently generates \(2048\) Thue–Morse symbols as parity of binary digit sums and confirms that its factor sets agree with the proposition-based factor sets for every length through \(13\).

The search checks \(228+12+36=276\) morphisms. After excluding \(\mu^n\) and \(\xi\circ\mu^n\), each of the three minimum lengths has exactly two witnesses, and the two are exchanged by \(\xi\).

The verification does not classify witness lengths for all proper atypical factors. Independent audit has not been performed.
