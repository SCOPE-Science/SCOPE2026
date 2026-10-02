# Independent scientific audit — SCOPE-20260918-cec7237f693b

Audited at: 2026-10-01T07:11:57.147372Z

Disposition: **passed**

## Correctness — PASS

With \(w=\sigma^{-(p-1)}\), the dual weight is exactly \(\sigma\). Lerner's mass recurrence gives the anchored characteristic estimate with geometric ratio \(3^{p-1}/2^{2p-1}<1\) for every \(p>1\), while a two-cell rectangle gives the matching lower scale \(\theta^{-(p-1)}\). Testing with \(f=\sigma\mathbf 1_Q\) normalizes the input exactly, and the hyperbolic set \(rs\le D\) contributes order \(\theta^{-1}\log(1/\theta)\) cells, yielding the claimed \(p\)-th-power lower bound. Reflection and product extension preserve the estimate in all dimensions.

## Originality — PASS

Lerner's primary lower obstruction is explicitly the two-dimensional \(p=2\) case. Ombrosi–Rey's all-\(p\) paper is an upper-bound theorem and cites the lower obstruction at \(p=2\); it does not state the all-\(p\) lower construction. Resultary finds this record as the first exact all-\(p\) logarithmic obstruction, with a stronger dimension-amplified result only appearing later.

### Equivalent formulations

No earlier equivalent all-p lower statement was found.

### Broader coverage

Neither prior result dominates the new lower-bound statement for \(p\ne2\).

### Exact database or table

The theorem is not a recomputation of tabulated constants.

### Claim versus prior implication

The all-p lower obstruction is not mechanically implied by the published \(p=2\) theorem alone.

## Value — PASS

The result answers a natural endpoint question uniformly over the whole \(L^p\) scale: the Buckley endpoint pure power fails for every \(1<p<\infty\), not merely at \(p=2\). The explicit logarithmic loss gives a quantitative obstruction with direct relevance to the open sharp-dependence problem.

## Sources inspected

- Failure of the linear A2 bound for the strong maximal operator — https://arxiv.org/abs/2609.14008. NOT_COVERING_ALL_P: The published lower theorem is stated at \(p=2\).
- Improved weighted bounds for the strong maximal function — https://arxiv.org/abs/2609.17246. NOT_COVERING_LOWER_EXTENSION: The paper proves improved all-p upper exponents; it does not provide the audited all-p logarithmic lower obstruction.

## Checked sources

- https://arxiv.org/abs/2609.14008
- https://arxiv.org/abs/2609.17246
- https://arxiv.org/abs/1512.01112
- Resultary semantic search

## Residual risks

- The two principal 2026 papers are recent, so unindexed simultaneous observations remain possible.
- The logarithmic exponent supplied by this family is not claimed optimal.

## Limitations

- The theorem excludes the endpoint pure-power estimate but does not prove that the infimum power exponent exceeds \(1/(p-1)\), does not establish optimality of the logarithmic exponent \(1/p\), and makes no \(p=1\) claim. Lerner's \(p=2\) construction and recurrence are prior work.
