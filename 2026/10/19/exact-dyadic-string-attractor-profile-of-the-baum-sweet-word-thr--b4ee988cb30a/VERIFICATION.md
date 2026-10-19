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
# Reproducibility and limits

Run `python3 baum_sweet_verify.py` in this directory with the accompanying `baum_sweet_certificate.json`. The program depends only on the Python standard library. It checks the digit-rule and independent length-doubling pair morphism yield identical binary prefixes, tests that the listed attractors meet all distinct contiguous factors, and recomputes every integer half-unit dual factor-packing load by enumerating every occurrence.

The checker was executed against the actual packaged data and produced success for all nine dyadic lengths \(2,4,8,16,32,64,128,256,512\). The certificate includes exactly specified zero-based indices, prefix lengths and all rational weights. At length \(512\), the full factor enumeration has \(108896\) distinct nonempty factors and the proposed nine positions attain the independently verified lower bound of nine.

The finite equality proof is based on exact checks of all factors in each prescribed finite word, together with the analytic dual inequality stated in `RESULT.md`. No conclusions are drawn for larger lengths or arbitrary prefixes. Independent external audit was not performed.
