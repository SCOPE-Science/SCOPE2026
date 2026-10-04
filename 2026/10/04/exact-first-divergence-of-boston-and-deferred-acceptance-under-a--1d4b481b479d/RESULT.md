# Exact first divergence of Boston and deferred acceptance under a common priority
## Finding
Consider a balanced school-choice market with unit-capacity schools, complete strict student preferences, and one common strict priority order shared by every school.

Truthful Boston, also called immediate acceptance, and student-proposing deferred acceptance coincide for every \(2\times2\) profile.

For three students and three schools with common priority
\[
1\succ2\succ3,
\]
the two mechanisms differ at exactly
\[
24
\]
of the
\[
6^3=216
\]
labeled preference profiles. Thus their exact divergence incidence under impartial culture is
\[
\frac{24}{216}=\frac19.
\]

There is a complete structural characterization. Let \(A\) be the first choice of student \(1\). Boston and deferred acceptance differ if and only if student \(2\) also ranks \(A\) first and student \(3\)'s first choice is student \(2\)'s second choice \(X\).

Write \(Y\) for the third school. At every divergent profile,
\[
\text{Boston}=(A,Y,X),
\qquad
\text{DA}=(A,X,Y),
\]
where coordinates are students \(1,2,3\). Therefore student \(1\) is indifferent, student \(2\) strictly prefers deferred acceptance, and student \(3\) strictly prefers Boston. Every divergence is Pareto-incomparable.

Under simultaneous relabeling of the schools, the \(24\) divergent profiles form exactly four classes, each of orbit size \(6\). Normalizing student \(1\)'s ranking to
\[
A\succ B\succ C,
\]
the four class representatives are
\[
(ABC,ABC,BAC),\quad
(ABC,ABC,BCA),\quad
(ABC,ACB,CAB),\quad
(ABC,ACB,CBA).
\]

The rank vectors under Boston and deferred acceptance are respectively
\[
(1,3,1)\quad\text{and}\quad(1,2,3)
\]
for twelve divergent profiles, and
\[
(1,3,1)\quad\text{and}\quad(1,2,2)
\]
for the other twelve.

## Assumptions and scope
There are equally many students and schools, every school has one seat, all student preferences are strict and complete, and all schools use the same strict priority order.

Boston is run truthfully: in round \(k\), each still-unassigned student applies to her \(k\)-th listed school; each school with an open seat immediately and irreversibly accepts its highest-priority applicant in that round.

Deferred acceptance is student-proposing: rejected students continue to their next school, while schools hold the highest-priority applicant seen so far and may replace lower-priority tentative holders.

The result is an ordinal profile statement. No strategic equilibrium interpretation of Boston is claimed.

## Proof
For two students and two schools, if the students have different first choices, both mechanisms assign those first choices. If they share a first choice, the high-priority student receives it and the low-priority student receives the other school under both mechanisms. Hence the \(2\times2\) market has no divergence.

Now consider three students with common priority
\[
1\succ2\succ3.
\]
With a common priority, deferred acceptance is equivalent to serial dictatorship in that priority order: student \(1\) gets her favorite school, then student \(2\) gets her favorite among the two remaining schools, then student \(3\) gets the last school.

Suppose first that students \(1\) and \(2\) do not share a first choice. Then student \(1\)'s first choice is fixed for her in both mechanisms, while student \(2\)'s first choice is a different school and is also accepted immediately in Boston. The third school goes to student \(3\), exactly as under serial dictatorship. Thus divergence requires students \(1\) and \(2\) to share a first choice \(A\).

Assume they do share \(A\). Boston gives \(A\) to student \(1\) in the first round. Deferred acceptance also ultimately gives \(A\) to student \(1\), and student \(2\) then receives her preferred school among the two remaining schools; call this school \(X\), with the other school \(Y\).

