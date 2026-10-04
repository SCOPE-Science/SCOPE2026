# Complete manipulability boundary for common-priority Boston assignment
## Finding
Consider the Boston mechanism, also called immediate acceptance, with three students and three schools. Every school has one seat, all students submit strict complete rankings, and every school uses the same strict priority order
\[
1\succ2\succ3.
\]

Exactly
\[
36
\]
of the
\[
6^3=216
\]
labeled preference profiles are manipulable by a unilateral misreport. Hence, under impartial culture on strict preference profiles, the exact profile incidence is
\[
\frac{36}{216}=\frac16.
\]

Every bad profile has exactly one vulnerable student. That student has exactly two profitable reports, and both reports improve the assignment from the student's third sincere choice to the second. Thus there are exactly
\[
36
\]
vulnerable student-profile pairs among \(216\cdot3=648\), for incidence
\[
\frac1{18},
\]
and exactly
\[
72
\]
profitable student-profile-report triples among \(216\cdot3\cdot5=3240\), for incidence
\[
\frac1{45}.
\]

There is a simple complete structural description. Let \(A\) be student \(1\)'s first choice. A profile can be manipulable only if student \(2\) also ranks \(A\) first. Write student \(2\)'s ranking as
\[
A\succ X\succ Y.
\]
Then the profile is manipulable if and only if one of the following holds:

1. student \(3\) ranks \(A\succ X\succ Y\); then student \(3\) is the unique vulnerable student; or
2. student \(3\) ranks \(X\) first, with either order of \(A\) and \(Y\) below it; then student \(2\) is the unique vulnerable student.

In both cases the profitable reports are exactly the two rankings with \(X\) first. Under school relabeling, the \(36\) bad profiles form exactly six classes, each with orbit size \(6\). Normalizing student \(1\)'s ranking to \(A\succ B\succ C\), the six representatives are
\[
(ABC,ABC,ABC),
\]
\[
(ABC,ABC,BAC),\qquad(ABC,ABC,BCA),
\]
\[
(ABC,ACB,ACB),
\]
\[
(ABC,ACB,CAB),\qquad(ABC,ACB,CBA).
\]

The two-student, two-school common-priority unit-capacity market is strategy-proof. Therefore \(3\times3\) is the first balanced square market size at which this common-priority Boston environment becomes manipulable.

## Assumptions and scope
The mechanism is immediate acceptance with final assignments in every round. In round \(1\), each student applies to her first reported school; each school permanently accepts its highest-priority applicant up to capacity. Rejected students move to their second reported schools in round \(2\), and so on.

All three schools have capacity one. The same exogenous strict priority order \(1\succ2\succ3\) is used by every school. All preference rankings are strict and complete. A misreport is profitable if the assigned school under the false report is strictly preferred, under the student's true ranking, to the school assigned under truth-telling.

The common-priority restriction is substantive. The result does not count arbitrary school-specific priority profiles.

## Proof
Student \(1\), who has highest priority everywhere, always receives her first reported school in round \(1\). Under truth-telling this is her sincere top choice, so she cannot profitably manipulate.

Let \(A\) be student \(1\)'s top school. If student \(2\)'s top school is not \(A\), then students \(1\) and \(2\) receive distinct first choices immediately. The third student either receives the remaining school immediately or, after rejection from an occupied school, eventually receives the only unoccupied school. The other two schools are permanently held by higher-priority students, so no unilateral report can give student \(3\) a school she sincerely prefers to her truthful assignment. Thus no profile of this form is manipulable.

It remains to suppose that student \(2\) also ranks \(A\) first. Write her sincere ranking as
\[
A\succ X\succ Y.
\]
Student \(1\) receives \(A\) in round \(1\), and student \(2\) is rejected.

If student \(3\) ranks \(X\) first, student \(3\) permanently takes \(X\) in round \(1\). Student \(2\) then applies unsuccessfully to \(X\) in round \(2\) and eventually receives \(Y\), her third choice. If instead she reports either ranking with \(X\) first, she applies to \(X\) in round \(1\) and defeats student \(3\) there by common priority, improving from \(Y\) to \(X\). No other report can improve her outcome. This gives the second family.

Suppose instead that student \(3\) also ranks \(A\) first. Both lower-priority students are rejected from \(A\) in round \(1\). If student \(3\)'s second choice is \(X\), then in round \(2\) students \(2\) and \(3\) both apply to \(X\); student \(2\) wins by priority, and student \(3\) eventually receives \(Y\), her third choice. By reporting either ranking with \(X\) first, student \(3\) takes \(X\) in round \(1\), before student \(2\) reaches it, and improves to her second sincere choice. This gives the first family. If student \(3\)'s second choice is \(Y\), the two rejected students separate in round \(2\), each obtaining a sincere second choice, so neither can gain by manipulation.

Finally, if student \(3\) ranks \(Y\) first, she permanently takes \(Y\) in round \(1\), while student \(2\) receives \(X\) in round \(2\); again no profitable deviation exists.

These cases prove the stated if-and-only-if classification. Counting is immediate. Student \(1\) has \(6\) possible rankings. Student \(2\) must share student \(1\)'s top choice and can order the other two schools in \(2\) ways. For each such pair there are exactly \(3\) bad rankings for student \(3\): one of the first family and two of the second. Hence
\[
6\cdot2\cdot3=36.
\]
Exactly one student is vulnerable in each bad profile, and she has exactly two profitable reports, yielding \(36\) vulnerable student-profile pairs and \(72\) profitable report triples.

For two students and two one-seat schools under a common priority, the high-priority student obtains her top choice. The other student then receives her top choice if distinct, and otherwise her best remaining school. This is already her best feasible assignment given the first student's permanent acceptance, so the \(2\times2\) market is strategy-proof.

## Verification
The embedded `verify_boston3_common_priority.py` uses only the Python standard library.

It implements immediate acceptance in two independent ways: a round-by-round application procedure and a rank-level school scan. The two implementations are required to agree on every truthful and deviating profile.

The replay exhausts all \(216\) three-student preference profiles, all three possible manipulators, and all five false reports for each manipulator. It verifies the exact structural criterion proved above, the counts \(36\), \(36\), and \(72\), the priority-rank split of vulnerable students, the six school-relabeling classes, and the two-student strategy-proof boundary.

Replay with:

`python3 verify_boston3_common_priority.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Abdulkadiroğlu and Sönmez formalized the school-choice problem and described the Boston assignment algorithm round by round. They explicitly emphasize that the Boston mechanism is not strategy-proof because students may lose priority at a school unless they rank it early enough. Their paper establishes the qualitative manipulation problem but does not provide the complete common-priority \(3\times3\) census above.

Kumano studies priority structures under which Boston becomes strategy-proof and stable, using acyclicity conditions. Chen sharpens the restricted-domain theory and characterizes when Boston is strategy-proof in terms of capacities and equivalence to the student-optimal stable mechanism. These are global structural characterizations, not a count or classification of the manipulable preference profiles for the fixed common-priority three-student environment.

Harless compares immediate acceptance with related school-choice rules and stresses that futile applications to already-full schools are a major source of Boston manipulability. The structural criterion here isolates exactly that mechanism in the smallest balanced common-priority market and gives its complete finite prevalence and orbit structure.

Targeted searches using the Boston and immediate-acceptance names, common-priority and common-lottery terminology, the \(3\times3\) market, the exact count \(36\), the incidences \(1/6\), \(1/18\), and \(1/45\), and the six school-relabeling classes did not locate an equivalent published census.

## Limitations
The theorem fixes one common strict priority order at all schools, unit capacities, and complete strict preferences. With school-specific priorities, multiple capacities, truncation, outside options, or random tie-breaking, the classification can change.

The result concerns unilateral ordinally profitable manipulation. It does not analyze Nash equilibrium selection, incomplete information, or welfare under strategic play.

The directly relevant full text of Chen's short 2014 paper was not obtainable during this run after open-access search and a lawful institutional-access attempt required human verification. Its accessible abstract was sufficient for the positive theorem-level comparison recorded here, but no whole-document absence claim rests on that source alone.

An unindexed note, thesis, software table, or unpublished calculation could contain an equivalent small-market census.

## References
1. A. Abdulkadiroğlu and T. Sönmez, “School Choice: A Mechanism Design Approach,” *American Economic Review* 93 (2003), 729–747. DOI: 10.1257/000282803322157061.
2. T. Kumano, “Strategy-proofness and stability of the Boston mechanism: An almost impossibility result,” *Journal of Public Economics* 105 (2013), 23–29. DOI: 10.1016/j.jpubeco.2013.05.008.
3. Y. Chen, “When is the Boston mechanism strategy-proof?”, *Mathematical Social Sciences* 71 (2014), 43–45. DOI: 10.1016/j.mathsocsci.2014.03.001.
4. P. Harless, “A School Choice Compromise: Between Immediate and Deferred Acceptance,” MPRA Paper 61417, 2014.
