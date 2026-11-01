# An orbit–basin inversion for five-color firefly dynamics on complete bipartite graphs

## Finding

Consider the synchronous five-color inhibitory firefly map on the labelled complete bipartite graph \(K_{a,b}\), for arbitrary integers \(a,b\geq1\). A vertex has a color in \(\{0,1,2,3,4\}\). Color \(2\) is the blinking color; a vertex of color \(3\) or \(4\) retains its color if a neighbor blinks, and otherwise all vertices advance one color modulo \(5\).

Every configuration has first periodic-entry time at most \(25\). The bound is attained, already on \(K_{1,5}\). The only eventual least periods are \(5\), \(6\), and \(18\).

For a positive integer \(n\), define the surjection number
\[
 A_j(n)=\sum_{r=0}^{j}(-1)^r\binom{j}{r}(j-r)^n.
\]
Thus \(A_j(n)\) counts assignments of \(n\) labelled sites using every color of a prescribed set of \(j\) distinct colors, and \(A_j(n)=0\) for \(j>n\).

Let \(N_p(a,b)\) denote the number of distinct primitive least-period-\(p\) orbits, without distinguishing their temporal phases. The complete orbit census is
\[
\begin{aligned}
N_5(a,b)&=1+\frac{2^a A_5(b)+2^b A_5(a)}{5},\\
N_6(a,b)&=\frac{A_3(a)A_3(b)}{3}+3A_2(a)A_2(b)
 +A_2(a)A_3(b)+A_3(a)A_2(b),\\
N_{18}(a,b)&=\frac{A_3(a)A_4(b)+A_4(a)A_3(b)}{6}.
\end{aligned}
\]
In particular, least period \(6\) exists exactly when \(a,b\ge2\), and least period \(18\) exists exactly when \((a\ge3,b\ge4)\) or \((a\ge4,b\ge3)\).

Let \(B_p(a,b)\) count *initial* configurations whose eventual least period is \(p\), including their nonperiodic transients. Define the exact integer matrix
\[
 C=\begin{pmatrix}
0&0&0&0&0\\
0&30&28&5&0\\
0&28&20&12&1\\
0&5&12&3&1\\
0&0&1&1&0
\end{pmatrix}.
\]
Then
\[
 B_6(a,b)=\sum_{k=1}^5\sum_{\ell=1}^5 C_{k\ell}A_k(a)A_\ell(b),
 \quad B_{18}(a,b)=18N_{18}(a,b),
 \quad B_5(a,b)=5^{a+b}-B_6(a,b)-B_{18}(a,b).
\]
**Every least-period-\(18\) state is already periodic: an \(18\)-cycle has no nonperiodic basin states.**

For balanced shores \(a=b=n\to\infty\),
\[
N_5(n,n)\sim\tfrac25 10^n,\quad
N_6(n,n)\sim\tfrac13 9^n,\quad
N_{18}(n,n)\sim\tfrac13 12^n.
\]
Consequently, a uniformly selected *primitive periodic orbit* has least period \(18\) with probability tending to \(1\). Conversely, a uniformly selected *initial configuration* eventually has least period \(5\) with probability tending to \(1\), and its first periodic-entry time equals exactly \(8\) with probability tending to \(1\). More precisely,
\[
\frac{B_6(n,n)}{5^{2n}}\sim2(4/5)^n,\qquad
\frac{B_{18}(n,n)}{5^{2n}}\sim6(12/25)^n.
\]
This is an orbit–basin inversion: almost every periodic orbit is long, but almost every initial configuration eventually joins a short orbit.

## Assumptions and scope

Graphs are simple and labelled, with no within-shore edges, and both shores nonempty. The update is deterministic and simultaneous at integer times, without self-loops or stochastic perturbations. A configuration is periodic at time \(t\) if its complete labelled vertex-color vector recurs after some positive number of further updates. The first periodic-entry time \(T\) is the least such \(t\), and the eventual least period is \(p\). Orbits differing only by a time shift are identified; differently labelled color assignments are not identified under graph automorphisms.

