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

# Reproducibility

Run `python3 verify.py` with Python 3.8+ from the artifact directory. The program uses no external packages, clocks, databases or network operations. It enumerates all projective linear forms over the two prime fields, applies the necessary rank-three quotient filter to all seven-element subsets, and checks each surviving subset for containment of all four multiplication matrices. The filter cannot discard a valid seven-term factorization because quotient rank is monotone and any containing span has quotient dimension at most three. It then solves the eight-term identities, checks the forms separate points and directly verifies multiplication for all pairs of algebra elements.

Recorded output:

```
FIELD=2: VERIFY_OK quotient_nodes=535 admissible_seven_subsets=1 valid_seven=0 exhaustive_product_pairs=256
FIELD=2: WITNESS_FORMS=('1000', '0100', '1100', '0010', '1010', '0110', '0001', '1001')
FIELD=2: WITNESS_OUTPUTS=('1111', '0111', '0100', '0011', '0010', '0001', '0001', '0001')
FIELD=3: VERIFY_OK quotient_nodes=31200 admissible_seven_subsets=2355 valid_seven=0 exhaustive_product_pairs=6561
FIELD=3: WITNESS_FORMS=('0001', '1210', '1100', '1110', '1002', '0120', '1220', '1001')
FIELD=3: WITNESS_OUTPUTS=('2122', '0110', '0010', '0101', '2120', '0221', '0201', '2121')
```

The proof connecting symmetric decompositions to evolution envelopes is mathematical, not asserted from computational output. All rank tests and product tests operate on the specified field and the complete parameter range of the claimed finite result. No generalization to other fields has been checked or claimed.
