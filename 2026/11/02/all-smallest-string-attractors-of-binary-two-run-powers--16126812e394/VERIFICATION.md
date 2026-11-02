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

# Reproducible finite checks

The included `verify.py` uses only Python 3 standard-library modules. Run `python3 verify.py` from the directory containing it. It reconstructs the finite words, lists all distinct contiguous factors and their exact union-of-occurrences position masks, then checks **all** unordered pairs independently of the proposed four-factor condition.

For run lengths from one through five and repetition counts from two through five, all 100 parameter triples pass, comprising 25,950 candidate pairs. The count formula, the complete predicted pair set, and every distance-spectrum coefficient for both run lengths at least two match. A separate literal occurrence test, without factor masks, compares 2,100 further pairs for run lengths one through three and repetitions two through four. The actual run returned:

`VERIFY_OK parameter_cases=100 masked_pair_tests=25950 direct_pair_tests=2100 span_spectra=True`

These tests certify only the indicated finite instances. The arbitrary-parameter result relies on the proof in `RESULT.md`; none of the tests is an independent infinite proof. No external audit was performed.
