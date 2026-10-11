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

Solving the equilibrium equations with \(x\ne0\) gives \(z=c/a\), \(xy=bc/a\), and \(x^2=bc^2/a^3\), hence the two isolated equilibria stated. Substitution in the Jacobian gives \(p(\lambda)=\lambda^3+(a+b)\lambda^2+(bc^2/a^2)\lambda+2bc^2/a\). For a cubic with all positive coefficients, the nontrivial Routh determinant is \((bc^2/a^2)(b-a)\): it is positive exactly for \(b>a\), while for \(0<b<a\) the first-column sign sequence has two changes, hence exactly two right-half-plane roots. At \(b=a\) direct multiplication gives \((\lambda+2a)(\lambda^2+c^2/a)\). At \((5,2,34)\) this cubic has no zero root, contradicting the source's printed local spectrum. The bundled verification directory was inspected; its computation is corroborative, while the all-parameter proof is exact Routh algebra.

## originality

PASS

The full primary article was read through its integer-order equilibrium section. It lists the same isolated equilibria and, at \((5,2,34)\), prints a spectrum containing a zero eigenvalue, then analyzes the separate equilibrium line. It does not give the exact isolated-equilibrium characteristic polynomial or the parameter-global boundary \(b=a\). Resultary search found the audited record itself and related equilibrium corrections for other flows, but no earlier theorem for this exact system. The correction and sharp classification are therefore original to the best of the inspected evidence.

## value

PASS

The theorem repairs a concrete published local-spectrum error and replaces a single incorrect numerical report with a complete sharp stability partition for both isolated equilibria over the full positive-parameter family. This directly affects interpretation of local dynamics in a system studied for chaos and fractional-order behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
