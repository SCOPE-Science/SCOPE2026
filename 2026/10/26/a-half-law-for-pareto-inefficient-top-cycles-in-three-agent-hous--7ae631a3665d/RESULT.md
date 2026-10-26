# A half-law for Pareto-inefficient top cycles in three-agent house assignment

## Finding
Consider three agents and three distinguishable houses, with each agent having a strict ranking and each house assigned to exactly one agent. Equip the 216 labeled preference profiles with the uniform distribution. Write \(T(P)\) for the top cycle of the weak majority relation over the six bijective assignments, \(E(P)\) for the Pareto-optimal assignment set, and \(U(P)\) for the McKelvey uncovered set. Then the complete joint distribution is:

| \((|T|,|E|,|U|)\) | Number of profiles |
|---|---:|
| \((1,1,1)\) | 48 |
| \((2,2,2)\) | 36 |
| \((4,3,2)\) | 36 |
| \((4,4,2)\) | 18 |
| \((6,3,2)\) | 36 |
| \((6,4,2)\) | 36 |
| \((6,6,6)\) | 6 |

In particular, \(U(P)\subseteq E(P)\subseteq T(P)\) for every profile, and exactly half the profiles have Pareto-dominated assignments in their top cycle:
\[
\Pr\bigl(T(P)\setminus E(P)\ne\varnothing\bigr)=\frac12.
\]
The size \(D(P)=|T(P)\setminus E(P)|\) has distribution
\[
\Pr(D=0)=\frac12,\qquad \Pr(D=j)=\frac16\quad(j=1,2,3),
\]
so \(\mathbb E[D]=1\), and conditional on \(D>0\) the number of Pareto-dominated top-cycle assignments is uniform on \(\{1,2,3\}\). The McKelvey uncovered set contains exactly two assignments in 162 of the 216 profiles and never contains a Pareto-dominated assignment. Two agents cannot exhibit the top-cycle inefficiency, making three the smallest square assignment market with this phenomenon.

## Assumptions and scope
Let agents be \(N=\{1,2,3\}\), houses \(H=\{1,2,3\}\), and \(\mathcal M\) the six bijections \(N\to H\). Each strict preference order \(\succ_i\) is one of the six permutations of the houses; the 216 ordered triples of orders are equally likely. For an assignment \(\mu\), put \(r_i(\mu(i))\in\{0,1,2\}\) for the rank of the assigned house, with zero best. Define the majority margin
\[
m_P(\mu,\nu)=\sum_{i=1}^3\bigl(\mathbf1[r_i(\mu(i))<r_i(\nu(i))]-\mathbf1[r_i(\mu(i))>r_i(\nu(i))]\bigr).
\]
There is a weak-majority edge \(\mu\to\nu\) exactly when \(m_P(\mu,\nu)\ge0\), including both directed edges on a tie. The top cycle \(T(P)\) consists of assignments from which all assignments are reachable along directed majority paths. An assignment is Pareto optimal if no bijection makes every agent weakly better off and one agent strictly better off. In the strict majority graph, \(\mu\) McKelvey-covers \(\nu\) if \(m_P(\mu,\nu)>0\), every strict successor of \(\nu\) is a strict successor of \(\mu\), and every strict predecessor of \(\mu\) is a strict predecessor of \(\nu\). The uncovered set \(U(P)\) consists of assignments not McKelvey-covered by any assignment. These definitions coincide with those of Brandt, Chen, Dong, Lederer, and Schlenga (2026). This is an exact finite-population result, not a statement for larger electorates or lotteries.

## Proof
For any profile, six orderings of the houses give six possible assignments. Relabeling the houses simultaneously leaves the majority graph and all three solution sets invariant up to vertex relabeling. Exactly one of the six relabelings makes the first agent's order \(123\). Thus every one of the 36 profiles \((123,s,t)\), where \(s,t\in\{123,132,213,231,312,321\}\), represents precisely six of the 216 labeled profiles.

