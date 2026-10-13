# Exact three-variable counting depth of finite paths
## Finding
Let \(P_n\) be the finite simple undirected path on \(n\ge1\) vertices, and let \(D^3_{\#}(P_n)\) be the minimum quantifier depth of a counting first-order sentence using at most three variables that defines \(P_n\) up to isomorphism. Then
\[
D^3_{\#}(P_1)=1,
\]
and, for every \(n\ge2\),
\[
D^3_{\#}(P_n)=2+\left\lfloor\log_2\!\left(\frac{n+1}{3}\right)\right\rfloor.
\]

There is also an exact pairwise statement. Let
\[
H=P_m\dot\cup C_{c_1}\dot\cup\cdots\dot\cup C_{c_t}
\]
be a nonisomorphic same-order rival with \(m\ge2\), \(c_i\ge3\), and put \(c=\min_i c_i\). The first diagonal round of standard ordered-pair two-dimensional Weisfeiler--Leman refinement that distinguishes \(P_n\) from \(H\) is
\[
r(P_n,H)=\min\!\left\{\left\lfloor\log_2(m+2)\right\rfloor,
1+\left\lfloor\log_2(c-1)\right\rfloor\right\}.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and uncolored. Standard ordered-pair 2-WL starts from the atomic equality/edge/nonedge coloring. Counting quantifiers have depth one regardless of their threshold. Different graph orders are already separated by the multiplicity of the round-zero diagonal color.

The 2010 survey of Pikhurko and Verbitsky records both the exact 2-WL/counting-game bridge and a logarithmic three-variable upper bound for paths in ordinary first-order logic. The result here concerns the sharper counting fragment and determines the exact depth, not only its order of growth.

## Proof
Pikhurko--Verbitsky Lemma 4.3 states that equality of the multisets of diagonal 2-WL colors after \(s\) rounds is equivalent to Duplicator surviving \(s+1\) rounds of the three-pebble counting game. Hence if \(R(P_n)\) is the largest first diagonal-distinguishing round among nonisomorphic rivals, then
\[
D^3_{\#}(P_n)=R(P_n)+1.
\]

For \(n\ge2\), after one diagonal refinement the color of \((v,v)\) records the degree of \(v\). Thus any same-order rival surviving round one has exactly two degree-one vertices and all other vertices of degree two. Consequently it has exactly one path component and any number of cycle components:
\[
H=P_m\dot\cup C_{c_1}\dot\cup\cdots\dot\cup C_{c_t},
\qquad m\ge2,\quad c_i\ge3.
\]

We use the following diagonal-census lemma. For every \(s\ge1\), the round-\(s\) diagonal multisets of \(P_n\) and such an \(H\) are equal if and only if
\[
m\ge2^{s+1}-2
\qquad\text{and}\qquad
c_i\ge2^s+1\quad\text{for every }i.
\]
To prove the lemma, set \(a_s=2^s-1\). The standard distance-doubling induction for ordered-pair 2-WL on a path shows that the round-\(s\) diagonal color of a path vertex is determined exactly by the unordered pair of endpoint distances clipped at \(a_s\). Thus a sufficiently long path has two vertices in each exposed boundary layer \(0,1,\ldots,a_s-1\), and all remaining vertices have one common interior diagonal color. The two boundary waves remain disjoint precisely when \(m\ge2a_s=2^{s+1}-2\). A cycle vertex has that same interior diagonal color through round \(s\) precisely when its cycle has length at least \(2^s+1\): in the preceding pair round, exact distances have propagated only through radius \(2^{s-1}\), so no wrap-around is visible at or above this threshold; below it the two distance fronts meet and change the row multiset. Under the two displayed inequalities, the path component of \(H\) contributes exactly the same exposed boundary colors as \(P_n\), while its missing interior multiplicity is replaced by the cycle vertices. If either inequality fails, boundary-wave overlap in the path component or wrap-around in a shortest cycle creates a diagonal color or multiplicity absent from \(P_n\). This proves the lemma.

Let \(c=\min_i c_i\). The lemma says that the first diagonal-distinguishing round is the largest \(s\) for which the two threshold inequalities still hold, namely
\[
r(P_n,H)=\min\!\left\{\left\lfloor\log_2(m+2)\right\rfloor,
1+\left\lfloor\log_2(c-1)\right\rfloor\right\}.
\]

Now maximize over all rivals. A rival can survive through diagonal round \(s\) only if
\[
n\ge(2^{s+1}-2)+(2^s+1)=3\cdot2^s-1.
\]
Conversely, whenever \(n\ge3\cdot2^s-1\), the single-cycle rival
\[
P_{2^{s+1}-2}\dot\cup C_{n-(2^{s+1}-2)}
\]
meets both thresholds and therefore survives through round \(s\). Hence, for \(n\ge2\), the largest first distinguishing round is
\[
R(P_n)=1+\left\lfloor\log_2\!\left(\frac{n+1}{3}\right)\right\rfloor.
\]
The bridge gives the claimed
\[
D^3_{\#}(P_n)=R(P_n)+1
=2+\left\lfloor\log_2\!\left(\frac{n+1}{3}\right)\right\rfloor.
\]
For \(P_1\), order alone defines the graph with depth one.

## Verification
The accompanying `artifacts/verify.py` independently implements joint ordered-pair 2-WL. It exhaustively checks every decomposition into one path plus one or more cycles for \(5\le n\le18\), 390 rivals in total, against the exact pairwise formula. It also checks the extremal witness through \(n=40\). The run returned:

`VERIFY_OK decompositions=390 exhaustive_n=5..18 extremal_n=19..40`

The computation is supplementary; the proof is uniform in \(n\).

## Relationship to prior work
Pikhurko and Verbitsky explicitly note that the path has an ordinary three-variable first-order definition of depth less than \(\log_2 n+3\), and their Lemma 4.3 gives the exact diagonal-WL/counting-game correspondence used here. Their survey does not state the exact three-variable counting depth above. Later general iteration work of Lichter, Ponomarenko, and Schweitzer proves an \(O(n\log n)\) upper bound for 2-WL and the corresponding three-variable counting depth when distinguishability holds, but does not specialize to an exact path law.

The current result is not implied by the exact two-variable counting depth of paths: that parameter is linear because one-dimensional color refinement propagates from the endpoints only one edge per round. It is also different from the strict stabilization depth of 2-WL on a single path, because defining depth is governed by the hardest nonisomorphic rival; the extremal rival here balances the amount of path needed to hide endpoint-wave collision with the amount of cycle needed to hide wrap-around.

## Limitations
The theorem is specific to finite simple paths and three-variable counting logic. The diagonal-census lemma uses the maximum-degree-two decomposition and does not directly extend to arbitrary trees. The originality search was targeted rather than exhaustive; an unindexed thesis or folklore occurrence of the exact constant remains a residual risk.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first posted 25 March 2010. Lemma 4.3 gives the diagonal 2-WL/counting-game equivalence; the introductory discussion records \(D^3(P_n)<\log_2 n+3\).
2. M. Lichter, I. Ponomarenko, and P. Schweitzer, *Walk refinement, walk logic, and the iteration number of the Weisfeiler-Leman algorithm*, arXiv:1905.03008, first posted 8 May 2019. It gives general iteration bounds for 2-WL and corresponding three-variable counting-depth bounds.