## Proof

**1. Exact support factor.** For each shore, retain only its set of occupied colors. A vertex's decision depends on its own color and whether color \(2\) occurs on the opposite shore. Thus the pair of nonempty supports evolves autonomously under the explicit map \(\Phi\) on exactly \((2^5-1)^2=961\) pairs of bitmasks. For a mask \(s\), let
\[
 g_t(c)=\begin{cases}c,&c>2\text{ and }2\in t,\\c+1\pmod5,&\text{otherwise},\end{cases}
 \quad \Phi(s,t)=\bigl(\{g_t(c):c\in s\},\{g_s(c):c\in t\}\bigr).
\]
Two vertices on the same shore that have the same color always remain identical in color. Distinct occupied colors may merge, so the support size on each shore never increases.

**2. Exhaustive finite lemma.** The attached executable `fca5_bipartite_verifier.py` enumerates every one of the \(961\) support pairs using the preceding transition formula and their entire functional graph. There are exactly \(16\) support cycles containing \(49\) periodic support states. The support cycle lengths occur with multiplicities \(6,1,4,1,4\) at lengths \(1,2,3,5,6\), respectively. The maximum distance of any support to the periodic subgraph is \(25\), attained for supports \((\{0\},\{0,1,2,3,4\})\); the all-five-colors support pair has distance \(8\). This is a finite *exhaustive* computation on a fixed state graph, not an experiment on bounded graph sizes. The complete state-by-state certificate is in `support_attractors.csv`.

**3. Lifting support cycles.** Along a periodic support cycle, the cardinalities on each shore return to their starting values. As they never increase, they cannot decrease anywhere on that cycle. Consequently, the color updates act bijectively on each occupied color set. After one support-cycle traversal of length \(q\), their composition gives permutations of the initial occupied colors. If the combined permutation order is \(L\), every labelled microscopic configuration on that support cycle has exact least period \(qL\). Indeed, a return requires a multiple of the least support period \(q\), and a nontrivial permutation of nonempty color classes changes at least one vertex's color. Conversely, any configuration whose support has reached a support cycle is already microscopically periodic. Thus microscopic periodic-entry time equals support periodic-entry time, including all transient cases.

**4. All support-cycle types.** The complete \(16\)-cycle table below uses \(k,\ell\) for the numbers of colors occupied on the two shores, \(q\) for support-cycle length, and \(L\) for color-permutation order; the last column counts distinct *support cycles* of that type.

| Least microscopic period | \(q\) | \(L\) | \(k\) | \(\ell\) | Number |
|---|---:|---:|---:|---:|---:|
| 5 | 5 | 1 | 1 | 1 | 1 |
| 5 | 1 | 5 | 1 | 5 | 2 |
| 5 | 1 | 5 | 2 | 5 | 1 |
| 5 | 1 | 5 | 5 | 1 | 2 |
| 5 | 1 | 5 | 5 | 2 | 1 |
| 6 | 2 | 3 | 3 | 3 | 1 |
| 6 | 3 | 2 | 2 | 2 | 2 |
| 6 | 6 | 1 | 2 | 2 | 2 |
| 6 | 6 | 1 | 2 | 3 | 1 |
| 6 | 6 | 1 | 3 | 2 | 1 |
| 18 | 3 | 6 | 3 | 4 | 1 |
| 18 | 3 | 6 | 4 | 3 | 1 |

The verifier enumerates the individual cycles, tracks each occupied color around it, verifies that the final map is a permutation, and computes its exact order. This table is therefore independently reproducible from the short update rule.

