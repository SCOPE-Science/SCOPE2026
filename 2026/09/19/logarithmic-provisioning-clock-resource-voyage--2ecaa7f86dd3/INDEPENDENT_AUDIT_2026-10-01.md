# Independent mathematical audit — Logarithmic provisioning clocks and finite consumption capacity in a resource-coupled mortality model

Audited on 2026-10-01 UTC.

**Disposition:** PASSED

## Correctness — PASS

For \(S=h+i\), \(S'=-\mu h-\delta i\le-mS\) gives \(S(t)\le e^{-mt}\) and \(q(t)=c_1h+c_2i\le c_+e^{-mt}\). The exact integrating-factor identity \(p(t)=p_0e^{-\rho t}-R(t)\) then gives the unique threshold equation and \(R(t_c)\to0\) as \(p_0\to\infty\), proving the logarithmic clock. When \(\rho=0\), total consumption is at most \(c_+/m\). In the large-buffer limit \(\lambda(p)=\alpha+O(p_0^{-1})\) uniformly; dominated convergence reduces the integrated health dynamics to the constant-coefficient \(2\times2\) system, whose inverse gives \(\int h=(\gamma+\delta)/D\) and \(\int i=\alpha/D\). This reconstructs the claimed \(J_\alpha\).

## Originality — PASS

The source paper reports an approximately linear finite-window critical-time dependence. The audited theorem gives the opposite large-buffer asymptotic structure of the same equations: logarithmic growth for \(\rho>0\), finite total consumption for \(\rho=0\), and an explicit limiting consumption constant. Resultary and source-specific searches found no earlier statement of this source-specific asymptotic correction.

### Equivalent formulations

The result is not a rephrasing of the paper's numerical observation; it distinguishes finite-window behavior from the true \(p_0\to\infty\) regime.

Evidence: Resultary's matching hit was this record; no earlier equivalent source-specific theorem appeared. The source abstract states an approximately linear dependence rather than the audited asymptotic law.

### Broader coverage

Standard comparison and integrating-factor tools are prior, but no found theorem applies them to give the precise source-specific conclusion.

Evidence: The source studies the transient model and reports linear-looking critical time; no broader theorem covering the logarithmic/finite-consumption dichotomy was located.

### Exact database or table

The claim is analytic rather than table-based; exact publication-database checks were performed.

Evidence: No independent database/table entry with \(J_\alpha\) or the large-buffer clock was found.

### Claim versus prior implication

The proof uses standard ODE facts, but the scientific statement is a motivated source-specific boundary/counterexample rather than a mechanical restatement of a prior theorem.

Evidence: The source's finite-window linear observation does not imply the large-buffer logarithmic theorem; indeed the audited result limits its extrapolation. The related Syracuse model does not supply the same resource equation and threshold conclusion.

### Source inspections

- **The dynamics of early transoceanic voyages: A resource-coupled model of crew health and survival** — NOT_COVERING for the asymptotic theorem; source reports an approximately linear finite-window dependence.. Material read: Abstract plus the exact ODE, threshold definition, and source interpretation reproduced in the assigned package. Evidence: The abstract explicitly says the critical provisioning time has an approximately linear dependence on initial resource buffer.
- **Modeling the Siege of Syracuse: Resources, strategy, and collapse** — NOT_COVERING for the voyage-model large-buffer theorem.. Material read: Bibliographic/abstract-level context as cited by the package. Evidence: No source-specific provisioning threshold theorem for arXiv:2609.20430 was identified.

### Checked sources

- arXiv:2609.20430
- arXiv:2504.01649
- Resultary published findings

### Residual risks

- Because the source preprint is recent, unindexed follow-up analysis may exist.
- The theorem concerns the deterministic model only and should not be read as a historical-calibration result.

## Scientific value — PASS

The theorem identifies a sharp structural dichotomy in a published model and corrects the interpretation of a reported scaling law outside its finite numerical window. This is a motivated boundary/counterexample with an exact asymptotic constant, not an arbitrary exercise.

## Limitations

- The theorem concerns the deterministic model exactly as written and a fixed positive threshold.
- The numerical integrations are corroboration only; the proof is analytic.
- No claim is made about historical realism or calibration.
