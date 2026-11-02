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

# Reproducible checks and limits

Run `python3 verify_schur.py` from a directory containing the packaged standalone verifier. It uses Python 3's standard library only. The associated `verification_output.txt` is the captured output from a successful execution and terminates in `VERIFY_OK`.

For \(\mathbb F_5\), the verifier exhaustively computes all \(25\) inputs to the binary quartic and all projective charts, obtaining \(n_0=9\), four remaining fibers of size four, and \(36\) rational projective points. For \(\mathbb F_{25}\), arithmetic is implemented explicitly in \(\mathbb F_5[u]/(u^2-2)\); the \(625\) binary inputs yield zero fiber size \(97\) and four six-element fourth-power cosets with fiber values \(16,0,48,24\). An independent enumeration of every uniquely normalized projective point obtains \(1176\). Multiplicative orders and the \(4,0,12,6\) cubic-power coset weights are asserted by exact arithmetic.

The code checks the numerical saturation \(1176=1+25^2+22\cdot25\) and the resulting algebraic Frobenius trace relation, but it does not implement or certify the mathematical proofs of geometric smoothness, étale cohomological purity, Lefschetz trace formula or the K3 Tate theorem. Those are stated and used explicitly in `RESULT.md`. Point enumeration over \(\mathbb F_{5^m}\) for \(m\ge3\) is neither performed nor needed; the all-extension formula follows from the established Frobenius spectrum. No independent audit has been performed.
