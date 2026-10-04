# Exact three-student Pareto-inefficiency census for deferred acceptance
## Finding
Consider balanced school choice with three students, three unit-capacity schools, complete strict student preferences, and complete strict school priorities. Let student-proposing deferred acceptance assign each student one school.

Exactly
\[
1296
\]
of the
\[
6^6=46656
\]
labeled preference-priority profiles have a Pareto-inefficient deferred-acceptance outcome. Hence the exact impartial-culture profile incidence is
\[
\frac{1296}{46656}=\frac1{36}.
\]

This is the first possible balanced size: every complete strict \(2\times2\) profile has a Pareto-efficient deferred-acceptance outcome.

The inefficient \(3\times3\) profiles have a rigid structure. Every one has exactly one Pareto-improving perfect matching. That improvement makes exactly two students strictly better off and leaves the third student at the same school. Thus every inefficiency is repaired by a unique two-student trading cycle.

Writing each student's assigned-school rank as a one-based integer, the deferred-acceptance rank multiset is
\[
(2,2,2)
\]
for exactly \(648\) inefficient profiles and
\[
(2,2,3)
\]
for the other \(648\).

There are \(6^3=216\) labeled strict school-priority structures. If priorities are fixed and only the \(216\) student-preference profiles vary, the number producing Pareto-inefficient deferred acceptance takes exactly four values:
\[
\begin{array}{c|rrrr}
\text{inefficient preference profiles} & 0 & 4 & 8 & 12\\
\hline
\text{priority structures} & 42 & 36 & 126 & 12.
\end{array}
\]
The \(42\) zero-inefficiency priority structures are exactly the Ergin-acyclic structures. The remaining \(174\) contain an Ergin cycle.

## Assumptions and scope
There are equally many students and schools, each school has capacity one, every student strictly ranks every school, and every school strictly ranks every student. No outside option is used because the market is balanced and all schools are acceptable.

Pareto efficiency is evaluated only from students' preferences: an assignment Pareto dominates another when no student is worse off and at least one student is strictly better off.

For unit quotas, an Ergin cycle consists of distinct schools \(x,y\) and distinct students \(i,j,k\) with
\[
i\succ_x j\succ_x k
\quad\text{and}\quad
k\succ_y i.
\]
A priority structure is acyclic when no such configuration occurs.

The exact census is complete for \(2\times2\) and \(3\times3\) markets. No frequency formula for larger markets is claimed.

## Proof
For \(2\times2\), the verifier enumerates all
\[
(2!)^4=16
\]
preference-priority profiles. Deferred acceptance is Pareto efficient in all of them.

For \(3\times3\), it enumerates every one of the \(6^6=46656\) labeled profiles. Deferred acceptance is implemented independently in two ways: a sequential free-student queue and simultaneous proposal rounds. Their assignments agree for every profile.

Every one of the six perfect assignments is then tested directly against the deferred-acceptance assignment using the students' strict preferences. This yields exactly \(1296\) inefficient profiles. A separate trading-cycle test on the assignment envy graph agrees profile by profile with the direct Pareto test.

As an additional correctness check, every perfect assignment is independently tested for stability. The deferred-acceptance output is stable and is weakly best for each student among all stable assignments at every profile.

For each inefficient profile, exhaustive comparison against all six perfect assignments finds exactly one Pareto improvement. In every case exactly two students improve. The two possible deferred-acceptance rank multisets occur \(648\) times each.

Finally, for each of the \(216\) priority structures the verifier counts inefficient preference profiles and separately tests the unit-capacity Ergin cycle condition. The inefficiency-count histogram is
\[
0:42,\qquad4:36,\qquad8:126,\qquad12:12,
\]
and the \(42\) priority structures with zero inefficient profiles are exactly the \(42\) acyclic structures.

## Verification
The embedded `verify_da_pareto_boundary.py` uses only the Python standard library.

It checks:
- all \(16\) complete strict \(2\times2\) profiles;
- all \(46656\) complete strict \(3\times3\) profiles;
- agreement of two deferred-acceptance implementations;
- stability and student-optimality among all stable perfect assignments;
- direct Pareto comparison against all perfect assignments;
- an independent trading-cycle characterization of Pareto inefficiency;
- exactly \(1296\) inefficient profiles;
- uniqueness of every Pareto improvement and exactly two strict beneficiaries;
- the \(648/648\) assigned-rank split;
- the exact priority-structure histogram and its agreement with the Ergin cycle test.

Run:

`python3 verify_da_pareto_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Ergin established acyclicity as the key condition governing whether priority-respecting allocation can be Pareto efficient. Klaus and Klijn give an open full-text formulation of Ergin's cycle condition and note that, for unit quotas, the cycle condition alone is sufficient to identify a cycle. They also restate the absence-of-couples result linking acyclicity to the unique fair and efficient placement mechanism obtained from deferred acceptance.

Narita later corrected two steps in the original proof of Ergin's main theorem and supplied an alternative proof while explicitly preserving the theorem itself.

These structural results imply that acyclic priority structures are exactly those for which deferred acceptance never creates student-side Pareto inefficiency as preferences vary. They do not give the complete \(3\times3\) frequency census, the \(0/4/8/12\) distribution across priority structures, the exact \(1/36\) profile incidence, or the uniqueness and two-student form of every Pareto repair. Targeted searches for these exact counts and equivalent small-market formulations did not locate a published table or theorem containing them.

## Limitations
The result is a finite exact classification for balanced unit-capacity markets with complete strict preferences and priorities. It does not cover weak priorities, outside options, unequal market sizes, capacities above one, or larger-market frequencies.

The oldest relevant paper is bibliographically dated 2002, but the earliest exact day-level public source date verified for this package is the publisher's online date recorded below. A March 2006 working-paper version of a closely related open source was also inspected, but only month-level evidence was available and no day was invented.

Search failure is not a proof of bibliographic uniqueness. An unindexed teaching note, thesis, or software enumeration could contain the same \(3\times3\) census.

## References
1. H. I. Ergin, “Efficient Resource Allocation on the Basis of Priorities,” *Econometrica* 70 (2002), 2489–2497. Publisher online record: 5 April 2006. DOI: 10.1111/j.1468-0262.2002.00447.x.
2. B. Klaus and F. Klijn, “Fair and Efficient Student Placement with Couples,” *International Journal of Game Theory* 36 (2007), 177–207. DOI: 10.1007/s00182-006-0059-9. Published online 30 January 2007.
3. Y. Narita, “Comment on ‘Efficient Resource Allocation on the Basis of Priorities’,” *Econometrica* 89 (2021), 15–17. DOI: 10.3982/ECTA8740.
