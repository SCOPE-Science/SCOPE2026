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

# Verification notes

The main proof is mathematical rather than computational: stationary cycle flux, renewal-reward variance, five scalar resolvent equations, a vanishing directed-tour feedback term, and a completed-square amplitude inequality establish the claim for all allowed asymptotic frequencies and all nonzero real amplitudes.

A standalone standard-library program, `verify.py`, was executed against the accompanying formulae and printed `PASS: 165 exact-rational groups; limiting ratio 12/5, efficiency lower bound 7/12`. It constructs exact finite-state resolvents through rational elimination, checks the analytic stationary spectrum expressions at rational parameters, and confirms the sum-of-squares inequality over rational test values. The particularly important exact identities are

\[
G_\varepsilon(0)=\frac{10\varepsilon(15\varepsilon^2+20\varepsilon+7)}{(3\varepsilon+2)^3}
\]

and the nonzero-frequency rational expression in `RESULT.md` with \(\omega=\sqrt\varepsilon\).

The program and finite tests cannot themselves prove the infinite limiting statement, disprove all possible alternative literature coverage, or determine the unrestricted five-state optimum. The singular limit and global lower-bound implication are established in the analytical proof. No independent audit or mathematical certification has been performed.
