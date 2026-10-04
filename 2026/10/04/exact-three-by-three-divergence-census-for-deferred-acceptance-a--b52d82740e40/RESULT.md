# Exact three-by-three divergence census for deferred acceptance and top trading cycles
## Finding
Consider strict unit-capacity school choice with the same number of students and schools. Schools have strict priority orders over students. Compare student-proposing deferred acceptance (DA) with the top trading cycles mechanism (TTC) of Abdulkadiroğlu and Sönmez.

For every profile with at most two students and two schools, DA and TTC select the same matching.

At three students and three schools there are
\[
(3!)^6=46{,}656
\]
labeled preference-priority profiles. The exact outcome comparison is
\[
42{,}336\text{ equal},\qquad
1{,}080\text{ with TTC Pareto-dominating DA},\qquad
3{,}240\text{ Pareto-incomparable}.
\]
Thus the mechanisms differ on exactly
\[
4{,}320=\frac{5}{54}\,46{,}656
\]
profiles, and TTC Pareto-dominates DA on exactly
\[
1{,}080=\frac{5}{216}\,46{,}656.
\]
There is no profile at this size where DA Pareto-dominates TTC.

DA is Pareto-inefficient on exactly \(1{,}296\) profiles, or \(1/36\) of all profiles. Of those, TTC Pareto-dominates DA on \(1{,}080\), but on the remaining
\[
216=\frac{1}{216}\,46{,}656
\]
profiles DA is Pareto-inefficient while TTC is Pareto-incomparable with it. This is the exact first-size frequency of the phenomenon highlighted qualitatively by Kesten: an inefficient DA outcome need not be Pareto-dominated by TTC.

Modulo independent relabeling of students and schools, the \(4{,}320\) divergent profiles form exactly \(120\) classes. Their refinement is
\[
30\text{ TTC-dominance classes},\qquad
84\text{ efficient-DA incomparable classes},\qquad
6\text{ inefficient-DA incomparable classes}.
\]
Every divergent class has full orbit size \(36\) under \(S_3\times S_3\).

## Assumptions and scope
Every school has capacity one. Every student strictly ranks all schools, and every school has a strict priority ordering of all students. Students are all assigned and every school receives one student.

DA means the standard student-proposing deferred-acceptance algorithm. TTC means the school-choice top trading cycles algorithm: each remaining student points to her favorite remaining school, each remaining school points to its highest-priority remaining student, and every directed cycle is executed before the next round.

Pareto comparisons use only the students' true strict preferences. A DA outcome is called Pareto-inefficient when some perfect matching weakly improves every student and strictly improves at least one.

The symmetry quotient preserves the two roles. Students may be relabeled arbitrarily and schools may be relabeled arbitrarily, but students and schools are not exchanged.

## Proof
For \(n=1\) and \(n=2\), the verifier enumerates every strict preference-priority profile. The two mechanisms coincide on every profile, establishing the finite boundary.

For \(n=3\), each of the three students has \(3!\) possible preference orders and each of the three schools has \(3!\) possible priority orders. Therefore the labeled domain has exactly \((3!)^6=46{,}656\) profiles. The verifier iterates over this entire Cartesian product.

DA is implemented twice. One implementation processes free students from a stack; the other performs simultaneous proposal rounds. Their outcomes are asserted identical at every profile.

TTC is also implemented twice. One implementation identifies all directed cycles in each round and executes them simultaneously. The other traces and executes one directed cycle at a time, recomputing the residual problem after each execution. Their outcomes are asserted identical at every profile.

For every profile, the two resulting matchings are compared student by student using the true preference ranks. This yields exactly \(42{,}336\) equal outcomes, \(1{,}080\) profiles at which TTC Pareto-dominates DA, and \(3{,}240\) incomparable outcomes. No reverse dominance occurs.

DA efficiency is checked independently of TTC by enumerating all \(3!=6\) perfect matchings. This gives exactly \(1{,}296\) Pareto-inefficient DA outcomes. Cross-tabulating efficiency with the DA-versus-TTC relation gives
\[
42{,}336\text{ efficient and equal},
\]
\[
3{,}024\text{ efficient and incomparable},
\]
\[
1{,}080\text{ inefficient and TTC-dominated},
\]
and
\[
216\text{ inefficient and incomparable}.
\]
These four cells sum to the full \(46{,}656\)-profile domain.

For the quotient, each divergent profile is transformed by all \(36\) elements of \(S_3\times S_3\) and reduced to a canonical code. The resulting \(120\) canonical representatives have the stated \(30+84+6\) refinement, and every representative has exactly \(36\) labeled profiles in its orbit. A separate Burnside fixed-point sum reproduces the same three class counts.

## Verification
The embedded `verify_ttc_da3_census.py` uses only the Python standard library. Replaying

`python3 verify_ttc_da3_census.py`

must begin with `VERIFY_OK`.

The replay checks every profile for \(n\le3\), two independently coded DA implementations, two independently coded TTC implementations, all six perfect matchings for the DA-efficiency test at \(n=3\), canonical symmetry reduction, and an independent Burnside quotient. It also reproduces the three-student, three-school Pareto-improvement example in Abdulkadiroğlu and Sönmez: DA assigns the diagonal matching while TTC swaps the first two students' schools and Pareto-improves it.

The theorem is finite. No large-market or arbitrary-\(n\) frequency claim is inferred from the enumeration.

## Relationship to prior work
Abdulkadiroğlu and Sönmez introduced both mechanisms into the school-choice framework, showed that DA can be Pareto-inefficient, and proved TTC Pareto efficient. Their three-student example exhibits a profile where TTC Pareto-improves DA, but it does not give an exhaustive small-market frequency or symmetry classification.

Kesten compares the two mechanisms directly. His later Journal of Economic Theory paper characterizes priority structures on which the mechanisms are equivalent, and the preceding working paper explicitly points out that TTC need not Pareto-dominate DA even when DA is Pareto-inefficient. That qualitative phenomenon is therefore prior work. The present result quantifies the complete first nontrivial finite domain: it identifies the exact divergence and dominance rates, the exact \(216\)-profile exceptional stratum, and the full role-preserving quotient.

Targeted searches using the exact counts, reduced fractions, mechanism aliases, three-by-three terminology, Kesten's Example 4 phenomenon, and symmetry language did not locate a published statement equivalent to this census.

## Limitations
The result is complete only for strict unit-capacity markets through three students and three schools. It does not provide a formula for larger markets, capacities greater than one, weak priorities, or incomplete preference lists.

The numerical theorem is proved by exhaustive finite computation rather than a closed symbolic counting formula. The duplicate implementations, independent DA-efficiency enumeration, and Burnside reconstruction reduce implementation risk but do not constitute an external independent audit.

An earlier Kesten working-paper version is dated only to February 2004 in the inspected copy. Because no day is stated there, no day was invented; the machine field uses 11 February 2005, the earliest day-resolved public date verified for the directly comparative paper.

A residual originality risk remains that an unindexed thesis, course note, software table, or supplementary data set contains the same complete \(3\times3\) census.

## References
1. A. Abdulkadiroğlu and T. Sönmez, “School Choice: A Mechanism Design Approach,” *American Economic Review* 93 (2003), 729–747. DOI: 10.1257/000282803322157061.
2. O. Kesten, “Student Placement to Public Schools in the US: Two New Solutions,” working paper, February 2004.
3. O. Kesten, “On two competing mechanisms for priority-based allocation problems,” *Journal of Economic Theory* 127 (2006), 155–171. DOI: 10.1016/j.jet.2004.11.001. Available online 11 February 2005.
