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
The arithmetic replay is `verify.py`.

Checked facts:
- \(83+1=84\) is divisible by \(14\), with one \(83\)-factor before the \(c(2621)\) cutoff.
- \(149+1=150\) is divisible by \(15\), with one \(149\)-factor before the \(c(4567)\) cutoff.
- \(127+1=128\) is divisible by \(16\), with one \(127\)-factor before the \(c(8011)\) cutoff.
- \(13633+1=13634=17\cdot802\), with one \(13633\)-factor before the \(c(13999)\) cutoff.

The proof does not recompute global minimality of the tabulated \(a_i\); it uses the exact A023199 values as input.
