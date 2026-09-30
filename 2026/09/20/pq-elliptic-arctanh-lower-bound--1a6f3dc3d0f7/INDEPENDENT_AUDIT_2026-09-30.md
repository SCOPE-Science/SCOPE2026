# Independent Audit — 2026/09/20/pq-elliptic-arctanh-lower-bound--1a6f3dc3d0f7

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `a15e4b8ae057028f178f57b5331b68a9f0615d70`
- Disposition: **PASSED**

## Correctness

**PASS** — The hypergeometric proof checks. Coefficientwise monotonicity in a=1-1/p reduces the problem to a=1/2. At b=1/2 the claimed logarithmic-derivative inequality follows from the displayed J(s) factorization: Q(s)=atanh(s)-3s/(3-s^2) has Q'(s)>0, making the first J' factor negative while the second is positive, so J'>0. For 0<b<=1/2, the identity x B_b'+bB_b=b/(1-x), together with B_b<=B_{1/2}, gives v/b>=2V; the two coefficient comparisons used to obtain H_b>2b^2/(1+b) are valid because 4b(1-b)<=1 and 4(1-b^2)>=3. Substitution in the hypergeometric Riccati equation leaves a strictly negative residual, and the first-order crossing argument for Delta=w-((1+b)/2)v is valid also at b=1/2 where Delta(0)=0. Integration gives the stated strict inequality for x>0. Independent numerical evaluation on a grid of p,q and r values found no violation and agrees with the endpoint expansion.

## Originality

**PASS** — Dou-Yin-Lin (2019) explicitly pose the weaker exponent (p+q-1)/(pq) as an open question in Remark 5, equation (33). Wang-Qi (2020) subsequently derive sharp (p,q)-elliptic inequalities involving the generalized inverse hyperbolic tangent, but the located literature does not state the exponent (q+1)/(2q). The submitted bound is genuinely stronger for p>2 and recovers the classical 3/4 exponent at p=q=2. Targeted searches by the exact exponent, the zero-balanced hypergeometric form, and the 2019 open question did not locate prior coverage. Because equivalent hypergeometric inequalities can be indexed under different notation, the priority conclusion retains that explicit residual risk.

## Scientific value

**PASS** — The theorem gives an affirmative solution to a published 2019 open inequality throughout p,q>=2 and improves it by a uniform larger exponent. The proof also isolates a reusable Riccati comparison for zero-balanced hypergeometric functions. Although optimality of the new exponent for general p,q is not proved, closing the stated open problem with a stronger bound is substantive.

## Sources

- **Functional Inequalities for Generalized Complete Elliptic Integrals with Two Parameters** — Xiaohui Dou; Liguo Yin; Xiaoli Lin. https://doi.org/10.1155/2019/4752856 — Remark 5 explicitly poses equation (33), the weaker lower-bound inequality addressed by the record.
- **Monotonicity and sharp inequalities related to complete (p,q)-elliptic integrals of the first kind** — Fei Wang; Feng Qi. https://doi.org/10.5802/crmath.119 — Later sharp-inequality work involving K_{p,q} and the generalized inverse hyperbolic tangent; no located statement matches the new exponent.
- **Monotonicity theorems and inequalities for the complete elliptic integrals** — Horst Alzer; Song-Liang Qiu. https://doi.org/10.1016/j.cam.2004.02.009 — Classical p=q=2 comparison and the sharp 3/4 exponent.

## Limitations

- The exponent (q+1)/(2q) is not shown optimal for fixed p,q.
- Only p,q>=2 are covered.
- A differently phrased zero-balanced hypergeometric inequality remains a residual originality risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "parameter_reduction_checked": true,
  "log_derivative_lemma_sign_chain_checked": true,
  "riccati_residual_checked": true,
  "numerical_grid_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access and preprint sources were checked first; no decisive comparison required institutional retrieval in this audit.
