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

# Reproducing the mathematical certificates

The standalone script `checker.py` uses the Python 3 standard library only. Run `python3 checker.py` in the same directory as `signature_certificate.csv` and `profile_certificate.csv`. It enumerates all 81 signatures, constructs the exhaustive fingerprint partition, compares the seven signature formulas with directly counted overlapping length-three factors for 2401 zero-gap quadruples, and compares all observations for lengths 3 through 28 against the finite-state fibers. It regenerates the two complete CSV certificates.

The signature table gives every possible truncated-gap quadruple and its fingerprint. The profile table lists every fingerprint class, its member signatures, its first appearance, its fiber cardinality at gap total 15, and all four successive Newton differences relative to the unique cubic dominant class. The full all-length proof uses only the exhaustive finite-state partition and exact polynomial reasoning. The checker does not establish publication priority or constitute independent scientific validation.

## Limits

Verification is restricted to binary linear words of weight exactly three with overlapping trigram multiplicities. Related primary literature includes a partially accessible 2016 conference article; historical priority is not certified.
