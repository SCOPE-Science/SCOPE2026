---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The reset sign process flips at independent thinned Poisson rate eta*r in addition to intrinsic gamma; future sign correlations decay with beta=2(gamma+eta*r). I independently derived M=E[Xsigma] from the jump generator: M'=v-(2gamma+r)M+r(1-2eta)J/t, J'=M-beta*J, J(0)=0. The boundedness argument gives J=O(1) and M=v/(2gamma+r)+O(t^-1). For V=E[X^2], V'=2vM-rV+r H/t, H'=V. With Y=H/t the exact quadrature Y'=e^{-rt} t^{-2} integral_0^t s e^{rs}(2vM(s))ds yields Y'=2v^2/[r(2gamma+r)t]+O(t^-2), and integrating gives the log law and finite C_eta. Independent one-reset event integrals yield -7r/18 for unchanged sign, -13r/18 for reversed sign; the single intrinsic tumble gives -2gamma/3. Thus the t^3 coefficient, invertible parameter formulas and eta independence are exact. A new numerical integration of the moment equations at eta=0,.25,.5,.75,1 and exact rational one-event checks corroborated the derivation. The all-t asymptotic follows from the integral equation, not numerics.

## originality

PASS

Best-of-knowledge PASS for the exact split-state history-reset kernel, eta-independent logarithmic MSD and three-parameter moment identification. Boyer–Majumdar copies position AND historical orientation, Evans–Majumdar reverses orientation at fixed-position reset, and Mailler–Uribe Bravo copies the whole Markov state. These published operators are not parameter reparametrizations of sampling historical position while retaining/flipping current velocity. The most relevant Boyer–Majumdar full manuscript remained inaccessible; only abstract and available model statements were read, so residual coverage risk is retained.

## value

PASS

The theorem distinguishes a physically motivated reset protocol from history-state copying, showing a nontrivial universality of the dominant logarithmic spreading despite eta-dependent transient variance. It also derives exact population-moment identifiability of three kinetic parameters, supplying a concrete reason for the subleading short-time calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
