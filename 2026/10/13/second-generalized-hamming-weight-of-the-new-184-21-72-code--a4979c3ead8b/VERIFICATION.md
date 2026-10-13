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

The accompanying `artifacts/verify.py` is a standalone Python checker using only the standard library.

It reconstructs the published code from the four factors of \(h\), the quotient \(g=(x^{85}-1)/h\), the second quasi-cyclic multiplier \(f_2\), and the fourteen five-bit tail patterns. It then:

1. checks that the reconstructed generator has binary rank \(21\);
2. enumerates all \(2^{21}\) messages and obtains minimum distance \(72\) with \(A_{72}=9826\);
3. tests all \(\binom{9826}{2}=48{,}270{,}225\) unordered pairs of minimum words;
4. obtains exactly \(1{,}748{,}433\) pairs whose sum is also minimum, hence \(582{,}811\) minimizing two-dimensional subcodes;
5. checks the explicit message triple \(0x63,0x318,0x37b\), whose three codewords have weight \(72\) and union support \(108\).

The finite enumeration is exhaustive for this \(21\)-dimensional code. It is not used as a substitute for the symbolic lower bound \(d_2\ge108\); that lower bound follows from the exact support identity for every binary two-dimensional subcode.

The checker does not determine \(d_r\) for \(r\ge3\), nor does it make a claim about inequivalent codes sharing the same ordinary parameters.
