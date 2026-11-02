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

The verification is self-contained. Run `python3 verify.py`, `python3 independent_check.py`, and `python3 amplification_check.py` together in one directory with Python 3; no third-party module is used. The first program exhausts all simple labeled graphs through five vertices and tests maximality by independence and external domination. The second implements a different maximality test via complement cliques and checks shattering via depth-by-depth Boolean tree search. Both obtain no strict gaps through four vertices and exactly \(90\) labeled five-vertex strict gaps in two isomorphism classes of respective sizes \(60\) and \(30\). The third program tests the connected cograph family at its first two parameters.

The mathematical proof of the infinite formula is in RESULT.md; finite checks are not treated as proof for all \(m\). Neither source priority beyond the documented comparisons nor external independent scientific audit is certified.
