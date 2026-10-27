# Cycle delegations have an exact ballot-count law and a sharp two-guru tie extremum

## Finding

Fix a simple labeled cycle \(C_n\) with \(n\ge3\). Suppose a fixed set of \(2\le k\le n\) direct voters (gurus) cast two-candidate ballots, and each remaining vertex chooses one of its two neighbors as delegate. A delegation is *feasible* precisely when following every delegation chain eventually reaches a direct voter; all feasible delegations receive equal probability. Let \(g_0,\dots,g_{k-1}\) be the gurus in clockwise order, \(m_i\ge0\) the number of intervening nongurus on the clockwise arc from \(g_i\) to \(g_{i+1}\), with subscripts modulo \(k\), and \(\sum_i m_i=n-k\).

**Joint-law theorem.** There are exactly \(N=\prod_{i=0}^{k-1}(m_i+1)\) feasible delegations. Their complete unnormalized joint guru-weight enumerator is

\[
\sum_{d\text{ feasible}}\prod_{i=0}^{k-1}z_i^{W_i(d)}
=\left(\prod_{i=0}^{k-1}z_i\right)
 \prod_{i=0}^{k-1}\left(\sum_{x=0}^{m_i}z_i^x z_{i+1}^{m_i-x}\right).
\]

In particular, if \(S\) is any subset of gurus, then

\[
\mathbb E W_i=1+\frac{m_{i-1}+m_i}{2},\qquad
\operatorname{Var}\left(\sum_{i\in S}W_i\right)
=\sum_{i:\,\mathbf 1_{i\in S}\ne\mathbf 1_{i+1\in S}}
\frac{m_i(m_i+2)}{12}.
\]

Equivalently the covariance matrix of the guru-weight vector is the weighted cycle *multigraph* Laplacian with edge weights \(m_i(m_i+2)/12\). The multigraph convention matters for two gurus, when the two physical arcs are parallel edges.

**Exact winner-count theorem.** Let \(S\) be the set of gurus voting for candidate \(A\), and define \(\alpha=|S|+\sum_{i:\,i,i+1\in S}m_i\), \(J=\{i:\mathbf1_{i\in S}\ne\mathbf1_{i+1\in S}\}\), and \(H=\{i:\mathbf1_{i\in S}=\mathbf1_{i+1\in S}\}\). The number of feasible delegations giving \(A\) precisely \(r\) votes is the coefficient of \(z^r\) in

\[
F_A(z)=z^{\alpha}\prod_{i\in H}(m_i+1)
                  \prod_{i\in J}(1+z+\cdots+z^{m_i}).
\]

Thus the number of delegations making \(A\) a *weak majority winner* is \(\sum_{r:\,2r\ge n}[z^r]F_A(z)\), and the number making it the *unique strict majority winner* is \(\sum_{r:\,2r>n}[z^r]F_A(z)\). These counts admit an exact polynomial-time algorithm by truncated integer-polynomial convolution; straightforward convolution uses \(O(n^2)\) arithmetic operations.

**Sharp tied-election effect.** Suppose \(k=2\), the two gurus vote for opposing candidates, and \(n\ge4\) is even. Then

\[
\Pr(\text{tie})=\frac{\min(m_0,m_1)+1}{(m_0+1)(m_1+1)}
=\frac{1}{\max(m_0,m_1)+1},
\quad
\frac1{n-1}\le \Pr(\text{tie})\le\frac2n.
\]

The lower bound holds exactly for adjacent gurus and the upper bound exactly for antipodal gurus. Each guru's candidate has strict-win probability \((1-\Pr(\text{tie}))/2\). For odd \(n\) there is never a tie.

## Assumptions and scope

