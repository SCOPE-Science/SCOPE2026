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

The associated `verify.py` performs deterministic, independent finite checks. It builds the first \(2^{17}\) terms from the Baum–Sweet digit definition and from a four-state uniform morphism, and confirms termwise agreement. It then scans all factors of dyadic lengths through \(2^{11}\) within the generated prefix, checks extrema against the Fibonacci count, and checks aligned-block coordinatewise domination for selected full blocks. Run `python3 verify.py` from a directory containing the extracted file. Successful output terminates with `VERIFY_OK`.

The tested finite prefix is not an exhaustive search of the infinite word; the unlimited assertions follow from the proof in `RESULT.md`. The public inputs are self-contained; no external data or hidden artifacts are necessary.