If student \(3\) does not rank \(X\) first, then \(X\) remains available after the first Boston round, so student \(2\) obtains \(X\) at her next application and the mechanisms coincide.

If student \(3\) ranks \(X\) first, Boston immediately and irreversibly gives \(X\) to student \(3\) in round one, alongside \(A\) to student \(1\). Student \(2\) is rejected from \(A\), later finds \(X\) full, and receives \(Y\). Thus Boston gives
\[
(A,Y,X).
\]
Under deferred acceptance, student \(2\), who has higher priority than student \(3\), eventually displaces student \(3\) from \(X\), giving
\[
(A,X,Y).
\]
This proves the if-and-only-if criterion.

The exact count follows immediately. Student \(1\) has \(6\) possible orders. Student \(2\), required to share student \(1\)'s first choice, has \(2\) possible orders. Once student \(2\)'s second choice \(X\) is fixed, student \(3\) has \(2\) possible orders with \(X\) first. Hence
\[
6\cdot2\cdot2=24.
\]

Student \(2\) moves from third choice under Boston to second choice under deferred acceptance. Student \(3\) moves from first choice under Boston to either second or third choice under deferred acceptance. Hence neither matching Pareto-dominates the other at any divergent profile.

The four school-relabeling classes are the four normalized representatives listed above.

## Verification
The embedded `verify_boston_da_common_priority_3x3.py` uses only the Python standard library.

It implements Boston twice: once as an ordinary round-by-round application process and once as an independent rank-by-rank irreversible-admission replay. It implements deferred acceptance twice: once by proposal-and-holding and once as priority serial dictatorship, which is equivalent under a common school priority.

The replay verifies:
- equality of the two Boston implementations on every profile;
- equality of deferred acceptance and serial dictatorship on every profile;
- no divergence in the \(2\times2\) market;
- exactly \(24\) divergences in the \(3\times3\) market;
- exact equivalence between divergence and the structural criterion;
- Pareto incomparability at all \(24\) divergences;
- exactly four school-relabeling classes, all of orbit size \(6\);
- the two rank-vector patterns and their twelve-versus-twelve split.

Run:

`python3 verify_boston_da_common_priority_3x3.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Abdulkadiroğlu and Sönmez formalized the school-choice model, the Boston mechanism, and student-proposing deferred acceptance. Their discussion emphasizes the central tradeoff: truthful Boston is Pareto efficient but is not strategy-proof, while deferred acceptance is strategy-proof and stable but need not be Pareto efficient.

Later work explicitly treats immediate acceptance and deferred acceptance as competing endpoints in school choice. Harless's immediate-acceptance-with-skips paper frames the comparison as efficiency versus strategic robustness, and Troyan studies welfare comparisons between Boston and deferred acceptance under uncertainty and priorities.

The present result is a finite exact refinement for the smallest balanced common-priority market where the truthful mechanisms can differ. The structural criterion, the exact incidence \(1/9\), the four school-symmetry classes, and the fact that every divergence is Pareto-incomparable were not found in the inspected literature.

## Limitations
The theorem assumes one common strict priority at all schools, unit capacities, balanced markets, truthful reports, and strict complete preferences.

It does not cover heterogeneous school priorities, capacities above one, outside options, strategic equilibrium play under Boston, or random tie-breaking.

The originality search did not locate an equivalent finite census, but an unindexed exercise, note, code base, or supplementary table could contain the same \(3\times3\) classification.

## References
1. A. Abdulkadiroğlu and T. Sönmez, “School Choice: A Mechanism Design Approach,” *American Economic Review* 93 (2003), 729–747. DOI: 10.1257/000282803322157061.
2. P. Troyan, “Comparing School Choice Mechanisms by Interim and Ex-Ante Welfare,” SIEPR Discussion Paper 10-021, 2011.
3. P. Harless, “A School Choice Compromise: Between Immediate and Deferred Acceptance,” MPRA Paper 61417, deposited 18 January 2015.
