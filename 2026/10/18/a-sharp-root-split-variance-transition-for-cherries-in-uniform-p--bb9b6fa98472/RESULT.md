# A sharp root-split variance transition for cherries in uniform phylogenetic trees

## Finding

**Theorem.** Let \(n\ge6\). Choose a uniformly random rooted, non-plane, fully binary phylogenetic tree with leaves labeled by \(\{1,\ldots,n\}\) (the PDA model). A **cherry** is an internal vertex with two leaf children. Let \(C_n\) count cherries, and let \(K\) be the smaller number of leaves descending from a root child. For every integer \(1\le k\le\lfloor n/2\rfloor\), define \(V_n(k)=\operatorname{Var}(C_n\mid K=k)\). Then

\[
V_n(k)=v(k)+v(n-k),\qquad
v(m)=\begin{cases}0,&1\le m\le3,\\
\dfrac{m(m-1)(m-2)(m-3)}{2(2m-3)^2(2m-5)},&m\ge4.
\end{cases}
\]

The unique minimizing split is \(k=3\) for every \(n\ge6\). The maximizing split exhibits one and only one finite-size transition:

\[
\underset{1\le k\le\lfloor n/2\rfloor}{\operatorname{argmax}}\ V_n(k)
=\begin{cases}\{1\},&6\le n\le14,\\
\{\lfloor n/2\rfloor\},&n\ge15.
\end{cases}
\]

The transition is strict; the balanced-minus-singleton variance is \(-1340/1344189\) at \(n=14\) and \(1687336/881863125\) at \(n=15\). Moreover,

\[
\lim_{n\to\infty}\left[V_n(\lfloor n/2\rfloor)-V_n(1)\right]=\frac1{32}.
\]

## Assumptions and scope

A rooted fully binary non-plane tree on a fixed \(m\)-element leaf set has \((2m-3)!!\) realizations for \(m\ge2\); the one-leaf tree is also allowed as a root subtree. Cherries are counted throughout the full tree, including those contained in its root subtrees. The root itself is a cherry only for a two-leaf tree; the stated theorem uses \(n\ge6\). A root split of size \(k\) means its two unordered sets of descendant leaves have sizes \(k\) and \(n-k\). Every such size is attainable.

## Proof

**Conditional decomposition.** For a specified unordered partition of the leaf labels into sets of sizes \(k\) and \(n-k\), root subtrees are independent uniform PDA trees: every ordered pair of underlying leaf-labeled subtree shapes corresponds to exactly one whole tree. The distribution of \(C_n\), conditional only on the split *size*, is consequently the sum of independent cherry counts of sizes \(k\) and \(n-k\). This remains true for the balanced split, because exchanging the two root children does not affect the sum. Thus \(V_n(k)=v(k)+v(n-k)\).

**Marginal variance from indicators.** In a PDA tree with \(m\ge4\) leaves, a fixed pair of leaves forms a cherry with probability \(1/(2m-3)\), by contracting the cherry. Two specified disjoint pairs simultaneously form cherries with probability \(1/[(2m-3)(2m-5)]\), by contracting both. Indicators of pairs that share a leaf cannot both be one. Consequently

\[
\mathbb EC_m=\frac{\binom m2}{2m-3},\quad
\mathbb E[C_m(C_m-1)]
=\frac{\binom m2\binom{m-2}2}{(2m-3)(2m-5)}.
\]

Inserting these into \(\operatorname{Var}(C_m)=\mathbb E[C_m(C_m-1)]+\mathbb EC_m-(\mathbb EC_m)^2\) and simplifying gives the displayed \(v(m)\). At \(m=1,2,3\) the cherry count is deterministic, hence \(v=0\).

**Strict minimum.** Extend the displayed rational function to real \(x\ge3\). Direct differentiation gives

\[
v''(x)=\frac{-3(8x^4-48x^3+90x^2-30x-45)}{(2x-5)^3(2x-3)^4}<0.
\]

Indeed, writing \(t=x-3\ge0\), the numerator polynomial is \(8t^4+48t^3+90t^2+78t+27>0\). Thus \(v'\) is strictly decreasing. It follows that \(F_n(x)=v(x)+v(n-x)\) is strictly increasing for \(3\le x\le n/2\), since \(F_n'(x)=v'(x)-v'(n-x)>0\) except when \(x=n/2\). Moreover, for all integers \(m\ge3\),

\[
v(m+1)-v(m)=
\frac{m(m-2)(m-1)(2m^2-7m+9)}{(2m-5)(2m-3)^2(2m-1)^2}>0.
\]

