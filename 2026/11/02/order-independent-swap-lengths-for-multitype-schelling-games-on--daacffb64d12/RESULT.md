# Order-independent swap lengths for multitype Schelling games on bicliques

## Finding
Fix positive integers \(a,b\) and a finite set of \(k\ge 2\) types. In the fully occupied swap Schelling game on \(K_{a,b}\), each agent's utility is the fraction of neighbors sharing her type, and a swap is permitted only when both participating agents strictly increase utility. For each type \(c\), let \(r_c\) and \(s_c\) be its numbers of agents in the two parts of sizes \(a\) and \(b\), respectively. Write
\[
d_c=b r_c-a s_c,\qquad h=a+b,
\]
and define two nonnegative integers
\[
P=\sum_c\max\left\{0,\left\lceil\frac{d_c-b}{h}\right\rceil\right\},\qquad
Q=\sum_c\max\left\{0,\left\lceil\frac{-a-d_c}{h}\right\rceil\right\}.
\]
**Theorem.** Every maximal sequence of strictly mutually profitable swaps from the given assignment has **exactly the same number of swaps**,
\[
\boxed{T=\min(P,Q)\le \min(a-1,b-1).}
\]
The final assignment need not be unique. Moreover, an assignment is a swap equilibrium if and only if
\[
\boxed{\max_c d_c\le b\quad\text{or}\quad\min_c d_c\ge-a.}
\]
These statements hold without balancing the bipartition, limiting the number of types to two, or imposing a swap-selection policy.

## Assumptions and scope
The graph is the simple, undirected complete bipartite graph \(K_{a,b}\), with \(a,b\ge1\), no vacancies, and one strategic agent per vertex. Each agent has a fixed type from \(\{1,\dots,k\}\), with \(k\ge2\); absent types are allowed. All agents have the same type-fraction utility and no private vertex preferences or immobility constraints. Both agents must gain strictly for a swap to occur; the pair may be selected globally. A maximal improving sequence is one that cannot be extended by another permitted swap. The initial type counts are arbitrary nonnegative integers satisfying \(\sum_c r_c=a\) and \(\sum_c s_c=b\).

## Proof
**Step 1: characterize every profitable swap.** A same-part exchange leaves both participants' utility fractions unchanged, so it is not strictly profitable. A same-type cross-part exchange merely exchanges the two type-specific payoff values between participants and cannot improve both. Consider therefore an agent of type \(i\) in the first part and one of a distinct type \(j\) in the second. Before the exchange, their utilities are \(s_i/b\) and \(r_j/a\). After the exchange, they are \((r_i-1)/a\) and \((s_j-1)/b\). Their two strict inequalities are equivalent, respectively, to
\[
b r_i-a s_i>b,\qquad b r_j-a s_j<-a,
\]
that is, \(d_i>b\) and \(d_j<-a\). Conversely, these inequalities ensure that the required agents exist: \(d_i>b\) forces \(r_i\ge2\), and \(d_j<-a\) forces \(s_j\ge2\), so they can perform the described swap.

**Step 2: exact updates.** The swap changes only the two chosen types, giving
\[
d_i'=d_i-h,\qquad d_j'=d_j+h.
\]
Since \(d_i>b\), its updated value satisfies \(d_i'>-a\), so type \(i\) cannot become a deficit type after sending an agent from the first part to the second. Similarly, \(d_j<-a\) implies \(d_j'<b\), so type \(j\) cannot become a surplus type after sending an agent in the opposite direction. These two strict boundary inequalities are essential; they rule out direction reversals.

**Step 3: count surplus and deficit tickets.** Define the individual tickets
\[
p_c=\max\left\{0,\left\lceil\frac{d_c-b}{h}\right\rceil\right\},\qquad
q_c=\max\left\{0,\left\lceil\frac{-a-d_c}{h}\right\rceil\right\}.
\]
For a profitable pair, \(p_i\ge1\) and \(q_j\ge1\). Subtracting \(h\) from \(d_i\) reduces \(p_i\) by exactly one, and adding \(h\) to \(d_j\) reduces \(q_j\) by exactly one. By Step 2, neither update introduces a ticket of the opposite sign. Every other type is unchanged. Thus every permitted swap satisfies the **exact identities**
\[
P'=P-1,\qquad Q'=Q-1.
\]
A permitted swap exists if and only if there is at least one positive surplus and at least one negative deficit, equivalently if and only if \(P>0\) and \(Q>0\). Therefore a sequence stops precisely when its current \(\min(P,Q)\) becomes zero, and that minimum decreases by exactly one per swap. Every maximal sequence has length \(\min(P,Q)\), regardless of which available pair is chosen. This simultaneously proves termination and the equilibrium criterion.

