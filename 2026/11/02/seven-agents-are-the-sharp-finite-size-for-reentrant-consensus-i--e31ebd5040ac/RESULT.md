# Seven agents are the sharp finite size for reentrant consensus in equally spaced bounded-confidence dynamics

## Finding

For the synchronous one-dimensional Hegselmann–Krause opinion model with confidence radius one, let \(n\) agents start at
\[
 x_i(0)=(i-1)d,\qquad 1\le i\le n,\quad 0<d\le1.
\]
Each agent simultaneously replaces its opinion with the arithmetic average of all opinions at distance at most one, including its own. Consensus means that all agents eventually have exactly one common opinion; otherwise the fixed terminal state consists of separated clusters.

**Exact smallest-size and phase theorem.** For every \(1\le n\le5\), and every \(0<d\le1\), consensus occurs. For \(n=6\), consensus occurs exactly when \(d\le4/7\); otherwise the terminal cluster sizes are \((3,3)\). For \(n=7\), consensus occurs **if and only if**
\[
 \boxed{\;0<d\le\frac{48}{61}\quad\text{or}\quad
 \frac45<d\le\frac{288}{337}\quad\text{or}\quad
 \frac{72}{79}<d\le\frac{1728}{1861}.\;}
\]
At all remaining spacings \(0<d\le1\), the seven agents terminate in exactly three clusters, of sizes \((3,1,3)\). Every endpoint is included or excluded exactly as printed. Consequently **seven is the minimum number of initially equally spaced agents** for which increasing their spacing, with the confidence radius fixed, can restore consensus after a nonconsensus regime; seven agents exhibit two separate restoration windows.

## Assumptions and scope

We use the usual closed-neighborhood convention: agents \(i,j\) interact when \(|x_i(t)-x_j(t)|\le1\), and every opinion updates synchronously by the uniform average over its own interaction neighborhood. There are no stubborn agents, time-dependent weights, asynchronous decisions, randomized initial positions, or external influences. The range \(0<d\le1\) is the complete range of positive spacings for which the initial interaction graph is connected; for \(d>1\) all agents are initially isolated and remain so. The theorem covers every real \(d\) in this range, including all rational threshold endpoints, but only \(n\le7\).

A frozen state is a state unchanged by a further full update. In this model it consists precisely of clusters of equal opinions separated from one another by more than one. A consensus fixed point is one such cluster.

## Proof

Write \(x_i(t)=d\,q_i(t)\). We prove the classification by an exhaustive **exact rational partition of the entire continuous spacing interval**, not by sampling a finite set of spacings. On any half-open cell \(I=(a,b]\subseteq(0,1]\) with a fixed past sequence of interaction graphs, the vector \(q(t)\) is constant across \(I\), with rational entries: initially \(q_i(0)=i-1\); averaging rational entries preserves this property.

