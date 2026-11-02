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

# Verification and scope
The proof uses exact polynomial congruences and induction. In the \(t=2\) case, the residue is \((b-1)^2+1\in(0,D)\). In the \(t\ge3\) case, \(1\le u\le y/3\) and the representative \(R\) lies in \((D,2D)\). No computational exhaustion over infinite parameters is asserted.

Run the standalone Python-standard-library checker as `python verify.py`. Actual execution outcome: `VERIFY_OK integer_base_cases=464 remainder_bounds=348 initial_quotients=[(2, 5), (3, 5)]`.

The finite checks evaluate all integer bases from \(2\) through \(59\), all eight exponent parameters from \(t=1\) through \(t=8\), residue congruences and interval bounds; selected direct divisor-sum identities are independently reconstructed. Tests are supporting evidence only.

The cited first public source was submitted in December 2013; no independent audit or external proof certification has been performed.
