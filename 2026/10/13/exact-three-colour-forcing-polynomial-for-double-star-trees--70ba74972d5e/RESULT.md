# Exact three-colour forcing polynomial for double-star trees

## Finding
Let \(D_{m,n}\) be a double-star tree: two adjacent vertices (centres), with \(m\) leaves incident to the first centre and \(n\) leaves incident to the second. For every integer \(m,n\ge2\) and real \(0\le p\le1/3\), the forced three-colouring polynomial is

\[\operatorname{FC}_3(D_{m,n};p)=6p^{m+n}\bigl[2^{m+n}p^2+(2^{m+n+1}-2^m-2^n)p(1-3p)+(2^{m+n}-2^m-2^n)(1-3p)^2\bigr].\]

Equivalently, put \(r=1-3p\). The exact numbers of successful partial colour assignments having respectively zero, one, or two initially coloured centres, after colouring all \(m+n\) leaves, are
\[
N_0=6(2^{m+n}-2^m-2^n),\quad
N_1=6(2^{m+n+1}-2^m-2^n),\quad
N_2=6\cdot2^{m+n}.
\]
Thus \(\operatorname{FC}_3(D_{m,n};p)=p^{m+n}(N_0r^2+N_1pr+N_2p^2)\). The identity also holds for \(m,n\ge1\); the case \(m=n=1\) agrees with the previously known four-vertex path.

## Assumptions and scope
Graphs are finite, simple, and undirected. An initially assigned colour is chosen from \(\{0,1,2\}\) independently with probability \(p\) for each particular colour, and a vertex is left blank with probability \(r=1-3p\). A partial assignment containing a monochromatic edge is unsuccessful. A blank vertex is forced when the set of colours currently used by its neighbours has cardinality two, in which case it receives the unique missing colour. The process continues until no more vertices can be forced, and succeeds only if the final total colouring is proper. For this tree, success is independent of the order of legal forces; this also follows from the disjoint cases below. The two centres are distinguished only for counting; the result is symmetric in \(m,n\).

## Proof
Every leaf has exactly one neighbour and therefore cannot be forced with three available colours. Hence **all leaves are initially assigned colours** in every successful configuration. There are just three possibilities for the initial states of the centres. For a word of length \(s\) on a specified two-colour alphabet, the number using both colours is \(q_s=2^s-2\).

**Both centres initially coloured.** Their colours must differ, giving \(3\cdot2=6\) choices. Each leaf must avoid the colour of its own centre and has two available colours. Thus \(N_2=6\cdot2^{m+n}\).

**Exactly one centre initially coloured.** Suppose the first centre has colour \(c\). Its leaves can use either of the other two colours, in \(2^m\) ways. The second centre can be forced precisely when the colours on its \(n\) leaves together with \(c\) comprise exactly two distinct colours. Those leaf words either use one colour different from \(c\) (two possibilities), or use \(c\) and exactly one other colour (\(2q_n\) possibilities). There are therefore \(2+2q_n=2(2^n-1)\) possibilities. Sum over three choices of \(c\) and both choices of initially coloured centre:
\[
N_1=6\bigl[2^m(2^n-1)+2^n(2^m-1)\bigr]
=6(2^{m+n+1}-2^m-2^n).
\]

**Neither centre initially coloured.** At least one centre must be forceable immediately from its leaves. Suppose the first centre is forceable first. Its leaves use exactly two colours: choose their support in three ways, and their assignments in \(q_m\) ways. Let \(c\) be the resulting missing centre colour. The second centre becomes forceable after this step if and only if its leaf colours, together with \(c\), use exactly two colours. They may form a constant word on one of two colours different from \(c\), or use the pair consisting of \(c\) and one of the other two colours. This contributes \(2+2q_n\) assignments; there are \(6q_m(1+q_n)\) first-centre-first configurations. Interchanging the centres gives \(6q_n(1+q_m)\). These configurations are counted twice exactly when both initial leaf supports have size two and their missing colours differ; there are \(6q_mq_n\) such configurations. If the missing colours agree, forcing either centre makes the other see all three colours, so that case is correctly excluded. Inclusion-exclusion gives
\[
N_0=6(q_m+q_n+q_mq_n)=6(2^{m+n}-2^m-2^n).
\]
Every case also yields a proper final colouring: the coloured centre always avoids its incident leaves, and the second centre when forced avoids the first. Conversely the cases exhaust all possible initial states and all legal forcing sequences. Multiplying each successful configuration by the probability of its initial state, \(p^{m+n+j}r^{2-j}\) for \(j\) initially coloured centres, establishes the formula. The zero-probability endpoint cases follow from the same polynomial identity.

## Verification
The standalone Python 3 program `verify_double_stars.py` constructs each double-star adjacency list, enumerates every initially coloured leaf word and all sixteen combinations of centre states for \(1\le m,n\le4\), rejects initially improper assignments, performs legal unique-colour forces, and checks the final proper colouring. It compares the resulting three integer counts against the closed forms, with assertions for every pair. The recorded output in `verification_output.txt` ends with `ALL_DOUBLE_STARS_PASS`. This is a finite independent stress test, not the proof of the universal result.

For \(m=n=1\), the formula reduces to \(24p^3(1-2p)\), the known four-vertex path value. For \(m=n=2\), the three exact counts are \((48,144,96)\).

## Relationship to prior work
Farr (2026) introduced and studied the forced-colouring function, established basic identities and hardness results, and provided exact formulas for all connected graphs of at most four vertices, including the four-vertex path. The paper also uses leaf-attached graphs in a complexity reduction; the inspected argument produces asymptotic bounds rather than this exact two-parameter double-star polynomial. An existing result computes forced three-colouring functions for all maximum-degree-two graphs, again including the path boundary; double-stars with \(m,n\ge2\) have maximum degree at least three. Neither inspected result supplies this formula. The new contribution is a complete two-hub interaction count, including the possibility that two individually forceable centres would force incompatible colours.

## Limitations
The formula is specifically for three colours and ordinary two-centre double-stars. It does not give the forced-colouring polynomial of arbitrary trees or of double-stars with a larger colour palette. Searches cannot exclude an unindexed equivalent formula; independent external validation is not claimed.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first publicly available 2026-09-15, https://arxiv.org/abs/2609.17108 .
2. *Exact forced 3-colouring polynomials at maximum degree two*, published-finding corpus record `2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd`, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd .
