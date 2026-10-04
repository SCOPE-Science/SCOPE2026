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
# Verification

The proof was checked directly against the defining transition maps. The critical steps are: (1) only \(b\) can decrease rank and it merges only \(2\) with \(n\); (2) after every nonfirst effective \(b\), both \(2\) and \(n\) are absent; (3) this forces two letters before the second effective \(b\) and three letters before every later one; (4) equality therefore forces \((bab)^{s-1}\); and (5) direct induction on the missing-state set proves exactly where those forced words stop gaining deficiency.

The packaged script `artifacts/verify_h_profile.py` was executed from its package staging path. It performs exact power-automaton BFS for every \(4\le n\le14\), verifies every claimed minimum and uniqueness count, and checks the first strict saturation boundary. It also directly replays the witness formulas for every \(4\le n\le300\). The captured output in `artifacts/verification_output.txt` is `VERIFY_OK`.

The exhaustive BFS range is finite corroboration only. The universal quantifiers in the finding rely on the symbolic spacing and missing-set proofs above. No claim is made for the later compression profile after the first saturation point.
