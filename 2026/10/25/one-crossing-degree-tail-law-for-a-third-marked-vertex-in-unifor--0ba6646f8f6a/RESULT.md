# One-crossing degree-tail law for a third marked vertex in uniform labelled trees

## Finding

Let \(T_n\) be uniform over the \(n^{n-2}\) labelled trees on \([n]\), where \(n\ge3\). Fix three pairwise distinct vertices \(u,v,w\). Put \(L=d_{T_n}(u,v)\), \(D=\deg_{T_n}(w)\), and
\[
F_\ell(k)=\Pr(D\ge k\mid L=\ell),\qquad 1\le\ell\le n-1,\quad k\in\mathbb Z_{\ge1}.
\]

**Theorem (sharp single crossing).** If \(n\ge4\), increasing the conditioned distance from \(1\) to \(2\) *stochastically raises* the third-vertex degree:
\[
F_2(k)\ge F_1(k)\quad\text{for every integer }k\ge1,
\]
with strict inequality for \(k=2\). But for **every** \(2\le\ell\le n-2\), the difference sequence
\[
\Delta_{\ell}(k)=F_{\ell+1}(k)-F_\ell(k),\qquad k\ge2,
\]
has precisely one sign reversal **from positive to negative** after zero terms are removed. More explicitly, \(\Delta_\ell(2)>0\), a later \(\Delta_\ell(k)<0\) exists, and no negative term precedes a positive term. Therefore neither of the two successive conditional degree laws dominates the other stochastically after the first distance increase, even though the conditional means strictly increase at *every* distance increase.

A complete exact generating-function law underlies this classification. For \(1\le\ell\le n-2\), set \(m=n-\ell-2\), \(a=(\ell-1)/(n-2)\), and \(s=\ell+1\). Let \(B\sim\operatorname{Bin}(m,1/n)\) and \(E\sim\operatorname{Bernoulli}(1/s)\), independently. Then
\[
D\mid (L=\ell)\ \overset{d}{=}
\begin{cases}
1+B,&\text{with probability }1-a,\\
2+B+E,&\text{with probability }a.
\end{cases}
\]
In particular, writing \(A(z)=1+(z-1)/n\),
\[
G_\ell(z)=\mathbb E[z^D\mid L=\ell]
=zA(z)^{n-\ell-2}\left(\frac{n-\ell-1}{n-2}+\frac{\ell-1}{n-2}\frac{z(\ell+z)}{\ell+1}\right).
\]
At \(\ell=n-1\), \(D=2\) almost surely.

For \(1\le\ell\le n-3\) the entire tail comparison has the coefficient identity
\[
\sum_{k\ge2}\Delta_\ell(k)z^k
=\frac{z^2 A(z)^{n-\ell-3}}{n(\ell+1)(\ell+2)(n-2)}
\Big[(\ell+1)^2(\ell+2)+(2n-\ell^3-\ell^2+2\ell)z-(\ell+2)(\ell-1)z^2\Big].
\]
For \(\ell=1\) the quadratic coefficient vanishes and the other two displayed coefficients are positive; for each \(\ell\ge2\), the polynomial has exactly one coefficient sign change.

## Assumptions and scope

All random trees are **unweighted**, labelled, and uniformly sampled. The third marked vertex \(w\) is distinct from both endpoints \(u,v\). The distance \(L\) takes every integer value between \(1\) and \(n-1\), each with positive probability. The stochastic-order assertion is a statement about all integer upper tails of \(D\), not just its mean.

The phrase “one sign reversal” means one reversal after omitting vanishing entries; it does not require strict signs at all intermediate thresholds. For \(n=3\), only distances \(1,2\) exist and the first stochastic dominance is strict at threshold \(2\). There is no claim about conditioning on degree of a path endpoint: that is a distinct statistic.

## Proof

Fix the ordered \(u\)-to-\(v\) path of length \(\ell\). It contains \(s=\ell+1\) vertices; the remaining \(N=n-s\) vertices must form a rooted forest attached to these \(s\) path vertices. Contracting the path to a single root gives a complete weighted graph on \(N+1\) contracted vertices, with \(s\) parallel-edge choices from each outside vertex to the root and one edge between each pair of outside vertices. The weighted Cayley identity
\[
\sum_{\tau\text{ tree on }[r]}\ \prod_{ij\in E(\tau)}x_i x_j
=\left(\sum_{i=1}^r x_i\right)^{r-2}\prod_{i=1}^r x_i
\]
(with its one-vertex limiting interpretation) shows that the total extension weight is \(s n^{N-1}\) for \(N\ge1\).

For a specified outside vertex, weighting all incident edges by \(z\) substitutes its vertex weight \(1\) by \(z\). After normalizing by the extension weight, the degree generating function is
\[
z\left(\frac{n-1+z}{n}\right)^{N-1}.
\]
For a specified path vertex, weight by \(z\) only its **new** incident edges. The multiplicity at the contracted root becomes \(s-1+z\), so the generating function for its extra degree is
\[
\frac{s-1+z}{s}\left(\frac{n-1+z}{n}\right)^{N-1}.
\]
Thus an outside vertex has degree \(1+\operatorname{Bin}(N-1,1/n)\), whereas an interior path vertex has degree \(2+\operatorname{Bin}(N-1,1/n)+\operatorname{Bernoulli}(1/s)\), independently summing the two auxiliary variates.

