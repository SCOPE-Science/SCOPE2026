# Scientific review: zero-product matrix-pair ranks

## Correctness

**PASS.** The finite rank-pair count follows by choosing a rank stratum for the first endomorphism and a rank stratum for a map into its kernel. Multiplying over the whole second-map fiber gives the exact first-rank weight. After centering the first rank at half the dimension, the weight is a discrete-Gaussian factor times a uniformly bounded finite-product correction with a pointwise limit; the resulting dominated-convergence argument proves the normalized partition function and total-variation limit. The probability of homology comes from the exact full-row-rank product of the conditional second map. A union bound and a two-dimensional-subspace bound prove, respectively, the first sharp defect and the higher-defect estimate. These are proved for every fixed finite-field order \(q\ge2\) and all dimensions \(n\ge1\) for exact formulas; asymptotics are parity-separated and require \(n\to\infty\). Five small matrix-pair models were exhaustively verified and 48 exact count identities were checked by integer arithmetic using `verify.py`. The computations test but do not imply the asymptotic statements.

## Originality

**PASS relative to available primary literature, with a residual priority risk.** Đurić--Jevđenić--Stopar (arXiv:1810.02776, Proposition 3.1) give the Gaussian-binomial degree distribution in the *compressed* zero-product digraph, not pair-uniform weighting of actual matrix edges or a fixed-field asymptotic distribution. Gould--Johnson--Naz (arXiv:1907.12518, especially introduction and rank/Green-stratum discussion) studies multiplicative semigroups and rank ideals, not pair-uniform zero products. Catanzaro--Zabka (arXiv:1901.00964, Lemma 2.5, §§3–4) develops sequential conditional chain-complex sampling; it neither has this globally uniform rank law nor the fixed-field dimension-growth limit. Huang (arXiv:2110.15566, §3.1) requires \(AB=BA=0\), which imposes an additional rank constraint and changes the fiber size from \(q^{n(n-r)}\) to \(q^{(n-r)^2}\). Ginzburg--Pasechnik (arXiv:1602.08538, Theorems 2.1–2.2) selects one square-zero operator rather than a jointly uniform pair of distinct compatible maps. The older works supply classical finite matrix/graph incidence counts and related settings, which are credited rather than presented as new. A hidden equivalent result in the representation-counting literature of a radical-square-zero quiver remains possible; a database search cannot prove uniqueness.

## Mathematical value

**PASS.** The zero-product relation is intrinsic to full matrix monoids, and the rank is the natural parameter indexing their Green strata. The theorem identifies a strong, initially counterintuitive bias induced by conditioning an entire ordered pair, replacing nearly full-rank matrices under sequential sampling with two nearly complementary half-rank matrices. The exact theta law quantifies the persistent order-one rank imbalance, while the sharp first-homology coefficient shows that, at fixed \(q\), a random jointly uniform three-term complex becomes exact at its middle term with exponentially high probability. This sharply contrasts the known nonzero fixed-field homology probabilities for a single square-zero differential. The result is thus more than an elementary computation or a small numerical improvement.

## Residual limits

No independent scientific audit has been performed. Exact equivalence with every older finite-module or quiver-representation enumeration has not been ruled out. The statement does not address growing finite fields, further differentials, or an explicit optimal total-variation rate.

Self-review: passed. Independent audit: not yet performed.
