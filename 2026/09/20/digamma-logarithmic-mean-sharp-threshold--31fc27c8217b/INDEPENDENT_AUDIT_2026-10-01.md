# Independent audit — 2026-10-01

## Final claim

The two best endpoint constants in Matejíčka's digamma logarithmic-mean problem coincide at the unique positive zero \(\alpha_0\) of \(5\psi'(x)+3x\psi''(x)=0\): the expression is negative for \(0<a<b\le\alpha_0\) and positive for \(\alpha_0\le a<b\).

## Correctness — PASS

Writing \(b=at\) reduces the inequality to the normalized function \(U(a,t)\). The published strict increase of \(U\) in \(a\) reduces the region \(at\le\alpha_0\) to the boundary \(a=\alpha_0/t\). The published sign \(5\psi'(x)+3x\psi''(x)<0\) below \(\alpha_0\) implies logarithmic growth greater than \(2/3\) for \(x\psi'(x)\) when moving toward zero, which compares the two adjacent logarithmic digamma increments by a factor greater than \(t^{1/3}\). The elementary logarithmic-mean coefficient inequality gives the opposite coefficient ratio strictly below \(t^{1/3}\), so the boundary value is negative. Alzer--Kwong's large-parameter theorem gives the opposite side and sharpness. Independent high-precision evaluation reproduces the stated root near \(0.56155939968\) and representative signs on both sides.

Checked sources:
- L. Matejíčka, Notes on three conjectures involving the digamma and generalized digamma functions, Journal of Inequalities and Applications 2018:342, full article inspected.
- H. Alzer, M. K. Kwong, Mean Value Inequalities for the Digamma Function, Analysis Mathematica 49 (2023), full text inspected.
- Published-record and web searches for the exact Matejíčka endpoint problem and the equation defining the transition constant.

Residual risks:
- The Alzer--Kwong monotonicity and sign lemmas are used as published inputs rather than reproved from first principles.

## Originality — PASS

Best-of-knowledge originality passes. Matejíčka explicitly asks for both best endpoint constants. Alzer--Kwong determine the large-parameter endpoint and provide the structural lemmas used here, but the inspected full text does not supply the complementary all-small-parameter inequality. Searches for the exact threshold equation and problem formulation found no earlier statement identifying the missing endpoint with the same transition constant.

### Equivalent formulations

Searches:
- Search for Matejíčka Open Problem 2 with both endpoint constants
- Search for the defining equation \(5\psi'(x)+3x\psi''(x)=0\) together with the logarithmic mean

Evidence:
- Matejíčka states the unresolved endpoint problem.
- Alzer--Kwong identify the same transition constant for the large-parameter direction.

Reasoning: The audited result is equivalently the sharp determination of the missing small-parameter endpoint.

### Broader coverage

Searches:
- Matejíčka 2018 full article
- Alzer--Kwong 2023 full text

Evidence:
- Matejíčka proves only a smaller small-parameter range.
- Alzer--Kwong prove the sharp reversed inequality above the transition and the monotonicity/sign ingredients.

Reasoning: Neither inspected theorem dominates the new small-side endpoint; together they motivate but do not imply it without the additional adjacent-scale comparison.

### Exact database or table

Searches:
- Exact-threshold web and published-record searches
- Numerical root checks

Evidence:
- No independent published exact endpoint value was located.
- Numerics only confirm the constant and cannot establish the global inequality.

Reasoning: This is a global analytic inequality rather than a table lookup; finite or numerical evidence is not a novelty or correctness substitute.

### Claim versus prior implication

Searches:
- Alzer--Kwong monotonicity/sign lemmas versus audited boundary argument
- Matejíčka stated bounds

Evidence:
- The known lemmas reduce the problem but do not themselves compare the two logarithmic increments with the required coefficient ratio.
- The additional logarithmic-growth and elementary mean inequality close that gap.

Reasoning: The missing endpoint is not a mechanical restatement of the large-parameter theorem; a separate argument is required.

### Source inspections

- **Notes on three conjectures involving the digamma and generalized digamma functions** — Defines the target problem and does not solve the sharp endpoint. Material read: Full primary article, including Open Problem 2 and the previously proved small-parameter range. Evidence: The paper asks for the largest small-side endpoint and the smallest large-side endpoint.
- **Mean Value Inequalities for the Digamma Function** — Covers the sharp large-side endpoint and ingredients, but not the audited small-side theorem. Material read: Full relevant primary text, including the transition sign lemma, monotonicity result, and large-parameter theorem. Evidence: The inspected theorem gives positivity above the transition; the audited proof supplies negativity below it.

Checked sources:
- L. Matejíčka, Notes on three conjectures involving the digamma and generalized digamma functions, Journal of Inequalities and Applications 2018:342, full article inspected.
- H. Alzer, M. K. Kwong, Mean Value Inequalities for the Digamma Function, Analysis Mathematica 49 (2023), full text inspected.
- Published-record and web searches for the exact Matejíčka endpoint problem and the equation defining the transition constant.

Residual risks:
- A differently phrased or poorly indexed prior resolution of the small-parameter endpoint remains a best-of-knowledge risk.
- The theorem does not classify the sign throughout the mixed region crossing the threshold.

## Scientific value — PASS

The theorem completes a named sharp-constant problem by showing the two endpoint constants coincide at the natural transition. The proof isolates a reusable logarithmic-growth comparison for digamma increments rather than merely extending a numerical bound.

Checked sources:
- L. Matejíčka, Notes on three conjectures involving the digamma and generalized digamma functions, Journal of Inequalities and Applications 2018:342, full article inspected.
- H. Alzer, M. K. Kwong, Mean Value Inequalities for the Digamma Function, Analysis Mathematica 49 (2023), full text inspected.
- Published-record and web searches for the exact Matejíčka endpoint problem and the equation defining the transition constant.

Residual risks:
- A differently phrased or poorly indexed prior resolution of the small-parameter endpoint remains a best-of-knowledge risk.
- The theorem does not classify the sign throughout the mixed region crossing the threshold.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
