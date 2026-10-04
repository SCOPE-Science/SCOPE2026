# Two preference types restore stochastic-dominance envy-freeness of random priority
## Finding
Consider a strict square one-sided assignment problem with \(n\) agents and \(n\) objects. Random Priority, equivalently Random Serial Dictatorship (RSD), chooses a uniformly random priority ordering and lets agents choose their favorite remaining object in that order.

If the reported profile contains at most two distinct preference orders, then the RSD random assignment is stochastic-dominance envy-free: for every pair of agents \(i,j\), agent \(i\)'s lottery weakly stochastically dominates agent \(j\)'s lottery according to \(i\)'s own ranking.

The restriction to at most two preference types is sharp. With three agents and three objects, exactly
\[
72
\]
of the \(6^3=216\) labeled strict profiles fail stochastic-dominance envy-freeness. Every one of those \(72\) profiles uses three distinct preference orders. Under independent relabeling of agents and objects, the \(72\) failures form exactly two isomorphism classes, each of orbit size \(36\).

A representative failure uses objects \(a,b,c\) and rankings
\[
a\succ c\succ b,\qquad a\succ b\succ c,\qquad b\succ a\succ c.
\]
RSD gives the three agents the lotteries
\[
(1/2,0,1/2),\qquad(1/2,1/6,1/3),\qquad(0,5/6,1/6)
\]
in the object order \((a,b,c)\). For the second agent, whose ranking is \(a\succ b\succ c\), her own cumulative probability of receiving \(a\) or \(b\) is \(2/3\), whereas the third agent's lottery assigns probability \(5/6\) to that same top-two set. Hence her own lottery does not stochastically dominate the third agent's lottery.

## Assumptions and scope
Preferences over the \(n\) objects are strict total orders. Each object has unit capacity and every agent receives exactly one object. RSD randomizes uniformly over all \(n!\) priority orders.

For a lottery \(p\) and agent \(i\)'s ranking, write \(T_i(k)\) for the set of her top \(k\) objects. Lottery \(p\) stochastically dominates lottery \(q\) for agent \(i\) when
\[
p(T_i(k))\ge q(T_i(k))
\]
for every \(k=1,\ldots,n\). A random assignment is stochastic-dominance envy-free when each agent's own lottery stochastically dominates every other agent's lottery according to her own ranking.

The theorem concerns the standard stochastic-dominance notion of envy-freeness. It does not concern lexicographic dominance over lotteries, subjective indifferences, multiple copies of objects, or unequal numbers of agents and objects.

## Proof
The key observation is a top-set lower bound that holds for every RSD profile. Fix agent \(i\) and \(k\in\{1,\ldots,n\}\). Whenever \(i\) appears among the first \(k\) positions of the random priority ordering, fewer than \(k\) objects have been removed before her turn. Therefore at least one object in her top-\(k\) set \(T_i(k)\) is still available, and she chooses an object in that set. Since each priority position is equally likely,
\[
p_i(T_i(k))\ge \frac{k}{n}.
\]

Now suppose the profile contains exactly two preference types, called \(A\) and \(B\), with \(r\) agents of type \(A\) and \(s=n-r\) agents of type \(B\). Equal treatment of equals under uniform RSD implies that all type-\(A\) agents receive the same lottery \(x^A\), and all type-\(B\) agents receive the same lottery \(x^B\).

Fix a top-\(k\) set \(T\) for preference type \(A\). Feasibility of the random assignment gives total probability \(k\) across all agents for the \(k\) objects in \(T\), so
\[
r x^A(T)+s x^B(T)=k.
\]
The top-set lower bound gives \(x^A(T)\ge k/n\). Thus
\[
s\bigl(x^A(T)-x^B(T)\bigr)
= n x^A(T)-k\ge0.
\]
Hence \(x^A(T)\ge x^B(T)\) for every top set of type \(A\), so a type-\(A\) agent's own lottery stochastically dominates a type-\(B\) agent's lottery according to type \(A\). The same argument with the roles exchanged proves the corresponding statement for type \(B\). Agents of the same type receive identical lotteries. Therefore RSD is stochastic-dominance envy-free at every profile with at most two preference types. The one-type case is immediate.

Sharpness follows from the displayed three-agent witness. The exact \(n=3\) census is finite: direct enumeration of all \(216\) labeled profiles finds \(72\) failures, all with three distinct preference orders, and quotienting by \(S_3\times S_3\) gives two failure classes of size \(36\).

## Verification
The embedded `verify_rsd_two_type_envy.py` uses exact integer priority counts. It exhaustively checks all strict profiles for \(n\le3\), obtaining zero failures for \(n\le2\) and exactly \(72\) failures among the \(216\) three-agent profiles. It independently canonicalizes every three-agent profile under all agent and object relabelings, obtaining \(10\) total profile classes and exactly two failing classes, each with orbit size \(36\).

The verifier also replays the displayed three-agent witness exactly and checks every two-preference-type multiplicity profile through \(n=6\), after using object relabeling to normalize the first preference type. These finite checks cover \(4{,}166\) two-type profiles and verify the top-set lower bound in every case. The all-\(n\) statement itself rests on the algebraic proof above, not on finite extrapolation.

## Relationship to prior work
Bogomolnaia and Moulin define stochastic-dominance envy-freeness for random assignments and prove that Probabilistic Serial is envy-free, whereas Random Priority is only weakly envy-free in general and may fail envy-freeness once \(n\ge3\). Their article was published online on 29 March 2001.

Hosseini, Larson, and Cohen revisit RSD fairness and give the same three-agent preference pattern used here as a standard non-sd-envy-free example. They emphasize that envy properties depend on preference structure and empirically examine envy across profile spaces. That example is therefore not claimed as new.

The new statement is the domain theorem: at most two distinct strict preference orders are sufficient for full stochastic-dominance envy-freeness of RSD for every square market size. The exact three-agent census shows that the preference-type bound is sharp and gives the complete smallest failure quotient. Targeted literature and published-finding corpus searches for two-preference-type, two-ranking, and exact small-market RSD envy statements did not locate an equivalent theorem or census.

## Limitations
The proof uses the square unit-capacity model, strict preferences, and uniform random priority. It does not assert the result for subjective ties, unequal numbers of agents and objects, nonuniform priority lotteries, or multi-unit allocation.

The originality search cannot exclude an unindexed thesis, teaching note, software table, or unpublished manuscript containing the same two-type argument or three-agent census. The finite census is secondary to the general proof and should not be extrapolated to counts at larger \(n\).

## References
1. A. Bogomolnaia and H. Moulin, “A New Solution to the Random Assignment Problem,” *Journal of Economic Theory* 100 (2001), 295–328. DOI: 10.1006/jeth.2000.2710. Published online 29 March 2001.
2. H. Hosseini, K. Larson, and R. Cohen, “Random Serial Dictatorship versus Probabilistic Serial Rule: A Tale of Two Random Mechanisms,” arXiv:1503.01488, first submitted 4 March 2015.
