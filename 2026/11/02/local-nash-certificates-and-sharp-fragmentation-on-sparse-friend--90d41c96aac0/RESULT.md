# Local Nash certificates and sharp fragmentation on sparse friendship networks

## Finding

Consider the standard simple symmetric fractional hedonic game of a finite simple undirected friendship graph \(G=(V,E)\) with \(1\leq\deg(v)\leq2\) for every vertex. A partition \(\pi\) assigns each vertex \(v\) a coalition \(\pi(v)\). The utility of \(v\) is
\[
u_v(\pi)=\frac{|N_G(v)\cap\pi(v)|}{|\pi(v)|}.
\]
A unilateral deviation may move \(v\) to any *other* existing coalition or to a new singleton; Nash stability forbids strictly improving deviations.

**Local certificate theorem.** Every partition \(\pi\), including partitions whose coalitions induce disconnected subgraphs, is Nash stable if and only if both conditions hold:

1. Every vertex has at least one neighbor in its own coalition: \(|N_G(v)\cap\pi(v)|\geq1\).
2. Every edge \(vw\in E\) with \(\pi(v)\ne\pi(w)\) joins coalitions whose *total* sizes differ by at most one:
   \[
   \bigl||\pi(v)|-|\pi(w)|\bigr|\leq1.
   \]

Given the graph, vertex coalition labels, and coalition sizes, these conditions certify Nash stability in \(O(|V|+|E|)\) time. For a cycle \(C_n\) of \(n\geq3\) labeled vertices, let \(F(n)\) denote the maximum number of connected components of the subgraph induced by a single coalition, over all Nash-stable partitions. Then
\[
\boxed{F(n)=\max\{1,\lfloor n/4\rfloor\}.}
\]
In particular, stable coalitions that are geographically disconnected first occur at \(n=8\); there are exactly two Nash-stable partitions with a disconnected coalition on the labeled eight-cycle.

## Assumptions and scope

The friendship graph is loopless, simple, undirected and unweighted; nonadjacent agents value one another at zero and adjacent agents at one. The denominator includes the deviating agent, even for the newly joined coalition. No agent consent requirement applies to joining an existing coalition. Tied utilities do **not** constitute an improving deviation. The graph can be a disjoint union of paths and cycles, but must have no isolated vertices. The component-count corollary concerns the usual connected cycle \(C_n\), not the total number of coalitions.

## Proof

**Necessity of a same-coalition friend.** Suppose \(v\) has no neighbor in \(\pi(v)\). Its utility is zero. Since its graph degree is positive, it has a neighbor \(w\) in another coalition. Joining \(\pi(w)\) yields utility at least \(1/(|\pi(w)|+1)>0\), a strict improvement. Therefore every stable partition satisfies the first condition.

**Necessity of size balance.** Consider an edge \(vw\) across coalitions \(A=\pi(v)\) and \(B=\pi(w)\). By the first condition, both endpoints have a same-coalition neighbor. Maximum graph degree two then forces each endpoint to have *exactly one* same-coalition neighbor and exactly one external neighbor. The utilities at the two boundary vertices are \(1/|A|\) and \(1/|B|\). The deviation of \(v\) to \(B\) yields exactly \(1/(|B|+1)\), and the deviation of \(w\) to \(A\) yields exactly \(1/(|A|+1)\). Both deviations must fail to strictly improve utility; hence \(|A|\leq|B|+1\) and \(|B|\leq|A|+1\). These are equivalent to the second condition.

**Sufficiency.** Assume both conditions. A vertex with two same-coalition neighbors has no external neighbor; joining any other coalition or becoming a singleton gives utility zero, so cannot improve. A vertex with one same-coalition neighbor earns \(1/|\pi(v)|\). It has at most one external neighbor. Joining a coalition without that external neighbor gives zero; if an external neighbor lies in coalition \(B\), the move gives exactly \(1/(|B|+1)\), at most its current utility by the second condition. Becoming a singleton always gives zero. Every unilateral deviation fails to strictly improve utility, proving the equivalence, including arbitrary disconnected coalitions. Counting sizes and checking the two local conditions needs linear time.

