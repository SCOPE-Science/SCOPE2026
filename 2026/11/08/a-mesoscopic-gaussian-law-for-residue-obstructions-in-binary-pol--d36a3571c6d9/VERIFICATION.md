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

# Reproducibility and proof verification

Execute `python3 VERIFY.py` with Python 3 and the standard library. The program independently implements binary-polynomial quotient/remainder, multiplication, finite-field inverses, derivatives, and traces. It enumerates every monic degree-10 polynomial to compare the two distinct prime-local simple-pole indicators, using \(P=T^2+T+1\) and \(Q=T^3+T+1\). It computes the exact joint counts \((0,0):840\), \((0,1):56\), \((1,0):120\), \((1,1):8\), agreeing with independent probabilities \(1/8\) and \(1/16\). It also checks the double-pole trace calculation for all admissible monic completions of degrees 4 and 6, with trace-one counts 6/12 and 28/56. Exact irreducible-polynomial counts for several degrees and a numerically convergent product for the constant \(\mathfrak C\) are evaluated independently.

The scientific proof does not depend on finite enumeration: the crucial universal steps are the source's prime-local trace balance; the dependence of local residues on finite prime-power jets; the exact Chinese remainder sampling condition \(2E\sum_{2\le\deg P\le B}\deg P<d\); the total-variation union/coupling bound \(7d^{-2}\); and the standard irreducible polynomial count plus Berry–Esseen. Each of these steps is explicitly justified in `RESULT.md`.

Finite verification does not certify that all-degree asymptotics hold, establish historical priority, or resolve the unresolved criterion for positive orthogonal multiplicity. No independent audit has been performed.
