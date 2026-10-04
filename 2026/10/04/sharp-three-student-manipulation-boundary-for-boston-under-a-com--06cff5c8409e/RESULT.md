# Sharp three-student manipulation boundary for Boston under a common priority
## Finding
Consider the Boston, or immediate-acceptance, school-choice mechanism with the same number of students and unit-capacity schools. Every school uses the same strict priority order. Students have complete strict preferences over all schools, and a manipulation means a unilateral reported ranking that gives the deviating student a school she strictly prefers to her truthful Boston assignment while all other students report truthfully.

Truthful reporting is strategy-proof for markets with at most two students. With three students and three schools, exactly
\[
36\text{ of }6^3=216
\]
truthful labeled preference profiles admit a profitable unilateral misreport. Thus the exact uniform-profile incidence is \(1/6\). Of the \(36\) manipulable profiles, \(24\) are manipulable only by the middle-priority student and \(12\) only by the lowest-priority student. The highest-priority student is never a manipulator, and no three-student profile has two manipulators.

The failure has a rigid form. In every manipulable profile, the unique manipulator truthfully receives her third choice and every profitable deviation gives her true second choice. There are exactly two profitable reports: the two rankings that put that true second choice first, with the other two schools in either order.

Modulo relabeling the three schools, there are \(36\) preference-profile classes and exactly \(6\) manipulable classes, split \(4\) for the middle-priority student and \(2\) for the lowest-priority student. Normalize the highest-priority student's ranking to \(a\succ b\succ c\). The six manipulable representatives are
\[
\begin{array}{c|c|c|c}
P_1&P_2&P_3&\text{manipulator}\\ \hline
abc&abc&abc&3\\
abc&abc&bac&2\\
abc&abc&bca&2\\
abc&acb&acb&3\\
abc&acb&cab&2\\
abc&acb&cba&2
\end{array}
\]
where students are ordered by the common priority \(1\succ2\succ3\). In the first and fourth rows student \(3\) promotes her true second choice to first; in the other four rows student \(2\) does so.

## Assumptions and scope
There are \(n\) students and \(n\) unit-capacity schools. The common school priority is strict and fixed, so student \(1\) has highest priority at every school, then student \(2\), and so on. Preferences are complete strict rankings of the schools; there is no outside option or truncation.

The Boston mechanism proceeds in rounds. In round \(1\), each student applies to the school ranked first in her report; every school permanently accepts its highest-priority applicant. In round \(k\), every still-unassigned student applies to the school ranked \(k\)-th in her report, and every still-open school permanently accepts its highest-priority current applicant. The process ends when all students are assigned.

The count concerns ex-post profitable unilateral deviations from a truthful profile. It is not a Bayesian-equilibrium probability, does not randomize priorities, and does not cover heterogeneous school priorities, capacities above one, truncated lists, or adaptive variants that skip already-filled schools.

## Proof
For \(n=1\) the claim is immediate. For \(n=2\), the highest-priority student obtains her first choice in round \(1\) regardless of the other report. The lower-priority student receives her first choice if it differs from the higher-priority student's first choice, and otherwise receives the only remaining school. No misreport can improve either outcome, so truthful reporting is strategy-proof.

Now let \(n=3\). School names are irrelevant to manipulability, and the highest-priority student's strict ranking has no nontrivial school-label stabilizer. Therefore every school-relabeling orbit has size \(6\), and every orbit has a unique representative in which student \(1\) reports \(a\succ b\succ c\). It is therefore enough to inspect the \(6\cdot6=36\) pairs of strict rankings for students \(2\) and \(3\).

The accompanying verifier performs that complete canonical enumeration and, independently, the full labeled enumeration of all \(6^3=216\) profiles. For each profile and each student it tries all five nontruthful rankings, runs Boston, and compares the deviator's assigned school using her true order. Exactly the six normalized rows displayed in the Finding admit any improvement. Multiplying their six-element school-label orbits gives \(36\) labeled profiles.

Direct inspection of the six rows establishes the structural refinement. In every row, the indicated student loses her first choice in round \(1\); her true second choice is filled before she can apply to it truthfully; and she is left with her third choice. If she instead lists that second choice first, she is its highest-priority round-\(1\) applicant among those applying there and receives it. The order of the remaining two schools is irrelevant, yielding exactly two profitable reports. Trying all reports in the exhaustive check confirms that no other student or deviation is profitable.

Four of the six normalized bad rows have student \(2\) as the unique manipulator and two have student \(3\); hence the labeled split is \(4\cdot6=24\) and \(2\cdot6=12\). Student \(1\) never manipulates because common highest priority guarantees her reported first choice in round \(1\), so truthfully reporting her actual first choice is optimal.

## Verification
The embedded `verify_boston_common_priority_n3.py` contains two separately coded Boston implementations. It checks their agreement on every profile through \(n=3\), verifies that no \(n\le2\) profile is manipulable, then exhausts all \(216\) three-student profiles and every unilateral strict-ranking report.

It independently constructs the school-relabeling quotient, verifies all \(36\) orbits have size \(6\), checks the exact six canonical bad representatives, and verifies the split \(180+24+12=216\). On every bad profile it also proves computationally that the truthful assignment is the manipulator's third choice and that the profitable reports are exactly the two reports placing her true second choice first.

Replay with

`python3 verify_boston_common_priority_n3.py`

and require the first line `VERIFY_OK`.

## Relationship to prior work
The Boston mechanism's strategic vulnerability is classical. The 2006 working paper *Changing the Boston School Choice Mechanism* documents preference manipulation in practice and explains the mechanism's vulnerability through endogenous effective priorities: ranking a school earlier can move a student ahead of students who rank it later. Pathak and Sönmez later formalize the Boston preference-revelation game and analyze equilibrium outcomes with sincere and sophisticated students.

Troyan and Morrill give a three-student, three-school example in which a student can improve from her third choice to her second by ranking that second choice first, and prove that Boston is obviously manipulable. Their displayed example uses school-specific, heterogeneous priority rankings. The present result does not claim that manipulation pattern as new. It instead gives the exact minimal-size census under a single common strict priority, including the \(1/6\) incidence, the priority-position split, the absence of simultaneous manipulators, and the complete six-class quotient.

Featherstone and Niederle show that truth-telling can be an ordinal Bayes--Nash equilibrium for Boston in symmetric incomplete-information environments. That Bayesian statement is compatible with the present ex-post census: a truthful equilibrium under uncertainty does not imply that every realized profile lacks a profitable deviation when opponents' realized preferences are known.

Targeted searches by mechanism name, immediate-acceptance terminology, common or homogeneous priorities, the exact counts \(36/216\) and \(1/6\), three-student size, and the second-choice-first manipulation pattern did not locate an equivalent finite classification.

## Limitations
The theorem is intentionally a sharp boundary result for the smallest square unit-capacity common-priority market. It does not provide a formula for larger \(n\), heterogeneous priorities, random tie-breaking, outside options, incomplete lists, or adaptive Boston.

The exhaustive computation is finite and complete for the stated domain; it is not evidence for an unrestricted asymptotic law. Literature search cannot exclude an unindexed thesis, teaching note, software table, or appendix containing the same six-class census.

## References
1. A. Abdulkadiroğlu, P. A. Pathak, A. E. Roth, and T. Sönmez, “Changing the Boston School Choice Mechanism,” Boston College Working Papers in Economics 639, public record dated 2006-01-07; later NBER Working Paper 11965.
2. P. A. Pathak and T. Sönmez, “Leveling the Playing Field: Sincere and Sophisticated Players in the Boston Mechanism,” *American Economic Review* 98 (2008), 1636–1652. DOI: 10.1257/aer.98.4.1636.
3. C. R. Featherstone and M. Niederle, “Boston versus deferred acceptance in an interim setting: An experimental investigation,” *Games and Economic Behavior* 100 (2016), 353–375.
4. P. Troyan and T. Morrill, “Obvious Manipulations,” *Journal of Economic Theory* 185 (2020), 104970. DOI: 10.1016/j.jet.2019.104970.
