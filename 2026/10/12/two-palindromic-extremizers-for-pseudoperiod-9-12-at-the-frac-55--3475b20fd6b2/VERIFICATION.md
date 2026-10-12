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

The verifier reconstructs every binary prefix with pseudoperiod \((9,12)\) that is \(\frac{55}{21}\)-free through length \(201\). Engine 1 tests a candidate suffix of the minimum forbidden length by slice equality; Engine 2 performs the same mathematical condition through an independently coded explicit index loop. Their complete level sets are required to be identical.

For each period \(p\), the critical suffix length is exactly
\[
\left\lceil\frac{55p}{21}\right\rceil.
\]
A suffix of this length with period \(p\) is present if and only if that extension creates a factor of exponent at least \(\frac{55}{21}\).

The verifier also performs whole-word pseudoperiod and repetition scans on both length-\(200\) survivors, verifies that neither can be extended to length \(201\), and checks that the pair consists of complementary palindromes.

Independent audit has not been performed.