The vertices of \(C_n\) are labeled and the guru set and their expressed alternatives are **fixed**, not drawn randomly. Nongurus must delegate to exactly one of their two graph neighbors; a guru must vote directly and has no outgoing delegation edge. Every feasible complete orientation is counted once. Uniformity is the conditional law obtained from independently fair neighbor choices given that all chains terminate at gurus. Every vertex has unit voting weight, and the delegation terminus receives the entire transitive weight. Ties are included for weak-majority winner counts and excluded for strict winner counts. The formulas include zero-length arcs and adjacent gurus; \(k=2\) uses both distinct arcs of the cycle.

## Proof

**1. Exact description of feasible arcs.** Any directed cycle in a graph obtained by orienting one incident edge outward from each nonguru would have to be either a pair of adjacent vertices delegating to each other or a directed circuit traversing the entire underlying cycle. The latter is impossible because at least two vertices are gurus and have no outgoing edge. On an arc between consecutive gurus, a pair of adjacent nongurus forms a directed two-cycle exactly when a rightward arrow is followed by a leftward arrow. The assignments with no such pattern consist precisely of a prefix of leftward arrows followed by a suffix of rightward arrows. The prefix length \(X_i\) has the \(m_i+1\) values \(0,\dots,m_i\), including the empty and full prefixes. Every such assignment reaches one of the two adjacent gurus. Since distinct arcs have disjoint interior vertices and there are no remaining cyclic obstructions, choices are independent and the count is \(N=\prod_i(m_i+1)\). Under the uniform feasible-delegation measure, each \(X_i\) is independently uniform on its own finite interval.

**2. Weight law and joint enumerator.** On arc \(i\), exactly \(X_i\) interior votes terminate at \(g_i\), while exactly \(m_i-X_i\) terminate at \(g_{i+1}\). Guru \(i\) therefore receives its own ballot, \(m_{i-1}-X_{i-1}\) votes from the preceding arc, and \(X_i\) from the succeeding arc:

\[
W_i=1+m_{i-1}-X_{i-1}+X_i.
\]

For each arc, independently sum its \(m_i+1\) monomials \(z_i^x z_{i+1}^{m_i-x}\), then multiply the guru ballot factors \(\prod_i z_i\). This gives the complete joint enumerator. Since a discrete uniform variable on \(\{0,\ldots,m\}\) has expectation \(m/2\) and variance \(m(m+2)/12\), its weight means are as claimed. The random part of the weight vector is \(\sum_iX_i(e_i-e_{i+1})\), hence its covariance is \(\sum_i\frac{m_i(m_i+2)}{12}(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T}\), exactly the asserted Laplacian. Summing coordinates over \(S\) gives the cut-variance identity. This derivation also covers \(k=2\) because the two oriented arcs are separate and their variances add.

**3. Vote-tally enumerator.** An arc with two \(A\)-voting endpoints always supplies all \(m_i\) votes to \(A\), with \(m_i+1\) feasible orientations. With two \(B\)-voting endpoints it always supplies zero \(A\) votes, again with \(m_i+1\) orientations. For opposing endpoints, as the cut ranges over its \(m_i+1\) positions, the \(A\)-vote contribution takes every integer \(0,\ldots,m_i\) exactly once, in one order or the other. Multiplying these factors and the \(|S|\) fixed guru ballots proves \(F_A\). Its coefficients are actual counts, so summing them on the required threshold side proves both winner-count claims. All degrees are at most \(n\); multiplying the cut-arc factors consecutively uses at most \(O(n^2)\) integer-arithmetic operations because their degrees sum to at most \(n\).

**4. Two-guru tie theorem and sharpness.** Write the independent arc contributions to \(A\) as \(U\in\{0,\ldots,m_0\}\) and \(V\in\{0,\ldots,m_1\}\), both uniform. Then \(W_A=1+U+V\) in distribution, with \(m_0+m_1=n-2\); \(W_B=n-W_A\). If \(n\) is even, a tie requires \(U+V=(n-2)/2\). Among the \((m_0+1)(m_1+1)\) equiprobable pairs, exactly \(\min(m_0,m_1)+1\) solve this equation: if \(m_0\le m_1\), each \(U\in\{0,\ldots,m_0\}\) determines an admissible \(V=(m_0+m_1)/2-U\), with the interval endpoints valid because \(m_0+m_1\) is even and \(m_1\ge m_0\). This proves the tie formula. Since \(m_0+m_1=n-2\), the largest possible \(\max(m_0,m_1)\) is \(n-2\) (adjacent gurus) and its smallest possible value is \((n-2)/2\) (antipodal gurus); both occur. Reflecting \((U,V)\) to \((m_0-U,m_1-V)\) exchanges strict \(A\) wins with strict \(B\) wins, establishing equal strict-win probabilities. For odd \(n\), the total vote count is odd, so a tie is impossible.

