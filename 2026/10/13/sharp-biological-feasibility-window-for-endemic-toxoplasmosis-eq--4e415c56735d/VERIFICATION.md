---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the sharp endemic-feasibility window

The scope is the four-equation reduced system (2) of Ouyadri, El Koufi and Belhdid, treated as a stand-alone ODE. The result uses the physical cat constraint \(S+I\leq1\) and \(V=1-S-I\). The unreduced equations (1) are not asserted to conserve cat totals.

**Algebraic verification.** Write \(d=\alpha-\mu t_1\) and \(H=\alpha+\mu(1-t_1-t_2)\). At an equilibrium with \(I>0\), the environmental and infection equations uniquely force \(O=kI/\mu_0\), \(S=d\mu_0/(\beta k)\), and the susceptible-mouse equation forces \(M=0\). The first equation then forces \(I=[\mu-(\mu+\gamma)S]/H\). Substituting these expressions gives four zero residuals. The derived vaccinated/recovered fraction is \(V=[a+(\gamma-a)S]/H\), with \(a=\alpha-\mu(t_1+t_2)\). The strict-infection threshold \(\beta_c\), the upper biological threshold \(\beta_{\max}\), their strict ordering, and endpoint equality are obtained by comparing signs of these two rational expressions under the stated domain assumptions. No root is discarded without checking its positivity.

**Boundary verification.** On the faces of the physical region, \(S'\), \(I'\), \(O'\), and the mouse flow point inward or tangent. The recovered/vaccinated face has outward derivative precisely when \(\gamma S+aI<0\). It is never outward if \(a\geq0\), and it is strictly outward at \((S,I,V)=(0,1,0)\) if \(a<0\). This establishes the if-and-only-if forward-invariance criterion; it is not a claim of global stability.

**Reproducible finite checks.** Extract the embedded `verify.py` alongside this file and run `python verify.py` with Python 3. The verifier uses only `fractions.Fraction`, evaluates every printed right-hand side exactly at the rational equilibrium witnesses, checks the vanishing residuals and the physical and unphysical endpoints, and prints `VERIFY_OK` on success. The checker was executed in the package working directory and returned `VERIFY_OK`. Exact rational tests check explicit witnesses but cannot prove the quantified general theorem; the proof above and in RESULT.md supplies the parameter-uniform argument.

**Limits.** No stability or convergence theorem is tested or claimed. The normalization from the unreduced system (1) is not justified by this theorem. The source article's first public date uses a day-stamped author posting; an earlier undated publisher posting remains possible. No independent scientific audit has been carried out.
