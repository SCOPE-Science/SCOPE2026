---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The central frozen coefficient is correct, but its categorical scope statement denying uniform remainder bounds as nontrap weights tend to zero is false. The complete corrected claim and proof are in /workspace/repairs/4/RESULT.md. On the three-dimensional bright block a nondecaying vector would have trap amplitude zero, then B-uniform amplitude zero by the trap row, then A'-uniform amplitude zero; hence the zero Liouvillian eigenspace consists exactly of dark-dark matrices and is semisimple. At positive class rates, zero real dissipation forces a diagonal eigenoperator with zero trap entry; vanishing off-diagonal commutator along every edge forces zero. The compressed dephasing is negative definite (no nonzero site-diagonal dark-dark matrix), and sends Q_A and Q_B to -alpha Q_A/k and -beta Q_B/n. The Schur inverse gives the coefficient by self-adjointness and yields the stated localization, pairwise difference and bright-only criteria, including k=1. For the repair, exact dark-population balance writes q'_t=L_br q_t-d'_A F_a-d'_B F_b for the compressed bright density. Integration gives -L_br^{-1} applied to q_0+d_A(0)F_a+d_B(0)F_b, positive of trace one. Integrating the dark balances gives the remainder as its integrated bright diagonal weighted by (1,k,n). Invertibility at zero noise then gives a uniform bound for small epsilon over bounded weights without a positive lower bound, while absorption still requires the stated positive-rate hypotheses. In 24 independent numerical comparisons varying sizes, rates (one or both small), and strengths, the full integrated solution minus the singular term agreed with the bright-resolvent remainder to max absolute error 1.23e-8 (python /workspace/independent_checks.py 4). This diagnostic does not prove the perturbative or uniform statement.

## originality

PASS

The supported distinct contribution is the explicit two-weight coefficient for every coherent or mixed state on K_(m,n), and the checked repair retains it and gives a rate-uniform remainder by a bright compression. Related same-day results on cycles and stars establish overlapping techniques, not this graph and coefficient. Later bipartite records materially cover localized or uniform-mixture special cases at equal rates, but do not cover arbitrary input coherence or independent rates. No priority assertion is based solely on dates.

## value

PASS

The exact functional of coherent initial conditions and two independent rates distinguishes states with identical site populations and puts a quantitative clock on each dark sector of a natural network. It is not supplied by coherent capture probabilities or localized equal-rate data. The corrected remainder estimate also separates the genuine singularity from the bounded transient when either class dephases far more slowly than the other.

The dated certificate retains the supplied scientific assessment, sources and limitations.
