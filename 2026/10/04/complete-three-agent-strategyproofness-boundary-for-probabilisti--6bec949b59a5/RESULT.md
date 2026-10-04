# Complete three-agent strategyproofness boundary for probabilistic serial
## Finding
Consider the probabilistic serial (PS) mechanism with the same number of agents and indivisible objects, interpreted fractionally: every object has mass one, every agent eats continuously at unit speed from the most-preferred object that still has positive mass, and the fraction eaten is the assignment probability.

For two agents and two objects, PS is fully strategyproof in stochastic-dominance terms. With three agents and three objects, full strategyproofness first fails, and the entire boundary can be classified exactly.

Among the
\[
6^3=216
\]
labeled strict preference profiles, exactly
\[
54
\]
fail full stochastic-dominance strategyproofness. Thus the exact profile incidence under impartial culture is
\[
\frac{54}{216}=\frac14.
\]

There are exactly \(72\) vulnerable agent-profile pairs. Each vulnerable agent has exactly one false report for which the truthful PS allocation fails to weakly stochastically dominate the allocation under that report. Consequently, if a profile and then one of its three agents are chosen uniformly, the exact incidence of vulnerability is
\[
\frac{72}{216\cdot3}=\frac19.
\]

The \(54\) bad profiles form exactly two classes under independent relabeling of agents and objects. One class has \(18\) labeled profiles and the other has \(36\).

Normalize the manipulator's true ranking to
\[
A\succ B\succ C.
\]
Every violating report is then
\[
B\succ A\succ C.
\]
Up to exchanging the two nonmanipulating agents, the other two rankings are exactly one of
\[
\{A\succ B\succ C,\ B\succ C\succ A\}
\]
or
\[
\{B\succ A\succ C,\ B\succ C\succ A\}.
\]
The first structural type generates the \(18\)-profile orbit; because the two \(A\succ B\succ C\) agents are symmetric, each such profile has two vulnerable agents. The second type generates the \(36\)-profile orbit and each such profile has one vulnerable agent. Both event orbits therefore contain \(36\) labeled deviations.

The lottery geometry is universal across all \(72\) deviations. Relative to the manipulator's true order \((A,B,C)\), the truthful and deviating allocations are one of
\[
\left(\frac12,\frac16,\frac13\right)
\quad\text{and}\quad
\left(\frac14,\frac12,\frac14\right),
\]
or
\[
\left(\frac34,0,\frac14\right)
\quad\text{and}\quad
\left(\frac12,\frac13,\frac16\right).
\]
In both cases, deviating minus truthful probability is
\[
\left(-\frac14,\frac13,-\frac1{12}\right).
\]
Hence, for any compatible von Neumann--Morgenstern utilities \(T>M>B\) assigned to the top, middle, and bottom objects, the expected-utility gain is
\[
\frac{-3T+4M-B}{12}.
\]
The deviation is profitable exactly when
\[
4M>3T+B.
\]
After affine normalization \(T=1\) and \(B=0\), the condition is simply \(M>3/4\).

No three-agent misreport strictly stochastically dominates the truthful lottery. Thus the classification is consistent with the classical result that PS is weakly strategyproof but not fully strategyproof from three agents onward.

## Assumptions and scope
There are exactly as many objects as agents, one unit of each object, and all preferences over sure objects are strict. The main boundary concerns \(n=3\); the \(n=2\) case is used only to establish sharpness.

For lotteries \(x\) and \(y\) and a strict ranking, \(x\) weakly stochastically dominates \(y\) if the cumulative probability of receiving one of the best \(k\) objects is at least as high under \(x\) for every cutoff \(k\).

Full strategyproofness requires the truthful PS lottery to weakly stochastically dominate the lottery induced by every unilateral misreport. Weak strategyproofness only rules out a misreport whose lottery strictly stochastically dominates the truthful lottery. The theorem classifies failures of the stronger property.

The profile incidence \(1/4\) treats all \(216\) labeled strict profiles equally. The agent incidence \(1/9\) additionally chooses one of the three labeled agents uniformly.

## Proof
For \(n=2\), exhaustive evaluation of the four labeled strict profiles gives no full-strategyproofness failure. This also agrees with the classical observation that PS and random priority coincide for two agents.

For \(n=3\), there are six strict orders and therefore \(216\) labeled profiles. For each profile, PS is computed exactly with rational arithmetic. Every one of the three agents is then assigned each of its five false reports in turn, PS is recomputed, and the truthful and deviating lotteries are compared by stochastic dominance using the agent's true ranking.

A deviation is recorded precisely when the truthful lottery does not weakly stochastically dominate the deviating lottery. This exhaustive profile-first calculation yields \(72\) deviations on \(54\) distinct profiles. It separately checks that none of those deviations strictly stochastically dominates truth, so the weak-strategyproofness property is preserved.

