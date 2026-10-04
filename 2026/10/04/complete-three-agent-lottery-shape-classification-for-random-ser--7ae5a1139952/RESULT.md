# Complete three-agent lottery-shape classification for random serial dictatorship
## Finding
Consider a house-allocation problem with three agents and three objects, strict complete preferences, and random serial dictatorship (RSD): choose one of the six priority orders uniformly and let agents choose their favorite remaining object in that order.

For a fixed preference profile, group the six priority orders by the deterministic matching they induce. The resulting multiplicity spectrum can take exactly five values:
\[
(6),\qquad (3,3),\qquad (3,2,1),\qquad (2,2,1,1),\qquad (1,1,1,1,1,1).
\]
Equivalently, the only possible nonzero matching-probability multisets are
\[
(1),\qquad \left(\frac12,\frac12\right),\qquad \left(\frac12,\frac13,\frac16\right),\qquad \left(\frac13,\frac13,\frac16,\frac16\right),\qquad \left(\frac16,\ldots,\frac16\right).
\]

Among all
\[
6^3=216
\]
labeled strict-preference profiles, the five spectra occur with counts
\[
48,\qquad36,\qquad72,\qquad54,\qquad6,
\]
respectively. Thus the support-size distribution is
\[
1:48,\qquad2:36,\qquad3:72,\qquad4:54,\qquad6:6.
\]
In particular, support size \(5\) is impossible, and the mean number of deterministic matchings in the RSD support is
\[
\frac{48+2\cdot36+3\cdot72+4\cdot54+6\cdot6}{216}=\frac{49}{18}.
\]

The classification has a simple preference-profile description.

1. If all three agents have different first choices, every priority order gives the same matching, so the spectrum is \((6)\).
2. If all three agents have the same full ranking, the six priority orders give six different matchings, so the spectrum is \((1,1,1,1,1,1)\).
3. If all three agents have the same first choice but exactly two different full rankings, the spectrum is \((2,2,1,1)\).
4. If first-choice multiplicities are \((2,1)\) and all three full rankings are different, the spectrum is \((3,2,1)\).
5. If first-choice multiplicities are \((2,1)\) and exactly two full rankings occur, let the duplicated ranking be \(A\succ B\succ C\). If the singleton agent ranks \(B\) first, the spectrum is \((2,2,1,1)\); if the singleton ranks \(C\) first, the spectrum is \((3,3)\).

For every profile, the same deterministic-matching multiplicities arise from the core-from-random-endowments construction when its six possible initial endowments are evaluated by top trading cycles.

## Assumptions and scope
There are exactly three agents and three objects. Preferences are strict and complete. RSD randomizes uniformly over the six agent priority orders.

For the core-from-random-endowments (CRE) formulation, each of the six initial endowment matchings is selected uniformly and the unique core matching of the induced Shapley--Scarf housing market is used. With strict preferences, top trading cycles computes that unique core matching.

The multiplicity spectrum records how many of the six primitive randomizations lead to each distinct deterministic matching, sorted in decreasing order. It is not merely the support size: for example, support size four always has multiplicity spectrum \((2,2,1,1)\).

## Proof
There are only three possible first-choice occupancy patterns.

If the first choices are all distinct, no priority order creates competition for any first choice. Every agent receives her first choice, so all six orders induce the same matching. This gives spectrum \((6)\). The count is
\[
3!\,2^3=48,
\]
because the three first choices can be assigned bijectively to agents and each ranking has two possible orders of its remaining objects.

If all first choices coincide at an object \(A\), then each ranking is either \(A\succ B\succ C\) or \(A\succ C\succ B\). When all three full rankings coincide, the first dictator gets \(A\), the second gets the common second choice, and the third gets the last object. The six priority orders therefore produce all six deterministic matchings once each, giving \((1,1,1,1,1,1)\). There are \(3\cdot2=6\) such profiles. If both lower-order types occur, a direct six-order calculation gives \((2,2,1,1)\). For each common first object there are \(2^3-2=6\) nonconstant choices of lower-order type across the three agents, for \(3\cdot6=18\) profiles.

