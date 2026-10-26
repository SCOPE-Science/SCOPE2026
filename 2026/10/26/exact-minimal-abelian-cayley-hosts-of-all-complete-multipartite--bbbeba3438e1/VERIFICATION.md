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

Run `python3 verify.py` with standard Python 3 only. Its expected exact output is embedded as `verify_output.txt` and must be compared byte-for-byte with the actual standard output.

The verifier constructs cosets of \(t\mathbb Z/(tM)\mathbb Z\) for all nondecreasing positive part tuples with \(2\le t\le6\) and \(m_i\le5\), then checks every graph edge/nonedge against the prescribed connection set, as well as the disjointness and coverage of the \(t\) forcing difference sets. It also tests complete normalized label enumerations for three small singleton-rich families in all abelian group isomorphism types of orders below the alleged threshold. Group types and normalization are visible in the code; these finite searches are not the basis of the general theorem.

The infinite formula follows from the paper-and-pencil difference packing and explicit cyclic host. The rigidity deduction requires no computational lemma beyond the finite-group set identities reproduced in the proof. This package does not assert a third-party certificate, an independent audit, or bibliographic priority beyond the inspected material.
