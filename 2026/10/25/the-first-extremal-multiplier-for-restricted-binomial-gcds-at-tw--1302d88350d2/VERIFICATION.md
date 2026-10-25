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

# Reproducibility and limitations

Execute `python3 verify.py` with standard Python. The program counts binomial valuations by checking exact base-\(p\) borrow thresholds independently for all odd primes through \(71\) and multipliers \(2\le q\le p+1\). The observed output is `CERTIFICATE_OK 637`, representing 637 fully enumerated parameter cells. The universal statement rests on the proof in `RESULT.md`. The program does not establish infinite validity, a global literature novelty claim, or an independent audit.
