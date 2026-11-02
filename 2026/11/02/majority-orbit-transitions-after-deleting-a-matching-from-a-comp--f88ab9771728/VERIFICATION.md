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

Extract `check_matching_majority.py` alongside this file and run `python3 check_matching_majority.py` with standard Python 3. The program constructs each graph's full set of neighbor bitmasks and applies synchronous strict majority, retaining the current bit on exact ties. For every \(4\le n\le16\) and \(1\le m\le\lfloor n/2\rfloor\), it checks the fixed-state formula, the primitive two-cycle formula, and that every trajectory reaches recurrence within three steps.

The replayed output reports \(62\) graph-parameter pairs and \(961184\) total input states. The code also verifies an explicit configuration on \(G_{5,3}\) whose first periodic state occurs only at time three. Representative output and the complete observed run output appear in `verification_output.txt`.

These computations are exact for the enumerated finite parameter set, but do not prove the theorem for arbitrarily many vertices. The case-by-case mathematical proof in `RESULT.md` supplies the infinite result. The historical literature comparison is not an independent priority certification; its source-access limitations are documented in `REVIEW.md`.
