# Independent mathematical audit

## correctness

PASS

The seven-state transitions are the standard unique coloring of the Wielandt digraph. An independent complete subset-BFS gives minimum reset length 31 and unique minimum-distance singleton state 2. Exact polynomial propagation along all shortest subset edges gives z^6(1+z)^20 and total 1048576; the inspected verifier independently reproduces the same polynomial by a reverse-distance optimal-DAG recursion. The published witness has length 31. The computation exhausts the complete finite power automaton.

## originality

PASS

The primary Wielandt-family source was inspected: it proves reset length n^2-3n+3, gives a shortest witness, and proves a shortest reset ends at state 2. It does not enumerate all shortest reset words or their letter-count distribution. Targeted Resultary and literature searches for W7 shortest-word multiplicity and reset-language enumeration found no source stating the polynomial or count.

## value

PASS

W7 is a canonical slowly synchronizing benchmark, and shortest-word multiplicity is a natural invariant of its optimal reset language rather than an arbitrary statistic. The compact binomial profile is an exact self-contained finite fact useful for checking enumeration/sampling methods. Under the stated standard, the existence of an unfinished larger-family pattern does not by itself make the exact W7 result worthless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
