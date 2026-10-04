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

The proof in `RESULT.md` is symbolic. The bundled `verify.py` independently generates unitary divisors of the exponent, computes the exponential-unitary harmonic-mean divisibility directly, and compares it with the squarefree-generator criterion.

Running `python verify.py` checks \(36,025\) triples with \(2\le a\le12\), primes \(p<40\), and squarefree \(m\le500\) coprime to \(p\). It also checks representative local generators, including a non-squarefree obstruction at \((a,p)=(4,2)\) and a positive case at \((a,p)=(4,3)\). Expected output begins with `VERIFY_OK`.

The finite computation is corroborative only. It does not prove the unrestricted theorem or the asymptotic. The asymptotic uses the standard fixed-modulus count of squarefree integers coprime to a fixed integer.
