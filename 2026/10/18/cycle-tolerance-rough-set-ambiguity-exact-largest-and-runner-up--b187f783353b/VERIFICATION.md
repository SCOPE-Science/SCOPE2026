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

The package's standalone `verify.py` uses only Python's standard library. Invoke it as `python3 verify.py`. It independently obtains approximate membership bits by testing each cyclic triple and groups all binary subsets into genuine observed lower/upper pairs, rather than assuming the claimed fiber structure. It cross-checks every realized fiber against the trace formula through cycle size \(11\), and sharp maxima through size \(16\). It checks the two path generating-function identities by exact integer matrix powers and a finite collection of endpoint supermultiplicativity instances. It does not constitute proof of the statement for unbounded cycle length; the proof is in RESULT.md.

Expected terminator: `VERIFY_OK binary_inputs 131064 observations 37596 all_fiber_traces_n_le_11=PASS sharp_runnerup_n_7_to_16=PASS`.

Independent external audit: not performed. Publication priority: not externally certified.
