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

The first engine builds all Dean prefixes avoiding \(\mathtt{10}\) and checks only newly created suffix squares. The second engine independently rescans each candidate prefix for every inverse-adjacent pair, every occurrence of \(\mathtt{10}\), and every square factor. Their complete level sets must agree through length \(59\).

The verified fixed-pair survivor counts end with \(7,6,6,4,1,0\) at lengths \(54,55,56,57,58,59\). The unique length-\(58\) survivor is checked to contain all seven other possible length-two Dean factors.

The verifier then constructs all eight alphabet permutations commuting with inversion, confirms transitivity on the eight possible length-two Dean factors, and verifies that the resulting eight boundary words are distinct and each misses exactly one such pair.

The verification establishes only the equality classification at the published length-two threshold. Independent audit has not been performed.
