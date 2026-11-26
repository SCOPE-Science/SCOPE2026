---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For σ,α,q,t>0, let B_q(t)=t^(−q)E[X^q 1_{X≤t}] and let G_a be the CDF of X. Conditioning on X and using P(Y≤u)=u^q for 0≤u≤1 gives S_Z=1−G_a+B_q, in agreement with the complement of the actual printed Proposition 2.4. The minus sign in the CDF is correct; the two minus signs in Corollary 2.1 (in the survival and in the hazard denominator after clearing positive factors) are not. Differentiation cancels the two density-at-t terms and gives f_Z=(q/t)B_q. Since the gamma upper tail is exponentially small and t^q B_q→C=(2σ)^qΓ(α/2+q)/Γ(α/2)>0, the correct S_Z and h_Z are asymptotic to Ct^(−q) and q/t, while the printed ones are asymptotic to their negatives. The heavy-tail conclusion of Proposition 2.5 is unchanged with the correct survival. Independent evaluation reproduces all nine SCHI Table 1 probabilities after rounding. For SCHI(1,3,1) at t=8, corrected survival and hazard are 0.36242334535 and 0.10913053882, versus −0.27039993397 and −0.14627020938 as printed. The printed survival crosses zero near 3.48777992429. Figure 2 explicitly labels that parameter choice as the black hazard and displays t=8 on a nonnegative hazard scale, inconsistent with the literal printed value; this does not identify the plotting implementation.

## originality

PASS

The correctly signed CDF and the quotient distribution are prior work, and the survival can be recovered directly from either. The supported distinct claim is the source-specific erratum: its two printed formulas disagree with its own Proposition 2.4 and give negative probabilities and hazards, while the actual table agrees with the repair. Neither the checked same-paper versions nor the bounded correction search disclosed an existing resolution of that discrepancy.

## value

PASS

This erratum prevents using a negative claimed reliability or hazard in the tail of a published model. It supplies the correct formulas, identifies their positive asymptotics and checks which published numerical evidence remains valid. The substantive impact is an invalid probability and hazard in the publication, not the routine algebra of taking a complement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
