# Cherry-biased pruning and exact Sackin covariance in uniform phylogenetic trees

## Finding

Let a rooted binary phylogenetic tree be uniformly sampled from all trees whose \(n\) leaves have distinct labels, with no left/right ordering at internal vertices (the proportional-to-distinguishable-arrangements, or PDA, law). Write \(C_n\) for its number of cherries (internal vertices with two leaf children) and \(S_n\) for its Sackin index, the sum of all root-to-leaf edge distances. Let \(D_m\) be the depth of a uniformly selected leaf in an independent uniform \(m\)-leaf PDA tree. For every integer \(n\ge2\) and every real test function \(f\) on the finite range of Sackin indices,

\[
\mathbb E[C_n f(S_n)]
=\frac{n(n-1)}{2(2n-3)}
 \mathbb E[f(S_{n-1}+D_{n-1}+2)]. \tag{1}
\]

In the right-hand expectation, \(D_{n-1}\) is sampled *conditional on the same tree* whose Sackin index is \(S_{n-1}\); those variables are not asserted independent. In particular, with

\[
q_n=\frac{4^{n-1}}{\binom{2n-2}{n-1}},
\]

the complete finite-size mixed covariance is

\[
\boxed{\operatorname{Cov}(C_n,S_n)
=\frac{n}{4(2n-3)}\left(4(n-1)-nq_n\right).} \tag{2}
\]

This covariance is exactly zero for \(n=2,3\), strictly negative for all \(n\ge4\), and has the sharp asymptotic

\[
\operatorname{Cov}(C_n,S_n)
\sim-\frac{\sqrt\pi}{8}n^{3/2}. \tag{3}
\]

Equation (1) is stronger than the covariance statement: it transfers the full Sackin distribution under cherry-size-biasing to a uniform smaller tree and its distinguished leaf depth.

## Assumptions and scope

For \(n\ge2\), let \(\mathcal T_n\) be the set of rooted, strictly binary, **non-plane**, leaf-labeled trees with label set \(\{1,\ldots,n\}\). Each member has probability \(1/(2n-3)!!\), where \((-1)!!=1\). An internal vertex counts as a cherry when both its children are leaves. Depth is the number of edges from the root, so the two-leaf tree has Sackin index \(2\). For \(n=1\), the unique single-leaf tree has Sackin index \(0\). In a uniform smaller tree, the distinguished leaf is selected uniformly among its leaves. All probability spaces are finite; no integrability restriction beyond being finite on the finite range is needed for \(f\).

This is the PDA measure, **not** the Yule/Kingman distribution on ranked genealogies or the uniform distribution on *unlabeled shapes*. Random child orientations convert the PDA model to the uniform distribution on plane full binary trees with a specified number of leaves.

## Proof

**1. Marked-cherry contraction.** Fix a pair \(\{a,b\}\) of distinct leaf labels. Trees in \(\mathcal T_n\) where \(a,b\) form a cherry correspond bijectively to rooted binary trees on \(n-1\) leaves labeled by the other \(n-2\) labels and a distinguished surrogate label \(\ast\): contract their cherry to the leaf \(\ast\). Conversely, expand \(\ast\) into a parent with the two children \(a,b\). This does not introduce a left/right choice because trees are non-plane. There are exactly \((2n-5)!!\) contracted trees per pair, out of \((2n-3)!!\) original trees.

If the surrogate leaf has root depth \(d\), and the contracted tree has Sackin index \(s\), then expansion deletes one contribution \(d\) and creates two contributions \(d+1\), so the expanded tree has index \(s+d+2\). Sum \(f(S_n)\) over all trees with a marked cherry, first selecting the unordered leaf pair and then contracting. Divide by \((2n-3)!!\) and use leaf-label exchangeability. This gives

\[
\mathbb E[C_n f(S_n)]
=\binom n2\frac{(2n-5)!!}{(2n-3)!!}
\mathbb E[f(S_{n-1}+D_{n-1}+2)],
\]

which is (1). Choosing \(f=1\) yields the previously known marginal mean

\[
\mathbb E C_n=\frac{n(n-1)}{2(2n-3)}. \tag{4}
\]

**2. Mean of the Sackin index.** Randomly orient the two children at every internal vertex. Every non-plane labeled tree has exactly \(2^{n-1}\) distinct orientations because its descendant leaf-label sets are disjoint. Conversely, any given plane shape with \(n\) leaves admits exactly \(n!\) distinct assignments of the leaf labels. Thus the induced plane shape is uniform over the Catalan full binary plane trees.

Let \(T(x)\) be their generating function by number of leaves and \(B(x)\) the generating function whose coefficient is the *sum* of their Sackin indices. Splitting a nontrivial tree at its root gives

\[
T(x)=x+T(x)^2=\frac{1-\sqrt{1-4x}}2,
\qquad B(x)=2T(x)B(x)+2xT(x)T'(x).
\]

