# Sharp no-show boundary for three-candidate Coombs voting
## Finding
Consider three-candidate Coombs voting with complete strict anonymous ballots. A candidate with a strict majority of first-place votes is elected immediately. Otherwise, the unique candidate with the most last-place votes is eliminated, and the remaining two candidates are compared by their pairwise majority. Profiles with a tied elimination or tied final comparison are excluded.

A no-show event occurs when a nonempty homogeneous group of voters, all having the same sincere ranking, strictly prefers the winner obtained after its abstention to the winner obtained when it participates.

No such event exists with fewer than \(10\) voters. At \(10\) voters, exactly \(12\) labeled anonymous profiles admit a no-show event. Every one of these \(12\) profiles has exactly one profitable homogeneous abstention, and the abstaining group consists of exactly one voter.

There are
\[
\binom{15}{5}=3003
\]
anonymous labeled-candidate profiles with \(10\) voters, of which \(2412\) have a unique Coombs outcome under the tie-independent convention above. Thus the incidence is
\[
\frac{12}{3003}=\frac{4}{1001}
\]
among all anonymous profiles and
\[
\frac{12}{2412}=\frac1{201}
\]
among unique-outcome profiles.

Modulo simultaneous relabeling of the three candidates, the \(12\) bad profiles form exactly \(2\) classes, each of orbit size \(6\).

Normalize the abstaining voter's sincere ranking to
\[
A\succ B\succ C
\]
and list ballot types in the order
\[
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA.
\]
Then the complete minimal boundary consists of exactly the two normalized profiles
\[
(1,0,2,3,4,0)
\]
and
\[
(1,1,2,3,3,0).
\]
In both profiles \(C\) wins when everyone participates, whereas \(B\) wins after the single \(ABC\) voter abstains. Since that voter ranks \(B\) above \(C\), the abstention is profitable.

There is also a sharp answer for the stronger, nonstandard variant in which exactly two identical voters must abstain. Under that restriction, no paradox occurs below \(13\) voters. At \(13\) voters there are exactly \(18\) labeled profiles, forming \(3\) candidate-relabeling classes of size \(6\). After the same normalization, the three classes are
\[
(2,0,2,4,5,0),\qquad
(2,1,2,4,4,0),\qquad
(2,2,2,4,3,0).
\]
In each case the participating winner is \(C\), and removing the two \(ABC\) voters makes \(B\) win.

## Assumptions and scope
Every ballot is one of the six strict linear orders of three candidates. Voters with the same ranking are anonymous. The no-show comparison uses each abstaining voter's sincere ranking and requires strict improvement.

The theorem is tie-independent: every full profile and post-abstention profile used in the claim has a unique Coombs outcome without an exogenous tie-breaker. A strict majority means more than half of all participating voters.

The standard no-show definition permits any nonempty abstaining group, including one voter. The exactly-two-voter statement is reported separately because some later literature imposed a stronger tie-independent interpretation and asserted that at least two abstainers were necessary for Coombs.

## Proof
The six ballot types make every anonymous \(n\)-voter profile a weak composition of \(n\) into six parts. The verifier exhausts all such profiles for every \(1\le n\le10\). For each profile with a unique Coombs winner, each ballot type present in the profile and every possible positive homogeneous abstention size are tested. The post-abstention winner is recomputed, and profitability is evaluated using the abstainers' original ranking.

Two independently coded Coombs implementations are required to agree throughout. The first uses the closed three-candidate description: strict first-place majority if present, otherwise eliminate the unique last-place plurality loser and compare the surviving pair. The second literally replays Coombs rounds on the surviving candidate set.

The exhaustive profile-first search finds no event for \(n\le9\) and exactly \(12\) events at \(n=10\). An independently organized event-first search starts with every possible post-abstention profile, adds homogeneous voter groups, and recomputes the participating election. It produces exactly the same event set.

Candidate relabeling under all \(6\) permutations gives precisely the two normalized representatives displayed above. Direct inspection verifies their mechanism.