As an independent replay of the three-by-three PS assignments, each object is represented by twelve equal micro-units. On this finite universe every event time lies on the corresponding twelve-step grid; the verifier checks directly, profile by profile, that the resulting integer-tick allocations agree exactly with the continuous event-driven rational implementation on all \(216\) profiles. The classification is then reconstructed from the event set by symmetry rather than inferred from one implementation's internal states.

Independent relabeling of the three agents and three objects partitions the full \(216\)-profile universe into exactly ten isomorphism classes. Exactly two of those classes contain full-strategyproofness failures. Canonical representatives are
\[
(A B C,\ A B C,\ B C A)
\]
and
\[
(A B C,\ A C B,\ B A C),
\]
with orbit sizes \(18\) and \(36\), respectively.

To classify deviations themselves, relabel objects so that the manipulator's true order is \(A\succ B\succ C\), place the manipulator first, and sort the two remaining rankings. The complete event set collapses to exactly two normalized forms:
\[
(A B C;\ \{A B C,B C A\};\ B A C)
\]
and
\[
(A B C;\ \{B A C,B C A\};\ B A C),
\]
where the final order is the false report. Each normalized event orbit has \(36\) labeled members.

For every recorded deviation, the false report swaps only the top two objects. Direct subtraction of the exact lotteries gives cumulative deviations \(-1/4\) at the top object and \(1/12\) at the top-two cutoff. Equivalently, objectwise deviations are \((-1/4,1/3,-1/12)\). The expected-utility condition follows immediately.

## Verification
The embedded `verify_ps3_strategyproof_boundary.py` uses only exact integer and rational arithmetic from the Python standard library.

It performs the following checks:

- every one of the four two-agent profiles and all false reports;
- all \(216\) three-agent profiles and all \(3\cdot5\) unilateral false reports per profile;
- exact stochastic-dominance comparisons under each true ranking;
- absence of any strict stochastic-dominance improvement, confirming weak strategyproofness on the enumerated boundary;
- equality of an event-driven continuous PS implementation and an independent twelve-microtick implementation on all \(216\) three-agent profiles;
- exactly \(54\) bad profiles, \(72\) vulnerable agent-profile pairs, and one violating report per vulnerable agent;
- the \(18+36\) profile-orbit decomposition and two \(36\)-event normalized orbits;
- the universal lottery difference and utility condition \(4M>3T+B\);
- the ten agent/object isomorphism classes of the full three-agent profile universe.

Replay with:

`python3 verify_ps3_strategyproof_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Bogomolnaia and Moulin introduced the probabilistic serial mechanism and proved that it is weakly strategyproof but not fully strategyproof for \(n\ge3\). Their Section 7 gives a three-agent profitable misreport for suitable compatible utilities, and their appendix records the ten preference-profile types up to relabeling. Thus the three-agent minimality of full-strategyproofness failure and one of the two structural failure types are prior work.

Aziz, Gaspers, Mattei, Narodytska, and Walsh later study strategic behavior under PS. Their three-agent introductory example is adapted from the original paper and exhibits the all-distinct structural type above. Their experimental section estimates manipulability frequencies from sampled profiles under specified utility models rather than exhaustively enumerating the three-by-three ordinal boundary.

Balbuzanov introduces convex strategyproofness, an intermediate property between weak and full strategyproofness, and proves that generalized PS satisfies it. This broader geometric result is compatible with the present census but does not, from the accessible inspected material, state the exact \(54\)-profile boundary, its two orbit types, or the common utility threshold.

The contribution here is therefore not the existence or minimum size of a PS manipulation. It is the complete smallest-market classification: exact profile and agent incidences, the second structural orbit, uniqueness of the violating report for every vulnerable agent, and the universal utility cone across all failures.

## Limitations
The theorem concerns exactly three agents and three objects for the full census. It does not give manipulability frequencies for larger markets.

A failure of full stochastic-dominance strategyproofness means that truth does not dominate every false report. Because PS remains weakly strategyproof here, the profitable deviation depends on the compatible cardinal utility representation; no false report stochastically dominates truth.

The exact census was not found in the inspected literature or semantic-index searches, but an unindexed note, thesis, code repository, or supplementary table may contain an equivalent enumeration. Full text for the 2016 convex-strategyproofness paper was not accessible from its institutional repository during this check; its abstract and bibliographic record were inspected, so no whole-document absence claim rests on that source alone.

## References
1. A. Bogomolnaia and H. Moulin, “A New Solution to the Random Assignment Problem,” *Journal of Economic Theory* 100 (2001), 295–328. DOI: 10.1006/jeth.2000.2710. Published online 29 March 2001.
2. H. Aziz, S. Gaspers, N. Mattei, N. Narodytska, and T. Walsh, “Strategic aspects of the probabilistic serial rule for the allocation of goods,” arXiv:1401.6523, submitted 25 January 2014.
3. I. Balbuzanov, “Convex strategyproofness with an application to the probabilistic serial mechanism,” *Social Choice and Welfare* 46 (2016), 511–520. DOI: 10.1007/s00355-015-0926-z.
