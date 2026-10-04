# Sharp five-alternative separation of the bipartisan and uncovered sets
## Finding
Let \(T\) be a tournament. Its **bipartisan set** \(BP(T)\) is the support of the unique maximal lottery of the symmetric zero-sum tournament game. Its **uncovered set** \(UC(T)\) consists of the alternatives that are not covered.

The classical inclusion
\[
BP(T)\subseteq UC(T)
\]
is an equality for every tournament on at most \(4\) alternatives.

At order \(5\), strict inclusion occurs for the first time. Among all
\[
2^{\binom52}=2^{10}=1024
\]
labeled five-alternative tournaments, exactly
\[
120
\]
satisfy
\[
BP(T)\subsetneq UC(T).
\]
Hence the exact uniform-tournament incidence is
\[
\frac{120}{1024}=\frac{15}{128}.
\]

Every strict case has
\[
|BP(T)|=3,
\qquad
|UC(T)|=4.
\]
Moreover, all \(120\) strict cases form a single isomorphism class.

A canonical representative on alternatives \(A,B,C,D,E\) has directed edges
\[
A\to B,\ C\to A,\ D\to A,\ A\to E,\ C\to B,
\]
\[
B\to D,\ E\to B,\ D\to C,\ E\to C,\ E\to D.
\]
Its unique maximal lottery is
\[
p=\left(\frac13,0,0,\frac13,\frac13\right),
\]
so
\[
BP(T)=\{A,D,E\}.
\]
The expected tournament-game payoff of this lottery against \((A,B,C,D,E)\) is
\[
\left(0,\frac13,\frac13,0,0\right),
\]
which verifies the maximal-lottery inequalities exactly.

The uncovered set is
\[
UC(T)=\{A,C,D,E\}.
\]
Thus \(C\) is the unique first-layer alternative that survives covering but receives zero probability in the tournament game's equilibrium.

The complete order-five joint-size census is
\[
\begin{array}{c|r}
(|BP(T)|,|UC(T)|) & \text{labeled tournaments}\\ \hline
(1,1) & 320\\
(3,3) & 520\\
(3,4) & 120\\
(5,5) & 64.
\end{array}
\]

## Assumptions and scope
A tournament is a complete asymmetric directed graph. The maximal lottery uses payoff \(+1\) for a win, \(-1\) for a loss, and \(0\) on the diagonal. The bipartisan set is the support of the unique equilibrium lottery.

The uncovered set uses the standard covering relation: \(y\) covers \(x\) when \(y\) defeats \(x\) and every alternative defeated by \(x\) is also defeated by \(y\).

The result is a complete classification through order \(5\). It does not give a formula for larger tournaments.

## Proof
For each tournament of orders \(1\) through \(5\), the verifier computes the maximal lottery exactly in two independent ways.

The first method enumerates candidate supports, solves the equilibrium equalities over the rationals by Gaussian elimination, and checks positivity and every external payoff inequality.

The second method enumerates odd supports and obtains the null vector of each skew-symmetric support matrix from principal Pfaffians. It independently checks positivity, normalization, and all maximal-lottery inequalities.

The two maximal-lottery implementations agree on every tournament.

The uncovered set is also computed twice: directly from the covering relation and independently from the equivalent two-step-king characterization. These implementations agree on every tournament.

The exhaustive disagreement counts are
\[
0,0,0,0,120
\]
for tournament orders \(1,2,3,4,5\), respectively. Thus order \(5\) is the sharp separation threshold.

At order \(5\), all \(120\) strict cases have size pair \((3,4)\). Canonicalizing all strict cases under every one of the \(5!=120\) relabelings yields one representative only. Its orbit therefore has full size \(120\), proving the isomorphism statement.

## Verification
The embedded `verify_bipartisan_uncovered_first_layer.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- all tournaments of orders \(1\) through \(5\);
- two independent maximal-lottery computations;
- two independent uncovered-set computations;
- the inclusion \(BP(T)\subseteq UC(T)\) throughout the domain;
- equality through order \(4\);
- exactly \(120\) strict cases at order \(5\);
- exact probability \(15/128\);
- the order-five joint-size census \(320,520,120,64\);
- a single strict isomorphism class of orbit size \(120\);
- the canonical equilibrium lottery and payoff vector.

Run:

`python3 verify_bipartisan_uncovered_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Laffond, Laslier, and Le Breton introduced the bipartisan set as the support of the unique equilibrium of the symmetric tournament game. Later tournament-solution work records the standard refinement relation that the bipartisan set is contained in the uncovered set.

Brandt develops a unified tournament-solution framework containing both the uncovered and bipartisan sets. Brandt and Grundbacher restate the maximal-lottery definition in exact skew-adjacency form and use it in a modern structural comparison with the Banks set.

The prior literature therefore supplies the definitions, uniqueness of the maximal lottery, and the inclusion \(BP(T)\subseteq UC(T)\). The contribution here is the sharp first strict order and its complete classification: equality through order \(4\), exactly \(120\) strict five-alternative tournaments, and a single unlabeled strict type.

Targeted searches for the exact count \(120\), probability \(15/128\), order-five threshold, and single-isomorphism-class statement did not locate an equivalent published result.

## Limitations
The result is an exact finite first-layer census, not an asymptotic theorem or a larger-order formula.

The originality search cannot exclude an unindexed historical table, teaching note, code archive, or unpublished enumeration containing the same order-five classification.

The 1993 foundational article was accessible bibliographically but not as lawful full text in the inspected sources. The first-public-date field therefore uses the earliest day-resolved open primary source inspected in full enough to anchor the tournament-solution framework.

## References
1. G. Laffond, J.-F. Laslier, and M. Le Breton, “The Bipartisan Set of a Tournament Game,” *Games and Economic Behavior* 5 (1993), 182–201. DOI: 10.1006/game.1993.1010.
2. F. Brandt, “Minimal Stable Sets in Tournaments,” arXiv:0803.2138, first submitted 14 March 2008; journal version, *Journal of Economic Theory* 146 (2011), 1481–1499. DOI: 10.1016/j.jet.2011.05.004.
3. F. Brandt and F. Grundbacher, “The Banks set and the bipartisan set may be disjoint,” arXiv:2308.01881; *Social Choice and Welfare* 66 (2026), 349–355. DOI: 10.1007/s00355-025-01608-8.
