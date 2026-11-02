# Quadratic NOR oscillation creation under matching deletion in complete bipartite graphs

## Finding

For integers \(p,q\ge2\) and \(0\le k\le\min(p,q)\), let \(G_{p,q,k}\) be the complete bipartite graph \(K_{p,q}\) with \(k\) pairwise disjoint edges removed. On its \(p+q\) vertices, use **synchronous open-neighborhood NOR**:
\[
F(x)_v=\prod_{u\sim v}(1-x_u),\qquad x\in\{0,1\}^{p+q}.
\]
The state of a vertex is not an input to its own update. Write
\[
h_p=2^p-k-1,\qquad h_q=2^q-k-1.
\]
The following gives the **complete orbit and attraction-basin census**, for every admitted parameter triple. A basin includes the recurrent phase(s) as well as their transient predecessors.

1. Exactly \((k+2)^2\) configurations are periodic. Among them, exactly \(k+2\) are fixed and the rest form exactly \(\binom{k+2}{2}\) primitive two-cycle *orbits*. Every other configuration enters one of these attractors after exactly one update. There are no longer cycles or transients. The one-update bound is sharp unless \((p,q,k)=(2,2,2)\), in which case every configuration is periodic from the outset.
2. The individual attraction basins have the following complete profile. Repeated sizes in the table are counted as separate orbits, even when their numerical values happen to coincide.

| Attractor | Number | Basin size of each |
| --- | ---: | ---: |
| Bipartition-monochromatic fixed point, left side active | 1 | \(h_p\) |
| Bipartition-monochromatic fixed point, right side active | 1 | \(h_q\) |
| Deleted-edge endpoint-pair fixed point | \(k\) | \(1\) |
| All-zero/all-one primitive two-cycle | 1 | \(h_ph_q+1\) |
| Deleted-edge cycles of right-singleton type | \(k\) | \(h_q+1\) |
| Deleted-edge cycles of left-singleton type | \(k\) | \(h_p+1\) |
| Cycles joining two different deleted-edge indices | \(\binom{k}{2}\) | \(2\) |

Consequently, the total population eventually reaching a fixed point is exactly
\[
B_{\mathrm{fix}}=h_p+h_q+k=2^p+2^q-k-2,
\]
while the single all-zero/all-one two-cycle has basin size \(B_{\mathrm{univ}}=h_ph_q+1\).
3. Relative to the undeleted complete bipartite graph, removing a matching of size \(k\) creates exactly \(k\) additional fixed points and \(k(k+3)/2\) additional primitive two-cycle orbits. Thus recurrent oscillation *counts* grow quadratically in the deletion size, but in the regime \(\min(p,q)\to\infty\), **uniformly for every** \(0\le k\le\min(p,q)\), the universal two-cycle captures a fraction tending to one:
\[
\frac{B_{\mathrm{univ}}}{2^{p+q}}
=1-(k+1)(2^{-p}+2^{-q})+
\frac{(k+1)^2+1}{2^{p+q}}\longrightarrow1.
\]
At the same time the probability of eventual fixation is \((2^p+2^q-k-2)/2^{p+q}\to0\). The count of recurrent two-cycles increases while almost every random initial condition still flows to one dominant oscillation.

## Assumptions and scope

Graphs are finite, simple, undirected, loopless, and vertex-labelled for configuration counting. A missing matching consists of \(k\) edges with pairwise distinct endpoints. Relabelling identifies every such matching with the pairs \((i,i)\), \(1\le i\le k\), between parts \(L=[p]\) and \(R=[q]\). Both sides have at least two vertices. The state alphabet is binary; all vertices update simultaneously; the local rule consults **only open neighbors**, never the updating vertex itself. The cases \(k=0\) and \((p,q,k)=(2,2,2)\) are included as explicit boundary checks. The model has no stochastic updates; probabilities refer solely to uniformly random independent initial bits.

