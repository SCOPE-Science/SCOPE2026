# Independent audit — 2026-10-01

## Final claim

Rank-one shear obstructions to CPPm on diagonal ℓp-sums

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

The rank-one map \(N_c(z,y)=(c f(y)z_0,0)\) satisfies \(N_c^2=0\), so \(T_c^{-1}=I+N_c\). Its norm is exactly the two-dimensional positive shear norm \(\kappa_p(c)\): the triangle inequality gives the upper bound and a norming sequence for the non-norm-attaining James functional gives the reverse bound. Any norm-attaining vector would force \(|f(y)|=\|y\|\), impossible. Thus \(m(T_c)=\kappa_p(c)^{-1}\) is not attained. For any compact \(K\), \(T_c+K=I+(K-N_c)\) and compact operators on infinite-dimensional spaces are not bounded below, so \(m(T_c+K)\le1\); taking \(K=N_c\) attains 1. The endpoint formula \(\kappa_1(c)=\kappa_\infty(c)=1+c\) and divergence as \(c\to\infty\) follow directly.

## Originality

Raposo--Ribeiro prove the scalar \(\mathbb K\oplus_\infty Y\) case, and Han's cited direct-sum obstruction uses distinct exponents. The audited all-\(p\) diagonal theorem with arbitrary nonzero \(Z\), exact compact-perturbation envelope, and unbounded defect ratio is not implied by the inspected prior statements without the new shear calculation.

### Equivalent formulations

**Searches**
- Published-record semantic search: compact perturbation property minimum modulus diagonal lp sum nonreflexive rank one shear
- Web search: CPPm diagonal p sum non-reflexive rank-one shear

**Evidence**
- The only exact published-record match was the audited record. Web results recovered the Raposo--Ribeiro scalar infinity-sum theorem, not the all-p diagonal statement.

**Reasoning**

The same nilpotent-shear idea appears in the prior infinity-sum case, but the finite-p norm identity and arbitrary complementary summand are additional quantified conclusions.

### Broader coverage

**Searches**
- A. Raposo Jr. and G. Ribeiro, arXiv:2605.01397
- M. Han, arXiv:2601.17316 / JMAA 562 (2026)
- R. C. James, Studia Math. 23 (1964)

**Evidence**
- Raposo--Ribeiro state CPPm failure for \(X=\mathbb K\oplus_\infty Y\) with non-reflexive \(Y\). Han introduces CPPm and treats other direct-sum regimes; James gives the non-norm-attaining functional criterion.

**Reasoning**

These sources cover a special endpoint, other direct-sum hypotheses, or a classical ingredient; none dominates the all-p diagonal result.

### Exact database or table

**Searches**
- Published-record search for CPPm p-sum obstruction and compact-perturbation envelope

**Evidence**
- No table or database source with the function \(\kappa_p(c)\), envelope 1, and arbitrary \(Z\) was located.

**Reasoning**

The result is structural operator theory, not a database computation.

### Claim versus prior implication

**Searches**
- Direct comparison with Raposo--Ribeiro Theorem 2.1 and Han direct-sum statements

**Evidence**
- Raposo--Ribeiro gives the \(p=\infty\), scalar-summand, essentially \(c=1\) case. The finite-p norm equality requires the scalar \(\ell_p^2\) shear optimization used in the audited proof.

**Reasoning**

Prior special cases do not imply the finite-p diagonal theorem by a formal parameter substitution.

### Source inspections

- **Weak Minimizing Property and the Compact Perturbation Property for the Minimum Modulus** — SPECIAL_CASE. Abstract and accessible theorem-level text describing the constructive rank-one perturbation and the \(\mathbb K\oplus_\infty Y\) non-reflexive theorem. The source covers the infinity norm with scalar complementary summand, not all diagonal p-sums.

- **Weak minimizing property on pairs of classical Banach spaces** — RELATED_NOT_DOMINATING. Current abstract and bibliographic theorem context available through the source record. It does not state the audited all-p diagonal arbitrary-summand theorem.

### Checked sources
- https://arxiv.org/abs/2605.01397
- https://arxiv.org/abs/2601.17316
- https://doi.org/10.4064/sm-23-3-205-216
- Published-record semantic search

### Residual risks
- The CPPm literature is new and rapidly developing; later or not-yet-indexed diagonal formulations may exist.

## Value

The theorem fills a natural diagonal direct-sum gap in the newly introduced CPPm property, works uniformly for every \(p\), and computes the exact perturbation envelope and arbitrarily large defect. This is a structural operator-theoretic statement rather than an isolated example.

## Limitations

The result applies to spaces presented with the stated isometric decomposition \(Z\oplus_pY\); it does not characterize CPPm under arbitrary equivalent renormings or for all non-reflexive Banach spaces. The exact all-\(p\) diagonal statement remains a best-of-knowledge originality conclusion.