It remains to consider a \((2,1)\) split in first choices. If the two agents sharing a first choice have different full rankings, then all three full rankings are distinct. Normalize the shared first choice to \(A\); the two shared-top rankings are then \(A\succ B\succ C\) and \(A\succ C\succ B\). The singleton agent has first choice \(B\) or \(C\), with either ordering of the other two objects. These four canonical cases all have six-order multiplicity spectrum \((3,2,1)\). There are \(72\) labeled profiles in this cell.

If the two shared-top agents have the same full ranking, normalize it to \(A\succ B\succ C\). The singleton agent's first choice is either \(B\) or \(C\). If it is \(B\), both possible lower tails give spectrum \((2,2,1,1)\); if it is \(C\), both give \((3,3)\). Each subcell has \(36\) labeled profiles.

The six disjoint structural cells therefore have sizes
\[
48,\ 6,\ 18,\ 72,\ 36,\ 36,
\]
which sum to \(216\), and merging cells with equal spectra gives the five counts in the finding.

The CRE statement is not a new equivalence theorem. Abdulkadiroğlu and Sönmez prove for every house-allocation problem that the number of serial dictatorships selecting each Pareto-efficient matching equals the number of assigned-endowment cores selecting that matching, and hence RSD and CRE are the same lottery. The verifier below independently reconstructs that equality for every three-agent profile.

## Verification
The embedded `verify_rsd_cre_three_agents.py` uses only the Python standard library.

For every one of the \(216\) profiles, it computes all six serial-dictatorship outcomes in two independently coded ways. It also computes all six CRE outcomes in two ways: top trading cycles and a direct brute-force core test that checks every deterministic matching against every blocking coalition and every reassignment of that coalition's endowed houses.

The replay verifies:
- exact equality of the RSD and CRE matching-multiplicity counters for every profile;
- exactly the five multiplicity spectra stated above;
- spectrum counts \(48,36,72,54,6\);
- structural-cell counts \(48,6,18,72,36,36\);
- support counts \(1:48,2:36,3:72,4:54,6:6\);
- impossibility of support size \(5\);
- mean support size \(49/18\).

Run:

`python3 verify_rsd_cre_three_agents.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Abdulkadiroğlu and Sönmez introduced the core-from-random-endowments formulation and proved a stronger all-market equivalence theorem: for each Pareto-efficient matching, its number of inducing serial dictatorships equals its number of inducing assigned-endowment cores. Consequently RSD and CRE generate exactly the same lottery at every preference profile. That frequency identity is prior work and is used here as a consistency target, not claimed as new.

Bogomolnaia and Moulin study random priority in the three-agent random-assignment problem and explicitly reduce three-agent preference profiles by relabeling when comparing random priority with probabilistic serial. Their analysis includes concrete three-agent random-priority lotteries, but the inspected material does not state the complete RSD multiplicity-spectrum classification or the exact labeled-profile counts above.

Targeted searches for three-agent RSD support sizes, the exact spectra \((6)\), \((3,3)\), \((3,2,1)\), \((2,2,1,1)\), the profile counts \(48,36,72,54,6\), and the corresponding CRE formulation did not locate an equivalent published table or theorem.

## Limitations
The classification is complete only for three agents and three objects with strict complete preferences and uniform priority randomization. It does not claim a comparable finite list for larger markets or weak preferences.

The originality conclusion is limited by search coverage: an unindexed note, exercise, supplementary enumeration, or unpublished table could contain the same five-spectrum classification.

The CRE equality itself is classical; only the exact three-agent shape stratification, its structural profile criterion, and the labeled counts are claimed as the new finite refinement.

## References
1. A. Abdulkadiroğlu and T. Sönmez, “Random Serial Dictatorship and the Core from Random Endowments in House Allocation Problems,” *Econometrica* 66 (1998), 689–701. DOI: 10.2307/2998580.
2. A. Bogomolnaia and H. Moulin, “A New Solution to the Random Assignment Problem,” *Journal of Economic Theory* 100 (2001), 295–328. DOI: 10.1006/jeth.2000.2710.
