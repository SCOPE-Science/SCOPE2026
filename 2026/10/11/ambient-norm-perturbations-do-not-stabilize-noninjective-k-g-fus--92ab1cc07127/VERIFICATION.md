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

The exact one-block complex Hilbert-space example meets the printed Definition 2.3 and every quantitative hypothesis of Huang--Yang Theorem 3.18. With K=P_{e1}, W_1=H, v_1=1, Lambda_1=K, Phi_1(x,y)=(x+delta*y,0), 0<delta<1, the unperturbed analysis energy equals ||K*f||^2=|x|^2 with A=B=1. The perturbation has exact ambient operator norm delta, so a=b=0,c=delta satisfies c/(1-a)<sqrt(A)/||K^dagger||=1. Yet f_delta=(-delta,1) belongs to ker Phi_1 while K*f_delta=(-delta,0) is nonzero; the asserted lower bound (1-delta)^2 delta^2>0 contradicts its zero right side. Sympy reconstructed the matrices and exact polynomial; no numerical extrapolation. Under W_j subset R(K), all analysis terms depend only on g=P_{R(K)}f, and the valid closed-range identity g=(K^dagger)^*K^*g establishes ||g||<=||K^dagger|| ||K^*g||. The perturbation triangle inequality then gives the repaired lower bound, while the usual upper triangle bound is unconditional.

## originality

PASS

Best-of-knowledge source-specific originality: no genuinely independent inspected source proves that Huang--Yang 2020 Theorem 3.18 fails for every arbitrarily small ambient-norm bound with noninjective closed-range K, nor establishes the stated W_j subset R(K) repair of that exact printed constant. The necessary kernel inclusion and Moore--Penrose projection identity are classical and not themselves claimed original. The target paper explicitly distinguishes its c||K^*f|| theorem from the false c||f|| theorem. A broader K-g-frame predecessor and Xiang correction paper remain unread at theorem level and are priority risks; their inaccessibility is neither proof of noncoverage nor automatic O-failure. Resultary exact match is assigned finding itself and does not constitute an independent prior.

## value

PASS

A source-specific correction to a published quantitative stability theorem is mathematically motivated: the assertion fails not only at a sharp constant but for every arbitrarily small c=delta>0, so no ambient operator-norm threshold of the printed form protects noninjective K when null directions may enter the perturbed analysis. A two-dimensional exact construction exposes a structural kernel-inclusion obstruction, and the W_j subset R(K) condition repairs the printed lower frame bound for the general closed-range problem. The Moore--Penrose identity and triangle estimate are standard, so value is credited to the precise theorem-level falsification plus valid scoped repair, not to novelty of the elementary linear algebra. No false claim of an optimal or necessary range restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