## Verification

Run `python verify_cycle_delegations.py` using Python 3 and only its standard library. The verifier directly enumerates all choices of clockwise or counterclockwise delegation for each nonguru, explicitly follows every path to reject directed cycles, and compares those results with an independently implemented uniform-cut law. Over \(1418\) cycle/guru configurations with \(3\le n\le10\) and \(2\le k\le\min(5,n)\), it checked \(19966\) feasible assignments; all exact count distributions, means, coalition variance identities, two-candidate tally-generating coefficients, and two-guru tie counts agreed. Fractions are compared exactly. These finite checks supplement but do not replace the proof for all \(n\).

## Relationship to prior work

Bentert, Boehmer, Rymar, and Tannenberg introduced formal winner-determination and robustness problems in liquid democracy and specifically identified counting delegations that make a candidate win as a useful question. Their decision complexity and winner algorithms do not state the present cycle-specific **joint weight law**, exact coefficient formula, coalition-cut variance, or sharp geographic tie extrema. Utke and Schmidt-Kraepelin develop uniform weighted-branching and random-walk assignment machinery that can obtain individual fractional connection probabilities on general graphs, but do not present this **joint election outcome distribution** or two-guru sharp tie formula; generic forest enumeration underlies rather than duplicates the explicit formulas here. Colley, Delemazure, and Gilbert analyze a priori power indices for a different random delegation model, rather than uniform cycle-feasible fixed-guru counting. Berinsky and collaborators study voting accuracy under competence-dependent random delegation, and derive concentration guarantees rather than these exact conditional fixed-root cycle laws. The result is narrowly about simple cycles, uniform feasible choices, and fixed direct voters.

## Limitations

This does not address arbitrary graphs, random or endogenous guru sets, nonuniform delegate preferences, ranked or fractional delegation, independent agent competence, nor actual voter behavior. The covariance identity is conditional on fixed gurus; it is not a universal statement about independently sampled randomized elections. The power-counting formula computes the number of delegation outcomes, not the number of distinct eventual opinion-weight vectors. For the two-guru tie extremum, the sharp bounds require an even cycle; for odd \(n\) the tie count is zero. Existing general rooted-forest and spanning-tree methods may imply abstract forms of some of the marginal counts, so the novelty is the joint closed-form factorization, count-by-tally evaluation, and sharp tie-position law, not the existence of an abstract matrix-tree theorem. Literature beyond the inspected material remains a bibliographic risk. No independent validation has been performed.

## References

1. Matthias Bentert, Niclas Boehmer, Maciej Rymar, and Henri Tannenberg, *Who won? Winner Determination and Robustness in Liquid Democracy*, arXiv:2205.05482 (first public version 2022-05-11), https://arxiv.org/abs/2205.05482.
2. Markus Utke and Ulrike Schmidt-Kraepelin, *Anonymous and Copy-Robust Delegations for Liquid Democracy*, arXiv:2307.01174 (2023), https://arxiv.org/abs/2307.01174.
3. Romain Colley, Théo Delemazure, and Hugo Gilbert, *Measuring a Priori Voting Power — Taking Delegations Seriously*, arXiv:2301.02462 (2023), https://arxiv.org/abs/2301.02462.
4. Adam Berinsky et al., *Tracking Truth with Liquid Democracy*, arXiv:2107.11868 (2021), https://arxiv.org/abs/2107.11868.