The last term accounts for the increase of one in the depth of every descendant leaf; the single-leaf tree contributes zero. Since \(T'(x)=(1-4x)^{-1/2}\),

\[
B(x)=\frac{x}{1-4x}-\frac{x}{\sqrt{1-4x}}.
\]

The coefficient of \(x^n\) is \(4^{n-1}-\binom{2n-2}{n-1}\), while the number of plane trees is \(\binom{2n-2}{n-1}/n\). Therefore

\[
\mathbb E S_n=n(q_n-1). \tag{5}
\]

Equation (5) is a self-contained reformulation of a known PDA Sackin mean; no novelty is claimed for this marginal result.

**3. Covariance reduction.** Under the uniform \((n-1)\)-leaf tree, averaging the depth of a uniformly selected leaf gives \(\mathbb E D_{n-1}=\mathbb E S_{n-1}/(n-1)\). Taking \(f(s)=s\) in (1) gives

\[
\mathbb E[C_nS_n]
=\mathbb E C_n\left(\frac n{n-1}\mathbb E S_{n-1}+2\right).
\]

Substitute (4) and (5), and use the exact ratio \(q_{n-1}/q_n=(2n-3)/(2n-2)\). After subtraction of \(\mathbb E C_n\mathbb E S_n\), obtain (2).

**4. Exact sign and asymptotic.** Define \(a_n=nq_n/(n-1)\). Directly \(a_2=a_3=4\), and for every integer \(n\ge3\),

\[
\frac{a_{n+1}}{a_n}=\frac{2(n^2-1)}{n(2n-1)}
=1+\frac{n-2}{n(2n-1)}>1.
\]

Consequently \(4(n-1)-nq_n\) vanishes for \(n=2,3\) and is strictly negative for \(n\ge4\). Finally, the central-binomial asymptotic \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\) implies \(q_n\sim\sqrt{\pi n}\). In (2), the term \(-nq_n\) dominates the term \(4(n-1)\), yielding (3). This proves the result for every size, independently of finite enumeration.

## Verification

The included standalone `verify.py` uses standard-library integer and rational arithmetic. It exhaustively enumerates all plane full binary trees with \(2\) through \(9\) leaves, comparing exact mixed moments and each probability-mass bin in (1). It independently enumerates every non-plane labeled rooted binary tree with \(2\) through \(7\) leaves, a total of \(11{,}464\) trees, and checks the mixed moments. It also checks the generating-function coefficient recurrence and covariance sign formulas for the first \(200\) nontrivial sizes. The observed run reports eight plane-tree sizes, 48 mass bins, 11,464 labeled trees, and 200 exact algebra cases, all passing. These finite checks are not presented as proofs of the infinite claims.

## Relationship to prior work

Mir and Rosselló (2012) computed the PDA mean of Sackin's index, presented in their paper as a terminating hypergeometric series; the equivalent binomial form (5) is not itself novel. McKenzie and Steel (2000) studied marginal cherry distributions under the standard models. Wu and Choi (2015) derived joint laws for cherries and *pitchforks*, rather than Sackin's global depth sum. Janson (2013) developed broad conditioned-Galton–Watson theory for local fringe-tree counts and suitable additive statistics; its stated joint limit theorems do not supply the exact finite-size cherry/Sackin law (1) or covariance (2). The new statement is the cherry-marked **distributional transfer**, the mixed covariance, its strict all-size sign, and its sharp scale; the two previously known marginal results alone do not state this joint relation.

## Limitations

The distributional identity requires uniform labeled non-plane rooted binary trees; no extension to the Yule/Kingman measure, random branch lengths, nonbinary phylogenies, or uniform *unlabeled* tree shapes is asserted. Covariance negativity does not imply negative association or a monotone conditional Sackin regression on the number of cherries. Although direct comparisons found no equivalent theorem, uncatalogued earlier work or an unstated corollary of a broader construction may exist. The asymptotic is an expectation identity, not a joint weak limit or a significance-test calibration.

## References

1. A. Mir and F. Rosselló, *Two results on expected values of imbalance indices of phylogenetic trees*, arXiv:1201.3884 (first public preprint 2012-01-18). https://arxiv.org/abs/1201.3884
2. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models*, arXiv:1508.03139 (first public preprint 2015-08-13). https://arxiv.org/abs/1508.03139
3. S. Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton–Watson trees*, arXiv:1312.1211 (2013). https://arxiv.org/abs/1312.1211
4. A. McKenzie and M. Steel, *Distributions of cherries for two models of trees*, Mathematical Biosciences **164** (2000), 81–92.
5. M. G. B. Blum, O. François and S. Janson, *The mean, variance and limiting distribution of two statistics sensitive to phylogenetic tree balance*, Annals of Applied Probability **16** (2006), 2195–2214.
