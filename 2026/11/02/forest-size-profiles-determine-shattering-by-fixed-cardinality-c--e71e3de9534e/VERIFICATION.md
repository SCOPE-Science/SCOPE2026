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

# Reproducibility

The file `verify.py` uses only the Python standard library. Execute `python3 verify.py`; its output is recorded in `verification_output.txt`.

The program enumerates every query-edge subset for \(2\le n\le6\) and every prescribed smaller-side size \(1\le a\le\lfloor n/2\rfloor\). It implements two different checks: direct realization of binary patterns by all \(a\)-element subsets, and the forest-component polynomial criterion. It asserts agreement for 100,490 parameter/support triples. It also checks the proposed stable-range star witnesses for \(1\le a\le8\), using the polynomial test.

The general forest theorem and stable-range formula are established by the mathematical proof in `RESULT.md`; verification on bounded parameters is not an infinite proof. The test does not investigate the adaptive Littlestone dimension, unpublished literature, or independent publication-priority certification.
