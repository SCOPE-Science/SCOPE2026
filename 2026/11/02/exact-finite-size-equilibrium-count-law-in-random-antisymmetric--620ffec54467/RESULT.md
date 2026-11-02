# Exact finite-size equilibrium-count law in random antisymmetric bimatrix games

## Finding
For every integer \(n\ge2\), let the row and column players have respective payoff matrices \(A\) and \(-A^{\mathsf T}\), where all \(n^2\) entries of \(A\) are independent and identically distributed with an atomless distribution. Let \(N\) be the count of pure Nash equilibria. Put \(t=z-1\). The full finite-population probability-generating function is
\[
\mathbb E[z^N]=n![x^n]\exp\!\left(x+\frac{x^2t/n^2}{1-xt/[n(n-1)]}+\sum_{m=3}^{\infty}\frac{1}{m}\left(\frac{xt}{n(n-1)}\right)^m\right).
\]
Here \([x^n]\) denotes formal coefficient extraction: only summands of \(x\)-degree at most \(n\) are required. Consequently, every \(\Pr(N=j)\) is exactly \([z^j]\) of that polynomial. In particular,
\[
\mathbb E[N]=1-\frac1n,\qquad
\operatorname{Var}(N)=1-\frac3n+\frac6{n^2}-\frac6{n^3}.
\]
For any \(n\ge2\), the sharp upper-tail probability has the exact cycle-partition formula
\[
\Pr(N=n)=\frac{n!}{[n(n-1)]^n}[x^n]\exp\!\left(\sum_{m=3}^{\infty}\frac{x^m}{m}\right).
\]
It equals zero for \(n=2\), while for \(3\le n\le5\) it reduces to \((n-1)!/[n(n-1)]^n\); for \(n\ge6\) multiple disjoint cycles also contribute. For illustration, the exact laws for \(n=2,3,4\), in increasing order of \(N\), are respectively \((1/2,1/2)\), \((47/108,17/36,1/12,1/108)\), and \((469/1152,389/864,37/288,1/72,1/3456)\).

## Assumptions and scope
There are precisely two players and \(n\) available pure strategies per player. The row player's payoff is \(A_{ij}\), and the column player's payoff at the same profile is \(-A_{ji}\). Matrix entries are iid and atomless; the distribution need not have moments or a density. A pure Nash equilibrium means that neither player can strictly increase their payoff by changing their action unilaterally. Every column has almost surely a unique maximum and minimum, at distinct row indices. All identities hold exactly for every integer \(n\ge2\); the result does not require an asymptotic approximation.

## Proof
For each column index \(v\), let \(H_v\) and \(L_v\) be the row indices of its largest and smallest entries. The iid atomless assumption implies that the pairs \((H_v,L_v)\), independently over the columns, are uniform among the \(n(n-1)\) ordered pairs of distinct indices. By the payoff definition, \((i,j)\) is a pure Nash equilibrium exactly when \(H_j=i\) and \(L_i=j\). Its indicator is zero for \(i=j\). Regard every possible off-diagonal equilibrium \((i,j)\) as a directed arc \(j\to i\) on the vertex set \(\{1,\dots,n\}\).

For any prescribed set of simultaneous equilibrium events, the resulting arc digraph must have indegree and outdegree at most one: each column has only one minimum and one maximum. Loops cannot occur, and a directed two-cycle would require \(H_v=L_v\) in each of its two columns, also impossible. Conversely, every digraph with those degree restrictions and without loops or directed two-cycles corresponds to a consistent set of equilibrium events. Such a digraph is a disjoint union of isolated vertices, directed paths of length at least one, and directed cycles of length at least three.

If a consistent set has \(k\) arcs, let \(h\) denote the number of vertices having both one incoming and one outgoing arc. On each such vertex the conditions specify both its maximum and minimum, at distinct positions, with probability \(1/[n(n-1)]\); at each remaining constrained vertex exactly one extreme is specified, with probability \(1/n\). Independence across columns makes the probability of simultaneous realization exactly
\[
 n^{-2k}\left(\frac{n}{n-1}\right)^h.
\]
Indeed, among the \(2k\) prescribed maximum/minimum positions, \(h\) pairs use the same column and the others occur in distinct columns.

