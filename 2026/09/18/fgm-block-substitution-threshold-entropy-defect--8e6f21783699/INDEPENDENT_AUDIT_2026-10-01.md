# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-8e6f21783699`

## Correctness — PASS

The three claims reconstruct analytically. Differentiating \(U=\prod_i x_i\) gives the composite density \(1+\theta(1-2^mU)(1-2v)\); the product factor spans exactly the interval with absolute maximum \(2^m-1\), so nonnegativity is equivalent to \(|\theta|\le(2^m-1)^{-1}\). In logarithmic coordinates, repeated mixed differentiation gives \(U^{-1}(u\partial_u)^m h(u)=(1+u\partial_u)^{m-1}h'(u)\), establishing the Euler-operator criterion. For entropy, the higher-dimensional factor is a mean-preserving spread of the one-dimensional factor. Uniform strong convexity of \((1+\theta ba)\log(1+\theta ba)\), together with \(E[B^2]=1/3\), \(E[Y_1^2]=4/3\), and \(\mathrm{Var}(W)=(4/3)^{m-1}-1\), yields exactly the stated strict defect; the \(m=2,\theta=1/4\) specialization equals \(1/378\).

### Correctness sources

- Lu, arXiv:2609.20512
- Brechmann 2014
- Li–Scarsini–Shaked 1996
- Fan–Henry 2023
- assigned RESULT.md

### Correctness risks

- The general Euler criterion assumes the stated smoothness and one independence-product block.
- The entropy lower bound is not claimed optimal.

## Originality — PASS

Lu's direct block-substitution construction states copula closure and entropy additivity using an ordinary chain-rule style density; the audited independence-block calculation shows the missing higher mixed derivatives and gives the sharp FGM phase boundary. Classical linkage, hierarchical Kendall, and vector-copula literature explains why multivariate blocks require special aggregation, but no inspected source states this exact FGM threshold, Euler-operator formula in this setting, or the quantitative entropy defect.

### equivalent_formulations

Searches:
- arXiv:2609.20512 full text
- searches for FGM direct block substitution threshold and Euler operator
- hierarchical Kendall and linkage literature

Evidence:
- Lu's formula treats the substituted multivariate block as though an ordinary scalar density chain rule applied.
- The audited derivative produces the dimension-dependent factor \(1-2^mU\).

Reasoning:
Equivalent formulations as copula-volume positivity, full mixed-density positivity and the Euler-operator condition were compared.

### broader_coverage

Searches:
- Brechmann hierarchical Kendall copulas
- Li–Scarsini–Shaked linkage functions
- Fan–Henry vector copulas

Evidence:
- These works give established ways to couple multivariate marginals/blocks and motivate transforming to a scalar uniform aggregate.

Reasoning:
They provide broader alternative frameworks, not the audited exact threshold or entropy inequality.

### exact_database_or_table

Searches:
- FGM admissibility tables under multivariate product substitution

Evidence:
- No exact database/table containing \((2^m-1)^{-1}\) as this block-substitution threshold was located.

Reasoning:
The threshold follows from a continuous density calculation, not finite tabulation.

### claim_vs_prior_implication

Searches:
- comparison of Lu's closure/additivity claims with the audited FGM specialization

Evidence:
- The FGM/independence family is a direct specialization of the proposed substitution and supplies both invalid and valid-but-nonadditive cases.

Reasoning:
A counterexample plus sharp phase diagram is not implied by the claimed general closure theorem; it refutes and refines it.

### source_inspections
- **Copula Operad and Copula Entropy** — https://arxiv.org/abs/2609.20512. Trigger: Direct source proposing the block substitution and entropy additivity. Material read: Full accessible preprint portions defining substitution, its density formula, closure claim and entropy theorem. Method: Primary full-text formula comparison. Assessment: The source's scalar-chain-rule treatment misses higher mixed derivatives of the multivariate inner block. Evidence: The audited independence block yields an explicit extra Euler-operator action and a sharp failure region.
- **Hierarchical Kendall copulas: Properties and inference** — https://doi.org/10.1002/cjs.11204. Trigger: Closest established block-copula aggregation framework. Material read: Published scope and method material. Method: Prior-framework comparison. Assessment: Uses Kendall transforms to create scalar uniform aggregates; it does not state the audited FGM threshold. Evidence: Its construction is designed precisely to avoid naive direct multivariate substitution.
- **Linkages: A Tool for the Construction of Multivariate Distributions with Given Nonoverlapping Multivariate Marginals** — https://doi.org/10.1006/jmva.1996.0002. Trigger: Older theory for nonoverlapping multivariate blocks. Material read: Published abstract/scope material. Method: Prior-literature comparison. Assessment: General linkage framework only; no exact FGM/product threshold found. Evidence: It addresses the broader multivariate-marginal coupling problem.

### checked_sources

- https://arxiv.org/abs/2609.20512
- https://doi.org/10.1002/cjs.11204
- https://doi.org/10.1006/jmva.1996.0002
- https://doi.org/10.1016/j.jeconom.2021.11.012
- assigned RESULT.md

### residual_risks

- Older linkage literature could contain an equivalent special-case differential identity under different notation; none was located.

## Scientific value — PASS

The result gives a sharp dimension-dependent closure boundary in a canonical copula family, identifies the exact higher-derivative operator missing from naive scalar substitution, and proves a positive entropy-additivity defect even inside the valid region. This cleanly separates two distinct failures in a recent general construction.

### Value sources

- Lu 2026 direct-substitution proposal
- classical multivariate-block linkage/Kendall alternatives

### Value risks

- No replacement operad or arbitrary-block classification is claimed.

## Limitations

- The sharp phase diagram is for a bivariate FGM outer copula and one independence block.
- The operator theorem assumes sufficient smoothness.
- The entropy bound is one-sided and not claimed optimal.
- Originality is best-of-knowledge with older linkage literature as residual risk.

## Disposition

**PASSED**
