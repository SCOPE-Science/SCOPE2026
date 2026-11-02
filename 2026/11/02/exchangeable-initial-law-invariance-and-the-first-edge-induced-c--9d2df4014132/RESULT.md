# Exchangeable-initial-law invariance and the first edge-induced consensus slowdown

## Finding

**Theorem (four-site universality and sharp simple-graph edge boundary).** Consider the continuous-time binary voter model on four sites. Each site updates at rate one by adopting the current opinion of another site, chosen according to its row of a fixed irreducible row-stochastic copying matrix with zero diagonal. For \(k=1,2,3\), initialize the \(k\) sites holding opinion one as a uniformly random \(k\)-subset, and let \(T_k\) denote the expected time to unanimous consensus. Then, independently of every entry of the copying matrix,

\[
T_3=T_1,\qquad T_2=\frac43T_1-\frac1{12}.
\]

For any exchangeable initial binary law, write \(\pi_k\) for the probability that exactly \(k\) sites initially hold opinion one. Its mean consensus time is

\[
\mathbb E_\pi T=\left(\pi_1+\pi_3+\frac43\pi_2\right)T_1-\frac{\pi_2}{12}.
\]

Thus, if \(\pi_1+\pi_2+\pi_3>0\), the strict ordering, equality, and reversal of mean consensus times between any two such networks are all independent of the chosen exchangeable initial distribution.

For simple connected undirected copying graphs on four vertices, the complete graph-type ranking is

\[
T_1(P_4)=\frac{23}{14}>
T_1(C_4)=\frac32>
T_1(K_4-e)=\frac{397}{288}>
T_1(K_4)=\frac{11}{8}>
T_1(\text{paw})=\frac{1143}{832}>
T_1(K_{1,3})=\frac{19}{16}.
\]

Among the six single-edge additions between connected four-vertex graph types, **exactly two increase expected consensus time**: the star-to-paw transition by \(155/832\), and paw-to-diamond by \(35/7488\), when the initial minority singleton is uniformly placed. For a general common exchangeable initial law, both increments are multiplied by \(\pi_1+\pi_3+4\pi_2/3\). An edge-induced strict increase is impossible on connected simple graphs with fewer than four vertices. Hence four is the sharp minimal population size for this effect under every nontrivial exchangeable initial law.

## Assumptions and scope

Time is continuous. Independently at each vertex, a Poisson clock of rate one selects a copying event. At an event, vertex \(i\) copies vertex \(j\) with probability \(p_{ij}\), where \(p_{ii}=0\), \(\sum_jp_{ij}=1\), and the directed graph of positive probabilities is irreducible. This makes consensus an almost-sure finite-time absorbing state. Initially the binary state is independent of the clocks and copying choices. Exchangeability means the conditional distribution given exactly \(k\) ones is uniform on the \(\binom4k\) subsets. The distribution \(\pi\) may assign mass to already-consensual configurations, whose time is zero.

The simple undirected specialization takes \(p_{ij}=1/\deg(i)\) at neighbors and zero elsewhere, with all graphs connected. Each displayed graph value is the expectation over the uniformly located single initial dissenter (or, equivalently, three dissenters after relabeling zero and one). The *paw* is a triangle with a fourth vertex attached to one triangle vertex; the *diamond* is \(K_4\) minus one edge. The edge comparison uses the same four vertices and the same initial law on both graphs.

## Proof

**1. Coalescing genealogies prove the universal identity.** Trace the state of every vertex at time \(t\) backward through its copying arrows. The resulting four lineages perform coalescing random walks, initially at all four distinct vertices. Let \(J_t\) be the number of distinct original ancestors reached at time zero. For any fixed \(j\) distinct ancestors, conditional on exactly \(k\) initial ones uniformly distributed, the probability that the observed four opinions are *not* unanimous is

\[
q_k(j)=1-\frac{\binom{4-j}{k}+\binom{4-j}{k-j}}{\binom4k},
\]

where binomial coefficients with inadmissible lower arguments are zero. Indeed, unanimity requires all \(j\) ancestors to be zero or all \(j\) to be one. Directly evaluating these finite hypergeometric probabilities gives

\[
\begin{array}{c|rrrr}
j&1&2&3&4\\\hline
q_1(j)=q_3(j)&0&1/2&3/4&1\\
q_2(j)&0&2/3&1&1
\end{array}
\]

Consequently \(q_2(j)-(4/3)q_1(j)\) equals \(-1/3\) when \(j=4\) and zero otherwise. Because genealogical coalescence is irreversible,

\[
\Pr(T_2>t)-\frac43\Pr(T_1>t)
=-\frac13\Pr(J_t=4).
\]

Before the first coalescence, all four vertices carry one lineage. Each lineage jumps at rate one, and, because there is no self-copy, every jump hits another occupied vertex and causes a coalescence. Thus the first coalescence time \(\tau\) is exponential with rate four, independent of the network weights, and \(\Pr(J_t=4)=e^{-4t}\). Integrating the survival-function identity gives

\[
T_2-\frac43T_1=-\frac13\int_0^\infty e^{-4t}\,dt=-\frac1{12}.
\]

Global interchange of zero and one establishes \(T_3=T_1\). Conditioning on \(k\) proves the formula for any exchangeable \(\pi\). The coefficient multiplying \(T_1\) is strictly positive whenever the initial law is nontrivial, establishing the universal graph-order invariance.

**2. Exact graph census.** For each connected simple graph and each nonconsensus binary configuration \(s\in\{0,1\}^n\), let \(u(s)\) be its conditional expected consensus time. A first-step argument gives the rational linear equations

\[
n\,u(s)-\sum_{i=1}^n\frac1{\deg(i)}
\sum_{j\sim i}u(s^{i\leftarrow j})=1,
\]

