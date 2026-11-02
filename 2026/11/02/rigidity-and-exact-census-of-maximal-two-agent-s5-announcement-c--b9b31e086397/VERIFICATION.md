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

# Verification procedure and scope

Run `python3 checker.py` with a standard Python 3 interpreter. The program enumerates set partitions to represent both equivalence relations. For each pair of relations, it computes repeated truthful public-announcement restrictions using the original atomic valuation and compares the resulting trace with the static dependency-walk prediction.

With all four Boolean atomic truth types allowed, the exhaustive search checks \(4,64,1600,57600\) labelled models for world counts \(1,2,3,4\), respectively. With the two exclusive atomic truth types allowed, it checks all \(86528\) models on five worlds. Every extremal model must use exclusive truth types by the proven self-loop lemma. In these domains, the exact maximal-extinction counts are \(2,4,12,48,240\). Every observed extremal model is checked against the full alternating-class normal form, including the absence of additional equivalence pairs. A separate exhaustive search confirms one-round stabilization for \(3840\) equal-agent-relation models on four worlds. Expected terminal output: `ALL_CHECKS_OK`.

The checker is a finite cross-check, not an independent proof for arbitrary carrier size or an independent mathematical audit. The symbolic proof in `RESULT.md` carries the general quantifiers and establishes the stated classification.