The polynomial \(2m^2-7m+9\) is everywhere positive (negative discriminant). So \(F_n(3)<F_n(2)<F_n(1)\) for \(n\ge6\), with the first two comparisons interpreted using \(v(1)=v(2)=v(3)=0\). Along with strict increase for \(k\ge3\), this proves unique minimization at \(k=3\), and reduces the global maximum to the singleton or the balanced split.

**Sharp maximum transition.** For even \(n=2m\), \(m\ge3\), exact common-denominator algebra yields

\[
V_{2m}(m)-V_{2m}(1)
=\frac{(m-2)(m-1)^2 P(m)}{(2m-5)(2m-3)^2(4m-7)(4m-5)^2},
\]

where \(P(m)=16m^3-164m^2+393m-270\). At integer \(m=3,4,5,6,7\), the values of \(P(m)\) are respectively \(-135,-298,-405,-360,-67\). For all integers \(m\ge8\), putting \(t=m-8\) gives \(P(m)=16t^3+220t^2+841t+570>0\). All denominators are positive.

For odd \(n=2m+1\), \(m\ge3\), similarly

\[
V_{2m+1}(m)-V_{2m+1}(1)
=\frac{2m(m-1)Q(m)}{(2m-5)(2m-3)^2(2m-1)^2(4m-5)(4m-3)^2},
\]

where

\[
Q(m)=32m^6-408m^5+1746m^4-3517m^3+3675m^2-1935m+405.
\]

For \(m=3,4,5,6\), this polynomial takes values \(-1674,-13367,-40770,-55377\). For every \(m\ge7\), write \(t=m-7\) to obtain

\[
Q(m)=32t^6+936t^5+10986t^4+64971t^3+196182t^2+256932t+60262>0.
\]

Therefore the singleton split is the unique maximum through \(n=14\), and the balanced split is the unique maximum from \(n=15\). Neither parity comparison has an equality case.

**Asymptotic difference.** Algebraic expansion gives \(v(x)=x/16-1/32-3/(32x)+O(x^{-2})\). Hence \(v(\lfloor n/2\rfloor)+v(\lceil n/2\rceil)-v(n-1)\to1/32\). This completes the proof.

## Verification

The included standalone standard-library program `verify.py` checks the algebraic sign certificates and the exact parity factorizations; computes entire cherry-count generating distributions by a root-split recurrence for all leaf counts through \(20\); verifies conditional variances for every root-split size in that range; and checks strict extrema and parity identities through \(n=200\). It runs as `python verify.py` with no dependencies. These finite checks detect algebraic mistakes but are not substitutes for the proof of the all-\(n\) statements.

## Relationship to prior work

Choi, Thompson and Wu's 2020 preprint (arXiv:2002.12643v1) treats cherry and pitchfork marginal/joint distributions under rooted and unrooted PDA and YHK models; it includes the rooted PDA cherry *marginal* variance stated here, so that formula is not claimed as new. Wu and Choi's 2015 preprint (arXiv:1508.03139) provides earlier PDA/YHK cherry–pitchfork distribution recurrences. McKenzie and Steel's earlier paper treats marginal cherry distribution under evolutionary models. The claim assessed here is the variance of the cherry count **conditional on a given root split size**, with a global strict minimizer, a complete finite-size maximizing phase diagram, and its persistent asymptotic comparison. None of the inspected relevant sections of those primary sources states this conditional extremum theorem. Conditioning and the already-known marginal variance make it straightforward to express the conditional variance, but the sharp root-split extremal classification requires the supplied strict concavity and parity-polynomial sign analysis.

## Limitations

This theorem concerns only the uniform rooted leaf-labeled PDA model, not the YHK model, nonbinary trees, random tree growth, or nonuniform leaf-label weights. It classifies conditional *variances*, not full stochastic order, distributional shape, or sampling performance. The conditional variance identity follows from familiar splitting properties; the claimed contribution is the strict global split extremum and size-15 transition. Some earlier general split/branching identity may implicitly cover its conclusions; independent historical-priority and mathematical verification have not been performed.

## References

1. K. P. Choi, A. Thompson and T. Wu, "On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees," arXiv:2002.12643v1, publicly submitted 2020-02-28; *Theoretical Population Biology* 132 (2020), 92–104. https://arxiv.org/abs/2002.12643
2. T. Wu and K. P. Choi, "On joint subtree distributions under two evolutionary models," arXiv:1508.03139v1 (2015). https://arxiv.org/abs/1508.03139
3. A. McKenzie and M. Steel, "Distributions of cherries for two models of trees," *Mathematical Biosciences* 164 (2000), 81–92. https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/cherry.pdf