A configuration is represented by two active sets \((A,B)\), where \(A\subseteq L\), \(B\subseteq R\). Its first periodic-entry time is the smallest nonnegative integer \(t\) for which \(F^t(A,B)\) is periodic. A primitive period-two orbit is an unordered pair of distinct phase configurations exchanged by \(F\).

## Proof

**Step 1: the two one-sided maps.** Write the synchronous update as
\[
F(A,B)=(f(B),g(A)),
\]
where \(f:2^R\to2^L\) and \(g:2^L\to2^R\). The vertex \(i\in L\) has every vertex of \(R\) as a neighbor except \(i\in R\) when \(i\le k\). Thus \(i\) is active next precisely when \(B\subseteq\{i\}\) if \(i\le k\), or when \(B=\varnothing\) if \(i>k\). As \(p,q\ge2\),
\[
f(B)=\begin{cases}
L,&B=\varnothing,\\
\{i\}\subset L,&B=\{i\},\ 1\le i\le k,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
The identical description with \(L,R\) exchanged gives \(g\).

**Step 2: recurrent phases.** Set
\[
\mathcal T_L=\{\varnothing,L,\{1\},\ldots,\{k\}\},
\qquad
\mathcal T_R=\{\varnothing,R,\{1\},\ldots,\{k\}\}.
\]
These sets have \(k+2\) distinct elements each. Both \(f\) and \(g\) are surjective onto the corresponding \(\mathcal T\) families, because the empty set, the entire opposite part, and each matched singleton produce their required images. Restricted to the \(\mathcal T\) families, \(f\) and \(g\) exchange the labels \(\varnothing\leftrightarrow\text{whole part}\) and preserve each labelled singleton. Their restrictions are mutual inverses. Hence
\[
\operatorname{im}F=\mathcal T_L\times\mathcal T_R,
\qquad F^2\big|_{\mathcal T_L\times\mathcal T_R}=I,
\qquad F^3=F.
\]
Every image phase is periodic; conversely any periodic phase lies in the image. For a fixed phase, \(B=g(A)\), and each of the \(k+2\) choices of \(A\in\mathcal T_L\) gives exactly one fixed point. The remaining \((k+2)^2-(k+2)\) periodic phases form pairs, giving \(\binom{k+2}{2}\) primitive two-cycle orbits.

More explicitly, the fixed configurations are \((L,\varnothing)\), \((\varnothing,R)\), and \((\{i\},\{i\})\) for \(1\le i\le k\). The distinct two-cycle orbits are
\[
(\varnothing,\varnothing)\leftrightarrow(L,R),
\]
\[
(\varnothing,\{i\})\leftrightarrow(\{i\},R),\qquad
(L,\{i\})\leftrightarrow(\{i\},\varnothing)
\quad(1\le i\le k),
\]
and
\[
(\{i\},\{j\})\leftrightarrow(\{j\},\{i\})
\quad(1\le i<j\le k).
\]
These exhaust the recurrent phases by count, or directly by the involution on \(\mathcal T_L\times\mathcal T_R\).

**Step 3: exact preimage fibers and basins.** For \(a\in\mathcal T_L\), the number of inputs \(B\subseteq R\) with \(f(B)=a\) is \(h_q=2^q-k-1\) when \(a=\varnothing\), and is one for \(a=L\) or a matched singleton. Similarly \(g^{-1}(b)\) has \(h_p=2^p-k-1\) elements when \(b=\varnothing\), otherwise one. Therefore the immediate predecessor fiber of a recurrent phase \((a,b)\) has cardinality
\[
\#F^{-1}(a,b)
=\big(h_q\text{ if }a=\varnothing\text{ else }1\big)
\big(h_p\text{ if }b=\varnothing\text{ else }1\big).
\]
Since every state maps into a recurrent phase in one update, the basin of a fixed phase is exactly its predecessor fiber, and the basin of a two-cycle is the **disjoint union** of the predecessor fibers of its two phases. Applying this rule to the explicit phase list in Step 2 yields every entry of the table. As a consistency identity, the sum of all the displayed basin populations is
\[
(h_ph_q+1)+k(h_p+h_q+2)+2\binom{k}{2}
+(h_p+h_q+k)
=(h_p+k+1)(h_q+k+1)=2^{p+q}.
\]
Thus there are no uncounted initial states.

**Step 4: boundary and asymptotics.** The set of all configurations equals the recurrent image exactly when \(2^p=k+2=2^q\). Since \(p,q\ge2\) and \(k\le\min(p,q)\), this happens precisely when \((p,q,k)=(2,2,2)\). In every other case the one-step transient bound is attained. Subtracting the \(k=0\) orbit counts gives \(k\) and \(k(k+3)/2\). Finally, dividing \(h_ph_q+1\) by \(2^{p+q}\) gives the displayed exact concentration formula. Because \(k\le\min(p,q)\), both \((k+1)2^{-p}\) and \((k+1)2^{-q}\) vanish as \(\min(p,q)\to\infty\), proving uniform concentration. The fixation probability similarly vanishes.

## Verification

Two standalone, separately written exhaustive implementations accompany this note. The graph-level Python checker constructs the actual graph and independently evaluates the open-neighbor NOR rule on every state for every \(2\le p,q\le6\) and every \(0\le k\le\min(p,q)\): **105 parameter instances and 86,384 configuration trajectories**. The compiled C++ checker uses vertex-neighbor bit masks, covers all \(2\le p,q\le8\) with \(p+q\le14\) and every admissible \(k\), and examines **213 instances and 804,208 configurations**. Both enumerate basins by actual orbit classes rather than assigning them from the claimed phase classification. They check the exact recurrence, fixed/two-cycle counts, basin-size multisets, and the all-zero/all-one basin. All checks passed. The Python and C++ programs and their actual output files are supplied as reproducible artifacts.

These computations test finitely many parameter values; the preceding algebraic argument, not enumeration, proves the quantified statement for all \(p,q,k\).

## Relationship to prior work

Veliz-Cuba and Laubenbacher (published online 15 October 2011) study fixed points of AND-NOT Boolean networks in relation to maximal independent sets. The fixed-state link is therefore background here. Aledo, Martínez, and Valverde (2015) survey maxterm/minterm parallel graph systems and qualitative period restrictions. Aledo et al. (2020) develop periodic-point bounds for minterm/maxterm systems. Those papers do not state the present family-specific **individual attraction-basin profile**, its quadratic deletion-size orbit census, and the uniform dominant-basin limit. In comparing models, it is essential to distinguish the present **open-neighborhood** rule from conventions including the updating vertex in its own minterm.

The one-step entry identity for open-neighborhood NOR on undirected graphs and the undeleted complete-bipartite special case are already known and are **not** claimed as original. The new asserted contribution is precisely the matching-deletion-dependent basin and recurrent-orbit census. The absence of an identical indexed theorem in the searches performed does not establish absolute historical priority.

## Limitations

The theorem assumes removed edges form a matching. Removing two edges sharing an endpoint need not preserve the one-sided three-type description; no claim is made for arbitrary deleted edge sets or other Boolean update rules. Attractor *counts* are by labelled configurations, with temporal phases of one two-cycle identified when counting orbits. The statistical concentration assumes independent uniformly random initial bits, not a stochastic state transition. The older fixed-point paper was available in abstract/bibliographic form but not in complete extracted text, leaving some historical-overlap risk. The calculations reported are internal consistency checks and are not an independent mathematical audit.

## References

1. A. Veliz-Cuba and R. Laubenbacher, *On the computation of fixed points in Boolean networks*, Journal of Applied Mathematics and Computing **39** (2012), 145–153; first online 15 October 2011. DOI: 10.1007/s12190-011-0517-9.
2. J. A. Aledo, S. Martínez, and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics **2015**, 594294; first online 24 March 2015. DOI: 10.1155/2015/594294.
3. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan, and J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity **2020**, 9708347; first online 14 September 2020. DOI: 10.1155/2020/9708347.
