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

Execute `python3 checker.py` from this directory. It requires only the Python standard library and prints `ALL_CHECKS_OK` if all assertions hold.

The executable checks all \(2^{n^2}\) directed relations for \(1\leq n\leq4\); checks the independently defined modal truth and stratified predecessor recurrences; and reproduces the \(m=1\) exact labelled count \(768\), including \(192\) fixed-root instances. It enumerates all canonical normal-form choices for \(m=0,1,2\), tests the singleton-layer identities and semantic separation, checks automorphism-freeness for the \(m=1\) family, samples the \(m=3\) family, and verifies all path-witness instances through \(m=12\).

The code does not exhaustively enumerate all relations on six or eight worlds, nor does it prove the general result by enumeration. The complete infinite-parameter correctness argument is the four-step symbolic proof in `RESULT.md`. No external formal proof assistant or independently audited certificate is claimed.
