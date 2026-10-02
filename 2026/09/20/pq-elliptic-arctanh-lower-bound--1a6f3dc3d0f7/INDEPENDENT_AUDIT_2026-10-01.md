# Independent mathematical audit — 2026-10-01

## Final claim assessed

A stronger lower bound for complete (p,q)-elliptic integrals

## Correctness — PASS

PASS. After the standard zero-balanced hypergeometric normalization, coefficient monotonicity in \(a=1-1/p\) reduces \(p\ge2\) to \(a=1/2\). The endpoint logarithmic-derivative estimate for \(B_{1/2}\) transfers coefficientwise to \(b=1/q\le1/2\). Substituting this estimate into the Riccati equation gives a strictly negative residual for the comparison exponent \(d=(1+b)/2\); a first-crossing argument then proves the claimed power inequality. The key algebraic residual was independently symbolically reduced to \(b^2/2-dH_b/2\), confirming the sign mechanism.

## Originality — PASS

PASS to the best of current knowledge. Dou--Yin--Lin's complete 2019 article explicitly poses the weaker target inequality as Remark 5. Wang--Qi's 2020 open-access article studies the same \((p,q)\)-elliptic and generalized hyperbolic-tangent functions and proves sharp inequalities, but the closest located lower bound is weaker than the exponent \((q+1)/(2q)\). Published-record and equivalent-hypergeometric searches found no earlier statement of the audited bound.

### equivalent_formulations

Searches: Dou Yin Lin 2019 Remark 5 complete (p,q)-elliptic arctanh lower bound; zero-balanced hypergeometric power lower bound \(K_{p,q}\) arctanh

Evidence: The 2019 full text poses the target as an open question; the 2020 same-function paper gives related but weaker inequalities.

Reasoning: The hypergeometric reformulation is equivalent, and no inspected theorem yields the stronger exponent.

### broader_coverage

Searches: DOI 10.1155/2019/4752856 full text; DOI 10.5802/crmath.119 open-access article; generalized elliptic inequalities literature cited by Wang--Qi

Evidence: The sources cover broad monotonicity and sharp inequalities but do not dominate the claimed power lower bound.

Reasoning: The audited theorem strengthens, rather than merely instantiates, the closest prior inequalities.

### exact_database_or_table

Searches: Resultary semantic search for \((q+1)/(2q)\) complete (p,q)-elliptic arctanh bound

Evidence: No earlier exact published record was found.

Reasoning: This is a continuous analytic inequality, not a table lookup.

### claim_vs_prior_implication

Searches: Dou--Yin--Lin Remark 5; Wang--Qi Theorem 2 and Corollary 3 context

Evidence: The first source leaves the target open; the second supplies related monotonicity/lower-bound information but not the stronger audited exponent.

Reasoning: The endpoint derivative lemma and Riccati comparison provide an additional implication absent from the inspected prior results.

## Scientific value — PASS

PASS. The result resolves a named published open inequality over its full requested range and strictly improves the closest located general lower bound. The endpoint reduction and Riccati comparison are reusable analytic mechanisms rather than a numerical special case.

## Source inspections

- **Functional Inequalities for Generalized Complete Elliptic Integrals with Two Parameters** — https://doi.org/10.1155/2019/4752856. Material read: Complete open-access article, including Theorem 2, Corollary 3, Theorem 4, and Remark 5. Assessment: PRIMARY_SOURCE_EXPLICITLY_LEAVES_TARGET_OPEN. Evidence: Remark 5 asks whether the relevant lower inequality holds for \(p,q\ge2\).
- **Monotonicity and sharp inequalities related to complete (p,q)-elliptic integrals of the first kind** — https://doi.org/10.5802/crmath.119. Material read: Open-access article text, theorem context, and references. Assessment: RELATED_WEAKER_PRIOR. Evidence: The paper establishes monotonicity and sharp bounds involving \(K_{p,q}\) and \(\operatorname{arctanh}_q\), but no inspected statement gives the audited stronger exponent.

## Limitations and residual risks

The exponent \((q+1)/(2q)\) is not claimed optimal for fixed parameters, and the result is restricted to \(p,q\ge2\).

- A differently phrased theorem in the extensive zero-balanced hypergeometric literature could have escaped the searches; no such implication was located.

## Disposition

**passed**
