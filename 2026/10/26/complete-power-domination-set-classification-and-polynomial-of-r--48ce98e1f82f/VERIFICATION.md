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

# Verification evidence

The self-contained `verify.py` implements the classical power-domination procedure independently of the row-column characterization. Initial observation is the closed neighborhood of the given sensor set. Every further step scans observed vertices for a unique unseen neighbor and adds that neighbor; termination is the absence of changes.

For all \(1,152,592\) subsets of the eight boards \(2\times2\), \(2\times3\), \(2\times5\), \(3\times3\), \(3\times4\), \(3\times5\), \(4\times4\), and \(4\times5\), the result equals the structural criterion; resulting polynomial coefficients and minimum multiplicities match independently evaluated inclusion-exclusion. An additional 2-dimensional exact-integer parameter sweep checks formulas for \(2\le p\le8\) and \(p\le q\le11\). See `verification_output.txt` for precise outcomes, and run `python3 verify.py` to repeat them.

Boundary cases \(p=2\), square \(p=q\), and empty selection are included in this test. The general theorem is proved by the geometric and unique-neighbor argument in `RESULT.md`; no finite test is offered as an infinite proof.

Independent mathematical audit status: not performed.
