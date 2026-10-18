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

Assuming the fixed positive lattice embedding q*:ell2->Y* from Costa--Miranda--Ribeiro with rho(q*u)=||u||+||Du|| and D(e_n)=n^-1 e_n, the norm on X1=(q*(ell2),rho) direct-sum-infinity R is max(rho(y),|t|). T(q*u,t)=u is norm one nonattaining. For each eps_k in (0,1) ->0, eventually eps_k<=1/2. Put delta_k=eps_k/(1-eps_k)<=1, bracket between adjacent diagonal levels 1/(m+1)<=delta<=1/m and choose alpha=(delta^2-(m+1)^-2)/(m^-2-(m+1)^-2). The nonnegative unit vector v=sqrt(alpha)e_m+sqrt(1-alpha)e_(m+1) has ||Dv||=delta and support m->infty. y=(1-eps)q*v then rho(y)=1, ||Ty||=1-eps. For finitely many eps>1/2 use v=e1, y=(1-eps)q*e1 of rho<1 and scalar t=1 to normalize; finite modifications do not alter cluster set. A scalar sequence t_k in [0,1] with arbitrary nonempty compact cluster set K exists via finite nets. Since supports escape, v_k weakly ->0 and bounded q* preserves this; rho is equivalent norm so weak topology agrees. Thus z_k=(y_k,t_k) weak cluster set exactly {0}xK, positive and normalized, with prescribed exact deficits. SymPy verified interpolation and rho normalization. This uses the specific focal space and operator; not a theorem about arbitrary operators.

## originality

PASS

The accessible Costa--Miranda--Ribeiro arXiv abstract states a positive nonattaining operator admitting one non-weakly-null positive maximizing sequence, rather than an explicit arbitrary joint rate/cluster classification. The full recent paper was inaccessible via arXiv and an authorized institutional attempt reported VPN disconnected; no further bypass was tried. Resultary returned the exact indexed claim plus different diagonal/weak-maximizing results without a confirmed stronger same-operator theorem. With named substantial source-access risk, originality is a best-of-knowledge judgment; no abstract-only whole-document noncoverage is asserted.

## value

PASS

The exact speed of near-norm-attainment and the weak limit-set geometry are natural independent features of weak maximizing-property counterexamples. For one fixed positive operator, the construction exhibits complete joint freedom for every null deficit profile and compact scalar cluster pattern without changing that operator or the positive lattice setting. This is a bounded structural analysis of an explicit natural witness, not a classification of all weak maximizing failures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
