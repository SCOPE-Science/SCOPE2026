# Distance-dual opening responses in the total domination game on the dodecahedron and Desargues graph

## Finding
Consider the classical twenty-vertex cubic graphs \(D=\operatorname{GP}(10,2)\) (the dodecahedron) and \(X=\operatorname{GP}(10,3)\) (the Desargues graph). In the standard **total domination game**, players alternate selecting a vertex whose **open** neighborhood contains at least one vertex not previously totally dominated. Dominator minimizes and Staller maximizes the number of selected vertices; a game ends only when all vertices are totally dominated.

The exact optimum numbers of moves are
\[
(\gamma_{\mathrm{tg}}(D),\gamma'_{\mathrm{tg}}(D))=(11,10),\qquad
(\gamma_{\mathrm{tg}}(X),\gamma'_{\mathrm{tg}}(X))=(10,10).
\]

There is a sharp distance-classification of the *second move*. Choose any first vertex \(a\), then force any distinct vertex \(b\) as the second move. Every such second move is legal in either graph. Let \(r=d_G(a,b)\). Assuming optimal play **after** these two fixed choices, the total numbers of moves are as follows; the columns labeled D-first and S-first mean that Dominator and Staller, respectively, made the first choice.

| \(r\) | Number of possible \(b\) for each \(a\) | D-first on \(D\) | S-first on \(D\) | D-first on \(X\) | S-first on \(X\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 10 | 11 | 10 | 10 |
| 2 | 6 | 11 | 11 | 10 | 10 |
| 3 | 6 | 10 | 11 | 10 | 10 |
| 4 | 3 | 10 | 11 | 10 | 10 |
| 5 | 1 | 10 | 10 | 10 | 10 |

Consequently, on the dodecahedron, if Dominator starts, **exactly the six distance-two vertices** are optimal replies for Staller; if Staller starts, **the unique antipode at distance five** is Dominator's sole optimal reply. On the Desargues graph, by contrast, **every possible second move** is optimal in either starting convention. In each graph every possible first move is optimal. Although both graphs have 20 vertices, degree three, diameter five, and identical distance-shell sizes \((1,3,6,6,3,1)\), their optimal-opening geometry is different.

## Assumptions and scope
The vertex set of \(\operatorname{GP}(10,k)\) is \(\{u_i,v_i:i\in\mathbb Z/10\mathbb Z\}\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\) for every \(i\), indices modulo ten. All graphs are finite, simple and loopless, and the result concerns only \(k=2,3\). The open neighborhood \(N(w)\) does not contain \(w\). A move is legal precisely if \(N(w)\setminus B\neq\varnothing\), where \(B\) is the set of vertices totally dominated by previously selected vertices. Previously selected vertices cannot be legal again because their neighborhoods are already contained in \(B\). An unsuccessful or merely attempted move is not counted. The length of a forced opening pair includes those two moves and presumes optimal decisions only from the third move onward.

## Proof
Write \(V=V(G)\), and define the remaining-game functions \(F_D(B)\) and \(F_S(B)\) for the position in which precisely \(B\subseteq V\) has been totally dominated and Dominator or Staller respectively acts next. When \(B=V\), both functions are zero. For \(B\neq V\),
\[
 F_D(B)=1+\min_{w:N(w)\not\subseteq B}F_S(B\cup N(w)),\qquad
 F_S(B)=1+\max_{w:N(w)\not\subseteq B}F_D(B\cup N(w)).
\]
These are exact minimax equations: the legal options are exactly those in the displayed index sets; the next state is the union with an open neighborhood; and the moving player determines the minimum or maximum. Because neither graph has an isolated vertex, a legal option always exists unless \(B=V\). Every legal option strictly increases \(B\), so these equations uniquely determine both functions by induction on \(|V\setminus B|\). No game history beyond \(B\) and the next player matters.

Both graphs have exactly twenty vertices. Enumerate all \(2^{20}\) subsets as twenty-bit masks. Iterate their integer mask values from \(2^{20}-1\) down to zero, using the strict-mask increase to fill the recurrence. This gives
\[
 (F_D(\varnothing),F_S(\varnothing))=(11,10)\ \text{for }D,
 \qquad (10,10)\ \text{for }X.
\]
For any ordered pair \((a,b)\) of distinct opening vertices, the next player is Dominator after a Dominator-first pair and Staller after a Staller-first pair. The *conditioned* final game lengths are therefore
\[
 L_D(a,b)=2+F_D(N(a)\cup N(b)),\qquad
 L_S(a,b)=2+F_S(N(a)\cup N(b)).
\]
A complete breadth-first enumeration of graph distances and evaluation of these formulas for **all 380 ordered pairs** on each graph yields the displayed five distance classes. The table also proves that every second move is legal, and that the shell sizes are the same. A separate check of all twenty first moves establishes \(1+F_S(N(a))=F_D(\varnothing)\) and \(1+F_D(N(a))=F_S(\varnothing)\), as required for optimality of arbitrary first moves. These computations are fully reproducible with the included source programs, and their exhaustive nature follows from the induction and the enumeration of all subsets and ordered pairs. In particular, merely enumerating sample plays would not suffice; the recurrence considers every legal continuation.

The alternate verifier reconstructs the dodecahedron from its canonical 30-edge adjacency list and the Desargues graph from containment between the ten two-subsets and ten three-subsets of a five-set. Explicit fixed graph isomorphisms between those constructions and \(\operatorname{GP}(10,2)\), \(\operatorname{GP}(10,3)\) are checked edge by edge. Its descending-mask dynamic program agrees exactly with a separately implemented memoized minimax recurrence on generalized Petersen graphs.

## Verification
Compile and run `verify_exact.cpp` using a C++17 compiler, then run `verify_recursive.py` using Python 3 with standard-library modules only. Each program independently prints the two game values, five distance-class tables per graph, full first-move checks, and completion of 380 ordered-pair checks per graph, ending with `VERIFY_OK`. The expected text is included in `exact_out.txt` and `recursive_out.txt`; the two records are byte-identical. The primary program evaluates both functions for **every** twenty-bit dominated-state mask, even unreachable masks, avoiding any dependence on selective traversal. The secondary checker starts from the empty mask and memoizes only positions reachable under the recurrence. Independent graph descriptions and verified permutations guard against accidentally identifying the wrong named graph.

## Relationship to prior work
Henning, Klavžar and Rall introduced the total version of the domination game, proved the Total Continuation Principle and established general inequalities for the two starting conventions [1]. Dorbec and Henning established exact formulas for paths and cycles [2]. These published results provide the correct game model, but neither statement implies the present graph-specific minimax values or the five-shell opening-response table. General results on ordinary total domination for generalized Petersen graphs, such as [3], optimize static total dominating sets; they do not determine an alternating adversarial-game value or optimal early-game responses. The new contribution is the exact comparative opening-response law in two equally sized canonical cubic graphs, not the pre-existing definitions or general bounds.

## Limitations
Only the two specified twenty-vertex graphs and the standard open-neighborhood game are covered; no extension to other generalized Petersen graphs is proved. The certificate is an exhaustive finite computation whose correctness rests on the explicitly supplied transition recurrence and executable implementations; it is not a noncomputational short-form determination. No exhaustive claim of worldwide novelty is made: independently published or unindexed equivalent evaluations may exist. The comparison with later work on generalized Petersen static total domination does not imply that every related game paper was accessible. No external independent audit has been performed.

## References
1. M. A. Henning, S. Klavžar, D. F. Rall, “Total Version of the Domination Game,” *Graphs and Combinatorics* 31 (2015), 1453–1462; first published 23 September 2014. https://doi.org/10.1007/s00373-014-1470-9
2. P. Dorbec, M. A. Henning, “Game total domination for cycles and paths,” *Discrete Applied Mathematics* 208 (2016), 7–18. https://doi.org/10.1016/j.dam.2016.03.014
3. T. Zhao et al., “The Numerical Invariants concerning the Total Domination for Generalized Petersen Graphs,” *Journal of Mathematics* (2020), Article 5473675. https://doi.org/10.1155/2020/5473675
4. M. A. Henning, D. F. Rall, “Progress Towards the Total Domination Game \(3/4\)-Conjecture,” arXiv:1512.02916 (2015). https://arxiv.org/abs/1512.02916
