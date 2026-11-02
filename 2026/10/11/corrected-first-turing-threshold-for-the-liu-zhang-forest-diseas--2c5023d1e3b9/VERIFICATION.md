---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed exactly from the original p.3181 printed reaction equations and p.3182 2x2 modal matrix. Positive equilibrium requires I=(beta/mu)S-alpha; clearing denominators gives the claimed rational cubic. Exact discriminant is negative, and a sign change between 17 and 18 gives its sole real, physically positive root. Differentiating original f,g yields p1=0.01072598427642497, q1=-0.002735311206719895, p2=0.2745085518131537, q2=-0.01726468879328010; Delta=0.0005656855375808754, trace at k=0 is negative. With x=0.12*k^2*pi^2, det_k(eps)=eps*x*(x-q2)-p1*x+Delta and tr_k=-(1+eps)x+p1+q2<0 for eps>=0. Epsilon threshold phi(x)=(p1*x-Delta)/(x*(x-q2)) has derivative numerator -p1*x^2+2Delta*x-Delta*q2, with sole positive zero x=0.11350168081233263 < x1=1.184352528130723. Hence phi strictly decreases for all k>=1, proving k=1 is the first crossing as eps is reduced. At eps_c=0.00852879885272517358 trace is -1.20099233713 and determinant zero; at paper eps=0.0011360854, det=-0.0105208543113 and positive eigenvalue=0.008760101432708765. Source rounded formula separately evaluates to 0.009592999111777033. The reported equilibrium residuals are nonzero. Finite computations corroborate and are not used as the infinite modal proof.

## originality

PASS

Qualified best-of-knowledge PASS specifically for the correction/diagnosis of the published false numerical specialization, not for the general dispersion determinant or the elementary method. The original 2024 paper prints the reaction system, general determinant and rounded threshold formula, but declares the incompatible numerical crossing 0.0011360854 and incorrect positive equilibrium (17.252,236.374). Correctly enforcing the same equations gives distinct equilibrium and crossing; the original symbolic formula by itself is prior and is not claimed as new. Exact-value, DOI/erratum and alternative-terminology searches and relevant published-record comparisons did not identify an independent earlier correction. Lack of matches is not proof of absolute priority.

## value

PASS

The first spectral Turing crossing and positive equilibrium are the explicit reference values organizing a published disease–fire reaction–diffusion numerical example. The true threshold differs by factor about 7.51 from the reported value and the printed equilibrium has nonzero reaction residuals; the independent rounded-formula inconsistency further demonstrates a substantive scientific correction. This is a motivated source-specific boundary diagnosis, not simply another arbitrary sample of a known formula. Future readers reproducing or comparing its stability diagram need the corrected location and cannot rely on the published values. No claim is made of a general theorem, model validation, or patterned-branch dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