with \(u(0^n)=u(1^n)=0\). Here \(s^{i\leftarrow j}\) is \(s\) after replacing the opinion at \(i\) by that at \(j\). The denominator-free exact-rational elimination in the companion `verify.py` evaluates these equations on **all 38 labeled connected four-vertex graphs**. Their permutation orbits are exactly the six listed graph types. For clarity, their single-dissenter expectations, in increasing order, are

\[
\begin{array}{c|cccccc}
G&K_{1,3}&\text{paw}&K_4&K_4-e&C_4&P_4\\\hline
T_1(G)&19/16&1143/832&11/8&397/288&3/2&23/14
\end{array}
\]

Every graph on four labeled vertices has six possible edges. Inserting one absent edge into any connected graph and reducing both resulting graphs under permutations gives exactly the following six unordered-type transitions, with **oriented** increment \(T_1(G+e)-T_1(G)\):

\[
\begin{array}{c|r}
\text{transition}&\text{increment}\\\hline
K_{1,3}\to\text{paw}&155/832\\
P_4\to\text{paw}&-1567/5824\\
P_4\to C_4&-1/7\\
\text{paw}\to(K_4-e)&35/7488\\
C_4\to(K_4-e)&-35/288\\
(K_4-e)\to K_4&-1/288
\end{array}
\]

These six cases cover all possible insertions. The proof uses an exhaustive list of graph orbits and exact elimination, not numerical sampling; the standalone code reproduces both the enumeration and all fraction calculations with integer arithmetic.

**3. Minimality.** A connected simple graph of order one or two has no edge to add while remaining simple (or admits no nontrivial comparison). On three vertices, the sole nontrivial addition changes \(P_3\) to \(K_3\). For \(P_3\), let \(E_L\) and \(E_M\) denote the consensus times with exactly one dissenter initially at an endpoint and the midpoint, respectively. First-step equations give \((3/2)E_L=1+(1/2)E_L\) and \(3E_M=1+2E_L\), so both equal one. For \(K_3\), the minority-count process has transitions at rate one in either direction from each of its nonabsorbing states. State complementation therefore gives \(2E=1+E\), hence \(E=1\). This proves \(T_1(P_3)=T_1(K_3)=1\); binary complementation also gives \(T_2=1\) on both graphs, so every exchangeable initial distribution yields the same mean consensus time for this pair. On four vertices, star-to-paw gives a positive increment for every nontrivial exchangeable initial law. This proves the sharp minimum.

## Verification

Run `python3 verify.py` with Python 3.9 or newer. No third-party modules, external data or network access are required. The program enumerates all 38 connected labeled four-vertex simple graphs, identifies six isomorphism classes using all 24 vertex permutations, solves the nonabsorbing first-step equations exactly over rational numbers, checks the three conditional means and their universal identity on all 38 graphs, and verifies the six transition increments. It also solves every connected labeled three-vertex graph and checks equality of the two nontrivial conditional means. The universal statement for arbitrary weighted directed copying networks follows from the foregoing genealogical proof; finite graph enumeration is not used as a surrogate for that proof. All displayed units assume rate one per vertex, not a single global update per unit time.

For fair independent initial opinions, the mean for each four-vertex graph simplifies to \(T_1-1/32\). Thus the star-to-paw change is exactly \(155/832\) in that sampling convention too.

## Relationship to prior work

Masuda (2014) studied voter-model consensus times on two-clique networks and their scaling with intercommunity connectivity. Iwamasa and Masuda (2014) provided a general exact finite-state mean-time method and optimized network shapes, including an illustrative four-vertex Markov calculation and ten-vertex network optimization. The exact first-step method used here is standard, not newly invented. Gastner and Ishida (2019) already showed that adding interclique links can have a nonmonotone influence on voter-model consensus time; a generic edge-slowdown phenomenon is therefore **not** claimed as new. Their regimes and initial states differ from the present four-vertex minimum and exchangeable-mixture invariance.

The specific contribution assessed here is the **graph-independent affine identity among all four-site conditional initial laws, the complete exact edge-insertion phase table for four-vertex simple graphs, and the sharp four-site minimum** for strict edge-induced slowdown under every nontrivial exchangeable initial distribution. Exact recursion alone does not state these structural implications. The possibility of an earlier unlocated algebraic identity or explicit small-graph table remains a historical-priority limitation.

## Limitations

The result concerns binary irreversible-absorption voter copying on a fixed network, independent rate-one vertex clocks and exchangeable initial laws. It does not apply without qualification to discrete-time normalized global update counts, non-exchangeable initial configurations, varying clock rates, self-copy probabilities, zealots, adaptive networks, multi-opinion variants, or nonstandard push/invasion update rules. It is a mathematical toy-model statement, not a measured social prediction. The finite classification uses rational linear algebra, whose computation is independently reproducible with the included program; no independent external audit has been performed. Historical novelty remains subject to broader scholarly checking.

## References

1. N. Masuda, *Voter model on the two-clique graph*, arXiv:1403.4763, first publicly submitted March 19, 2014; Physical Review E **90**, 012802 (2014). https://arxiv.org/abs/1403.4763
2. Y. Iwamasa and N. Masuda, *Networks maximizing the consensus time of voter models*, arXiv:1404.6360, first publicly submitted April 25, 2014; Physical Review E **90**, 012816 (2014). https://arxiv.org/abs/1404.6360
3. M. T. Gastner and K. Ishida, *Voter model on networks partitioned into two cliques of arbitrary sizes*, arXiv:1908.00849, publicly submitted August 2, 2019; Journal of Physics A **52**, 505701 (2019). https://arxiv.org/abs/1908.00849