Conditional on \(L=\ell\), symmetry among the \(n-2\) possible nonendpoint labels shows that \(w\) is one of the \(\ell-1\) interior path vertices with probability \((\ell-1)/(n-2)\). This proves the displayed mixture and \(G_\ell\). If \(\ell=n-1\), every nonendpoint vertex lies in the Hamiltonian path and therefore has degree \(2\).

For a positive integer-valued random variable \(Y\),
\[
\sum_{k\ge1}\Pr(Y\ge k)z^k=\frac{z(1-\mathbb E[z^Y])}{1-z}.
\]
Substituting the two neighbouring \(G\)'s, cancelling \(1-z\), and expanding gives the coefficient identity in the Finding section. When \(\ell=1\), the polynomial has constant coefficient \(12\), linear coefficient \(2n\), and zero quadratic coefficient. Both nonzero coefficients are positive, so multiplying by \(A(z)^{n-4}\) proves the initial stochastic increase.

For \(2\le\ell\le n-3\), the quadratic bracket has positive constant coefficient, negative quadratic coefficient, and an unrestricted middle coefficient. Its nonzero coefficient sequence thus changes from positive to negative exactly once. The positive-coefficient linear factor \(A(z)=(n-1+z)/n\) preserves the property “at most one positive-to-negative change”: if a finite sequence is nonnegative through index \(r\) and nonpositive thereafter, multiplying its generating polynomial by \(q+pz\) for \(q,p>0\) produces a sequence nonnegative through index \(r\), nonpositive from index \(r+2\) onward, and with just one possibly mixed coefficient between. Iterating proves that the new coefficients have at most one reversal. The first and final coefficients remain **strictly** positive and **strictly** negative, respectively, so exactly one reversal occurs.

Finally, for \(\ell=n-2\), the mixture gives \(\Pr(D=1\mid L=n-2)=1/(n-2)>0\) and \(\Pr(D\ge3\mid L=n-2)=(n-3)/[(n-2)(n-1)]>0\), whereas \(D\mid (L=n-1)=2\) surely. Hence the tail difference is positive at \(k=2\), negative at \(k=3\), and zero at all higher thresholds.

The conditional mean from the mixture equals
\[
\mathbb E[D\mid L=\ell]
=1+\frac{n-\ell-2}{n}+\frac{(\ell-1)(\ell+2)}{(n-2)(\ell+1)}.
\]
For \(1\le\ell\le n-3\), its next-distance difference is
\[
\frac{2(\ell^2+3\ell+n+2)}{n(n-2)(\ell+1)(\ell+2)}>0.
\]
This also holds at the terminal comparison by directly substituting \(\ell=n-2\) and the limiting mean \(2\), completing the claim.

## Verification

Run `python3 verify_threepoint_degree_tails.py` using only the Python standard library. It exhaustively enumerates all Prüfer codes for \(3\le n\le7\) and reconstructs the joint law of the marked-vertex distance and third-vertex degree, comparing it with the exact mixture in rational arithmetic. Independently, it verifies every tail crossing and every coefficient of the difference polynomial for \(3\le n\le30\). Its successful terminal output is `VERIFY_OK`. The proof above is valid for every integer \(n\ge3\); finite checks do not establish the infinite claim.

## Relationship to prior work

The finite labelled-forest counts and their Prüfer/Foata–Fuchs constructions are classical. Addario-Berry, Donderwinkel, Maazoun and Martin give a rooted-forest coding and probabilistic consequences; their general machinery **already implies the displayed conditional one-vertex generating functions** by weighted enumeration. Those conditional marginals are explicitly not the originality claim.

Berzunza Ojeda and Janson study complete pair-distance profiles and conditioned simply generated trees, including the uniform labelled-tree case. Their investigated results address the large-tree distance profile rather than adjacent-distance third-vertex degree **tail ordering**. A related exact result in the published record, “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” proves the opposite-sign stochastic regression for the degree at a **path endpoint**, not a distinct third vertex. Even the first two conditional moments of the third vertex do not imply the classification of every threshold's sign.

The assessed new contribution is the **sharp, all-distance dichotomy**: initial stochastic dominance, followed by exactly one opposite tail crossing for every subsequent consecutive distance pair, established using the explicit quadratic factor and variation-diminishing multiplication. This is a statement-level comparison, not a claim that earlier literature lacks the requisite counting methods.

## Limitations

This theorem concerns the exact uniform labelled-tree model and distinct third vertex. The crossing location need not be the same threshold at different distances, and the theorem makes no claim of monotonicity under nonuniform tree laws. The endpoint degree, the full distance profile, and the rooted-forest code are prior knowledge. A historical equivalent in classical multivariate tree-enumeration or total-positivity literature remains possible; priority has not been independently audited. The verifier proves only finite instances; the general conclusion rests on the algebraic proof.

## References

1. G. Berzunza Ojeda and S. Janson, “The distance profile of rooted and unrooted simply generated trees,” arXiv:2009.00572, first publicly submitted 2020-09-01; *Combinatorics, Probability and Computing* 31 (2022), 368–410. https://arxiv.org/abs/2009.00572
2. L. Addario-Berry, S. Donderwinkel, M. Maazoun and J. B. Martin, “The Foata–Fuchs proof of Cayley's formula, and its probabilistic uses,” arXiv:2107.09726, first publicly submitted 2021-07-20. https://arxiv.org/html/2107.09726v2
3. “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” published mathematical research record, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae
