# An exponential–polynomial oscillation gap in two matched cliques

## Finding
Consider two labelled complete graphs of size \(n\), with the corresponding vertices joined by a perfect matching, and synchronous binary majority updates with ties resolved by retaining the vertex's previous opinion. This is the Cartesian product \(G_n=K_n\square K_2\). Write \(F_n\) for the update of all \(2n\) opinions and \(T(x)\) for the least time after which the trajectory of \(x\) is periodic. For every integer \(n\ge2\), eventual least periods belong to \(\{1,2\}\), and the following counts are exact.

If \(n=2m\), with \(m\ge1\), put \(C=\binom{2m}{m}\). The number of fixed configurations is \(4+C\), the number of distinct primitive two-cycle orbits is \((C^2-C)/2\), and the total attraction basin of all primitive two-cycles has exactly \(C^2-C\) configurations. Thus **all oscillatory initial configurations are periodic from the start**.

If \(n=2m+1\), with \(m\ge1\), put \(D=\binom{2m+1}{m}\). There are exactly four fixed configurations and exactly \((m+2)D\) distinct primitive two-cycle orbits. The total attraction basin of these orbits contains exactly \(2(m^2+2m+2)D\) configurations; the \(2m(m+1)D\) nonperiodic configurations in this basin enter a two-cycle after exactly one update.

The sharp maximum of \(T(x)\) is \(1\) for \(n=2\); \(2\) for \(n=3\) and all even \(n\ge4\); and \(3\) for all odd \(n\ge5\). In particular, \(F_n^4=F_n^2\) for even \(n\) and \(F_n^5=F_n^3\) for odd \(n\).

Under independent unbiased initial opinions, the exact probability \(p_n\) of ultimately oscillating is the basin count divided by \(4^n\). Stirling's formula yields
\[
p_{2m}=\frac{2}{\pi(2m)}\bigl(1+O(m^{-1})\bigr),\qquad
p_{2m+1}=\frac{(2m+1)^{3/2}}{\sqrt{2\pi}\,2^{2m+1}}\bigl(1+O(m^{-1})\bigr).
\]
This is a polynomial versus exponential parity separation for an infinite family of connected regular networks.

## Assumptions and scope
Vertices are \((i,A)\) and \((i,B)\), \(1\le i\le n\). Within each shore all different vertices are adjacent; across shores only same-index vertices are adjacent. Every vertex has degree \(n\), has an opinion in \(\{0,1\}\), and updates simultaneously to the strict neighbor majority, retaining its current opinion if the counts tie. Let \(U=\{1,\ldots,n\}\), and represent a configuration by the pair \((A,B)\) of indices holding opinion one in the two shores. Define \(a=|A|\), \(b=|B|\), and \(c=|A\cap B|\). Configurations are fully labelled and cycles are identified only under time translation, not graph automorphisms or opinion complementation. The basin of primitive two-cycles counts initial configurations, not orbits.

## Proof
**1. Exact update formulas.** A vertex of the first shore with current bit \(x\) and matched bit \(y\) sees exactly \(a-x+y\) positive neighbors; its degree is \(n\). For even \(n=2m\), comparing this count with \(m\) and retaining \(x\) on equality gives the complete set-valued rule
\[
A'=\begin{cases}\varnothing&a<m,\\ B&a=m,\\ U&a>m.\end{cases}
\]
The formula for \(B'\) is obtained by interchanging \(A,B\). In particular, if \(a=b=m\), the update simply interchanges \(A,B\). Otherwise at least one shore becomes \(\varnothing\) or \(U\) after one update. Extremal shores remain extremal, and the other shore becomes extremal after at most one further update. All four extremal pairs are fixed. The only other fixed states are \((S,S)\) with \(|S|=m\), and the remaining pairs with \(|A|=|B|=m\) are primitive two-cycles. There are \(C\) choices for each balanced shore, hence \(C\) extra fixed configurations and \(C^2-C\) primitive two-cycle states. If a state maps into one of these two-cycles then both original shores had size \(m\), so it was already periodic. For \(m\ge2\), take \(|A|=m\) and \(|B|=m-1\) with \(B\ne\varnothing\); then the dynamics is \((A,B)\to(B,\varnothing)\to(\varnothing,\varnothing)\), requiring exactly two steps. When \(m=1\), direct application of the same three-case rule gives maximum one step.

**2. Odd-sized shores.** Write \(n=2m+1\), \(m\ge1\). The same neighbor-count comparison gives
\[
A'=\begin{cases}
\varnothing&a<m,\\
B\setminus A&a=m,\\
(U\setminus A)\cup B&a=m+1,\\
U&a>m+1.
\end{cases}
\]
Again interchange the two shores for \(B'\). Both shore sizes must belong to \(\{m,m+1\}\) for a recurrent nonextremal state. Indeed a shore outside this range becomes extremal in one update, remains so forever, and the other shore then becomes fixed within at most two more updates: if the first is empty, the second shore can pass from size \(m+1\) to size \(m\) to empty; if the first is full, it can pass from size \(m\) to size \(m+1\) to full. No nonextremal shore can be fixed: when its size is \(m\), its update is disjoint from itself, and when its size is \(m+1\), its update contains the nonempty complement of itself. Therefore exactly the four extremal pairs are fixed.

It remains to check the three possibilities for the two middle sizes. For \((a,b)=(m,m)\), both next shore sets are the symmetric differences \(B\setminus A\) and \(A\setminus B\), of sizes \(m-c\). If \(c=0\), they swap, giving primitive two-cycles. If \(c\ge1\), both sizes fall below \(m\) and the next state after that is empty on both shores.

For \((a,b)=(m+1,m+1)\), both next sizes equal \(m+c\), with \(c\ge1\). When \(c=1\), the union of the two original shore sets is \(U\) and the update swaps the shores; this is a primitive two-cycle since the shores cannot be identical. When \(c\ge2\), both next sizes exceed \(m+1\), so the following update gives the fully positive fixed state.

For \((a,b)=(m,m+1)\) (and symmetrically the reverse), the next shore sizes are \(m+1-c\) and \(m+c\). When \(c=0\), the shores are complementary and swap, giving a primitive two-cycle. When \(c=1\), the next shores have sizes \(m,m+1\) and are disjoint, hence enter the preceding primitive two-cycle class after one update. When \(c\ge2\), one next shore has size below \(m\) and the other above \(m+1\), hence the following update gives an extremal fixed pair. These cases are exhaustive and establish the period and basin classification. They also give a universal three-step first-periodic-entry bound. For \(m\ge2\), take an initial first shore consisting of one vertex contained in a second shore of size \(m+1\); the successive first/second shore sizes are \((1,m+1)\), \((0,m+1)\), \((0,m)\), \((0,0)\), proving sharpness. At \(m=1\) the first case has initial size \(1=m\), so the same rule establishes a maximum of two, attained by initial shores \((U,B)\) with \(|B|=1\).

**3. Exact enumeration and basin sizes.** In the odd case, states on primitive two-cycles comprise exactly the following disjoint classes: (i) two disjoint shores both of size \(m\), with \(\frac{n!}{m!m!}\) configurations; (ii) shores both of size \(m+1\), meeting in exactly one vertex, again \(\frac{n!}{m!m!}\) configurations; and (iii) two complementary shores of sizes \(m,m+1\), in either order, with \(2\binom{n}{m}\) configurations. Since \(\frac{n!}{m!m!}=(m+1)\binom{n}{m}\), there are precisely \(2(m+2)\binom{n}{m}\) periodic two-cycle states, hence \((m+2)\binom{n}{m}\) distinct orbits. The only additional states attracted to these cycles are mixed middle-size configurations with \(c=1\), in either shore orientation. Their number is \(2\frac{n!}{m!(m-1)!}=2m(m+1)\binom{n}{m}\). Adding yields the asserted total basin size. For the even case, Step 1 already gives all counts and exact basin membership.

**4. Asymptotics.** The uniform initial distribution has \(4^n\) equally likely configurations. Use \(\binom{2m}{m}=4^m/\sqrt{\pi m}\,(1+O(m^{-1}))\) and \(\binom{2m+1}{m}=2\cdot4^m/\sqrt{\pi m}\,(1+O(m^{-1}))\) in the exact basin formulas. This gives the two probabilities and their differing decay scales.

## Verification
The standalone program `verify.py` independently evaluates the per-vertex neighbor-majority rule for every labelled configuration of sizes \(2\le n\le8\), a total of \(87{,}376\) configurations. It also checks all matched-pair population profiles for every \(2\le n\le40\), weighting each profile by its exact multinomial multiplicity; this includes all fixed-state counts, primitive-period counts, two-cycle basins, and sharp transient bounds for those finite sizes. The script prints `TWO_CLIQUE_MAJORITY_PARITY_VERIFY_OK` if every assertion succeeds. Finite verification is corroboration only; the parameter-uniform proof is the exhaustive set-theoretic case division above.

## Relationship to prior work
The Goles–Olivos theorem establishes eventual periods at most two for symmetric threshold systems, without supplying this matched-two-clique periodic census or sharp universal transient. Benjamini–Chan–O'Donnell–Tamuz–Tan (arXiv:1405.2486) investigate majority dynamics on unimodular and random graphs, including the general finite period-two property; their inspected introduction and principal results concern different graph families and measures. Tamuz–Tessler (arXiv:1307.4035) develop information-retention and stabilization estimates on graphs; the inspected results do not give the present exact matched-clique orbit/basin formulas. The static majority C-coloring problem on graph products is not the synchronous opinion evolution studied here. The present graph is the complement of the standard crown graph on the same matched vertices, but complementing the graph does not conjugate the neighbor-majority update: local neighbor sums change in a state-dependent way. These comparisons do not certify global originality.

## Limitations
The theorem concerns only the stated binary synchronous, tie-retaining rule on the matching-coupled pair of complete cliques; it does not classify arbitrary two-community graphs, weighted votes, asynchronous updates, biased initial laws, or multicolor updates. The source comparison is not an exhaustive literature census. The foundational 1980 Goles–Olivos article was accessible through its abstract and bibliographic record, not through a complete inspectable full text; an unindexed specialized prior enumeration remains possible. Independent verification has not been performed.

## References
1. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, initial arXiv posting 2013-07-15, arXiv:1307.4035.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, initial arXiv posting 2014-05-11, arXiv:1405.2486.
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI 10.1016/0012-365X(80)90121-1.
