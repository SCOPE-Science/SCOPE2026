# Exact size-resolved blocking-coalition counts in two-type fractional hedonic games

## Finding

In a simple symmetric fractional hedonic game whose valuation graph is a complete bipartite graph \(K_{a,b}\), the entire **blocking-coalition size polynomial** of *any given partition* is computable exactly in polynomial time. For every \(a,b\geq1\), every partition \(\pi\) and the eligible-agent counts defined below,

\[
P_\pi(z)=\sum_{x=1}^{a}\sum_{y=1}^{b}
\binom{A_\pi(x,y)}{x}\binom{B_\pi(x,y)}{y}z^{x+y}.
\]

In particular the exact fraction of all coalitions which strictly core-block \(\pi\) is \(\varepsilon_\pi=P_\pi(1)/2^{a+b}\). All coefficients and a decision about core stability can be obtained in \(O((a+b)^2+ab\log(a+b))\) integer-arithmetic and comparison operations.

For the natural partition consisting of \(a\) mixed pairs and \(m\) extra singleton agents on the larger side, where \(a\geq1\), \(m\geq0\), and the graph is \(K_{a,a+m}\), the number of blocking coalitions is exactly

\[
M(a,m)=\sum_{x=1}^{a}\sum_{y=x+1}^{m}\binom ax\binom my,
\qquad \varepsilon_{a,m}=2^{-(2a+m)}M(a,m).
\]

This partition is core-stable precisely when \(m\leq1\); at \(m=2\) it has exactly \(a\) blockers. Moreover, if \(a\) tends to infinity and \(m=a+t\sqrt a+o(\sqrt a)\) for a fixed real \(t\), then

\[
2^a\varepsilon_{a,m}\longrightarrow\Phi(t/\sqrt2),
\]

where \(\Phi\) denotes the standard normal distribution function. If \(m/a\to c<1\) the rescaled fraction tends to zero, whereas if \(m/a\to c>1\) it tends to one. This describes a Gaussian imbalance transition in the probability of a random coalition blocking a matching-based partition, even though some such partitions are not in the core.

## Assumptions and scope

The agents are the disjoint union \(U\sqcup W\), with \(|U|=a\geq1\) and \(|W|=b\geq1\). Distinct agents have valuation one if they belong to opposite sides and zero otherwise; an agent's self-valuation is zero. Agent \(i\)'s utility in a nonempty coalition \(S\ni i\) equals the number of her opposite-side neighbors in \(S\), divided by \(|S|\). For an arbitrary partition \(\pi\), a nonempty coalition \(S\) **strictly core-blocks** \(\pi\) exactly when each agent in \(S\) strictly prefers \(S\) to her block \(\pi(i)\). Indifference does not count as blocking. The uniform sampling space is all \(2^{a+b}\) subsets, including the empty set (which cannot block).

For each agent \(i\), put \(u_i=|\pi(i)\cap U|\) and \(v_i=|\pi(i)\cap W|\). Thus \(u_i\geq1\) for \(i\in U\), and \(v_i\geq1\) for \(i\in W\). For each integer pair \(1\leq x\leq a\), \(1\leq y\leq b\), define

\[
A_\pi(x,y)=|\{i\in U:y u_i>x v_i\}|,
\qquad
B_\pi(x,y)=|\{j\in W:x v_j>y u_j\}|.
\]

Use \(\binom nk=0\) if \(k>n\). The size polynomial records one coefficient for each possible coalition cardinality, not just the total. These are **core** blockers, not weak blockers defining the strict core.

## Proof

**Exact eligibility.** A candidate coalition meeting \(U\) in \(x\) agents and \(W\) in \(y\) agents gives any of its \(U\)-members utility \(y/(x+y)\). The old utility of \(i\in U\) is \(v_i/(u_i+v_i)\), so strict improvement is equivalent, by cross multiplication with positive denominators, to \(y u_i>x v_i\). Similarly a \(W\)-member strictly improves exactly when \(x v_j>y u_j\). A one-sided candidate gives all its members utility zero, which cannot strictly improve a nonnegative previous utility. Thus blockers must have \(x,y\geq1\).

For fixed \(x,y\), every choice of precisely \(x\) agents among the \(A_\pi(x,y)\) eligible \(U\)-agents and \(y\) among the \(B_\pi(x,y)\) eligible \(W\)-agents blocks. No other choice does. Every coalition has a unique pair of side counts, hence summation without duplication gives the stated polynomial and the exact uniform-sampling fraction.

**Computing the polynomial.** For \(i\in U\), eligibility is the strict comparison \(v_i/u_i<y/x\); for \(j\in W\), it is \(u_j/v_j<x/y\). Both stored ratios have positive denominators. Sort these two rational lists using cross-products to avoid floating-point error. For each of the \(ab\) pairs \(x,y\), binary searches give both strict-rank counts in \(O(\log(a+b))\) comparisons. Pascal's recurrence precomputes all \(\binom nk\) for \(0\leq k\leq n\leq a+b\) in \(O((a+b)^2)\) integer operations. Updating the coefficient at degree \(x+y\) takes constant additional operations. This proves the stated complexity, excluding the bit cost of large integers; the numbers may have exponentially many possible subsets but only \(O(a+b)\) output coefficients.

