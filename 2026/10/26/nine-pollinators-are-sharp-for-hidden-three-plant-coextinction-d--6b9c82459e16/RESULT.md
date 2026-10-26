# Nine pollinators are sharp for hidden three-plant coextinction dependence under two survivors

## Finding

**Theorem.** Let \(U\) be a finite pollinator set of size \(N\), and retain exactly two pollinators chosen uniformly from all \(\binom N2\) pairs. Three plants have nonempty pollinator neighborhoods \(A,B,C\subseteq U\); a plant becomes extinct precisely when its neighborhood misses the retained pair. Assume every plant-extinction event has probability strictly between zero and one.

If all three plant-extinction indicators are pairwise independent, then \(N\ge9\). This is sharp. At \(N=9\), the three indicators are pairwise independent **if and only if** each plant has exactly five pollinator neighbors and each two plant neighborhoods intersect in exactly three pollinators. There are exactly three incidence types up to relabeling pollinators, parameterized by \(t=|A\cap B\cap C|\in\{1,2,3\}\). Their common single-plant extinction probability is \(1/6\), and every pair's joint extinction probability is \(1/36\). But the probability that all three plants become extinct is \(1/36\) at \(t=1\) and zero at \(t=2,3\), never the mutually independent prediction \(1/216\).

Among nine-pollinator networks in which every pollinator serves at least one plant, exactly one such incidence type is possible: three universal pollinators are shared by all three plants, and each plant has two additional pollinators serving that plant alone. For this network, at least one plant is guaranteed to survive, even though all three extinction indicators are pairwise independent. As an additional sharp nonmonotonicity, at \(N=10\) no three nondegenerate extinction indicators can be pairwise independent under the same two-survivor protocol.

## Assumptions and scope

The pollinator and plant guilds are labeled for probability calculations but networks are classified up to pollinator relabeling, with three named plants. The initial bipartite network is fixed and simple, with no restriction against pollinators unused by these three plants unless explicitly imposed. The two surviving pollinators are a uniformly chosen unordered pair; there are no subsequent interactions or rescue mechanisms. Extinction is the complement of at least one neighbor surviving. Independence is *stochastic independence of extinction indicators*, not disjointness of neighbor sets. The theorem fixes exactly two survivors: the first quota for which a surviving pair interacts with the plant-neighborhood structure.

## Proof

For nonempty plant neighborhoods \(A,B\), put \(x=N-|A|\), \(y=N-|B|\), \(z=N-|A\cup B|\), and \(D=\binom N2\). Nondegenerate extinction probabilities require \(2\le x,y\le N-1\); pairwise independence additionally forces \(z\ge2\). Since extinction means the two surviving pollinators both lie in the complement of the relevant neighborhood,

\[
\Pr(E_A)=\frac{\binom x2}{D},\qquad
\Pr(E_A\cap E_B)=\frac{\binom z2}{D}.
\]

Thus independence is equivalent to the exact integer equation

\[
\binom z2\binom N2=\binom x2\binom y2,
\quad 2\le x,y<N,\quad
\max(2,x+y-N)\le z\le\min(x,y).
\tag{1}
\]

The exhaustive reduced integer enumeration in `verify.py`, which iterates the displayed finite integer bounds, gives **no** solutions for any \(3\le N\le8\), exactly \((x,y,z)=(4,4,2)\) for \(N=9\), and exactly \((3,6,2)\) up to exchanging \(x,y\) for \(N=10\). The computation is an exhaustive certificate for these *finite* sizes, rather than an extrapolation to arbitrary \(N\). Any nondegenerate pairwise-independent pair must have \(N\ge9\). At \(N=9\), equation (1) forces \(|A|=|B|=5\) and \(|A\cap B|=3\). Applied to all three pairs, this gives the stated common sizes and pair intersections. Conversely, those sizes force equation (1) for every pair, establishing pairwise independence.

Let \(t=|A\cap B\cap C|\). In the Venn decomposition, the common core has \(t\) pollinators, each pair-only region has \(3-t\), each plant-only region has \(t-1\), and the unused region has \(3-t\). Nonnegativity gives precisely \(1\le t\le3\). These numbers completely determine the incidence structure up to relabeling, and each \(t=1,2,3\) is realizable. The union has size \(6+t\), so simultaneous extinction has probability \(\binom{3-t}{2}/36\), which equals \(1/36,0,0\) in order; mutual independence would require \((1/6)^3=1/216\). No unused pollinators forces \(3-t=0\), giving the unique \(t=3\) configuration. Finally, at \(N=10\), equation (1) forces every independent pair to have complementary neighborhood sizes \(3\) and \(6\). Three plants cannot have every pair with opposite sizes, so no pairwise-independent triple exists.

## Verification

Run `python verify.py` with a standard Python interpreter. The checker enumerates all integral parameters in (1) for \(N=3,\ldots,10\), checks the exact list of solutions and constructs the three nine-pollinator incidence types by their seven Venn regions. It independently enumerates all 36 surviving pairs and checks each extinction marginal, pairwise intersection and triple intersection. See `verification_output.txt` for its deterministic output. There is no floating-point arithmetic. The finite exclusions are exhaustive because (1) depends only on the enumerated three cardinalities, not on unenumerated network labels.

## Relationship to prior work

Memmott, Waser and Price (2004) motivate random pollinator removal and secondary plant extinction in bipartite mutualisms. Burgos et al. (2006) study nested topology and robustness to extinction. Standard examples of pairwise but not joint independence demonstrate the logical distinction, but do not impose the **uniformly sampled two-survivor** representation through intersections with three fixed pollinator neighborhoods. The present contribution is the sharp nine-pollinator cardinality boundary and complete classification of its three incidence realizations, including the ten-pollinator impossibility. General two-species co-survival formulas alone do not state the three-species incidence classification or the triple-event law.

## Limitations

These are exact population-model probabilities, not estimates from sampled field observations. The finite exclusions apply to exactly two surviving pollinators; no claim is made about all larger survival quotas or arbitrary heterogeneous survival mechanisms. Independent publication review has not been performed. Classical pairwise-independent Boolean examples and general hypergeometric-event theory are significant possible routes to an equivalent earlier formulation; the available searches and source access cannot establish absolute novelty.

## References

1. Memmott, J., Waser, N. M., and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions.* Proceedings of the Royal Society B 271, 2605–2611. DOI: 10.1098/rspb.2004.2909. First published online 2004-12-06.
2. Burgos, E., Ceva, H., Perazzo, R., Devoto, M., Medan, D., Zimmermann, M., and Delbue, A. M. (2006). *Why Nestedness in Mutualistic Networks?* arXiv:q-bio/0609005, first public version 2006-09-05.
3. Kaiser-Bunbury, C. N., et al. (2010). *The robustness of pollination networks to the loss of species and interactions: a quantitative approach incorporating pollinator behaviour.* Ecology Letters 13, 442–452. DOI: 10.1111/j.1461-0248.2009.01437.x.
