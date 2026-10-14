---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For any finite row generator Q, s=h/2 and R=(I-sQ)^-1, the exact Cayley identity gives C_h=2R-I. I-sQ is a nonsingular M-matrix so R>=0 and R1=1, hence all offdiagonals of C are nonnegative and C>=0 iff each R_ii>=1/2. For irreducible reversible Q, symmetric similarity yields R_ii=pi_i+sum_(k>=1)u_ki²/(1+s lambda_k), strictly decreasing from 1 to pi_i when n>1. Unique crossings occur precisely for pi_i<1/2, defining a sharp interval 0<=h<=h*. Positive-mixture spectral bounds imply 2/[lambda_max(1-2pi_i)]<=h_i<=2/[lambda_min(1-2pi_i)]. The irreducible resolvent limit R->1pi^T rules out all-step positivity for n>=3; direct two-state inversion gives h*=2/|a-b| unless a=b, and a complete-graph spectral projection yields 2/[c(n-2)] for n>=3. Independently checked exact rational two-state and complete graph sizes 3,4,6,10. No finite check is used to infer universal proof.

## originality

PASS

The Cayley identity itself is already explicit in Fallat--Tsatsomeros Lemma 2.2, and Horváth develops worst-case Runge--Kutta positivity-radius theory; neither is claimed as new. The final claim concerns exact one-generator Markov end-step positivity and derives diagonal return tests, an irreducible reversible spectral single-crossing law, statewise spectral bounds and unconditional-chain classification. These fixed-generator consequences have not been found as one prior implication from available primary portions, but the 1998 Horváth full paper was inaccessible and institutional retrieval safety-blocked; Fallat complete text was not retrieved. Best-of-knowledge O PASS with MATERIAL residual risk; do not misstate these as full-text noncoverage.

## value

PASS

A second-order A-stable time step applied to a Markov generator need not preserve probabilistic nonnegativity. An exact per-generator threshold and one-interval criterion on reversible chains are useful for positive-step selection, distinct from generic worst-case sufficient radii. The balanced two-state and complete-graph formulas are motivated complete classifications, not arbitrary small numerical slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