**Cycle fragmentation: upper bound.** On \(C_n\), if a coalition \(A\) has \(t\geq2\) induced connected components, each component is a consecutive cyclic run of at least two vertices by the first condition. The \(t\) cyclic gaps between these runs also have length at least two: a gap of length one would have both its neighbors in \(A\), giving that outside vertex no same-coalition neighbor and contradicting the first condition. Thus \(n\geq4t\). For any coalition with at most one component, the bound \(t\leq\max\{1,\lfloor n/4\rfloor\}\) is immediate.

**Sharpness for every cycle size.** For \(n=3\), the grand coalition is stable and connected. For \(n\geq4\), put \(t=\lfloor n/4\rfloor\) and \(r=n-4t\in\{0,1,2,3\}\). Partition the cycle into \(2t\) consecutive runs alternating between coalitions \(A\) and \(B\), initially all of length two. Increase the length of one \(A\)-run by \(\lfloor r/2\rfloor\), and the length of one \(B\)-run by \(\lceil r/2\rceil\). Every run has length at least two and the two complete coalition sizes differ by at most one. The local certificate proves the partition Nash stable, and coalition \(A\) has exactly \(t\) induced components. This attains the upper bound.

**First occurrence and exact eight-cycle count.** A disconnected coalition requires \(t\geq2\), so the upper bound forces \(n\geq8\). When \(n=8\), equality in the counting bound forces exactly two coalition runs of size two separated by two gaps of size two. The size-balance condition prevents the two gaps from being distinct coalitions of size two, because each would border a coalition of size four. Thus precisely two coalitions occupy the cyclic run pattern \(A,A,B,B,A,A,B,B\), up to swapping their names. There are eight possible starting positions and a fourfold identical periodic/run-name representation, giving exactly two distinct labeled set partitions. Both satisfy the certificate.

## Verification

The standalone finite checker in `checks/verify_cycle_nash.py` compares every possible unilateral move, by exact integer cross multiplication, with the new two-condition certificate for every set partition of cycles of orders three through ten, paths of orders two through nine, and eleven disjoint unions of paths/cycles. Command: `python3 checks/verify_cycle_nash.py`. The completed run compared 172,620 unrestricted set partitions without a discrepancy; on cycles the Nash-stable counts for orders three through ten were \(1,3,6,6,15,17,31,48\). Exactly \(2,9,15\) stable partitions had a disconnected coalition for cycle orders eight, nine and ten respectively. Finite enumeration confirms boundary cases but is not used as an infinite proof.

## Relationship to prior work

Hanaka, Ikeyama and Ono (2023) study welfare optimization in fractional hedonic games on tree-like graphs, including general bounded-treewidth algorithms; they do not establish an if-and-only-if Nash-certificate or the sharp cycle-fragmentation law here. Bilò, Fanelli, Flammini, Monaco and Moscardelli (2018) study existence, efficiency and computation of Nash-stable fractional-hedonic outcomes. Their grand-coalition existence observation and the possibility of low-welfare equilibria on paths do not imply the present full characterization of *all* stable partitions on degree-two networks. Brandl, Brandt and Strobel (2015) develop the general stability landscape, not a degree-two all-partition criterion. These earlier general definitions and results are credited, and no novelty is claimed for the definition of Nash stability itself.

## Limitations

The if-and-only-if certificate assumes no isolated vertex and maximum graph degree two; no statement is made for signed or weighted preferences, higher degrees, modified fractional utilities that divide by coalition size minus one, group deviations, or coalition-access constraints. The sharp component law concerns cycles; it is not a formula for the total number of stable partitions for arbitrary cycle orders. Exhaustive calculations cover only the specified finite orders. The originality assessment is based on inspected sources and search evidence, not an absolute priority guarantee, and independent external validation has not been performed.

## References

1. T. Hanaka, A. Ikeyama and H. Ono, *Maximizing Utilitarian and Egalitarian Welfare of Fractional Hedonic Games on Tree-like Graphs*, first public October 8, 2023, https://arxiv.org/abs/2310.05139 .
2. V. Bilò, A. Fanelli, M. Flammini, G. Monaco and L. Moscardelli, *Nash Stable Outcomes in Fractional Hedonic Games: Existence, Efficiency and Computation*, Journal of Artificial Intelligence Research 62 (2018), 315–371, https://doi.org/10.1613/jair.1.11211 , full text https://www.jair.org/index.php/jair/article/download/11211/26422 .
3. F. Brandl, F. Brandt and M. Strobel, *Fractional Hedonic Games: Individual and Group Stability*, AAMAS 2015, https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2015/aamas/p1219.pdf .
