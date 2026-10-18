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

# Verification and reproducibility

Run `python verify.py` from the directory containing this document. It uses only Python's standard library and directly implements the original nonassociative multiplication \(e_ie_j=e_{2j-i}\).

The checker tests the predicted multiplicative-orbit partitions for every odd \(n\) from \(3\) through \(79\). It exhaustively evaluates all \(4^3\) native elements of \(\mathbb F_4[R_3]\); all \(7^3\) of \(\mathbb F_7[R_3]\); all \(11^5\) of \(\mathbb F_{11}[R_5]\); and ten other coprime nonsplit prime-field instances, including \(\mathbb F_2[R_{11}]\) and \(\mathbb F_3[R_{11}]\). It independently constructs and checks each Fourier-parametrized idempotent in nine prime-field split cases, by inverse Fourier transform followed by direct multiplication.

Expected final output: `ALL_QUANDLE_IDEMPOTENT_CHECKS_PASSED`.

The finite experiments check examples, not all quantifiers. The infinite proof rests on Fourier inversion, active-orbit cancellation, and Frobenius descent. The characteristic-dividing-order case is excluded. Independent mathematical audit has not been performed.
