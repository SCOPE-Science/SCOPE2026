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

`verify_pal3.py` was executed from the packaged working directory and returned:

```text
VERIFY_OK 7140 ordered gap triples (lengths 3..36)
```

The verifier enumerates each distinct cyclic substring of length between one and the circle length directly. It tests every possible ordered three-gap triple for all lengths 3 through 36, comparing a literal palindrome count against the proved piecewise count, as well as testing the predicted maximum and equality conditions separately. The fully symbolic proof covers all lengths and is independent of this finite experiment.

The Simpson 2014 paper's abstract and 2014-07-22 first-publication date were identifiable. The full manuscript was not inspected, because accessible public full-text retrieval did not succeed and no readable authorized full-text copy was obtained. This affects historical-priority confidence, not the internally derived arithmetic proof. Independent mathematical review and historical-priority verification have not been performed.
