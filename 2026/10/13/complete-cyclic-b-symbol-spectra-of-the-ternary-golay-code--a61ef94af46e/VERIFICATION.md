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

Run `python3 verify.py`. The verifier uses only the Python standard library and performs the following exact checks:

- constructs the standard cyclic ternary Golay code from \(g(x)=2+x^2+2x^3+x^4+x^5\);
- confirms exactly \(3^6=729\) distinct codewords;
- computes cyclic \(b\)-symbol weight by direct sliding windows for every \(1\le b\le11\);
- independently computes the same weight from cyclic zero-gap lengths and compares the two values for every codeword;
- checks the ordinary Hamming enumerator against the published one;
- checks every coefficient of the claimed \(b\)-symbol enumerators and confirms that each sums to \(729\);
- checks the minimum \(b\)-symbol distance sequence against the published hierarchy.

The finite census proves only the stated code in its standard cyclic coordinate order. It does not establish uniqueness of the spectra among equivalent coordinate permutations, and it does not substitute for an independent external audit.
