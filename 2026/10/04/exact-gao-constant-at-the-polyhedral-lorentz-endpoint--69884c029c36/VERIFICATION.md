---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For \(N_\omega(s,t)=\max\{|s|,|t|\}+\omega\min\{|s|,|t|\}\), the absolute-norm comparison bound at Gao exponent two gives \(c'_{NJ}\ge(M_1M_2)^{-2}\). On \(0\le t\le1/2\), direct Cauchy--Schwarz gives \(M_1=\sqrt{1+\omega^2}\). With \(u=t/(1-t)\), differentiating \(\sqrt{1+u^2}/(1+\omega u)\) shows \(M_2=\max\{1,\sqrt2/(1+\omega)\}\). Independent symbolic substitution of the two proposed unit-vector pairs gives the two branch values exactly, and their equality reduces to \(\omega=\sqrt2-1\).

## originality

PASS

The open 2022 primary article treats the same two-dimensional Lorentz family in its displayed Lorentz example only for exponent \(r\ge2\); the audited theorem is the polyhedral endpoint \(r=1\). Targeted searches and Resultary returned the assigned endpoint formula but no earlier exact endpoint source. The prior comparison theorem supplies the lower bound but equality here additionally requires the two branch-specific extremizers.

## value

PASS

The case \(r=1\) is the natural polyhedral boundary of the Lorentz family adjacent to the published \(r\ge2\) calculations. The exact answer has a genuine phase transition in extremizing geometry at \(\sqrt2-1\), making it a useful structural endpoint benchmark rather than a cosmetic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
