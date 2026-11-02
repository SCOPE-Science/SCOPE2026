# Independent mathematical audit

## correctness

PASS

For a winning committee W, set T=W∩A of size t, L=A\W of size r−t and U=W\A of size k−t. Every elected U score dominates every L score; with h=|L|+|U| and α=|L|/h, sum_L v<=α(sum_L+sum_U). Every mean Borda score vector is a convex combination of score permutations, so rearrangement gives sum_A v<=S_t+α(S_{t+h}−S_t), S_j=j(2m−j−1)/2, yielding upper [r(2m−r−k−1)+t(r+k−t)]/[m(m−1)]. Swapping parties gives lower [r(r−1)+t(m−r−k+t)]/[m(m−1)]. Cyclic rotation of middle group L∪U attains upper, party swap lower with same W; rational mixing yields every rational score, with all selected/unselected score comparisons strict in the interval. Independent exact rational checks established endpoint and strict mixture for 570 bounded feasible tuples plus direct one-ballot bound through m=6.

## originality

PASS

Best-of-knowledge original for the restricted final claim after direct implication-based comparison; primary overlap, unavailable full text and mathematical reduction risks are explicitly documented, not treated as absence-proof.

## value

PASS

The interval fully quantifies a natural mismatch between candidate affiliation totals and actual k-Borda representation. Even a party whose candidates collect almost all aggregate Borda points can win no seat as m grows at fixed k, and the exact bounds distinguish ties at endpoints from uniquely selected interior committees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