Expand \(\mathbb E[(1+t)^N]\) by subsets of realized equilibrium indicators. Each arc contributes a factor \(t\). To enumerate admissible labeled arc digraphs, use the labeled exponential formula: an isolated vertex contributes \(x\). A directed path with \(m\ge2\) vertices has \(m!\) directed linear orders on a prescribed label set, \(m-1\) arcs and \(m-2\) internal vertices, so its exponential-generating-function contribution is
\[
 x^m\frac{t^{m-1}}{n^{2(m-1)}}\left(\frac{n}{n-1}\right)^{m-2}.
\]
Summing over \(m\ge2\) yields \(x^2t/n^2\big/(1-xt/[n(n-1)])\). A directed cycle with \(m\ge3\) vertices has \((m-1)!\) labeled cyclic orders, and all \(m\) vertices are doubly constrained, giving contribution \(\frac1m(xt/[n(n-1)])^m\). The exponential formula for disjoint unions now gives precisely the claimed probability-generating function, after replacing \(t\) by \(z-1\).

For the moments, a single prescribed off-diagonal equilibrium occurs with probability \(n^{-2}\), giving \(\mathbb E[N]=(n-1)/n\). For an unordered pair of distinct equilibria, the only possible simultaneous arc shapes are two vertex-disjoint arcs and a two-arc directed path; two-cycles are forbidden. They occur with \((n)_4/2\) and \((n)_3\) labelings, and respective probabilities \(n^{-4}\) and \(1/[n^3(n-1)]\). Therefore
\[
\mathbb E\binom N2=\frac{(n)_4}{2n^4}+\frac{(n)_3}{n^3(n-1)}
=\frac{(n-2)(n^2-2n+3)}{2n^3},
\]
where \((n)_k\) is the falling factorial (zero for \(k>n\)). Substituting \(\operatorname{Var}(N)=2\mathbb E\binom N2+\mathbb E N-(\mathbb E N)^2\) yields the variance formula.

Since at most one equilibrium can share any given column, \(N\le n\). An admissible arc digraph with all \(n\) arcs must be a directed permutation consisting exclusively of cycles of length at least three. **But multiple cycles are possible:** consequently its exact probability is not generally a single-cycle expression. The coefficient formula already gives \(\Pr(N=n)\) exactly, and the explicit single-cycle probability \((n-1)!/[n(n-1)]^n\) is only one contribution. The correct all-cycle expression is \(n![x^n]\exp(\sum_{m\ge3}(x/[n(n-1)])^m/m)\). This formula includes every permitted cycle partition and also covers \(n=2\) with value zero.

## Verification
The supplementary standalone file `verify.py` computes the probability-generating polynomial by exact rational arithmetic using the labeled exponential recurrence. It checks normalization, nonnegativity, mean, and variance for \(2\le n\le10\), and compares the entire law against independent exhaustive enumeration of the columnwise maximum/minimum choices for \(n=2,3,4\), totaling \(4+216+20{,}736=20{,}956\) ordered-column configurations. Execute `python verify.py` with Python 3 and no third-party packages.

## Relationship to prior work
Karelas, Lugosi, and Zhang (2026), Section 4.1, prove the mean \(1-1/n\) and an asymptotic Poisson law for equilibria of \((A,-A^{\mathsf T})\). The present exact coefficient formula is a finite-size refinement: it retains interactions between extreme positions in shared columns and the combinatorics of directed cycles. Stanford (1996) derives exact and asymptotic equilibrium laws for the **different** symmetric model \((A,A^{\mathsf T})\). Classical independent-payoff equilibrium laws concern two independent payoff arrays, unlike the antitranspose dependence here. These different statements do not directly yield the formula displayed above.

## Limitations
The law relies on independent, identically distributed, atomless entries, and exactly the negative-transpose payoff relation. It does not apply unchanged to correlated entries, ties, general zero-sum games \((A,-A)\), or mixed Nash equilibria. The all-equilibria tail must include all partitions into cycles of length at least three; a single-cycle term alone is insufficient for larger \(n\). Full-text access was unavailable for some older random-game articles, so publication priority beyond the inspected sources remains provisional.

## References
Karelas, G. N., Lugosi, G., and Zhang, R.-R. (2026), *Cycle structure of best-response dynamics in random bimatrix games*, arXiv:2610.29153v1, publicly submitted October 21, 2026, Section 4.1, https://arxiv.org/html/2610.29153v1 .

Stanford, W. (1996), *The Limit Distribution of Pure Strategy Nash Equilibria in Symmetric Bimatrix Games*, Mathematics of Operations Research 21(3), 726–733, https://doi.org/10.1287/moor.21.3.726 .

Stanford, W. (1995), *A Note on the Probability of k Pure Nash Equilibria in Matrix Games*, Games and Economic Behavior 9(2), 238–246, https://doi.org/10.1006/game.1995.1019 (bibliographic record consulted; full text not inspected).
