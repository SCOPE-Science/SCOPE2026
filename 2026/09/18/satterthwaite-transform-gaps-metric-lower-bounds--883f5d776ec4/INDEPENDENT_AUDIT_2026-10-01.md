---
audit_date: 2026-10-01
status: repaired
---

# Scientific audit

## Final claim

For a sum of independent Gamma variables and its first-two-moment matched Gamma law, scale heterogeneity forces a strict global Laplace-transform gap \(L_S(s)<L_U(s)\) for every \(s>0\), with \(\log(L_U/L_S)\ge A V_\beta s^3/[3(1+sM)^3]\); this yields explicit lower certificates in the \(d_1\) and \(d_2\) smooth metrics. The previously claimed all-order cumulant domination and positive-MGF comparison are removed from the novelty claim because prior literature already implies them.

## Correctness — PASS

Writing \(g_s(x)=\log(1+sx)/x=\int_0^s(1+ux)^{-1}du\), one has strict convexity and \(g_s''(x)\ge 2s^3/[3(1+sM)^3]\) for \(x\le M\). Jensen and strong convexity therefore give the stated Laplace order and quantitative gap. The test functions \((1-e^{-sx})/s\) and \(e^{-sx}/s^2\) have first- and second-derivative bounds one, respectively, yielding the metric lower certificates. Equality at one positive Laplace parameter forces all scales equal by strict Jensen. No finite experiment is needed.

**Checked sources.** frozen assigned RESULT.md; Bailly et al. arXiv:2609.17880; Mountain–Sherlock, Biometrics 2022, DOI 10.1111/biom.13447

**Residual risks.** None found for the repaired analytic inequalities.

## Originality — PASS

Mountain and Sherlock already prove that the moment-matched Gamma has no larger cumulants of every order at least three than the independent-Gamma sum; their theorem also makes the package's positive-MGF direction mechanically non-novel. Those parts are explicitly removed. Searches did not locate the repaired negative-axis Laplace order, its quantitative size-biased-scale-variance lower gap, or the resulting \(d_1/d_2\) lower certificates.

### Equivalent formulations

The repaired claim is a negative-transform convexity order, not the already-known positive cumulant hierarchy.

### Broader coverage

No checked broader theorem was found to imply the general varying-shape, moment-matched repaired statement.

### Exact database or table

There is no standard table; the relevant database check is theorem-level semantic coverage.

### Claim versus prior implication

The final claim survives after deleting the covered positive-transform material.

**Checked sources.** https://onlinelibrary.wiley.com/doi/full/10.1111/biom.13447; https://arxiv.org/abs/2609.17880; https://doi.org/10.1214/14-EJS914; Resultary search

**Residual risks.** Covo–Elalouf full text remained inaccessible; an unnoticed related transform inequality is the main residual risk.

## Value — PASS

The repaired claim gives a signed global transform obstruction and computable lower bounds in the same smooth metrics used by current Gamma-Stein upper-bound work. This is a motivated diagnostic of when Satterthwaite approximation cannot be exact or arbitrarily close, not merely a restatement of the known cumulant hierarchy.

**Residual risks.** The certificates are not claimed optimal and do not yield a Kolmogorov lower bound.

## Disposition

REPAIRED. Acceptance requires PASS on correctness, originality, and value.
