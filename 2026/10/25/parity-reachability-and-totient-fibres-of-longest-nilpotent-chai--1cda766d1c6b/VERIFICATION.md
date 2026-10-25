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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The script independently enumerates all directed Hamiltonian paths on \([n]\) for \(3\le n\le9\), tests the cyclic-descent orientation criterion, counts every ordered terminal/initial endpoint pair, and confirms \(\varphi(n-1)\) realizations for each neighboring pair. It then builds explicit cyclic-shift constructions for all allowable endpoint pairs through \(n=35\). Expected final line: `VERIFY_OK`.

The finite tests do not establish the theorem beyond their tested bounds; the general argument is the permutation-sign obstruction, explicit cycle construction, reflection and contraction proof in `RESULT.md`. The 2000 paper listed as a literature risk was not inspected in full text. No independent audit or validation has been performed.
