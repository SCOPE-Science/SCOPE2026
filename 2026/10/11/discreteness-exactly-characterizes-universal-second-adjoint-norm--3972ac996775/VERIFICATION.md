---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For discrete K, C0(K) is isometric to c0(K); Dantas–Jung–Martín Remark 3.5 proves universal second-adjoint norm attainment, with finite-dimensional K elementary. If t_n are distinct converging to p, regular locally compact nested annuli and compactly supported pairwise-disjoint bumps psi_n, plus a cutoff h identically one near p, construct E:c→C0(K), Ea=a_infty h+sum(a_n-a_infty)psi_n and Rf=(f(t_n)). The supports and continuous convergence give ||E||=||R||=1 and RE=I. On c the explicit Dantas-type operator with u=sum 2^-j e_j and b_n=(e_{n+1}-e_{n+2})/2 has adjoint columns Se_1=u/2 and Se_{n+1}=u/2+b_n/2. Exact l1 norms are 1-2^-(n+2), approaching 1, while the bidual is nonattaining: any ζ attaining upper bound must satisfy |ζ(u)|=1, forcing all coordinates the same sign and ζ(b_n)=0, reducing all S* columns below norm one. Transfer A=ETR and RE=I force norm attainment of T** if A** attained, contradiction. First-countability of nondiscrete K produces such sequence. Independent exact rational column checks succeeded n=1..60; the infinite proof uses exact column formula and convexity.

## originality

PASS

The c0 positive theorem and c negative example are acknowledged prior work. The new statement is their precise topological dichotomy for every nonempty first-countable locally compact C0(K), with explicit norm-one convergent-sequence retract and preservation of the second-adjoint obstruction.

## value

PASS

The broad C0(K) function-space class has a natural topological variable; a clean discreteness iff universal operator property is a meaningful characterization. The norm-one transfer identifies the exact topological obstruction and also supplies the more general non-first-countable sufficient obstruction whenever a convergent sequence exists.

The dated certificate retains the supplied scientific assessment, sources and limitations.