**5. Primitive-orbit enumeration.** Each support with color cardinalities \(k,\ell\) has exactly \(A_k(a)A_\ell(b)\) labelled configurations. A support cycle of length \(q\) contains \(qA_k(a)A_\ell(b)\) such configurations, all in microscopic orbits of least period \(qL\). Therefore it contributes exactly \(A_k(a)A_\ell(b)/L\) distinct microscopic cycles. Summation over the complete preceding table, using \(A_1(n)=1\) and \(2+A_2(n)=2^n\), gives all three orbit formulas.

**6. Attraction basins and asymptotics.** Follow each of the \(961\) support states to its unique terminal support cycle. The number of states with a given pair of support cardinalities \((k,\ell)\) entering least period \(6\) is precisely the coefficient \(C_{k\ell}\) displayed above. Exactly six supports enter least period \(18\): three with cardinalities \((3,4)\), and three with cardinalities \((4,3)\). All six are already on their support cycles. Multiplying by surjection counts proves the basin formulas, as well as the no-transient assertion for period \(18\).

For each fixed \(j\), inclusion-exclusion gives \(A_j(n)=j^n+O((j-1)^n)\). Substitution yields the three displayed periodic-orbit asymptotics. In the basin matrix \(C\), the largest products \(k\ell\) among nonzero coefficients are \(20\), attained in the two positions \((4,5)\), \((5,4)\) with coefficient one. Thus \(B_6(n,n)\sim2\cdot20^n\); the period-\(18\) basin is asymptotic to \(6\cdot12^n\). Finally, with independent uniformly chosen initial colors, the probability that each shore contains all five colors is \([A_5(n)/5^n]^2\to1\). Every such configuration has support periodic-entry time exactly \(8\), proving the typical-entry assertion.

## Verification

The attached standard-library Python program exhaustively derives the \(961\)-support transition graph, the \(16\) cycles and their monodromies, the exact first-entry depths, all basin coefficients, and the three orbit formulas at \(64\) parameter pairs. As an independent microscopic check, it directly simulates all \(97{,}525\) labelled color vectors over five graph sizes through \(K_{3,4}\) and compares both their genuine least periods and their first periodic-entry times with the support predictions. For \(K_{3,4}\) alone, the \(78{,}125\) initial vectors split into basin counts \(60{,}005\) for period \(5\), \(17{,}688\) for period \(6\), and \(432\) for period \(18\). Running `python3 fca5_bipartite_verifier.py` prints `FCA5_BIPARTITE_EXACT_VERIFY_OK` on success. The accompanying CSV provides every support pair's attractor class and exact entry depth; it is supplementary to the independently executable exhaustive logic.

## Relationship to prior work

Lyu's 2014 firefly-network paper defines this pulse-inhibition rule and proves qualitative synchronization results on paths and trees, including a degree obstruction on stars; the 2016 follow-up studies tree synchronization and its time complexity. Those results do not contain this bipartite orbit/basin census or the statistical inversion between orbit-weighting and initial-state weighting. A related complete-tripartite period-\(18\) enumeration uses three **nonempty** shores and thus does not give the present bipartite graph's sharp \(25\)-update bound, other orbit classes, or basin coefficients. Existing work supplies the model and context, while the explicit bipartite finite quotient analysis establishes the statements proved here.

## Limitations

The period classification and basin formulas are restricted to this exact five-color inhibitory rule and complete bipartite interaction, not general coupled-oscillator networks, variants of the flashing rule, or stochastic dynamics. The finite certificate exhausts the fixed support factor, whose completeness for all shore sizes is proved above; finite microscopic simulations are auxiliary checks, not a replacement for the all-size argument. The originality comparison is limited to identified relevant papers and mathematical-record searches; unindexed equivalent enumerations may exist. There has been no independent formal proof audit.

## References

1. H. Lyu, *Synchronization of finite-state pulse-coupled oscillators*, preprint first publicly available July 4, 2014. arXiv:1407.1103. https://arxiv.org/abs/1407.1103
2. H. Lyu, *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees*, preprint first publicly available October 4, 2016. arXiv:1610.00837. https://arxiv.org/abs/1610.00837
