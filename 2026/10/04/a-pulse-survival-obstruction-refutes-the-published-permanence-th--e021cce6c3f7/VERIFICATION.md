---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Since \(rbx_1/(k_2+x_1)<rb\), pulse values satisfy \(x_2((n+1)T^+)\le qx_2(nT^+)\), \(q=(1-\omega)e^{(B+rb)T}\). Thus \(q<1\) forces extinction; when \(q=1\), eventual boundedness of \(x_1\) replaces \(rb\) by a strict smaller bound and again forces extinction. For the source biological parameters and \((\gamma,\omega,T)=(0.1,0.5,0.01)\), all printed Theorem 3.8 hypotheses hold, \(T_{\max}=0.005246815758790803\ldots<T\), but \(q=0.608567660439097\ldots<1\).

## originality

PASS

The primary theorem asserts permanence under the listed hypotheses but omits the necessary pulse-survival multiplier. Targeted searches found no erratum, correction, or earlier counterexample to this exact theorem; related impulsive predator-prey papers concern different systems.

## value

PASS

An exact counterexample to a published permanence theorem is a motivated correction, and the general pulse-survival obstruction explains the failure mechanism beyond the single parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