To compute the cardinalities without any qualitative or asymptotic approximation, enumerate the six assignments in lexicographic order and compute the sign of \(m_P\) for every ordered pair. The Boolean transitive closure of the nonnegative-margin adjacency matrix determines \(T(P)\). Direct comparison of each candidate against the other five determines \(E(P)\). The explicit McKelvey-covering implication from the previous section determines \(U(P)\). These are finite formulas using at most six vertices and three rank comparisons per ordered pair, so there is no unexamined profile or assignment. The complete resulting normalized table follows. Each entry \(abc\) means \((|T|,|E|,|U|)=(a,b,c)\); headers encode preference orders, not arithmetic.

```text
agent 3 ->   123 132 213 231 312 321
agent 2
123          666 642 642 442 222 222
132          642 642 632 432 632 432
213          642 632 642 632 111 111
231          442 432 632 222 111 111
312          222 632 111 111 442 432
321          222 432 111 111 432 222
```

Every entry can be reconstructed directly from the preceding margin formula; the included executable `verify.py` enumerates the underlying rank comparisons and asserts each complete aggregate count. In the table, the seven patterns occur respectively \(8,6,6,3,6,6,1\) times. Multiplying by six proves the seven joint frequency counts in the Finding. Subtracting \(|E|\) from \(|T|\) gives frequencies \(108,36,36,36\) for differences \(0,1,2,3\), respectively. Thus the claimed probability and expectation follow. Every entry also verifies \(|U|\le |E|\le |T|\), and the executable independently verifies the stronger set inclusions rather than inferring them from cardinalities.

For the minimality claim, with two agents and two houses there are only two bijections. If both agents prefer the same bijection, it Pareto-dominates the other and uniquely lies in the top cycle. Otherwise each agent prefers a different bijection; the majority relation ties, both are Pareto optimal, and both are in the top cycle. For a single agent there is one assignment. Hence three agents are the smallest possible size for Pareto-dominated top-cycle assignments.

## Verification
Running `python3 verify.py` with standard Python independently reconstructs the top cycle using both Floyd–Warshall closure and per-vertex graph searches, Pareto optimality using both direct dominance and all six serial dictatorships, and McKelvey uncoveredness via both direct covering and two-step majority paths. It checks all 216 profiles, all 36 normalized profiles, the complete seven-atom table, set inclusions, and the four two-agent cases. Exact integer comparisons are used throughout. This finite certificate is exhaustive within its explicitly stated finite domain; it gives no basis for claiming the distribution persists with four or more agents.

## Relationship to prior work
Brandt, Chen, Dong, Lederer, and Schlenga, *Majoritarian Assignment Rules* (arXiv:2602.14816v1, publicly submitted 16 February 2026), prove that every Pareto-optimal assignment lies in the top cycle and investigate the McKelvey uncovered set. Their Remark 3 identifies the possible sizes \(1,2,4,6\) for three-agent top cycles; their main structural characterization concerns at least five agents and their displayed uncovered-set census concerns larger markets. Those statements do not furnish the seven joint frequencies or the half-law, though they supply the central motivation and many definitions. Brandt, Hofbauer, and Suderland, *Majority Graphs of Assignment Problems and Properties of Popular Random Assignments* (AAMAS 2017), count majority-graph types but do not provide this distribution of three majoritarian/economic solution-set sizes. Separate existing classifications of three-agent random serial dictatorship lotteries concern different outcomes and do not imply the present joint law. An indexed-literature search cannot rule out every unindexed equivalent census.

## Limitations
All probabilities are with respect to independently uniform strict preferences for exactly three agents and three houses. This is a finite classification, not a general tail bound, complexity theorem, or strategyproofness claim. Only McKelvey uncoveredness is classified (not the Bordes and Gillies variants separately). The cited literature and searchable records might omit a prior independently computed equivalent classification.

## References
1. F. Brandt, H. Chen, C. Dong, P. Lederer, and A. Schlenga, *Majoritarian Assignment Rules*, arXiv:2602.14816v1 (16 February 2026), https://arxiv.org/html/2602.14816v1.
2. F. Brandt, J. Hofbauer, and M. Suderland, *Majority Graphs of Assignment Problems and Properties of Popular Random Assignments*, AAMAS (2017), https://www.ifaamas.org/Proceedings/aamas2017/pdfs/p335.pdf.