**Step 4: uniform linear bound.** If \(p_c>0\), then \(r_c\ge2\), and
\[
p_c=\left\lceil\frac{b(r_c-1)-a s_c}{a+b}\right\rceil\le r_c-1.
\]
Thus, if any surplus type exists, \(P\le\sum_{c:p_c>0}(r_c-1)\le a-1\); if none exists, \(P=0\). Symmetrically, \(Q\le b-1\). Hence \(T\le\min(a-1,b-1)\) also at the boundary sizes \(a=1\) or \(b=1\).

**Examples distinguishing the result from standard potential bounds.** On \(K_{m,m}\), starting with all first-part agents of one type and all second-part agents of another gives \(T=\lfloor m/2\rfloor\), so the linear scale cannot generally be replaced by a constant. On \(K_{2,7}\), take three types with part counts \(r=(0,0,2)\) and \(s=(2,2,3)\). Swapping a third-type agent in the first part with a first-type agent in the second is strictly profitable, but the usual monochromatic-edge count \(\Phi=\sum_c r_cs_c\) **decreases from \(6\) to \(5\)**. Thus the standard monochromatic-edge increasing-potential proof for regular graphs does not establish this result on arbitrary bicliques.

## Verification
The standalone file `verify_biclique.py` uses integer cross multiplication for strict utilities and checks all explicitly colored assignments on \(K_{a,b}\) for \(1\le a,b\le4\) with two or three types, covering \(15{,}300\) colorings, \(191{,}080\) potential agent-pair comparisons, and \(26{,}760\) profitable swaps. An independent profile-state recursion checks \(272{,}868\) states and \(310{,}832\) transition instances for \(1\le a,b\le8\) and \(2\le k\le4\). For each branching state it compares the shortest and longest possible terminal path lengths with \(\min(P,Q)\); all agree. More than \(30{,}000\) states have distinct reachable terminal type profiles, emphasizing that path-length uniqueness does not assert equilibrium uniqueness. The \(K_{2,7}\) decreasing-edge-potential witness is also verified. These finite checks corroborate the algebraic all-size proof but do not replace it. Reproduce with `python3 verify_biclique.py`.

## Relationship to prior work
Agarwal, Elkind, Gan, and Voudouris formulated the mutually profitable multi-type swap model and studied equilibrium existence, complexity, and efficiency; their 2019 preprint does not state a biclique-specific, order-independent exact improvement duration. Bilò, Bilò, Lenzner, and Molitor proved finite improvement on regular and almost-regular topologies using a monochromatic-edge potential; that sufficient graph-regularity condition does not cover arbitrarily unbalanced bicliques, and their theorem does not fix the number of moves for every schedule. Kreisel, Boehmer, Froese, and Niedermeier analyzed computational hardness and robustness of Schelling equilibria, a different question. The new contribution claimed here is the two-ticket exact-length law together with its equilibrium characterization and linear bound, not the general Schelling swap model or the known existence results. An equivalent specialized statement in unexamined literature remains a priority risk.

## Limitations
Utilities must be the strict fraction of like-typed neighbors, and both agents must improve strictly. Stubborn agents, vacancies, extra graph edges, non-complete bipartite graphs, payoff heterogeneity, and unilateral jumps are outside the theorem. The result does not assert that all schedules reach the same equilibrium or the same social welfare, or that the linear upper bound is globally sharp for every bipartition size. Literature searches and full-text comparisons reduce but cannot eliminate publication-priority uncertainty. No independent external validation has been performed.

## References
1. L. Kreisel, N. Boehmer, V. Froese, and R. Niedermeier, *Equilibria in Schelling Games: Computational Hardness and Robustness*, arXiv:2105.06561, first public version 2021-05-13. https://arxiv.org/abs/2105.06561
2. A. Agarwal, E. Elkind, J. Gan, and A. A. Voudouris, *Swap Stability in Schelling Games on Graphs*, arXiv:1909.02421, first public version 2019-09-05. https://arxiv.org/html/1909.02421v3
3. D. Bilò, V. Bilò, P. Lenzner, and L. Molitor, *Topological Influence and Locality in Swap Schelling Games*, arXiv:2005.02752, first public version 2020-05-06. https://link.springer.com/article/10.1007/s10458-022-09573-7