For a pair \(i,j\) with \(q_i(t)\ne q_j(t)\), its interaction edge exists precisely when
\[
 d\,|q_i(t)-q_j(t)|\le1.
\]
Thus the only possible event in \(I\) for that pair is the *exact rational* cutoff \(d=1/|q_i(t)-q_j(t)|\). Split \(I\) at **every** cutoff strictly within its interior. A split at \(c\) gives \((a,c]\) and \((c,b]\). On each resulting cell all pairwise interaction decisions are identical, including the weak-inequality decision at the **included upper endpoint**. The coefficient vector after the next update is exactly
\[
 q_i(t+1)=\frac{\sum_{j:\,d|q_i(t)-q_j(t)|\le1}q_j(t)}
 {\#\{j:\,d|q_i(t)-q_j(t)|\le1\}},
\]
where any \(d\) from that cell yields the same neighbor set. A cell is terminal if and only if this update reproduces its vector \(q(t)\); this criterion then holds for **every** spacing in the cell, not just its midpoint.

Starting from the single cell \((0,1]\), this subdivision-and-update induction yields exactly the following numbers of terminal cells for \(n=1,2,3,4,5,6,7\), respectively:
\[
 1,\ 1,\ 2,\ 5,\ 10,\ 11,\ 26.
\]
There is no unfinished cell: all cells have become fixed by at most twelve updates. Their mutually disjoint half-open ranges cover exactly \((0,1]\); `certificate.tsv` records every rational endpoint, exact freezing time, and ordered terminal cluster-size vector. The proof-reproducing standard-library script `verify.py` independently constructs the whole recursive partition from the update definition and checks that its complete output equals that certificate. This finite certificate is an exhaustive proof of the universal statement because the preceding induction proves that each entire continuous cell shares its reported exact trajectory and terminal state.

The five seven-agent boundaries also have explicit local rational explanations. In the table, the indicated pair distances have the form \(d\,c\) at the displayed update time, and the pair edges exist exactly on the left side **including** the indicated boundary; they disappear immediately to its right. Each coefficient follows by rational averaging along the graph sequence preceding the first differing decision.

| Critical spacing | Update time | First affected symmetric edges | Pair-distance coefficient \(c\) |
| --- | ---: | --- | --- |
| \(48/61\) | \(3\) | \((3,4),(4,5)\) | \(61/48\) |
| \(4/5\) | \(2\) | \((1,3),(5,7)\) | \(5/4\) |
| \(288/337\) | \(4\) | \((3,4),(4,5)\) | \(337/288\) |
| \(72/79\) | \(3\) | \((1,3),(5,7)\) | \(79/72\) |
| \(1728/1861\) | \(5\) | \((3,4),(4,5)\) | \(1861/1728\) |

The six-agent boundary \(4/7\) likewise occurs when the middle edge \((3,4)\) has pair-distance coefficient \(7/4\) at time \(2\). These event equalities explain the displayed threshold fractions; the complete cell certificate also rules out any additional crossings or later separations.

Compressing the cell certificate by the **terminal number and sizes of clusters** produces the complete classification:

| Agent count | Spacing intervals | Ordered terminal sizes |
| --- | --- | --- |
| \(1\le n\le5\) | \((0,1]\) | \((n)\) |
| \(n=6\) | \((0,4/7]\); \((4/7,1]\) | \((6)\); \((3,3)\) |
| \(n=7\) | \((0,48/61]\) | \((7)\) |
| \(n=7\) | \((48/61,4/5]\) | \((3,1,3)\) |
| \(n=7\) | \((4/5,288/337]\) | \((7)\) |
| \(n=7\) | \((288/337,72/79]\) | \((3,1,3)\) |
| \(n=7\) | \((72/79,1728/1861]\) | \((7)\) |
| \(n=7\) | \((1728/1861,1]\) | \((3,1,3)\) |

For \(n\le5\), the certificate shows consensus for all connected initial spacings; for \(n=6\), a single one-way loss of consensus at \(4/7\). For \(n=7\), the cluster count changes \(1\to3\to1\to3\to1\to3\) as \(d\) increases. This proves the asserted minimum and both restoration windows. Every equality boundary is resolved by the closed-neighborhood convention in the exact rational proof.

## Verification

Run `python3 verify.py` in the directory containing `certificate.tsv` and `verify.py`; no third-party package is needed. It checks every terminal rational cell, all contiguous endpoint joins and coverage, all terminal cluster sizes, the closed-endpoint interaction graph, the stipulated global phase classification, and an exact rational forward replay at both the midpoint and included right endpoint of **every** terminal cell. The observed output was:

```
PASS: exact exhaustive half-open interval certificate for n=1..7
Terminal intervals by n: {1: 1, 2: 1, 3: 2, 4: 5, 5: 10, 6: 11, 7: 26}
Maximum freezing time: 12
PASS: right-endpoint equalities, midpoint trajectories and phase classification
```

An independent direct rational forward-update implementation also checked the five seven-agent boundaries from both sides and at equality, along with the six-agent cutoff. Those comparisons returned the displayed alternating cluster outcomes. The proof of continuum coverage, rather than these additional trajectory samples alone, is what establishes the theorem for all admissible real spacings.

## Relationship to prior work

Lorenz (2006) identified the qualitative 'consensus strikes back' phenomenon for bounded-confidence opinion dynamics, principally using simulations and an interactive-Markov-chain description. Hegarty and Wedin (2014) analyzed equally spaced synchronous agents: their main exact theorem concerns the spacing \(d=1\), and their Section 3 and Table 1 provide an exact phase study for a one-sided infinite configuration, with a qualitative finite-seven-agent discussion. Their table already contains some of the rational values appearing as boundaries here; it does not state the complete terminal cluster classification for every \(d\) with seven agents or the seven-agent minimality theorem. Kurz (2014) studied worst-case convergence time across unrestricted initial configurations, a different parameterized question. Wedin (2021) rigorously studied the reentrant phenomenon in a large-population/equidistributed limit, not the exact finite seven-agent phase diagram. The present result supplies a minimal finite-size theorem and exact closed-endpoint rational transition intervals; it does not claim that the underlying dynamics or reentrance phenomenon was newly discovered.

## Limitations

The classification applies only to synchronous, uniform, deterministic, one-dimensional confidence averaging with **equally spaced** starting opinions and \(n\le7\), and should not be extrapolated to other opinion models or larger populations. It is a mathematical statement about a stylized social-dynamics mechanism, not evidence of empirical social behavior. The proof's exact rational enumeration is small and fully terminating, but its novelty relative to every unpublished finite-size computational table cannot be guaranteed by a literature search alone.

## References

1. J. Lorenz, *Consensus Strikes Back in the Hegselmann-Krause Model of Continuous Opinion Dynamics Under Bounded Confidence*, Journal of Artificial Societies and Social Simulation 9(1), article 8 (2006). https://www.jasss.org/9/1/8/8.pdf
2. P. Hegarty and E. Wedin, *The Hegselmann-Krause Dynamics for Equally Spaced Agents*, arXiv:1406.0819, first version June 2, 2014; Journal of Difference Equations and Applications 22 (2016), 1621–1645. https://arxiv.org/abs/1406.0819
3. S. Kurz, *How Long Does It Take to Consensus in the Hegselmann-Krause Model?*, arXiv:1405.5757 (2014). https://arxiv.org/abs/1405.5757
4. E. Wedin, *A Rigorous Formulation of and Partial Results on Lorenz's 'Consensus Strikes Back' Phenomenon for the Hegselmann-Krause Model*, arXiv:2107.12906 (2021). https://arxiv.org/abs/2107.12906
