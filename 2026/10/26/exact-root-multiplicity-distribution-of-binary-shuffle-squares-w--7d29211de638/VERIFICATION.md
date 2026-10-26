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

The accompanying `verify.py` is a standalone, standard-library-only Python 3 program. Execute `python3 verify.py`. It performs three logically separate checks: (i) an independent two-copy interleaving-state computation for all \(2856\) binary linear words with exactly two ones and \(0\le m\le15\); (ii) independent direct self-shuffle construction and duplicate removal for roots with \(0\le m\le9\), covering \(715\) root-output incidences; (iii) distribution, root-incidence and extremal identity checks for every \(0\le m\le100\). All ran successfully in the provided environment.

The software independently verifies finite instances and cross-checks the arithmetic identities. It does not serve as an infinite proof, does not establish historical priority, and does not constitute independent audit. All-length claims rely on the gap-interval and peeling-bijection proof in `RESULT.md`.