**Matched pairs and the core boundary.** Suppose \(b=a+m\) and the partition has \(a\) disjoint mixed pairs plus \(m\) singleton \(W\)-agents. Each \(U\)-agent is in a pair and has old utility \(1/2\), hence strictly improves only if \(y>x\). Each paired \(W\)-agent also has old utility \(1/2\) and strictly improves only if \(x>y\). No blocking coalition can contain both types of paired agents. A blocker must contain a positive number \(x\) of paired \(U\)-agents and \(y>x\) of the \(m\) unmatched \(W\)-agents, all of which strictly improve from utility zero. Conversely every such choice blocks, yielding the formula for \(M(a,m)\). If \(m\leq1\), no \(y>x\geq1\) is possible. If \(m\geq2\), selecting one paired \(U\)-agent and two unmatched \(W\)-agents gives a blocker. For \(m=2\), those \(a\) choices are all blockers. As a concrete example, \(M(3,5)=132\) and \(\varepsilon_{3,5}=33/512\).

**Asymptotic transition.** Let \(X\sim\mathrm{Bin}(a,1/2)\) and \(Y\sim\mathrm{Bin}(m,1/2)\) be independent. Enumerating equally likely subsets gives the exact identity

\[
2^a\varepsilon_{a,m}=\mathbb P(Y>X,\ X\geq1).
\]

The restriction \(X\geq1\) changes \(\mathbb P(Y>X)\) by at most \(2^{-a}\). If \(m=a+t\sqrt a+o(\sqrt a)\), the mean of \(Y-X\) is \((m-a)/2\) and its variance is \((m+a)/4\sim a/2\). The central limit theorem for sums of independent bounded Bernoulli variables therefore gives \(\mathbb P(Y-X>0)\to\Phi(t/\sqrt2)\); equality probabilities vanish by continuity of the Gaussian limit. If \(m/a\to c\ne1\), the difference of means is of order \(a\) while its standard deviation is of order \(\sqrt a\), so Chebyshev's inequality yields the two one-sided limits. The conclusions follow.

## Verification

The standalone standard-library script `verify.py` evaluates the size-polynomial formula independently against literal rational utilities and all nonempty coalitions. It passed **2,628 complete labeled set partitions**, **19,814 coefficient comparisons**, **450 additional randomized partitions**, and **90 matched-pair configurations**. The tested exhaustive instances have \(1\leq a,b\leq4\) and \(a+b\leq7\). The larger randomized cases have \(1\leq a,b\leq6\). The script checks the sharp \(m\leq1\) stability boundary, \(M(a,2)=a\), and \(M(3,5)=132\). The proof, not the finite experiments, establishes the unrestricted theorem; the Gaussian limit follows analytically from the classical central limit theorem.

To reproduce, save the embedded `verify.py` and run `python verify.py` using a Python 3 standard-library installation.

## Relationship to prior work

Aziz, Brandl, Brandt, Harrenstein, Olsen and Peters established that Bakers-and-Millers games on complete multipartite graphs have a strict-core partition, including the grand coalition, and characterized strict-core partitions (Theorem 5.3 and Corollary 5.4 of *Fractional Hedonic Games*). These are **not** new existence or strict-core classification claims here. The new object is the exact *size distribution of strictly blocking coalitions for every supplied, possibly unstable partition*, together with the sharp matching-split count and its Gaussian imbalance window.

Fioravanti, Flammini, Kodric and Varricchio introduced \(\varepsilon\)-fractional core stability, interpreted as the uniform random-coalition blocking probability, and derived approximate guarantees for general simple fractional games. Their broad existence theorem does not furnish the present exact partition-by-partition size enumerator. The later results of Demeulemeester and Peters concern multiplicative improvement factors and coalition size restrictions, not the number of blocking coalitions. The restricted-location Bakers-and-Millers model of Krogmann, Lenzner and Skopalik analyzes Nash equilibria, not the strict core-blocking distribution of the unrestricted complete bipartite game.

## Limitations

Only simple, symmetric, **complete bipartite** valuation graphs are covered, with coalition utility normalized by full coalition size. The counting guarantee is an arithmetic/comparison complexity statement, not a bit-complexity bound. The exact formula does not evaluate arbitrary sampling distributions or count weakly blocking coalitions. The matching asymptotics are for the specific paired-plus-singletons partition and uniform sampling; they do not imply that this partition is socially optimal or that it is in the strict core. A complete external priority audit has not been performed, and an equivalent specialized enumeration could still exist.

## References

1. S. Fioravanti, M. Flammini, B. Kodric, G. Varricchio, *ε-fractional Core Stability in Hedonic Games*, arXiv:2311.11101v1, first publicly posted 2023-11-18. https://arxiv.org/abs/2311.11101
2. H. Aziz, F. Brandl, F. Brandt, P. Harrenstein, M. Olsen, D. Peters, *Fractional Hedonic Games*, arXiv:1705.10116 (conference precursor 2014), §§3, 5.3 and 5.5. https://arxiv.org/abs/1705.10116
3. T. Demeulemeester, J. Peters, *Quantifying Core Stability Relaxations in Hedonic Games*, arXiv:2412.01666v2, 2024. https://arxiv.org/abs/2412.01666
4. S. Krogmann, P. Lenzner, A. Skopalik, *The Bakers and Millers Game with Restricted Locations*, arXiv:2501.05334, 2025. https://arxiv.org/abs/2501.05334
