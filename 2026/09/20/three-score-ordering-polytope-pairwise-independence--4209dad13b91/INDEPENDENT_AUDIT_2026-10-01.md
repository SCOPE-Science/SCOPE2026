# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** For three pairwise-independent real observations with one common atomless marginal law, the six labeled strict-order probabilities are exactly \((a,b,c,b,c,a)\) with \(0\le a,b,c\le1/4\) and \(a+b+c=1/2\), every such point is attainable, and the resulting maximum-rank and two-calibration-score rank envelopes are sharp.

## C — PASS

Conditioning on one coordinate leaves each of the other two with the common marginal by pairwise independence; conditional Fréchet bounds integrate to \(1/4\le q_i\le1/2\). Pairwise comparison probabilities and total mass force reversal symmetry. The torus construction \((U,V,(U+V)\bmod1)\) realizes a vertex with exact pairwise-product marginals; coordinate permutations give all three vertices, and mixing them preserves the identical pairwise-product marginals, so the full triangle is attained. The inspected rational-arithmetic artifact is consistent with these identities but is not needed for the proof.

## O — PASS

The closest inspected primary literature treats symmetric order statistics—distributions of the sorted values and their joint reliability functions—under \(k\)-independence. The 2025 full text frames its optimization entirely through \(X_{j:n}\) and count vectors and does not encode which named observation occupies each rank. Published SCOPE searches found related pairwise-independence extremal problems but no theorem that implies this complete six-pattern labeled-order polytope.

### Equivalent formulations

**Searches:** Published SCOPE search: three pairwise-independent common-marginal ordering probabilities labeled ranks reversal symmetry; Literature search: pairwise independent order patterns labeled ranks

**Evidence:** No distinct SCOPE theorem with the six labeled permutation probabilities was located. The inspected 2025 order-statistic paper formulates events only in terms of sorted variables \(X_{j:n}\), not label-to-rank assignments.

**Reasoning:** Symmetric order-statistic laws lose label information and are not equivalent to the audited ordering polytope.
### Broader coverage

**Searches:** Okolewski & Błażejczyk-Okolewska 2025 DOI 10.3390/e27121250 full text; Kemperman 1997 k-independent order statistics

**Evidence:** The 2025 theorem gives broad sharp bounds for linear combinations of joint distribution/reliability functions of selected order statistics under \(k\)-independence, summarizing Kemperman’s earlier sorted-statistic bounds.

**Reasoning:** That broader-looking framework is permutation-symmetric in the sample values and therefore does not imply the label-sensitive six-order law.
### Exact database or table

**Searches:** Published SCOPE semantic search for pairwise-independent ranking polytope; Exact literature searches for six permutation probabilities under pairwise independence

**Evidence:** No exact table or database entry was found for the labeled six-pattern region.

**Reasoning:** The claim is an analytic feasible-polytope theorem; no known table mechanically supplies it.
### Claim versus prior implication

**Searches:** Implication comparison with DOI 10.3390/e27121250

**Evidence:** Knowing all sorted order-statistic distributions does not identify which label realizes each order; the audited extremal vector changes under label-specific dependence while the sorted-value functionals are symmetric.

**Reasoning:** The inspected prior theorem does not imply the label-sensitive conclusion.

## V — PASS

The complete labeled-rank identification region is a natural finite extremal problem under a standard limited-independence assumption, and its exact conformal/rank calibration consequence quantifies a concrete inferential failure mode. It is not merely a recomputation of sorted-order-statistic bounds.

## Source inspections

- **Tight Bounds for Joint Distribution Functions of Order Statistics Under k-Independence** — https://doi.org/10.3390/e27121250. Trigger: Closest recent primary theorem on order statistics under \(k\)-independence Material read: Open-access full text, including introduction, problem formulation in terms of \(X_{j:n}\), moment reduction, and explicit bounds section. Method: Open full HTML text Assessment: NOT_COVERING_LABEL_SENSITIVE_CLAIM. Evidence: The paper optimizes symmetric functions of sorted order statistics; it does not state the six probabilities for named labels occupying ranks.
- **Bounding Moments of an Order Statistic When Each K-Tuple is Independent** — DOI 10.1007/978-94-011-5532-8_34. Trigger: Classical source cited as the origin of k-independent order-statistic bounds Material read: Bibliographic/summary material as quoted and contextualized in the inspected 2025 full text; the 1997 chapter itself was not fully accessible. Method: Secondary primary-literature trail Assessment: INACCESSIBLE_PLAUSIBLE_SOURCE. Evidence: The available description concerns moments/distributions of order statistics, not labeled permutation patterns; full theorem text remains a terminology risk.

## Residual risks

- Kemperman (1997), Okolewski (2017), or older copula/order-pattern literature could contain an equivalent label-sensitive formulation under different terminology; their unavailable portions were not treated as proof of noncoverage.

## Limitations

- Specific to three observations and one common atomless marginal.
- Sharp torus extremizers may be singular as three-dimensional laws.
- Older label-sensitive copula/order-pattern terminology remains a residual originality risk.
