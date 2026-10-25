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
# Reproducibility and verification limits

Run `python3 verify.py` using Python 3 with the standard library. The program constructs the exact rational reproduction probabilities using integer powers of two, reconstructs the quartic polynomial in the monomial basis, and independently verifies vector-field signs at four rational points. The signs and polynomial degree provide an exact certificate for three simple interior roots with alternating stability. The universal two- and three-person result uses the proof in `RESULT.md` and is not inferred from a sample search. The source's original varying-group-size simulations are not claimed as new evidence. Mathematical correctness and publication priority have not been independently audited.
