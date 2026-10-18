---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For coherent resonant trimer H with couplings J1,J2>0, Lindblad sink L=sqrt(kappa)|vac><1| with kappa>0, and initial |3>, Q=-iH-kappa|1><1|/2 has Re all eigenvalues<0: equality of dissipative energy forces zero first component then via positive links all vanish. Thus survival integral Gramian X is uniquely defined and solves Q^*X+XQ=-I. Substitution of explicit 3x3 Hermitian X yields tau=X33=kappa/(2J1^2)+(2J2^2/J1^2+J1^2/J2^2)/kappa. Set x=J1^2/J2^2 and E=J1^2+J2^2; AM-GM minimizes over kappa, leaving (x-2)^2(2x+1)/(2x^2)>=0, equality iff x=2. Hence J1^2=2E/3,J2^2=E/3,kappa=2sqrt(E), tau=3/sqrt(E). Equal links give tau=2sqrt(3)/sqrt(E). Independent SymPy verified all nine symbolic Lyapunov entries and exact factorization; endpoints x->0,infty diverge. No optimizer outside positive coupling domain or other cost class claimed.

## originality

PASS

The uniform-coupling opposite-end trapping-time formula (Zhang et al. 2017 Eq17 for clean linear N-site chain) and optimizing a single sink rate are prior facts; at N=3 it yields the equal-link benchmark. Riberi 2026 treats a semi-infinite absorbing walk, not independently adjustable two finite links. No inspected primary result solves the same unconstrained J1,J2,kappa joint optimization at fixed sum of squared couplings. Prior Lyapunov inversion itself is classical and not claimed novel.

## value

PASS

Given the natural quadratic Frobenius hopping resource, allocating strength toward the absorbing endpoint and tuning the sink together is a concrete minimum-first-passage optimization. Its unique fully analytic solution beats equal couplings by ~13.4%, a reproducible design benchmark even for a small canonical graph; no longer-chain or general cost optimality is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
