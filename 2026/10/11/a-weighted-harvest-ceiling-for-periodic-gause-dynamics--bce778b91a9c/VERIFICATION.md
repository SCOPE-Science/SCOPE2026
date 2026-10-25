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

Directly reconstruct q=s/p and Phi=x+q y: the Holling-III term s x²/(x²+a²)y cancels against q p x²/(x²+a²)y exactly; the product-rule term is +qdot*y, so Phi_dot=G-H1-qH2-q b y²-(q c-qdot)y. A T-periodic Phi has mean derivative 0. For every u>=0 and 0<m<K the cubic G has unique positive global maximum at u*=(K+m+sqrt(K²-Km+m²))/3; equality in the harvest-only ceiling is impossible for any strictly positive periodic solution because q b y²>0 and eta y>=0. Theta=min qb>0 and eta_L=min eta>=0 together with Jensen yield theta (mean y)^2+eta_L mean y<=Delta; solving gives the stated quadratic-root bound. Hypotheses and quantifiers, including strictly positive cycles only, are consistently stated.

## originality

PASS

Best-of-knowledge narrowly scoped PASS for the particular source-vector-field periodic formula and joint-harvest/mean-predator conclusions. The classical weighted biomass cancellation and absolute maximum production bound ARE prior methods; they are NOT claimed as novel. The exact Yu–Liu–Lin theorem addresses multiple positive-cycle existence and does not state the necessary variable-conversion-ratio q=s/p weighted budget. Etoua–Rousseau has a weaker autonomous prey-only-harvest structural predecessor and Wang 2020 exhibits the classical analogous weighted-total-population technique. No inspected prior theorem with assumptions that dominate periodic positive coefficients, differentiable q, Allee factor, dual harvesting, predator competition and eta=qc-qdot>=0 was shown to entail all three submitted statements. A same-source theorem may still be an unindexed consequence of standard bioeconomic energy-budget theory; no exhaustive priority certification.

## value

PASS

A source-motivated and mathematically useful necessary nonexistence test: the original Yu–Liu–Lin paper establishes positive-cycle existence regimes but does not give a combined prey-and-predator harvest obstruction. The proven joint-harvest inequality is strictly stronger than the immediate prey-only bound for positive H2 and remains checkable for arbitrarily varying positive periodic coefficients with qdot compensated by mortality. The nontriviality is demonstrated by K=3,m=1,r=1,q=1,H1=1/5,H2=3/5: H1 lies below the exact maximal G=(20+14 sqrt(7))/81, but H1+q H2=4/5 exceeds it, so the new test excludes locked cycles although prey-only MSY does not. The explicit predator-mean root adds genuinely quantitative control. These are narrow, motivated harvest-management quantities, not arbitrary parameter slices, despite a short elementary proof; neither novel weighted cancellation in general nor global sharpness is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
