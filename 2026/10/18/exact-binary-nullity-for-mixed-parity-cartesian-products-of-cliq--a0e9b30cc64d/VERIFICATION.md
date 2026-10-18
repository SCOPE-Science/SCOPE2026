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

Run `python3 verify_hamming_lights.py` from a directory containing this file and the standalone verifier. This exact-arithmetic checker independently enumerates the closed-neighborhood matrix and performs GF(2) row reduction; it does not use the tensor-space proof as its rank algorithm.

The checked parameter grid consists of all tuples of coordinate sizes \(2\), \(3\), or \(4\) with dimension between \(2\) and \(4\), at least one even coordinate size, and product size at most \(180\). It covers 109 graph families and 6,230 separately tested toggle equations. The output is `PASS 109 mixed-alphabet or all-even graph families, 6230 exact toggle equations, ranks and nullities`.

The mathematical proof uses the characteristic-two identities \(J_q^2=(q\bmod2)J_q\), the parity splitting of odd-index factors, and a contracting homotopy on every even-index tensor summand containing a size-two Jordan block. Those steps establish the formula for arbitrarily large inputs. Finite verification cannot establish all cases or bibliographic novelty.
