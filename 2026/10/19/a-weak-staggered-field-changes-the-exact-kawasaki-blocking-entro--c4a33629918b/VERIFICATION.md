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

# Reproducible scientific checks

Execute `python3 verify.py` with Python 3 and SymPy installed. The executable constructs the exact two-step transfer matrix from the local Kawasaki energy rule and proves, by exact symbolic arithmetic, its characteristic polynomial and determinant. The generating-function coefficients are compared against matrix traces through eight powers.

An independent direct Hamiltonian implementation enumerates every configuration and every allowed neighboring exchange on periodic rings of lengths \(4,6,8,10,12\) using exact rational field strengths \(h/J=1/7\) and \(h/J=9/10\). For each length and both choices, its complete magnetization polynomial matches the transfer trace. The run completed with all assertions passing.

Finite checks do not certify the limiting entropy or all system sizes. Those conclusions follow analytically from the local-window bijection, a polynomial determinant identity and a strict dominant-root argument in the accompanying proof. The zero-field comparison assumes all energy-neutral Kawasaki moves have positive rate, as specified. Independent audit has not been performed.
