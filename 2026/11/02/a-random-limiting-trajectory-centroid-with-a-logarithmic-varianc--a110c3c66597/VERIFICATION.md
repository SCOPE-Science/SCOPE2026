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

# Verification record

The independent path-enumeration and second-moment checker is contained in `checker.py` in this package. It uses Python's standard library, `Fraction`, direct trajectory-law propagation, and scalar moment recurrences. The command `python3 checker.py` passed 177 exact/computed assertions on the supplied file. Exact paths were enumerated for three exploration probabilities and two centered step distributions of equal variance; the endpoint second-moment identity was separately tested at seven time indices. The leading logarithmic finite-size correction was evaluated from a half-million-step scalar recurrence at several fixed probabilities, checking stability of the remaining order-one coefficient.

Analytic verification consists of the definitions and complete derivation in `RESULT.md`: exact conditioning, a square-summable martingale, integral generating functions, elementary integration-by-parts evaluation, and singularity transfer. Independent mathematical audit has not been performed. The numerical checks neither establish the infinite asymptotic nor decide literature priority; those are addressed respectively by the proof and the qualified literature comparisons.