For
\[
(1,0,2,3,4,0),
\]
the first-place counts are \((1,5,4)\), so there is no strict majority. The last-place counts are \((3,4,3)\), so \(B\) is uniquely eliminated. Among \(A\) and \(C\), candidate \(C\) wins \(7\) to \(3\). After the single \(ABC\) voter abstains, \(9\) voters remain and \(B\) has \(5\) first-place votes, so \(B\) wins immediately.

For
\[
(1,1,2,3,3,0),
\]
the first-place counts are \((2,5,3)\) and the last-place counts are again \((3,4,3)\). Candidate \(B\) is uniquely eliminated and \(C\) defeats \(A\) by \(6\) to \(4\). After the single \(ABC\) voter abstains, \(B\) has \(5\) of \(9\) first-place votes and wins immediately.

The exactly-two-identical-voter variant is checked separately over every anonymous profile through \(13\) voters. No event occurs below \(13\); exactly \(18\) occur at \(13\). Relabeling gives the three displayed normalized forms, and all \(18\) orbits have size \(6\).

## Verification
The embedded `verify_coombs10_noshow.py` uses only exact integer arithmetic and the Python standard library.

It performs two independent traversals of the standard no-show search through \(10\) voters: profile-first and event-first. Their complete event sets must agree exactly. It also compares two independent implementations of the Coombs rule on every tested full and post-abstention profile.

The replay verifies:
- zero standard no-show events for \(1\) through \(9\) voters;
- exactly \(12\) bad \(10\)-voter profiles;
- exactly one profitable homogeneous abstention per bad profile, always of size one;
- incidence \(4/1001\) among all \(10\)-voter anonymous profiles and \(1/201\) among unique-outcome profiles;
- exactly \(2\) candidate-relabeling classes of size \(6\);
- the two normalized forms above;
- zero exactly-two-voter events below \(13\), followed by exactly \(18\) at \(13\);
- exactly \(3\) candidate-relabeling classes for that two-voter variant.

Run:

`python3 verify_coombs10_noshow.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Felsenthal's 2010 survey gives a three-candidate Coombs no-show example with \(15\) voters: two voters of type \(C\succ B\succ A\) abstain and improve from winner \(B\) to winner \(C\).

Felsenthal and Tideman subsequently use the standard participation formulation in which a single voter should never lose by joining an election when voting sincerely. Their comparison confirms that Coombs is vulnerable to participation failures.

Brandt, Matthäus, and Saile revisit minimal voting paradoxes under a tie-independent convention. In their Coombs discussion they state that, as a consequence of their restriction, the no-show paradox can appear only if at least two voters abstain. The \(10\)-voter profiles above are tie-independent and use one abstainer, so they give an explicit counterexample to that assertion. Their introduction also reports smaller examples than Felsenthal's for the studied paradoxes except the Coombs no-show case; the exactly-two-abstainer census above sharpens that boundary from the earlier \(15\)-voter example to \(13\).

Targeted searches by the rule name, participation/no-show terminology, the voter counts \(10\) and \(13\), the exact profile vectors, and the exact census sizes did not locate a published complete boundary classification matching the \(12\)-profile or \(18\)-profile results.

The archival record for Felsenthal's paper says that it was available online in April 2010 but does not provide a day for that availability. The first exact public day used for dating this finding is the documented LSE presentation on 27 May 2010; no artificial day is assigned to the month-only online record.

## Limitations
The census is restricted to three candidates, strict complete ballots, anonymous profiles, and tie-independent unique outcomes. Different tie-breaking conventions can create additional cases.

The exactly-two-voter statement is a separate restricted variant and should not be confused with the standard participation axiom, which permits a single voter to abstain.

The originality search found no equivalent census, but an unindexed note, thesis, software table, or unpublished correction could contain the same finite classification.

## References
1. D. S. Felsenthal, “Review of Paradoxes afflicting various voting procedures where one out of \(m\) candidates \((m\ge2)\) must be elected,” LSE Research Online eprint 27685, 2010.
2. D. S. Felsenthal and N. Tideman, “Varieties of failure of monotonicity and participation under five voting methods,” *Theory and Decision* 75 (2013), 59–77. DOI: 10.1007/s11238-012-9306-7.
3. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Journal of Theoretical Politics* 34 (2022), 527–551. DOI: 10.1177/09516298221122104.
